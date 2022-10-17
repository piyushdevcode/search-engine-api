import contextlib
from playwright.sync_api import sync_playwright
import urllib
from api.route_interceptor import intercept_route


def scrape_duck_results(query, pages_to_scrape=1):
    """
    scrapes search results from duckduckgo
    query: whose search result is required
    pages_to_scrape: no of pages to scrape
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, devtools=False)

        # for intercepting the route
        page = browser.new_page()

        # generating our search url
        q = urllib.parse.urlencode({"q": query})

        url = f"https://duckduckgo.com/?{q}"

        page.route("**/*", intercept_route)
        page.goto(url)

        pages_to_scrape = int(pages_to_scrape)

        ads = page.locator("#ads article")
        no_of_ads = ads.count()

        page.pause()
        # to get more search results
        if pages_to_scrape > 1:
            for _ in range(pages_to_scrape):
                element_button = page.locator(".result--more__btn")
                element_button.click()

        # getting all the articles
        all_articles = page.locator("article")
        results = []

        # to remove the ads result in our response slicing the articles list
        for idx, article in enumerate(all_articles.element_handles()[no_of_ads:], 1):
            element_link = article.query_selector("h2")

            element_snippet = article.query_selector(":nth-child(3)")

            element_sitelink = article.query_selector_all(":nth-child(4) a")

            sitelinks = [
                {"title": link.inner_text(), "link": link.get_attribute("href")}
                for link in element_sitelink
            ]

            result = {
                "position": idx,
                "title": element_link.inner_text(),
                "link": element_link.query_selector("a").get_attribute("href"),
                "snippet": element_snippet.inner_text(),
            }

            # handling ads don't have favicon
            with contextlib.suppress(Exception):
                result["favicon"] = "https:" + article.query_selector(
                    "a > img"
                ).get_attribute("src")

            # every result doesn't have sitelinks
            if sitelinks:
                result["sitelinks"] = sitelinks

            results.append(result)

        return results
