# Metro Cheese Scraper

Проект для сбора информации о сырах с сайта Metro. Использует многопоточность для одновременного парсинга данных из Москвы и Санкт-Петербурга.

## Возможности

- Параллельный сбор данных о сырах для Москвы и Санкт-Петербурга
- Сохранение результатов в JSON-файлы
- Обработка обычных и акционных цен
- Структурированный и типизированный код

## Требования

- Python 3.7+
- Зависимости из `requirements.txt`

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/anxnas/metro-cheese-scraper.git
   cd metro-cheese-scraper
   ```

2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

Запустите скрипт:

```
python main.py
```

Результаты будут сохранены в файлах `metro_cheeses_msk.json` и `metro_cheeses_spb.json`.

## Вклад в проект

1. Форкните репозиторий
2. Создайте новую ветку (`git checkout -b feature/NewFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add NewFeature'`)
4. Отправьте изменения в репозиторий (`git push origin feature/NewFeature`)
5. Создайте Pull Request

## Лицензия

Распространяется под лицензией MIT. Смотрите `LICENSE` для дополнительной информации.

## Контакты

Хренов Святослав - тг канал [@anxnas](https://t.me/anxnas) - slavakhrenov02@gmail.com