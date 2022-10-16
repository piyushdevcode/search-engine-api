import contextlib
from playwright.sync_api import sync_playwright
import urllib

#! OPTIMIZING BROWSER REQ


def scrape_duck_results(query, pages=1):
    """
    scrapes search results from duckduckgo
    query: whose search result is required
    pages: no of pages to scrape
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        # generating our search url
        q = urllib.parse.urlencode({"q": query})

        url = f"https://duckduckgo.com/?{q}"

        page.goto(url)

        pages = int(pages)

        # to get more search results
        if pages > 1:
            for _ in range(pages):
                element_button = page.locator(".result--more__btn")
                element_button.click()

        # getting all the articles
        all_articles = page.locator("article")
        results = []

        for idx, article in enumerate(all_articles.element_handles(), 1):
            element_link = article.query_selector("h2")

            #! ----------- CAN be optimized --------------------
            element_snippet = element_link.query_selector("xpath=..").query_selector(
                "xpath=following-sibling::*"
            )
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

            # ads don't have favicon
            with contextlib.suppress(Exception):
                result["favicon"] = "https:" + article.query_selector(
                    "a > img"
                ).get_attribute("src")

            # every result doesn't have sitelinks
            if sitelinks:
                result["sitelinks"] = sitelinks

            results.append(result)

            with open("temp.json", "w", encoding="utf-8") as f:
                f.writelines(str(results))

        return results
