def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
   plaintext = "ATTACKATDAWN"
   keyword = "LEMON"
   ciphertext = ""
   nonaplhacount = 0 
   for index, char in enumerate(plaintext):
       if not char.isalpha():
           ciphertext = ciphertext + char
           nonalphacount += 1
        d = 'A' if char.isupper() else 'a'
        keyword_char_index = (index - nonalphacount)%len(keyword)
        keyword_char = keyword[keyword_char_index].upper() if char.isupper() else keyword[keyword_char_index]
        key = ord(keyword_char) - ord(d)
        cipher = (((ord(char) + key) - ord(d)) % 26) + ord(d)
        ciphertext = ciphertext + chr(cipher)
    print(ciphertext)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    ciphertext = "LXFOPVEFRNHR"
    keyword = "LEMON"
    plaintext = ""
    nonaplhacount = 0 
    for index, char in enumerate(ciphertext):
       if not char.isalpha():
           plaintext = plaintext + char
           nonalphacount += 1
        d = 'A' if char.isupper() else 'a'
        keyword_char_index = (index - nonalphacount)%len(keyword)
        keyword_char = keyword[keyword_char_index].upper() if char.isupper() else keyword[keyword_char_index]
        key = ord(keyword_char) - ord(d)
        key = 26 - key
        cipher = (((ord(char) + key) - ord(d)) % 26) + ord(d)
        plaintext = plaintext + chr(cipher)
    print(plaintext)
    return plaintext