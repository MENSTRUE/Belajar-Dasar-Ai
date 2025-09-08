# ==============================
# Library Web Scraping (Perbaikan untuk gzip)
# ==============================

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import gzip

url = "http://python.org/"

# ==============================
# 1️⃣ BeautifulSoup
print("=== BeautifulSoup ===")
try:
    # Beberapa situs mengirim gzip content, jadi kita tambahkan header
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)

    # Mengecek apakah konten dikompresi gzip
    if response.info().get('Content-Encoding') == 'gzip':
        html = gzip.decompress(response.read()).decode('utf-8')
    else:
        html = response.read().decode('utf-8')

    # Parsing dengan BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    print("Judul halaman:", soup.title.string)
except Exception as e:
    print("Terjadi error BeautifulSoup:", e)

# ==============================
# 2️⃣ Urllib langsung
print("\n=== Urllib ===")
try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)

    # Handle gzip
    if response.info().get('Content-Encoding') == 'gzip':
        html = gzip.decompress(response.read()).decode('utf-8')
    else:
        html = response.read().decode('utf-8')

    # Ekstrak title
    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print("Judul halaman:", title)
except Exception as e:
    print("Terjadi error Urllib:", e)
