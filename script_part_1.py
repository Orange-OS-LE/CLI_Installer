import sys

print("Welcome to the Orange OS LE 1.0.0-alpha install script.")
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
    "path": "/usr/lib/python3.10/site-packages/archinstall/profiles/minimal.py"
{'}'},
"script": "guided",
"silent": false,
"sys-language": "{language}",
"timezone": "{time_zone}",
"version": "2.5.0"
{'}'}
"""
)
user_config.close()
print("Okay, now we are going to setup users for you.")
user_creds = open("user_credentials.json", "w")
user_creds.write(
    """
{
    "!users": [
"""
)
users_no = int(input("First, how many users do you want the system to hold: "))
for x in range(0, users_no):
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
