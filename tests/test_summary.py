from analyzer.summary import (
    summarize_number_column,
    summarize_text_column,
)


def test_summarize_number_column():
    result = summarize_number_column(["1", "", "3"])

    assert result["count"] == 2
    assert result["missing"] == 1
    assert result["min"] == 1
    assert result["max"] == 3
    assert result["mean"] == 2


def test_text_missing_is_not_unique():
    result = summarize_text_column(["Lahore", "", "Lahore"])

    assert result["missing"] == 1
    assert result["unique"] == 1


def test_text_tie_preserves_first_seen_order():
    result = summarize_text_column(
        [
            "cherry",
            "apple",
            "banana",
            "cherry",
            "apple",
            "banana",
        ]
    )

    assert result["top"] == [
        ("cherry", 2),
        ("apple", 2),
        ("banana", 2),
    ]