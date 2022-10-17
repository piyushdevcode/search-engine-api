BLOCK_RESOURCE_TYPES = [
    "beacon",
    "csp_report",
    "font",
    "image",
    "imageset",
    "media",
    "object",
    "texttrack",
]


# we can also block popular 3rd party resources like tracking:
BLOCK_RESOURCE_NAMES = [
    "adzerk",
    "analytics",
    "cdn.api.twitter",
    "doubleclick",
    "exelator",
    "facebook",
    "fontawesome",
    "google",
    "google-analytics",
    "googletagmanager",
]


def intercept_route(route):
    """
    intercepts all requests and aborts the blocked one's
    """
    if route.request.resource_type in BLOCK_RESOURCE_TYPES:
        return route.abort()
    if any(key in route.request.url for key in BLOCK_RESOURCE_NAMES):
        return route.abort()

    return route.continue_()
