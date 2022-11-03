# Orange OS LE CLI Install Script

The name says it all, a install script for the [Orange OS Linux Edition](https://scratch.mit.edu/discuss/topic/620114/) OS!

A GUI install system is coming soon, but for now, this is your only option.

## How to install:

### Using v86:
Since, by default, Arch Linux v86 doesn't come with internet support, you will need to do the curl command on your host, then send the install.py file to the emulator then run `python3 install.py` there.

### Installation (latest 0.2.0) (recommended for most people)
Download and boot an [Arch linux ISO](https://archlinux.org/download/), then in the live enviroment, connect to internet and run

```
curl https://orange-os-le.github.io/0.2.0_CLI_Install.txt > install.py
python3 install.py
```
You can replace 0.2.0 with the version you want to download.
0.0.0 is not an option.

Then answer the questions. Note, that this isn't the final release and a lot is missing.

### Raspberry Pi Edition (Dev Version) (Not recommended)

Setting up the raspberry pi for Orange OS LE is complicated, so first follow [this](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4) guide (signing in as "root"), then run
```
sudo pacman -Syu
sudo pacman -S python3
curl https://raw.githubusercontent.com/Orange-OS-LE/CLI_Installer/master/raspberry_pi.py > install.py
sudo python3 install.py
```

This has not been tested, so if you tried this please tell us what happened.

### Dev version (not recommended)

Download and boot an [Arch linux ISO](https://archlinux.org/download/), then in the live enviroment, run

```
curl https://raw.githubusercontent.com/Orange-OS-LE/CLI_Installer/master/script_part_1.py > install.py
python3 install.py
```

Then answer the questions. Note, that this isn't the final release and a lot is missing.

The install process is a bit buggy right now, so testing is apreciated.

### TheChaosCommunity's fork (0.2.0 alternative) (even less recommended)

Download and boot an [Arch linux ISO](https://archlinux.org/download/), then in the live enviroment, run

```
curl https://raw.githubusercontent.com/michaeleldar/CLI_Installer/master/script_part_1.py > install.py
python3 install.py
```

Then answer the questions. Note, that this isn't the final release and a lot is missing or different from the "official" version. ONLY USE THIS IF YOU KNOW WHAT YOU ARE DOING, AND KNOW THAT ISSUES FOR THIS SPECIFIC VERSION SHOULD BE REPORTED TO @UniqueName12345, NOT @michaeleldar!

The install process is a bit buggy right now, so testing is apreciated.

## Config (now released!)

### Config file syntax
```
line 1: Path to hard drive
line 2: Hostname
line 3: Keyboard layout (all lowercase)
line 4: Language locale
line 5: Timezone (slash between places, places starting with a capital letter)
line 6: Country
line 7: Amount of users to be added
```
After that, the lines are username, password and whether the user is a superuser (leave blank if not). Repeat those lines for each user.

You can find an example config file in examples/simple.config. Warning: That config file needs to be edited to work properly, for example the time-zone needs to be changed.

### How to use a config file

Run the installer with an extra argument, that being the config file path
```
python3 install.py my_config.config
```
## Credits

@michaeleldar (@applejuiceproduc on scratch) for the code.
@UniqueName12345 (@DifferentDance8 on scratch) for ideas and problem solving.
@ScratchcatandGobo (on scratch) for ideas.
@JaydenDev (@MagicCrayon9342 on scratch) for the iso (WIP) and ideas.
