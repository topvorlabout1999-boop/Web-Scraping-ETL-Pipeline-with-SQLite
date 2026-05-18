from extractor import extract_quotes
from transformer import transform_quotes
from loader import create_database, load_quotes_to_database, export_quotes_to_csv


def main():
    print("Starting Web Scraping ETL Pipeline...")

    create_database()

    raw_quotes = extract_quotes()

    clean_quotes = transform_quotes(raw_quotes)

    load_quotes_to_database(clean_quotes)

    export_quotes_to_csv()

    print("Process completed successfully")


if __name__ == "__main__":
    main()