from analyzer.columns import is_number, detect_column_type


def test_is_number_accepts_decimal():
    assert is_number("8.5") is True


def test_is_number_accepts_negative():
    assert is_number("-3") is True


def test_is_number_accepts_scientific_notation():
    assert is_number("1e3") is True


def test_is_number_rejects_text():
    assert is_number("abc") is False


def test_is_number_rejects_empty():
    assert is_number("") is False


def test_is_number_rejects_nan():
    assert is_number("nan") is False


def test_is_number_rejects_inf():
    assert is_number("inf") is False


def test_detect_column_type_empty():
    assert detect_column_type(["", ""]) == "empty"


def test_detect_column_type_number_with_missing():
    assert detect_column_type(["1", "", "3"]) == "number"


def test_detect_column_type_mixed():
    assert detect_column_type(["1", "abc", "3"]) == "text"