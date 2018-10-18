import sys
from cs50 import get_string


def main():
    # check to see if argc value is > 2
    if len(sys.argv) != 2:
        print('Usage: ./caesar k')
        exit(1)
# convert argument string to an integer
    key = int(sys.argv[1]) % 26
# get user input for a string
    plain_text = get_string('plaintext : ')
    cipher_text = ''
# iterate through the plain_Text string
    for char in plain_text:
        if char.isupper():
            # calculate alphabetical index of each char in plain_text
            cipher_text += chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        elif char.islower():
            cipher_text += chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        else:
            cipher_text += char

    print('ciphertext: ' + cipher_text)


if __name__ == '__main__':
    main()
