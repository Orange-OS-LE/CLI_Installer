"""
This program is an installer for Orange OS LE Raspberry Pi Edition, you can find more information in the README
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

import os

# Thanks to this guide: https://gist.github.com/theramiyer/cb2b406128e54faa12c37e1a01f7ae15#install-packages for some of the commands.
os.system(
    "pacman -S --needed --noconfirm nfs-utils blueman autofs alsa-utils alsa-firmware alsa-lib alsa-plugins git wget base-devel binutils diffutils libnewt dialog wpa_supplicant wireless_tools iw crda lshw sudo"
)

os.system(
    "mkdir builds && cd builds && git clone https://aur.archlinux.org/bluez-utils-compat.git && makepkg -si && git clone https://aur.archlinux.org/pi-bluetooth.git && cd pi-bluetooth && makepkg -si"
)

os.system("systemctl enable bluetooth.service")
os.system("systemctl start bluetooth.service")


os.system(
    "pacman -S --noconfirm pulseaudio-alsa pulseaudio-bluetooth pavucontrol bluez bluez-libs bluez-utils bluez-firmware"
)
os.system('echo "dtparam=audio=on" >> /boot/config.txt')

os.system("pacman -S --noconfirm xorg xorg-server gnome")

os.system("systemctl enable gdm.service")
