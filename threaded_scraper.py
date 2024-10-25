import threading
from queue import Queue
from typing import Dict, List
from models.product import Product
from scrapers.metro_scraper import MetroScraper

class ThreadedMetroScraper:
    def __init__(self):
        self.msk_scraper: MetroScraper = MetroScraper("msk")
        self.spb_scraper: MetroScraper = MetroScraper("spb")
        self.result_queue: Queue = Queue()

    def scrape_city(self, scraper: MetroScraper, num_products: int) -> None:
        cheeses = scraper.scrape(num_products)
        self.result_queue.put((scraper.city, cheeses))

    def scrape_all(self, num_products: int) -> Dict[str, List[Product]]:
        threads = [
            threading.Thread(target=self.scrape_city, args=(self.msk_scraper, num_products)),
            threading.Thread(target=self.scrape_city, args=(self.spb_scraper, num_products))
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        results = {}
        while not self.result_queue.empty():
            city, cheeses = self.result_queue.get()
            results[city] = cheeses

        return results