import os

term = os.system
term("sudo pacman -Syu")
term("sudo pacman -S git")
term("sudo pacman -S fish")
os_release = """NAME="Orange OS LE"
ID=orange-os-le
ID_LIKE=arch
PRETTY_NAME="Orange OS LE 1.0.0 alpha (Genesis)"
VARIANT="Desktop Edition"
VARIANT_ID=desktop
VERSION="1.0.0 alpha 1.1.0 (Genesis)"
VERSION_ID=1.0.0-alpha-1.1.0
VERSION_CODENAME=genesis
HOME_URL=https://duskend6.wixsite.com/orange-os-le
DOCUMENTATION_URL=https://duskend6.wixsite.com/orange-os-le/documentation
SUPPORT_URL=https://duskend6.wixsite.com/orange-os-le/forum
BUG_REPORT_URL=https://duskend6.wixsite.com/orange-os-le/forum
ANSI_COLOR="\\033[48;2;255;165;0m"
DEFAULT_HOSTNAME="orangeosle\""""
term(f"sudo echo {os_release} > /etc/os-release")
term(f"sudo echo {os_release} > /usr/lib/os-release")