import os
import sys
import re

book: dict[int, str] = {}
BOOK_PATH = 'books/book.txt'
PAGE_SIZE = 1050


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    cropped_text = text[start:start + size]
    punctuation = [',', '.', '!', '?', ':', ';']
    last_punctuation_index = max(cropped_text.rfind(char) for char in punctuation)
    if len(cropped_text) < size or text[start + last_punctuation_index + 1] not in punctuation:
        result_text = cropped_text[:last_punctuation_index + 1]
    else:
        cropped_text = cropped_text.rstrip(''.join(punctuation))
        last_punctuation_index = max(cropped_text.rfind(char) for char in punctuation)
        result_text = cropped_text[:last_punctuation_index + 1]
    return result_text, len(result_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
            i = 0
            while text:
                i += 1
                page = _get_part_text(text, 0, PAGE_SIZE)
                book[i] = page[0]
                text = text[len(book[i]):].lstrip()
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


# Вызов функции prepare_book для подготовки книги из текстового файла
# prepare_book(os.path.join(os.path.dirname(sys.path[0]), os.path.normpath(BOOK_PATH)))
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))