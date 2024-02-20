"""
Task:-

● Create a file called alternative.py
● Write a program that reads in a string and makes each alternate
character into an upper case character and each other alternate character
a lower case character.
e.g. The string “Hello World” would become “HeLlO WoRlD”
● Now, try starting with the same string but making each alternative word
lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”.

"""

# To alter alternate char in the string

# Take the string from user
string_before_alter = input(" Please enter a string you wish ")

# comprehension way
"""
makes each even character into an upper case character 
if i % 2 == 0 will be true if the index is even
and each odd character a lower case character
looping over the length of string as range
using join method to concatenate each letter to form a string

"""

string_after_alter = "".join(string_before_alter[i].upper() if i % 2 == 0
                             else string_before_alter[i].lower() for i in range(len(string_before_alter)))

# for i in range(len(string_before_alter)):
#     # checking the condition for even index
#     # and making even indexed character to upper and odd indexed char to lower
#     if i % 2 == 0:
#         string_after_alter += string_before_alter[i].upper()
#     else:
#         string_after_alter += string_before_alter[i].lower()

# print the result string
print(f"Alteration of alternative charactor result {string_after_alter}")

# To alter alternate words in the string

# converting a string to list of words
# and iterating over list using enumerate as we need both position and word
# word_after_alter = " "
# for pos, word in enumerate(list(string_before_alter.split(" "))):
# pos % 2 == 0 checking the condition for even index
# and making even indexed word to lower and odd indexed word to upper

word_list_before = list(string_before_alter.split(" "))
# created empty list to save result
word_list_after = " ".join([word.lower() if pos % 2 == 0 else word.upper() for pos, word in enumerate(word_list_before)])
print(f"Alteration of alternative word result {word_list_after}")
