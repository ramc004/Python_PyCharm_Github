email = input("Enter your email:")
email_list = []

for i in email:
    email_list.append(i)
print(email_list)

for x in range(len(email_list)):
    if email_list[x] == "@":
        print("'@' symbol included.")
    if email_list[x] == ".":
        if len(email_list)-x == 4:
            if (email_list[x+1]+email_list[x+2]+email_list[x+3]) == "com":
                print("Domain included. ")
