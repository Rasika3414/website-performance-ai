def get_title(soup):
    """
    Extract website title.
    """
    if soup.title and soup.title.string:
        return soup.title.string.strip()

    return "No Title"


def get_image_count(soup):
    """
    Count images on the webpage.
    """
    return len(soup.find_all("img"))


def get_css_count(soup):
    """
    Count linked CSS files.
    """
    return len(soup.find_all("link", rel="stylesheet"))


def get_js_count(soup):
    """
    Count JavaScript files.
    """
    return len(soup.find_all("script", src=True))


def get_meta_description(soup):
    """
    Extract meta description.
    """
    meta = soup.find("meta", attrs={"name": "description"})

    if meta and meta.get("content"):
        return meta["content"].strip()

    return "No Meta Description"


def get_h1_count(soup):
    """
    Count H1 headings.
    """
    return len(soup.find_all("h1"))


def get_internal_links_count(soup, base_url):
    """
    Count internal links.
    """
    count = 0

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href.startswith("/") or base_url in href:
            count += 1

    return count


def get_external_links_count(soup, base_url):
    """
    Count external links.
    """
    count = 0

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href.startswith("http") and base_url not in href:
            count += 1

    return count


def get_dom_elements_count(soup):
    """
    Count all DOM elements.
    """
    return len(soup.find_all())


def get_font_count(soup):
    """
    Count detected font resources.
    """
    count = 0

    for link in soup.find_all("link", href=True):
        href = link["href"].lower()

        if (
            "fonts.googleapis.com" in href
            or "fonts.gstatic.com" in href
        ):
            count += 1

    for tag in soup.find_all(["style", "link"]):
        text = str(tag).lower()

        if "@font-face" in text:
            count += 1

    return count

def get_lazy_loading_count(soup):
    count = 0

    for img in soup.find_all("img"):
        if img.get("loading") == "lazy":
            count += 1

    return count