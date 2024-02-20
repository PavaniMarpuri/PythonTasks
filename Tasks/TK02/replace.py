"""
Task:-

● Create a new Python file in this folder called replace.py.
● Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a
single string.
○ Reprint this sentence as “The quick brown fox jumps over the lazy
dog.”
○ Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER
THE LAZY DOG.”
○ Reprint the sentence in reverse.
"""

# creating a string with sentence
string_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(string_sentence)

# replacing the '!' mark in the sentence and printing it
string_sentence = string_sentence.replace("!", " ")
print(string_sentence)

# printing the sentence in capital letters
print(string_sentence.upper())

# printing the sentence in reverse order

print(string_sentence.upper()[::-1])




