"""
Примечание: Данная фунция работает только с латинским алфавитом.
"""


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_char = char  # Если символ не буква, оставляем его без изменений
        encrypted_text += encrypted_char
    return encrypted_text


plain_text = input("Введите текст для шифрования: ")
shift_amount = 3
encrypted_text = caesar_cipher(plain_text, shift_amount)
print("Зашифрованный текст: ", encrypted_text)