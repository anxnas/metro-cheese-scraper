from abc import ABC, abstractmethod
from typing import List, Dict
from bs4 import BeautifulSoup
import requests
from models.product import Product

class AbstractScraper(ABC):
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url: str = base_url
        self.headers: Dict[str, str] = headers

    @abstractmethod
    def scrape(self, num_products: int) -> List[Product]:
        pass

    def get_soup(self, url: str) -> BeautifulSoup:
        response: requests.Response = requests.get(url, headers=self.headers)
        return BeautifulSoup(response.content, 'html.parser')