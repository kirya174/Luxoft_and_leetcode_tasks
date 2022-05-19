
from math import log2

n = int(input())
word_encoded = map(int, input().split())
alphabet = 'abcdefghijklmnopqrstuvwxyz '
word = ''
prev_char = 0
for char in word_encoded:
    val = int(log2(abs(char-prev_char)))
    word += alphabet[val]
    prev_char = char
print(word)