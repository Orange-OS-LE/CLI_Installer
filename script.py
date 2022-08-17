import sys

print("Welcome to the Orange OS LE 1.0.0-alpha install script.")
print("We will ask you a few questions to make sure you get a great configuration.")

hard_drive = input("Please input your disk drive file, like /dev/sda: ")
host_name = input(
    "Please enter the name you want to give your computer (a.k.a your hostname): "
)
keyboard_layout = input("Now enter your keyboard layout, like uk or us: ")

user_config = open("user_configuration.json", "w")
user_config.write(
    f"""
{'{'}
"config_version": "2.5.0",
"debug": false,
"harddrives": [
    "{hard_drive}"
],
"hostname": "{host_name}",
"keyboard-layout": "{keyboard_layout}",
"mount_point": null, 
"nic": {'{'}
    "dhcp": true,
    "dns": null,
    "gateway": null,
    "iface": null,
    "ip": null,
    "type": "iso"
{'}'},
"plugin": null,
"profile": {'{'}
    "path": "/usr/lib/
{'}'}
"""
)
print(sys.version)
