import archinstall

print("Welcome to the Orange OS LE Installer")
print("This will ask you some questions to help make your installation great!")
invalidInput = True
while invalidInput:
    choice = input("1. What language do you use? ")
    try:
        test = archinstall.select_language(choice)
    except:
        continue
    invalidInput = False
print(test)
