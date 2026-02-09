def atbash_cipher(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_text += alphabet[25 - char_index]
        else:
            encrypted_text += char

    return encrypted_text