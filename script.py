import archinstall, os

if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
    raise PermissionError("You need to run this script with sudo or as root.")

archinstall.log("Welcome to the Orange OS LE Installer")
archinstall.log(
    "This will ask you some questions to help make your installation great!"
)
input("Press enter when you are ready to start!")
menu = archinstall.GlobalMenu(data_store=archinstall.arguments)

menu.enable("archinstall-language")
menu.enable("keyboard-layout")
menu.enable("mirror-region")
menu.enable("sys-language")
menu.enable("abort")
menu.run()
