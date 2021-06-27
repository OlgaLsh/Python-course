import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
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
    lower_case_chars = 'abcdefghijklmnopqrstuvwxyz'
    for ch in plaintext:
        if ch.isalpha():
            if ch.islower():
                ciphertext += lower_case_chars[(lower_case_chars.index(ch) + shift) % len(lower_case_chars)]
            else:
                ciphertext += lower_case_chars[(lower_case_chars.index(ch.lower()) + shift) % len(lower_case_chars)].upper()
        else:
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
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
    lower_case_chars = 'abcdefghijklmnopqrstuvwxyz'
    for ch in ciphertext:
        if ch.isalpha():
            if ch.islower():
                plaintext += lower_case_chars[(lower_case_chars.index(ch) - shift) % len(lower_case_chars)]
            else:
                plaintext += lower_case_chars[(lower_case_chars.index(ch.lower()) - shift) % len(lower_case_chars)].upper()
        else:
            plaintext += ch
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
