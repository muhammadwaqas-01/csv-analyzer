from analyzer.report import format_number, build_report


def test_format_number_removes_zero_decimal():
    assert format_number(20.0) == "20"


def test_format_number_keeps_decimal():
    assert format_number(8.5) == "8.5"


def test_build_report_contains_number_column():
    overview = {
        "rows": 2,
        "columns": 1,
    }

    summaries = {
        "age": {
            "type": "number",
            "count": 2,
            "missing": 0,
            "min": 20.0,
            "max": 24.0,
            "mean": 22.0,
        }
    }

    report = build_report(overview, summaries)

    assert "age (number)" in report