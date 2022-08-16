import archinstall

print("Welcome to the Orange OS LE Installer")
print("This will ask you some questions to help make your installation great!")
invalidInput = True
while invalidInput:
    choice = input("1. What language do you use? ")
    try:
        out = archinstall.select_language(choice.capitalize())
    except:
        print("Sorry, that didn't work. Here are all the options: ")
        print(
            """
Czech
Dutch
English
French
German
Italian
Polish
Portuguese
Russian
Spanish
Swedish
Turkish
Urdu
        """
        )
        continue
    invalidInput = False
print(out)
