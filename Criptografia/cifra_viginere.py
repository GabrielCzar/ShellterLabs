# Cifra de Viginere
from itertools import cycle
from functools import reduce

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print ('Key: %s' % key)
    print ('Plaintext: %s' % plaintext)
    print ('Encrytped: %s' % encrypted)
    print ('Decrytped: %s' % decrypted)

#show_result(input('Texto: '), input('key: '))
print (decrypt(input('key: '), input('Texto: ')))
