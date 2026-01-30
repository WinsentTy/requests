
def request(method, url, **kwargs):
    """
    Sends a request using the specified HTTP method.

    :param method: str, the HTTP method to use (e.g., 'GET', 'POST').
    :param url: str, the URL for the request.
    :param kwargs: Additional parameters for request configuration, 
                   such as headers and data.
    :return: Response object containing the server's response to the HTTP request.
    :raises: HTTPError, ConnectionError, Timeout, and other exceptions derived from
    RequestException.
    """
    # function implementation
