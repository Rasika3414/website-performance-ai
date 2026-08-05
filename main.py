from feature_extractor.extractor import fetch_website
from feature_extractor.parser import (
    get_title,
    get_image_count,
    get_css_count,
    get_js_count
)
url = "https://github.com"

soup = fetch_website(url)

print("Website Title:", get_title(soup))
print("Image Count:", get_image_count(soup))
print("CSS Files:", get_css_count(soup))
print("JavaScript Files:", get_js_count(soup))