print("# 2.3 personal message")
name = input(print("Please enter you name:"))
print("Hello", name, ", would you like to learn some Python today?")

print("# 2.4 name cases")
name = input(print("Please enter your name:"))
print(name.lower())
print(name.upper())
print(name.titlecase())

print("# 2.5 famous quote")
name_of_author = Einstein
quote = "A person who never made a mistake never tried anything new"
print(name_of_author, "once said,", quote, ".")

print("# 2.6 famous quote 2")
var = print(name_of_author, "once said,", quote, ".") == famous_person
message = famous_person
print(message)

print("#2.7 Stripping Names")
name_whitespaces = input(print("\tWhat is your name?\t"))
name_whitespaces2 = input(print("\nWHat is your name?\n"))
print(name_whitespaces.rstrip())
print(name_whitespaces.lstrip())
print(name_whitespaces.strip())
print(name_whitespaces2.rstrip())
print(name_whitespaces2.lstrip())
print(name_whitespaces2.strip())
