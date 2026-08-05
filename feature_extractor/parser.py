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