from threaded_scraper import ThreadedMetroScraper
from utils.data_saver import DataSaver

def main() -> None:
    threaded_scraper = ThreadedMetroScraper()
    results = threaded_scraper.scrape_all(100)

    for city, cheeses in results.items():
        DataSaver.save_to_json(cheeses, f'metro_cheeses_{city}.json')
        print(f"Спарсено товаров для {city}: {len(cheeses)}")

if __name__ == "__main__":
    main()