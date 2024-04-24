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

text = 'Раз. Два. Три. Четыре. Пять. Прием!'

print(*_get_part_text(text, 5, 9), sep='\n')

text = ('Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, '
        'что можно сделать. И никаких возражений! Завтра, значит, завтра!')

print(*_get_part_text(text, 22, 145), sep='\n')

text = ('— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть '
        'ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, '
        'в чём вопрос.')

print(*_get_part_text(text, 54, 70), sep='\n')