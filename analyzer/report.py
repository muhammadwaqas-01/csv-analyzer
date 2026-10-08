def format_overview(overview: dict) -> str:
    """Format row and column counts."""
    return f"Rows: {overview['rows']}\nColumns: {overview['columns']}"


def format_number(value: float) -> str:
    """Format a number without unnecessary .0."""
    if value.is_integer():
        return str(int(value))
    return str(value)


def format_column(header: str, info: dict) -> str:
    """Format one column summary as readable text."""
    column_type = info["type"]

    if column_type == "number":
        return (
            f"{header} (number)\n"
            f"  Values: {info['count']}   Missing: {info['missing']}\n"
            f"  Min: {format_number(info['min'])}   "
            f"Max: {format_number(info['max'])}   "
            f"Mean: {info['mean']:.2f}"
        )

    if column_type == "text":
        top = ", ".join(
            f"{value} ({count})"
            for value, count in info["top"]
        )

        return (
            f"{header} (text)\n"
            f"  Values: {info['count']}   Missing: {info['missing']}\n"
            f"  Unique: {info['unique']}\n"
            f"  Top: {top}"
        )

    if column_type == "empty":
        return (
            f"{header} (empty)\n"
            f"  Missing: {info['missing']}"
        )

    return f"{header} ({column_type})"


def build_report(overview: dict, summaries: dict) -> str:
    """Build the complete readable report."""
    sections = [format_overview(overview)]

    for header, info in summaries.items():
        sections.append(format_column(header, info))

    return "\n\n".join(sections)