from collections import Counter

from analyzer.columns import get_column


def summarize_number_column(values: list[str]) -> dict:
    """
    Summarize a number column.

    Args:
        values: List of string values from a number column.

    Returns:
        A dictionary containing count, missing, min, max, and mean.
    """
    non_empty_values = [value for value in values if value != ""]
    missing = len(values) - len(non_empty_values)

    numbers = [float(value) for value in non_empty_values]

    if not numbers:
        return {
            "count": 0,
            "missing": missing,
            "min": None,
            "max": None,
            "mean": None,
        }

    return {
        "count": len(numbers),
        "missing": missing,
        "min": min(numbers),
        "max": max(numbers),
        "mean": round(sum(numbers) / len(numbers), 2),
    }


def summarize_text_column(values: list[str]) -> dict:
    """
    Summarize a text column.

    Args:
        values: List of string values from a text column.

    Returns:
        A dictionary containing count, missing, unique, and top.
    """
    non_empty_values = [value for value in values if value != ""]
    missing = len(values) - len(non_empty_values)

    counter = Counter(non_empty_values)

    return {
        "count": len(non_empty_values),
        "missing": missing,
        "unique": len(counter),
        "top": counter.most_common(3),
    }


def summarize_columns(
    headers: list[str],
    rows: list[dict[str, str]],
    column_types: dict[str, str],
) -> dict:
    """
    Create a summary for every column.

    Args:
        headers: List of column headers.
        rows: List of CSV rows.
        column_types: Detected type of each column.

    Returns:
        A dictionary containing summaries for every column.
    """
    summaries = {}

    for header in headers:
        values = get_column(rows, header)
        column_type = column_types[header]

        if column_type == "number":
            summary = summarize_number_column(values)

        elif column_type == "text":
            summary = summarize_text_column(values)

        else:
            summary = {
                "count": 0,
                "missing": len(values),
            }

        summary["type"] = column_type
        summaries[header] = summary

    return summaries


def get_overview(
    headers: list[str],
    rows: list[dict[str, str]],
) -> dict:
    """
    Return an overview of the CSV data.

    Args:
        headers: List of column headers.
        rows: List of CSV rows.

    Returns:
        A dictionary containing the number of rows and columns.
    """
    return {
        "rows": len(rows),
        "columns": len(headers),
    }