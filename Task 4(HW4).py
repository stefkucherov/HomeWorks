def censor_prohibited_words(text, prohibited_words):
    """
    Заменяет запрещённые слова в тексте звездочками.

    Args:
        text (str): Исходный текст.
        prohibited_words (list): Список запрещённых слов.

    Returns:
        str: Текст с заменёнными запрещёнными словами.
    """
    for word in prohibited_words:
        text = text.replace(word, '*' * len(word))
    return text


def main():
    # Заготовленный текст для замены
    original_text = """«Ублюдок, мать твою, а ну, иди сюда, говно собачье, а? Сдуру решил ко мне лезть, ты? Засранец вонючий, мать твою, а?"""

    # Список запрещенных слов
    prohibited_words = ["Ублюдок", "говно собачье", "Засранец вонючий", "мать твою", ]

    # Замена запрещенных слов
    censored_text = censor_prohibited_words(original_text, prohibited_words)

    print("Исходный текст:")
    print(original_text)
    print("\nТекст с заменой запрещённых слов:")
    print(censored_text)


if __name__ == "__main__":
    main()
