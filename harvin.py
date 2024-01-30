import requests
from bs4 import BeautifulSoup


def get_product_link_harwin(product_name):
    base_url = 'https://www.harwin.com/products/{}/'.format(product_name)
    response = requests.get(base_url)
    print(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_div = soup.find('div', class_='cta-group__item')


        if first_div:
            first_a_tag = first_div.find('a')
            if first_a_tag:
                product_link = first_a_tag['href']
                return product_link

    print(f"Hata: Ürün bulunamadı.")
    return None
