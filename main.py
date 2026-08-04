from feature_extractor.extractor import fetch_website
from feature_extractor.parser import get_title

url = "https://github.com"

soup = fetch_website(url)

print("Website Title:", get_title(soup))
