import math


def is_number(value: str) -> bool:
    """
    Check whether a string represents a finite number.

    Args:
        value: String value to check.

    Returns:
        True if the value is a finite number, otherwise False.
    """
    try:
        number = float(value)
        return math.isfinite(number)
    except ValueError:
        return False


def get_column(rows: list[dict[str, str]], header: str) -> list[str]:
    """
    Get all values from a specific column.

    Args:
        rows: List of row dictionaries.
        header: Name of the column.

    Returns:
        A list containing the values from the selected column.
    """
    return [row[header] for row in rows]


def detect_column_type(values: list[str]) -> str:
    """
    Detect whether a column is empty, numeric, or text.

    Args:
        values: List of string values from a column.

    Returns:
        'empty', 'number', or 'text'.
    """
    non_empty_values = [value for value in values if value != ""]

    if not non_empty_values:
        return "empty"

    if all(is_number(value) for value in non_empty_values):
        return "number"

    return "text"


def detect_types(
    headers: list[str],
    rows: list[dict[str, str]]
) -> dict[str, str]:
    """
    Detect the type of every column.

    Args:
        headers: List of CSV headers.
        rows: List of CSV rows.

    Returns:
        A dictionary mapping each header to its detected type.
    """
    types = {}

    for header in headers:
        values = get_column(rows, header)
        types[header] = detect_column_type(values)

    return types