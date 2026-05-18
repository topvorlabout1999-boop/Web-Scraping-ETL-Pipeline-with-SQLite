import requests
from bs4 import BeautifulSoup
from config import BASE_URL, MAX_PAGES


def fetch_page(url):
    """
    โหลด HTML จาก URL ที่กำหนด
    """

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as error:
        print(f"Error fetching page: {error}")
        return ""


def parse_quotes(html):
    """
    แยก quote, author, tags ออกจาก HTML
    """

    soup = BeautifulSoup(html, "html.parser")

    quote_boxes = soup.select(".quote")
    records = []

    for box in quote_boxes:
        quote_text = box.select_one(".text")
        author = box.select_one(".author")
        tags = box.select(".tag")

        records.append({
            "quote": quote_text.get_text(strip=True) if quote_text else "",
            "author": author.get_text(strip=True) if author else "",
            "tags": ", ".join(tag.get_text(strip=True) for tag in tags)
        })

    return records


def extract_quotes():
    """
    ดึงข้อมูล quotes จากหลายหน้า
    """

    all_quotes = []

    for page in range(1, MAX_PAGES + 1):
        url = f"{BASE_URL}/page/{page}/"
        print(f"Scraping page {page}: {url}")

        html = fetch_page(url)

        if not html:
            continue

        quotes = parse_quotes(html)
        all_quotes.extend(quotes)

    print(f"Extracted {len(all_quotes)} quotes")
    return all_quotes