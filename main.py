from feature_extractor.extractor import fetch_website
from feature_extractor.parser import (
    get_title,
    get_image_count,
    get_css_count,
    get_js_count,
    get_meta_description,
    get_h1_count,
    get_internal_links_count,
    get_external_links_count
)
url = "https://github.com"

soup = fetch_website(url)

print("Website Title:", get_title(soup))
print("Image Count:", get_image_count(soup))
print("CSS Files:", get_css_count(soup))
print("JavaScript Files:", get_js_count(soup))
print("Meta Description:", get_meta_description(soup))
print("H1 Count:", get_h1_count(soup))
print("Internal Links:", get_internal_links_count(soup, url))
print("External Links:", get_external_links_count(soup, url))
