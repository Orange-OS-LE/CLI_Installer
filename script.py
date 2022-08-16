from time import time
import archinstall, os

if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
    raise PermissionError("You need to run this script with sudo or as root.")

archinstall.log("Welcome to the Orange OS LE Installer")
archinstall.log(
    "This will ask you some questions to help make your installation great!"
)
input("Press enter when you are ready to start!")


def menustuff():
    menu = archinstall.GlobalMenu(data_store=archinstall.arguments)

    menu.enable("archinstall-language")
    menu.enable("keyboard-layout")
    menu.enable("mirror-region")
    menu.enable("sys-language")
    menu.enable("sys-encoding")
    menu.enable("harddrives")
    menu.enable("disk_layouts")
    # bootloader and swap
    menu.enable("hostname")
    menu.enable("!root-password")
    menu.enable("!users")
    # profile and audio and kernel and packages and nip
    menu.enable("timezone")
    # ntp and additional repos
    menu.enable("__separator__")
    menu.enable("install")
    menu.enable("abort")
    menu.run()


def filesys():
    if archinstall.arguments.get("harddrives", None):
        print(
            "This is your last chance to stop the program before it makes un-revertable changes!"
        )
        print("Press command/control C to cancel.")
        archinstall.do_countdown()
        mode = archinstall.GPT
        if archinstall.has_uefi() is False:
            mode = archinstall.MBR

        for drive in archinstall.arguments.get("hardrives", []):
            if archinstall.arguments.get("disk_layouts", {}).get(drive.path):
                with archinstall.Filesystem(drive, mode) as fs:
                    fs.load_layout(archinstall.arguments["disk_layouts"][drive.path])


def do_install(mountpoint):

    with archinstall.Installer(
        mountpoint, base_packages=None, kernels=None
    ) as installation:
        if archinstall.arguments.get("disk_layouts"):
            installation.mount_ordered_layout(archinstall.arguments["disk_layouts"])

        for partion in installation.partitions:
            if partion.mountpoint == installation.target + "/boot":
                if partion.size < 0.19:
                    raise archinstall.DiskError(
                        f"The selected /boot partition in use is not large enough to properly install a boot loader. Please resize it to at least 200MiB and re-run the installation."
                    )

        while archinstall.service_state("reflector") not in ("dead", "failed"):
            time.sleep(1)
