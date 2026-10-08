# CSV Analyzer

A small command line tool that reads a CSV file and describes what is inside it: how many rows and columns it has, what type each column is, and a summary of every column.

> **Status:** work in progress. Built as my Week 1 project while learning Python for AI Engineering.

## What it does so far

- Loads a CSV file and cleans it (removes extra spaces, treats missing values as empty strings).
- Detects the type of each column: `number`, `text` or `empty`. Missing values are ignored when deciding the type, and `nan` / `inf` are treated as text.
- Summarizes every column:
  - number columns: count, missing, min, max, mean
  - text columns: count, missing, number of unique values, the 3 most common values
  - empty columns: how many values are missing
- Gives clear error messages for: a file that does not exist, an empty file, a file with a header but no data rows, and a row that has more values than headers (with the line number).

## Project structure

```
csv-analyzer/
  analyzer/
    loader.py     # load_csv: reads and cleans the file
    columns.py    # detects the type of each column
    summary.py    # summarizes each column
    report.py     # planned: formatted report output
  data/
    sample.csv    # example data (10 rows, 4 columns, some missing values)
  tests/
    data/         # small CSV files used to try edge cases
  main.py         # demo entry point
  SPEC.md         # what the tool should do and not do
```

## How to run

You need Python 3.9 or newer. There are no external packages.

```
git clone https://github.com/muhammadwaqas-01/csv-analyzer.git
cd csv-analyzer
python main.py
```

## Example output

Running it on `data/sample.csv`:

```
Overview: {'rows': 10, 'columns': 4}
name {'count': 10, 'missing': 0, 'unique': 10, 'top': [('Ali', 1), ('Sara', 1), ('Ahmed', 1)], 'type': 'text'}
age {'count': 8, 'missing': 2, 'min': 20.0, 'max': 24.0, 'mean': 22.0, 'type': 'number'}
city {'count': 9, 'missing': 1, 'unique': 8, 'top': [('Lahore', 2), ('Karachi', 1), ('Islamabad', 1)], 'type': 'text'}
marks {'count': 9, 'missing': 1, 'min': 76.0, 'max': 95.0, 'mean': 86.22, 'type': 'number'}
```

## Known limitations

- Column types are guessed from the values, so IDs or phone numbers may be treated as numbers.
- Two columns with the same name are not handled yet.
- The whole file is read into memory, so it is not meant for very large files.

## Planned

- A readable report instead of raw dictionaries (`report.py`)
- Pass the file path on the command line
- Automated tests for the edge cases in `tests/data/`