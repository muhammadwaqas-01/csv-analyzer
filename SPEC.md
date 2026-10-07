# CSV Analyzer: Spec

- Input: A path to a CSV file with a header row.
- Output: The number of rows and columns, then for each column its type (number or text) and how many values are missing. Number columns also show the minimum, maximum and average. Text columns show how many different values they have and the 3 most common ones.
- Usage: `python main.py data/sample.csv`
- Errors handled: File not found, empty file, and a file that has only a header and no data rows.
- Out of scope: Charts, Excel files, databases, saving the report to a file, and very large files.