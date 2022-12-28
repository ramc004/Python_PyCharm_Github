import webbrowser
import random

print("Welcome to a phone troubleshooting program")
sol1 = "Keep holding the power on button until the screen is on. If it doesn't turn on, contact your phone provider" \
       " to get a replacement."
sol2 = "Charge your phone fully and switch it on."
sol3 = "Delete some apps, you need a minimum of at least 5 GB of free  memory to run the phone correctly.You are " \
       "probably out of memory. "
sol4 = "Reset your phone."
sol5 = "You need a screen replacement. Either got to a shop or ask your insurance company covers the phone"
sol6 = "You need to get your buttons replaced!"
sol7 = "Get a screen replacement or contact your phone provider to get a  phone replacement."
sol8 = "You don't need to do anything. Your phone doesnt have any problems."
sol9 = "Please update your phone software."
sol10 = "The best advice that I would suggest is to either contact apple for support or visit a shop to get it fixed"
sol11 = "Take the phone and put it in a bag of rice for  24-36 hours to let the rice absorb the water."
while True:
    def apple():
        global prob_3, rnd
        prob_1 = None
        while prob_1 not in ('software', 'hardware'):
            prob_1 = input("Is your problem hardware or software").lower()

            if prob_1 == 'software':
                prob_2 = None
                while prob_2 not in ('yes', 'no'):
                    prob_2 = input("Does your iphone still turn on : yes or no").lower()

                if prob_2 == 'yes':
                    prob_3 = None
                    while prob_3 not in ('yes', 'no'):
                        prob_3 = input("Has your phone slowed down during usage?").lower()

                elif prob_2 == 'no':
                    print(
                        "Keep holding the power on button until the screen is on. If it doesn't turn on, contact your "
                        "phone provider to get a replacement.")
                    rnd = (int(random.randrange(50)) + 1)
                    print("If that does not work you should contact the apple. With the case number", str(rnd))

                if prob_3 == 'yes':
                    print(
                        "Delete some apps, you need a minimum of at least 5 GB of free  memory to run the phone "
                        "correctly.You are probably out of memory.")

                elif prob_3 == 'no':
                    prob_4 = "Is there a reoccurrence of a bug in the phone".lower()
                    if prob_4 == 'yes':
                        print("install a antivirus or reinstall/update the app")
                        Web_Cho = input(
                            "Would you like to visit the apple site to check if you still have a warranty left for "
                            "your phone: yes / no").lower()
                        if Web_Cho == 'yes':
                            webbrowser.open("http://www.apple.com/uk/support/")
                        elif Web_Cho == 'no':
                            print("Hopefully you get the phone fixed. Contact us for more queries")
                    elif prob_4 == 'no':
                        print(sol7)

            elif prob_1 == 'hardware':
                prob = None
                while prob not in ('yes', 'no'):
                    prob = input("Has your phone been in contact with water in the last 48 hours").lower()
                if prob == 'yes':
                    prob2 = None
                    while prob2 not in ('yes', 'no'):
                        prob2 = input("Does your iphone still turn on").lower()

                        if prob2 == 'no':
                            print(sol10)
                            print("if that doesnt work then try", sol9)
                        elif prob2 == 'yes':
                            prob6 = input("Has the water entered the internal screen")
                            if prob6 == 'yes':
                                print(
                                    "You should contact apple. They will deal with your case. If the phone still has "
                                    "the 1 year warranty then it will be cost free.\n If not then you will have to "
                                    "pay")
                                print("If it not fixable then you should look for a replacement")
                                break
                            elif prob6 == 'no':
                                print(sol7)
                elif prob == 'no':
                    prob_3 = input("Is your phone screen cracked or not: yes / no").lower()
                    if prob_3 == 'yes':
                        print(
                            "The best advice that I would suggest is to either contact apple for support or visit a "
                            "shop to get the screen fix")
                        Web_Cho = input(
                            "Would you like to visit the apple site to check if you still have a warranty left for "
                            "your phone: yes / no").lower()
                        if Web_Cho == 'yes':
                            webbrowser.open("http://www.apple.com/uk/support/")
                        elif Web_Cho == 'no':
                            print("Hopefully you get the phone fixed.  Contact us for more queries")
                    elif prob_3 == 'no':
                        prob4 = input("Are your headphone port or charging port not working").lower()
                        if prob4 == 'yes':
                            prob5 = None
                            while prob5 not in (
                                    'earphone port', 'earphone', 'headphone', 'headphone port', 'charging',
                                    'charging port'):
                                prob5 = input(
                                    "Which port is not working : earphone/headphone port or charging port").lower()
                            if prob5 == 'earphone port':
                                print(
                                    "The best advice that I would suggest is to either contact apple for support or "
                                    "visit a shop to get it fixed")
                            elif prob5 == 'charging port':
                                print(
                                    "You should contact us for more detail and we will look further into the problem "
                                    "and hopefully we can fix it ASAP")
                                print("Your case number is", rnd, "Use this number when contacting our repair service.")


    def android():
        global prob_3, rnd2
        prob_1 = None
        while prob_1 not in ('software', 'hardware'):
            prob_1 = input("Is your problem hardware or software").lower()

            if prob_1 == 'software':
                prob_2 = None
                while prob_2 not in ('yes', 'no'):
                    prob_2 = input("Does your iphone still turn on : yes or no").lower()

                if prob_2 == 'yes':
                    prob_3 = None
                    while prob_3 not in ('yes', 'no'):
                        prob_3 = input("Has your phone slowed down during usage?").lower()
                if prob_3 == 'yes':
                    print(
                        "Delete some apps, you need a minimum of at least 5 GB of free  memory to run the phone "
                        "correctly.You are probably out of memory.")
                elif prob_2 == 'no':
                    print(
                        "Keep holding the power on button until the screen is on. If it doesn't turn on, contact your "
                        "phone provider to get a replacement.")
                    rnd2 = (int(random.randrange(50)) + 1)
                    print("If that does not work you should contact the apple. With the case number", str(rnd2))

                elif prob_3 == 'no':
                    prob_4 = "Is there a virus in the phone".lower()
                    if prob_4 == 'yes':
                        print("install a antivirus or stuff")
                        Web_Cho = input(
                            "Would you like to visit the apple site to check if you still have a warranty left for "
                            "your phone: yes / no").lower()
                        if Web_Cho == 'yes':
                            webbrowser.open("http://www.apple.com/uk/support/")
                        elif Web_Cho == 'no':
                            print("Hopefully you get the phone fixed. Contact us for more queries")
                    elif prob_4 == 'no':
                        print(sol7)

            elif prob_1 == 'hardware':
                prob = None
                while prob not in ('yes', 'no'):
                    prob = input("Has your phone been in contact with water in the last 48 hours").lower()
                if prob == 'yes':
                    prob2 = None
                    while prob2 not in ('yes', 'no'):
                        prob2 = input("Does your iphone still turn on").lower()

                        if prob2 == 'no':
                            print(sol10)
                            print("if that doesnt work then try", sol9)
                        elif prob2 == 'yes':
                            prob6 = input("Has the water entered the internal screen")
                            if prob6 == 'yes':
                                print(
                                    "You should contact apple. They will deal with your case. If the phone still has "
                                    "the 1 year warranty then it will be cost free.\n If not then you will have to "
                                    "pay")
                                print("If it not fixable then you should look for a replacement")
                                break
                            elif prob6 == 'no':
                                print(sol7)
                elif prob == 'no':
                    prob_3 = input("Is your phone screen cracked or not: yes / no").lower()
                    if prob_3 == 'yes':
                        print(
                            "The best advice that I would suggest is to either contact apple for support or visit a "
                            "shop to get the screen fix")
                        Web_Cho = input(
                            "Would you like to visit the apple site to check if you still have a warranty left for "
                            "your phone: yes / no").lower()
                        if Web_Cho == 'yes':
                            webbrowser.open("http://www.apple.com/uk/support/")
                        elif Web_Cho == 'no':
                            print("Hopefully you get the phone fixed.  Contact us for more queries")
                    elif prob_3 == 'no':
                        prob4 = input("Are your headphone port or charging port not working").lower()
                        if prob4 == 'yes':
                            prob5 = None
                            while prob5 not in (
                                    'earphone port', 'earphone', 'headphone', 'headphone port', 'charging',
                                    'charging port'):
                                prob5 = input(
                                    "Which port is not working : earphone/headphone port or charging port").lower()
                            if prob5 == 'earphone port':
                                print(
                                    "The best advice that I would suggest is to either contact apple for support or "
                                    "visit a shop to get it fixed")
                            elif prob5 == 'charging port':
                                print(
                                    "You should contact us for more detail and we will look further into the problem "
                                    "and hopefully we can fix it ASAP")
                                print("Your case number is", rnd2,
                                      "Use this number when contacting our repair service.")


    phone_Ty = input("What type of phone do you have : apple / android").lower()
    if phone_Ty == 'apple':
        apple()
        WebCho = input(
            "Would you like to visit the apple site to check if you still have any queries: yes / no").lower()
        if WebCho == 'yes':
            webbrowser.open("http://www.apple.com/uk/support/")
        elif WebCho == 'no':
            print("Hopefully you get the phone fixed. Contact us for more queries")



    elif phone_Ty == 'android':
        android()
        WebCho = input(
            'Would you like to visit the apple site to check if you still have a warranty left for your phone: '
            'yes / no').lower()
        if WebCho == 'yes':
            webbrowser.open("http://www.samsung.com/uk/support/")
        elif WebCho == 'no':
            print("Hopefully you get the phone fixed.  Contact us for more queries")
