plaintext1 = input("Zadejte text, který chcete zasifrovat: ")
key1=int(input("Zadejte klic: "))

def caesar_encrypt(text, key):
    result = ""
    for char in text:
            if char.isalpha():
             xd = ord('A') if char.isupper() else ord('a')
             result = result + chr((ord(char) - xd + key) % 26 + xd)
            else:
             result+= char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

plain_text = plaintext1
key = key1

result = caesar_encrypt(plain_text, key)
print(f"Šifrovaný text: {result}")
print(f"Dešifrovaný text: {caesar_decrypt(result, key)}")

        