def encrypt(text, s):
    result = ""


def text(args):
    pass


for i in range(len(text)):
    char = text[i]
    if not char.isupper():
        result += chr((ord(char) + s - 97) % 26 + 97)
    else:
        result += chr((ord(char) + s - 65) % 26 + 65)
    return result
# check the above function
text = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))