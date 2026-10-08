import pytest

from analyzer.loader import load_csv


def test_load_csv_returns_headers_and_rows(tmp_path):
    file = tmp_path / "data.csv"

    file.write_text(
        "name,age\nAli,21\nSara,22\n",
        encoding="utf-8",
    )

    headers, rows = load_csv(str(file))

    assert headers == ["name", "age"]
    assert rows == [
        {"name": "Ali", "age": "21"},
        {"name": "Sara", "age": "22"},
    ]


def test_load_csv_strips_spaces(tmp_path):
    file = tmp_path / "data.csv"

    file.write_text(
        " name , age \n Ali , 21 \n",
        encoding="utf-8",
    )

    headers, rows = load_csv(str(file))

    assert headers == ["name", "age"]
    assert rows == [
        {"name": "Ali", "age": "21"},
    ]


def test_load_csv_empty_file_raises_value_error(tmp_path):
    file = tmp_path / "empty.csv"

    file.write_text(
        "",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_csv(str(file))


def test_load_csv_header_only_raises_value_error(tmp_path):
    file = tmp_path / "header.csv"

    file.write_text(
        "name,age\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_csv(str(file))


def test_load_csv_too_many_values_includes_line_number(tmp_path):
    file = tmp_path / "bad.csv"

    file.write_text(
        "name,age\nAli,21,extra\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Line 2"):
        load_csv(str(file))


def test_load_csv_missing_file_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("does-not-exist.csv")

def test_load_csv_duplicate_headers_raises_value_error(tmp_path):
    file = tmp_path / "duplicate.csv"

    file.write_text(
        "name,age,name\nAli,21,Ali\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="name"):
        load_csv(str(file))

def test_load_csv_handles_utf8_bom(tmp_path):
    file = tmp_path / "bom.csv"

    file.write_bytes(
        b"\xef\xbb\xbfname,age\nAli,21\n"
    )

    headers, rows = load_csv(str(file))

    assert headers == ["name", "age"]
    assert rows == [
        {"name": "Ali", "age": "21"},
    ]

def test_load_csv_invalid_utf8_raises_value_error(tmp_path):
    file = tmp_path / "invalid.csv"
    file.write_bytes(b"name,age\nAli,\xff\n")

    with pytest.raises(ValueError):
        load_csv(str(file))