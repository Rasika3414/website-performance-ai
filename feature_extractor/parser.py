def get_title(soup):
    """
    Extract website title.
    """

    if soup.title:
        return soup.title.string.strip()

    return "No Title"