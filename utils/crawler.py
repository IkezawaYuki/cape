from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    domain = "hp-standard.jp"
    url = f"https://{domain}/"
    response = requests.get(url + "sitemap.xml")

    soup = BeautifulSoup(response.content, 'lxml-xml')

    loc_tags = soup.find_all('loc')

    words = []
    # 抽出した 'a' タグの表示
    for loc_tag in loc_tags:
        response = requests.get(loc_tag.text)
        soup = BeautifulSoup(response.content, 'lxml-xml')
        l_tags = soup.find_all('loc')

        for l_tag in l_tags:
            if l_tag.text.endswith(".png") or l_tag.text.endswith(".jpg") or l_tag.text.endswith("jpeg"):
                continue
            resp = requests.get(l_tag.text)
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()
            text = soup.get_text(separator=' ', strip=True)
            words.append(text)

    with open(f"{domain}.json", "w", encoding="utf-8") as f:
        for word in words:
            f.write(word)