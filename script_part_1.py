"""
This program is an installer for Orange OS LE, you can find more information in the README
    Copyright (C) 2022 Michael Halpin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# There is no part 2 of this script anymore, but the name remains for backward compatability.

import sys, os

hard_drive = ""
host_name = ""
keyboard_layout = ""
language = ""
time_zone = ""
location = ""

def ui():
    global hard_drive, host_name, keyboard_layout, language, time_zone, location
    print("Welcome to the Orange OS LE install script.")
    print("We will ask you a few questions to make sure you get a great configuration.")

    hard_drive = input("Please input your disk drive file, like /dev/sda: ")
    host_name = input(
    "Please enter the name you want to give your computer (a.k.a your hostname): "
    )
    keyboard_layout = input("Now enter your keyboard layout, like uk or us: ")

    language = input(
        'Now please enter your locale language. This should be something like "en_US": '
    )

    time_zone = input(
        "Now we need your timezone, this is usually in the format of <Continent>/<City>, e.g Europe/Paris: "
    )

    location = input(
        "Finally, we need to know what country you live in. If you don't want to answer this, enter worldwide."
    ).capitalize()

    print("Okay, now we are going to setup users for you.")
    with open("user_credentials.json", "w") as user_creds:
        user_creds.write(
            """{
        "!users": ["""
        )
        users_no = int(input("First, how many users do you want the system to hold: "))
        for x in range(users_no):
            user_creds.write("{\n")
            username = input(f"Ok what the you want the username of user {x + 1} to be: ")
            password = input(f"Now, what password do you want to give {username}: ")
            superuser = input(
                f"Lastly do you want {username} to be a superuser? Leave blank if you don't: "
            )
            user_creds.write(f'"!password": "{password}",\n')
            if superuser:
                user_creds.write('"sudo": true,\n')
            else:
                user_creds.write('"sudo": false,\n')

            user_creds.write(f'"username": "{username}"\n')
            user_creds.write("}")
            if x == users_no - 1:
                user_creds.write("\n")
            else:
                user_creds.write(",\n")
        user_creds.write("]\n}")

def config_file():
    global hard_drive, host_name, keyboard_layout, language, time_zone, location
    config = open(sys.argv[1], 'r')
    hard_drive = config.readline().replace("\n", "")
    host_name = config.readline().replace("\n", "")
    keyboard_layout = config.readline().replace("\n", "")
    language = config.readline().replace("\n", "")
    time_zone = config.readline().replace("\n", "")
    location = config.readline().capitalize().replace("\n", "")
    with open("user_credentials.json", "w") as user_creds:
        user_creds.write("""{
        "!users": [""")
        users_no = int(config.readline().replace("\n", ""))
        for x in range(users_no):
            user_creds.write("{\n")
            username = config.readline().replace("\n", "")
            password = config.readline().replace("\n", "")
            superuser = config.readline().replace("\n", "")
            user_creds.write(f'"!password": "{password}",\n')
            if superuser:
                user_creds.write('"sudo": true,\n')
            else:
                user_creds.write('"sudo": false,\n')
            user_creds.write(f'"username": "{username}"\n')
            user_creds.write("}")
            if x == users_no - 1:
                user_creds.write("\n")
            else:
                user_creds.write(",\n")
        user_creds.write("]\n}")




if sys.argv.__len__() == 2:
    config_file()
else:
    ui()


with open("user_configuration.json", "w") as user_config:
    user_config.write(
        f"""{'{'}
"additional-repositories": "",
"audio": "pipewire",
"bootloader": "grub-install",
"filesystem": "ext4",
"HSM": null,
"config_version": "2.5.0",
"debug": false,
"harddrives": [
    "{hard_drive}"
],
"kernels": [
    "linux"
],
"swap": true,
"keyboard-language": "{keyboard_layout}",
"mirror-region": "{location}",
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
"ntp": true,
"plugin": null,
"profile": {'{'}
    "path": "/usr/lib/python3.10/site-packages/archinstall/profiles/minimal.py"
{'}'},
"script": "guided",
"silent": false,
"sys-language": "{language}",
"sys-encoding": "utf-8",
"timezone": "{time_zone}",
"version": "2.5.0",
"packages": ["git", "python3"],
"custom-commands": [
        "pacman -S xorg xorg-server --noconfirm",
        "pacman -S gnome --noconfirm"
]
{'}'}"""
    )
print("Now we will setup the disks for you. Unfourtuanatley, we can't offer to let you")
print("do the disk partioning, but we might offer this in future.")
confirm_installation = input(
    "This will delete all data on the disk you have chosen,\nIf you agree to the conditions, submit with a \"Y\". Otherwise, submit with any other letter."
)

user_disks = open("user_disk_layout.json", "w")
user_disks.write(
    f"""{'{'}
    "{hard_drive}": {'{'}
        "partitions": [
            {'{'}
                "boot": true,
                "encrypted": false,
                "filesystem": {'{'}
                    "format": "fat32"
                {'}'},
                "mountpoint": "/boot",
                "size": "{'203MiB' if not os.path.exists("/sys/firmware/efi") else '512MiB'}",
                "start": "{'3MiB' if not os.path.exists("/sys/firmware/efi") else '1MiB'}",
                "type": "primary",
                "wipe": true
            {'}'},
            {'{'}
                "encrypted": false,
                "filesystem": {'{'}
                    "format": "ext4",
                    "mount_options": []
                {'}'},
                "mountpoint": "/",
                "size": "100%",
                "start": "{'206MiB' if not os.path.exists("/sys/firmware/efi") else '513MiB'}",
                "type": "primary",
                "wipe": true
            {'}'}
        ],
        "wipe": true
    {'}'}
{'}'}"""
)
user_disks.close()
os.system(
    "sudo archinstall --silent --config ./user_configuration.json --creds ./user_credentials.json --disk_layouts ./user_disk_layout.json"
)
os.system(
    "sudo archinstall --silent --config ./user_configuration.json --creds ./user_credentials.json --disk_layouts ./user_disk_layout.json"
)