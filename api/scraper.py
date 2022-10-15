from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    # go to url
    page.goto("https://duckduckgo.com/?q=latest+news")

    all_articles = page.locator("article")
    results = []

    for idx, article in enumerate(all_articles.element_handles(), 1):
        sitelinks = []
        element_link = article.query_selector("h2")
        element_snippet = element_link.query_selector("xpath=..").query_selector(
            "xpath=following-sibling::*"
        )
        element_sitelink = article.locator("div >>nth=-1")
        for link in element_sitelink.element_handles():
            sitelinks.append(
                {"title": link.inner_text(), "link": link.get_attribute("href")}
            )
        result = {
            "position": idx,
            "title": element_link.inner_text(),
            "link": element_link.query_selector("a").get_attribute("href"),
            "snippet": element_snippet.inner_text(),
            "favicon": article.query_selector("a > img").get_attribute("src"),
            "sitelinks": sitelinks,
        }
        results.append(result)

    print(results)
