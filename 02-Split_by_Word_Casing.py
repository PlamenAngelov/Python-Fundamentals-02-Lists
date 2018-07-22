inp_str = input()
lowercase_list = []
uppercase_list = []
mixed_list = []
char_for_replacement = [",", ";", ":", ".", "!", "(", ")", "\"", "'", "\\", "/", "[", "]"]

for char in char_for_replacement:
    inp_str = inp_str.replace(str(char)," ")

inp_list = inp_str.split()

for word in inp_list:
    if word == word.lower() and word.isalpha():
        lowercase_list.append(word)
    elif word == word.upper() and word.isalpha():
        uppercase_list.append(word)
    else:
        mixed_list.append(word)

lowercase_str = ", ".join(lowercase_list)
print(f"Lower-case: {lowercase_str}")

mixed_str = ", ".join(mixed_list)
print(f"Mixed-case: {mixed_str}")

uppercase_str = ", ".join(uppercase_list)
print(f"Upper-case: {uppercase_str}")