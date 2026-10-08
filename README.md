# CSV Analyzer

A small command line tool that reads a CSV file and describes what is inside it: how many rows and columns it has, what type each column is, and a summary of every column. It also fails with a clear message instead of a crash when the file is a problem.

> Built as my Week 1 project while learning Python for AI Engineering. It uses only the Python standard library.

## Example

```
python main.py data/sample.csv
```

```
Rows: 10
Columns: 4

name (text)
  Values: 10   Missing: 0
  Unique: 10
  Top: Ali (1), Sara (1), Ahmed (1)

age (number)
  Values: 8   Missing: 2
  Min: 20   Max: 24   Mean: 22.00

city (text)
  Values: 9   Missing: 1
  Unique: 8
  Top: Lahore (2), Karachi (1), Islamabad (1)

marks (number)
  Values: 9   Missing: 1
  Min: 76   Max: 95   Mean: 86.22
```

## What it does

- Loads a CSV file and cleans it: removes extra spaces, treats blank cells as missing, and accepts the hidden marker Excel adds at the start of a UTF-8 file.
- Detects the type of each column: `number`, `text` or `empty`. Missing values are ignored, and `nan` / `inf` count as text.
- Summarizes every column:
  - number: values, missing, min, max, mean
  - text: values, missing, unique, the 3 most common values (ties keep the order of first appearance)
  - empty: how many values are missing
- Reports problems clearly (message on stderr, exit code 1): file not found, a path that cannot be read (such as a folder), an empty file, a header with no data rows, a row with more values than headers (with the line number), duplicate column names, and text that is not valid UTF-8.

## Requirements

Python 3.10 or newer. Running the tool needs no extra packages.

## Usage

```
git clone https://github.com/muhammadwaqas-01/csv-analyzer.git
cd csv-analyzer
python main.py data/sample.csv
```

| Exit code | Meaning |
|---|---|
| 0 | Report printed |
| 1 | The file could not be read or analyzed |
| 2 | Wrong usage (for example no path given) |

`python main.py -h` shows the help text.

## Tests

The tests use `pytest` (version 7 or newer).

```
pip install -r requirements-dev.txt
python -m pytest -v
```

Run the command from the project root. There are 29 tests for the loader, column types, summaries, the report and the command line. Tests that need files create them in a temporary folder, so the real data is never changed.

## Project structure

```
csv-analyzer/
  analyzer/
    loader.py     # load_csv: reads and validates the file
    columns.py    # detects the type of each column
    summary.py    # summarizes each column
    report.py     # turns the summaries into readable text
  data/
    sample.csv    # example data (10 rows, 4 columns, some missing values)
  tests/
    data/         # small CSV files for trying edge cases by hand
    test_*.py     # automated tests
  main.py         # command line entry point
  SPEC.md         # what the tool does and does not do
  pytest.ini
  requirements-dev.txt
```

## Design notes

- `loader.py`, `columns.py` and `summary.py` only compute; they never print. They raise errors, and `main.py` decides what to show.
- `report.py` returns a string, so the report can be tested without capturing output.
- `main()` returns an exit code and `sys.exit(main())` sits at the bottom, so tests can call `main([...])` directly.

## Limitations

- Column types are guessed from the values, so IDs or phone numbers may be treated as numbers.
- Only comma separated files are supported.
- The whole file is read into memory, so it is not meant for very large files.

## Ideas for later

- A choice of separator for files that use `;` or tabs
- More column types, such as dates
- Saving the report to a file