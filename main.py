import argparse
import sys

from analyzer.loader import load_csv
from analyzer.columns import detect_types
from analyzer.summary import summarize_columns, get_overview
from analyzer.report import build_report


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Analyze a CSV file and generate a readable report."
    )

    parser.add_argument(
        "path",
        help="Path to the CSV file",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CSV analyzer and return an exit code."""
    args = build_parser().parse_args(argv)

    try:
        headers, rows = load_csv(args.path)

        column_types = detect_types(headers, rows)

        summaries = summarize_columns(
            headers,
            rows,
            column_types,
        )

        overview = get_overview(headers, rows)

        report = build_report(overview, summaries)

        print(report)

        return 0

    except FileNotFoundError:
        print(
            f"Error: file not found: {args.path}",
            file=sys.stderr,
        )
        return 1

    except OSError as e:
        print(
            f"Error: cannot read '{args.path}': {e}",
            file=sys.stderr,
        )
        return 1

    except ValueError as e:
        print(
            f"Error: {e}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())