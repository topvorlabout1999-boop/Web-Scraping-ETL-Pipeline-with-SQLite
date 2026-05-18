import sqlite3
import pandas as pd
from config import DATABASE_FILE, CSV_EXPORT_FILE


def create_database():
    """
    สร้าง database และ table quotes
    """

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT NOT NULL,
            author TEXT NOT NULL,
            tags TEXT,
            UNIQUE(quote, author)
        )
    """)

    conn.commit()
    conn.close()

    print("Database checked/created successfully")


def load_quotes_to_database(df):
    """
    บันทึก quotes ลง SQLite database
    """

    if df.empty:
        print("No quotes to save")
        return

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    inserted_count = 0

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO quotes
                (quote, author, tags)
                VALUES (?, ?, ?)
            """, (
                row["quote"],
                row["author"],
                row["tags"]
            ))

            if cursor.rowcount > 0:
                inserted_count += 1

        except sqlite3.Error as error:
            print(f"Database insert error: {error}")

    conn.commit()
    conn.close()

    print(f"Inserted {inserted_count} new quotes into database")


def export_quotes_to_csv():
    """
    Export ข้อมูล quotes จาก database เป็น CSV
    """

    conn = sqlite3.connect(DATABASE_FILE)

    df = pd.read_sql_query(
        "SELECT * FROM quotes ORDER BY author ASC",
        conn
    )

    conn.close()

    df.to_csv(CSV_EXPORT_FILE, index=False, encoding="utf-8-sig")

    print(f"Quotes exported to CSV: {CSV_EXPORT_FILE}")