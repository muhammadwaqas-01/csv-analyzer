from pathlib import Path

from main import main


SAMPLE = Path(__file__).parent.parent / "data" / "sample.csv"


def test_cli_success(capsys):
    exit_code = main([str(SAMPLE)])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Rows: 10" in captured.out


def test_cli_missing_file(capsys):
    exit_code = main(["does-not-exist.csv"])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "file not found" in captured.err


def test_cli_empty_file(tmp_path, capsys):
    file = tmp_path / "empty.csv"
    file.write_text("", encoding="utf-8")

    exit_code = main([str(file)])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Error:" in captured.err

def test_cli_directory_path(capsys, tmp_path):
    exit_code = main([str(tmp_path)])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Error: cannot read" in captured.err