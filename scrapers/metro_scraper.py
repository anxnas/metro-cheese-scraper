from decimal import Decimal
from typing import List, Optional, Dict
from bs4 import Tag, BeautifulSoup
import time
from models.product import Product
from parsers.price_parser import PriceParser
from scrapers.abstract_scraper import AbstractScraper

class MetroScraper(AbstractScraper):
    def __init__(self, city: str):
        base_url: str = "https://online.metro-cc.ru"
        headers: Dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        if city == "msk":
            headers["Cookie"] = "metroStoreId=10; metroStore=%7B%22id%22%3A%2210%22%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B5%20%D1%88.%2C%20%D0%B4.%2013%D0%90%22%2C%22city%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%7D"
        elif city == "spb":
            headers["Cookie"] = "metroStoreId=15; metroStore=%7B%22id%22%3A%2215%22%2C%22name%22%3A%22%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%2C%20%D0%9A%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D0%BD%D1%82%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80.%2C%20%D0%B4.%203%22%2C%22city%22%3A%22%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%7D"
        super().__init__(base_url, headers)
        self.city: str = city

    def scrape(self, num_products: int) -> List[Product]:
        url: str = f"{self.base_url}/category/molochnye-prodkuty-syry-i-yayca/syry/polutverdye?from=under_search"
        products: List[Product] = []
        page: int = 1

        while len(products) < num_products:
            soup: BeautifulSoup = self.get_soup(f"{url}&page={page}&in_stock=1")

            for product_card in soup.find_all('div', class_='product-card'):
                if len(products) >= num_products:
                    break

                product: Product = self.parse_product(product_card)
                products.append(product)

                print(f"Продуктов спарсено: {len(products)}")
                time.sleep(0.5)

            page += 1
            time.sleep(1)

        return products

    def parse_product(self, product_card: Tag) -> Product:
        product_id: int = int(product_card['data-sku'])
        name: str = product_card.find('span', class_='product-card-name__text').text.strip()
        link: str = self.base_url + product_card.find('a', class_='product-card-photo__link')['href']

        product_soup: BeautifulSoup = self.get_soup(link)

        brand: str = product_soup.find_all('li', class_='product-attributes__list-item')[6].find('a', class_='product-attributes__list-item-link reset-link active-blue-text').text.strip()

        regular_price: Optional[Tag] = product_soup.find('span', class_='product-price nowrap product-unit-prices__actual style--product-page-major-actual')
        promo_price: Optional[Tag] = product_soup.find('span', class_='product-price nowrap product-unit-prices__actual style--product-page-major-actual color--red')
        old_price: Optional[Tag] = product_soup.find('span', class_='product-price nowrap product-unit-prices__old style--product-page-major-old')

        if promo_price:
            regular_price_str: Optional[str] = old_price.find('span', class_='product-price__sum').find('span', class_='product-price__sum-rubles').text.strip() if old_price else None
            promo_price_str: str = promo_price.find('span', class_='product-price__sum').find('span', class_='product-price__sum-rubles').text.strip()
        else:
            regular_price_str: Optional[str] = regular_price.find('span', class_='product-price__sum').find('span', class_='product-price__sum-rubles').text.strip() if regular_price else None
            promo_price_str: Optional[str] = None

        regular_price_decimal: Optional[Decimal] = PriceParser.parse(regular_price_str)
        promo_price_decimal: Optional[Decimal] = PriceParser.parse(promo_price_str)

        return Product(product_id, name, link, regular_price_decimal, promo_price_decimal, brand)