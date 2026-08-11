#!/usr/bin/env python3
"""Calculate a monthly AI workload cost from runtime-verified unit prices."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from decimal import Decimal
from urllib.parse import urlparse


TOKEN_UNIT = Decimal("1000000")


def nonnegative(value: str) -> Decimal:
    number = Decimal(value)
    if number < 0:
        raise argparse.ArgumentTypeError("value must be non-negative")
    return number


def positive(value: str) -> Decimal:
    number = nonnegative(value)
    if number == 0:
        raise argparse.ArgumentTypeError("value must be greater than zero")
    return number


def rate(value: str) -> Decimal:
    number = nonnegative(value)
    if number > 1:
        raise argparse.ArgumentTypeError("rate must be between 0 and 1")
    return number


def verified_timestamp(value: str) -> str:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("verified_at must be ISO 8601") from exc
    if parsed.tzinfo is None:
        raise argparse.ArgumentTypeError("verified_at must include a timezone")
    return value


def official_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise argparse.ArgumentTypeError("source_url must be an HTTP(S) URL")
    return value


def calculate(
    monthly_requests: Decimal,
    input_tokens: Decimal,
    output_tokens: Decimal,
    input_price: Decimal,
    output_price: Decimal,
    cached_input_price: Decimal | None = None,
    cache_hit_rate: Decimal = Decimal("0"),
    model_calls_per_request: Decimal = Decimal("1"),
    retry_rate: Decimal = Decimal("0"),
    image_cost_per_request: Decimal = Decimal("0"),
    fixed_cost_per_request: Decimal = Decimal("0"),
) -> dict[str, Decimal]:
    cached_price = input_price if cached_input_price is None else cached_input_price
    billable_calls = monthly_requests * model_calls_per_request * (Decimal("1") + retry_rate)
    normal_input_cost = (
        billable_calls * input_tokens * (Decimal("1") - cache_hit_rate)
        / TOKEN_UNIT * input_price
    )
    cached_input_cost = (
        billable_calls * input_tokens * cache_hit_rate
        / TOKEN_UNIT * cached_price
    )
    output_cost = billable_calls * output_tokens / TOKEN_UNIT * output_price
    image_cost = monthly_requests * image_cost_per_request
    fixed_cost = monthly_requests * fixed_cost_per_request
    total_cost = normal_input_cost + cached_input_cost + output_cost + image_cost + fixed_cost
    per_request = total_cost / monthly_requests if monthly_requests else Decimal("0")
    return {
        "monthly_requests": monthly_requests,
        "billable_model_calls": billable_calls,
        "normal_input_cost": normal_input_cost,
        "cached_input_cost": cached_input_cost,
        "output_cost": output_cost,
        "image_cost": image_cost,
        "fixed_cost": fixed_cost,
        "monthly_total": total_cost,
        "cost_per_user_request": per_request,
    }


def decimal_string(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def self_test() -> None:
    # Synthetic arithmetic fixtures only; these are not provider prices.
    result = calculate(
        monthly_requests=Decimal("1000"),
        input_tokens=Decimal("1000"),
        output_tokens=Decimal("500"),
        input_price=Decimal("1"),
        cached_input_price=Decimal("0.5"),
        output_price=Decimal("2"),
        cache_hit_rate=Decimal("0.5"),
        image_cost_per_request=Decimal("0.1"),
        fixed_cost_per_request=Decimal("0.02"),
    )
    assert result["normal_input_cost"] == Decimal("0.5")
    assert result["cached_input_cost"] == Decimal("0.25")
    assert result["output_cost"] == Decimal("1")
    assert result["monthly_total"] == Decimal("121.75")
    assert decimal_string(Decimal("3E+4")) == "30000"
    print("self-test: ok")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--monthly-requests", type=nonnegative)
    parser.add_argument("--input-tokens", type=nonnegative)
    parser.add_argument("--output-tokens", type=nonnegative)
    parser.add_argument("--input-price-per-million", type=nonnegative)
    parser.add_argument("--cached-input-price-per-million", type=nonnegative)
    parser.add_argument("--output-price-per-million", type=nonnegative)
    parser.add_argument("--cache-hit-rate", type=rate, default=Decimal("0"))
    parser.add_argument("--model-calls-per-request", type=positive, default=Decimal("1"))
    parser.add_argument("--retry-rate", type=rate, default=Decimal("0"))
    parser.add_argument("--image-cost-per-request", type=nonnegative, default=Decimal("0"))
    parser.add_argument("--fixed-cost-per-request", type=nonnegative, default=Decimal("0"))
    parser.add_argument("--budget", type=nonnegative)
    parser.add_argument("--currency")
    parser.add_argument("--source-url", type=official_url)
    parser.add_argument("--verified-at", type=verified_timestamp)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--self-test", action="store_true")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return

    required = {
        "monthly-requests": args.monthly_requests,
        "input-tokens": args.input_tokens,
        "output-tokens": args.output_tokens,
        "input-price-per-million": args.input_price_per_million,
        "output-price-per-million": args.output_price_per_million,
        "currency": args.currency,
        "source-url": args.source_url,
        "verified-at": args.verified_at,
    }
    missing = [name for name, value in required.items() if value is None]
    if missing:
        parser.error("missing required arguments: " + ", ".join(missing))

    result = calculate(
        monthly_requests=args.monthly_requests,
        input_tokens=args.input_tokens,
        output_tokens=args.output_tokens,
        input_price=args.input_price_per_million,
        cached_input_price=args.cached_input_price_per_million,
        output_price=args.output_price_per_million,
        cache_hit_rate=args.cache_hit_rate,
        model_calls_per_request=args.model_calls_per_request,
        retry_rate=args.retry_rate,
        image_cost_per_request=args.image_cost_per_request,
        fixed_cost_per_request=args.fixed_cost_per_request,
    )
    payload = {key: decimal_string(value) for key, value in result.items()}
    payload.update({
        "currency": args.currency,
        "source_url": args.source_url,
        "verified_at": args.verified_at,
    })
    if args.budget is not None:
        payload["budget"] = decimal_string(args.budget)
        payload["budget_delta"] = decimal_string(args.budget - result["monthly_total"])
        payload["within_budget"] = result["monthly_total"] <= args.budget

    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(f"monthly total: {args.currency} {payload['monthly_total']}")
    print(f"per user request: {args.currency} {payload['cost_per_user_request']}")
    print(
        "breakdown: "
        f"normal input {payload['normal_input_cost']}, "
        f"cached input {payload['cached_input_cost']}, "
        f"output {payload['output_cost']}, "
        f"images {payload['image_cost']}, "
        f"fixed {payload['fixed_cost']}"
    )
    print(f"verified_at: {args.verified_at}")
    print(f"source_url: {args.source_url}")


if __name__ == "__main__":
    main()
