import archinstall, os

if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
    raise PermissionError("You need to run this script with sudo or as root.")

print("Welcome to the Orange OS LE Installer")
print("This will ask you some questions to help make your installation great!")
input("Press enter when you are ready to start!")
'''
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
'''
menu = archinstall.GlobalMenu(data_store=archinstall.arguments)

menu.enable("archinstall-language")
menu.enable("abort")
menu.run()
