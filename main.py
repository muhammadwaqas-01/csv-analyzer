from analyzer.loader import load_csv
from analyzer.columns import detect_types
from analyzer.summary import summarize_columns, get_overview


def main():
    try:
        headers, rows = load_csv("data/sample.csv")

        column_types = detect_types(headers, rows)

        summaries = summarize_columns(
            headers,
            rows,
            column_types,
        )

        overview = get_overview(headers, rows)

        print("Overview:", overview)

        for header, info in summaries.items():
            print(header, info)

    except FileNotFoundError:
        print("CSV file not found.")

    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()