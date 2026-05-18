import pandas as pd


def clean_quote_text(text):
    """
    ทำความสะอาดข้อความ quote
    """

    if not isinstance(text, str):
        return ""

    return (
        text.replace("“", "")
            .replace("”", "")
            .strip()
    )


def transform_quotes(records):
    """
    แปลง list ของ quotes ให้เป็น DataFrame และ clean ข้อมูล
    """

    if not records:
        print("No records to transform")
        return pd.DataFrame()

    df = pd.DataFrame(records)

    df["quote"] = df["quote"].apply(clean_quote_text)
    df["author"] = df["author"].fillna("").str.strip()
    df["tags"] = df["tags"].fillna("").str.strip()

    df = df.drop_duplicates(subset=["quote", "author"])

    df = df[df["quote"] != ""]
    df = df[df["author"] != ""]

    print(f"Transformed {len(df)} clean quotes")
    return df