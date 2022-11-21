text="0P"
List=[letter.lower() for letter in text if letter.isalpha() or letter.isnumeric()]
print(List==List[::-1])