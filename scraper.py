import requests
from bs4 import BeautifulSoup


def get_website_text(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("article") or soup.find("main") or soup.body

    if content is None:
        raise ValueError("No readable content found on this page.")

    for tag in content.find_all(["script", "style", "nav", "footer"]):
        tag.decompose()

    return content.get_text(" ", strip=True)

if __name__ == "__main__":
    # print(get_website_text("https://www.atlassian.com/devops/what-is-devops/benefits-of-devops"))
    print(get_website_text("https://substack.com/home/post/p-212373735"))