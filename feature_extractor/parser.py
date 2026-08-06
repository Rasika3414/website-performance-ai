def get_title(soup):
    """
    Extract website title.
    """

    if soup.title:
        return soup.title.string.strip()

    return "No Title"

def get_image_count(soup):
    return len(soup.find_all("img"))

def get_css_count(soup):
    return len(soup.find_all("link", rel="stylesheet"))

def get_js_count(soup):
    return len(soup.find_all("script", src=True))

def get_meta_description(soup):
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        return meta["content"]
    return "No Meta Description"

def get_h1_count(soup):
    return len(soup.find_all("h1"))

def get_internal_links_count(soup, base_url):
    count = 0

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href.startswith("/") or base_url in href:
            count += 1

    return count

def get_external_links_count(soup, base_url):
    count = 0

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href.startswith("http") and base_url not in href:
            count += 1

    return count