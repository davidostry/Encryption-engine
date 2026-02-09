from function import atbash_cipher

def show_encryption_menu():
    user_text = input("Enter text to encrypt: ")
    user_choice = input()
    "Please choose encryption method:\n"
    "1. Caesar Cipher\n"
    "2. Rail Fence Cipher\n"
    "3. Atbash Cipher\n"
    if user_choice == "1":
        pass
    elif user_choice == "2":
        pass
    elif user_choice == "3":
        encrypted_result = atbash_cipher(user_text)
        return encrypted_result
print(show_encryption_menu())