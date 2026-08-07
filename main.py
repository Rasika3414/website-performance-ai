from feature_extractor.extractor import (
    fetch_website,
    get_page_size,
    get_compression_type,
    get_cache_control
)
from feature_extractor.parser import (
    get_title,
    get_image_count,
    get_css_count,
    get_js_count,
    get_meta_description,
    get_h1_count,
    get_internal_links_count,
    get_external_links_count,
    get_dom_elements_count,
    get_font_count,
    get_lazy_loading_count
    
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
print("Page Size:", get_page_size(url), "bytes")
print("DOM Elements:", get_dom_elements_count(soup))
print("Font Count:", get_font_count(soup))
print("Lazy Loading Images:", get_lazy_loading_count(soup))
print("Compression:", get_compression_type(url))
print("Cache Control:", get_cache_control(url))