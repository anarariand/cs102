def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if not char.isalpha():
            ciphertext = ciphertext + char
        else:
            d = 'A' if char.isupper() else 'a'
            cipher = (((ord(char) + 3) - ord(d)) % 26) + ord(d)
            ciphertext = ciphertext + chr(cipher)
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if not char.isalpha():
            plaintext = plaintext + char
        else:
            d = 'A' if char.isupper() else 'a'
            cipher = (((ord(char) + 23) - ord(d)) % 26) + ord(d)
            plaintext = plaintext + chr(cipher)
    return plaintext
