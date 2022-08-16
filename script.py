import archinstall, os

if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
    raise PermissionError("You need to run this script with sudo or as root.")

print("Welcome to the Orange OS LE Installer")
print("This will ask you some questions to help make your installation great!")
input("Press enter when you are ready to start!")
menu = archinstall.GlobalMenu(data_store=archinstall.arguments)

menu.enable("archinstall-language")
menu.enable("abort")
menu.run()
