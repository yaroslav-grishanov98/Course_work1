import argparse
import json
from datetime import datetime
from typing import Any, Dict

from src.utils import logger
from src.views import generate_events_page_response, generate_main_page_response


def main() -> Dict[str, Any]:
    """Главная функция программы, парсит аргументы командной строки и
    генерирует соответствующий JSON-ответ"""
    parser = argparse.ArgumentParser(description="Генерация данных для финансовых отчетов")
    parser.add_argument("--page", choices=["main", "events"], default="main",
                        help="Страница для генерации (main или events)")
    parser.add_argument("--date", help="Дата в формате YYYY-MM-DD",
                        default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--period", choices=["W", "M", "Y", "ALL"], default="M",
    help="Период для страницы events (W - неделя, M - месяц, Y - год, ALL - все данные)")

    args = parser.parse_args()

    try:
        date_str = f"{args.date} 12:00:00"

        if args.page == "main":
            response = generate_main_page_response(date_str)
        else:
            response = generate_events_page_response(date_str, args.period)

        print(json.dumps(response, indent=2, ensure_ascii=False))

        logger.info(f"Программа успешно выполнена для страницы {args.page}")
        return response
    except Exception as e:
        logger.error(f"Ошибка программы: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    main()
