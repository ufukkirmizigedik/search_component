import requests
from bs4 import BeautifulSoup


def get_product_link_weller(product_name):
    base_url = 'https://www.weller-tools.com/us/en/search?search='
    search_url = base_url + product_name.replace(' ', '+')
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_div = soup.find('div', class_='product-teaser__cta')

        if first_div:
            first_a_tag = first_div.find('a')
            if first_a_tag:
                product_link = first_a_tag['href']
                print(product_link)
                return product_link

    print(f"Hata: Ürün bulunamadı.")
    return None