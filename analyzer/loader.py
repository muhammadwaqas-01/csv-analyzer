import csv
def load_csv(path: str) -> tuple[list[str],list[dict[str,str]]]:
    """
    Load a CSV file and return its headers and rows.

    Args:
        path: Path of the CSV file.

    Returns:
        A tuple containing the headers and rows.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the file is empty or has no data rows.
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("The CSV file is empty!")
        headers = [header.strip() for header in reader.fieldnames]

        rows = []

        for row in reader:
            if None in row:
                raise ValueError(f"Line {reader.line_num}: row has more values than headers")
            clean_row = {}
            for key,value in row.items():
                clean_key = key.strip()
                clean_value = "" if value is None else value.strip()
                clean_row[clean_key] = clean_value
            rows.append(clean_row)
    if not rows:
        raise ValueError("The CSV file has a header but no data rows")

    return headers,rows