# Orange OS LE CLI Install Script

The name says it all, a install script for the [Orange OS Linux Edition](https://scratch.mit.edu/discuss/topic/620114/) OS!

A GUI install system is coming soon, but for now, this is your only option.

Note: 0.1.1 is broken, but 0.1.2 will be out soon to fix that.

## How to install:

### A stable version (latest 0.1.2) (recommended for most people)
Download and boot an [Arch linux ISO](https://archlinux.org/download/), then in the live enviroment, run

```
curl https://orange-os-le.github.io/0.1.2_CLI_Install.txt > install.py
python3 install.py
```
You can replace 0.1.2 with the version you want to download.
0.0.0 is not an option.

Then answer the questions. Note, that this isn't the final release and a lot is missing.

The install process is a bit buggy right now, so testing is apreciated.

### Beta version (0.2.0) (not recommended)

Download and boot an [Arch linux ISO](https://archlinux.org/download/), then in the live enviroment, run

```
curl https://raw.githubusercontent.com/Orange-OS-LE/CLI_Installer/master/script_part_1.py > install.py
python3 install.py
```

Then answer the questions. Note, that this isn't the final release and a lot is missing.

The install process is a bit buggy right now, so testing is apreciated.

### TheChaosCommunity's fork (0.3.0 beta) (even less recommended)

Download and boot an [Arch linux ISO](https://archlinux.org/download/), then in the live enviroment, run

```
curl https://raw.githubusercontent.com/TheChaosCommunity/CLI_Installer/master/script_part_1.py > install.py
python3 install.py
```

Then answer the questions. Note, that this isn't the final release and a lot is missing or different from the "official" version. ONLY USE THIS IF YOU KNOW WHAT YOU ARE DOING, AND KNOW THAT ISSUES FOR THIS SPECIFIC VERSION SHOULD BE REPORTED TO @UniqueName12345, NOT @michaeleldar!

The install process is a bit buggy right now, so testing is apreciated.

## Roadmap
```
0.1.x (released) - Adds gnome desktop enviroment
0.2.x (beta) - Config file support
0.3.x - UI changes
0.4.x - Adds some gnome extensions
1.0.x - Adds an updating system
```

This roadmap may not be completely followed.

## Config (not released yet) (probably broken)

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

You can find an example config file in examples/simple.config.

### How to use a config file

Run the installer with an extra argument, that being the config file path
```
python3 install.py my_config.config
```
## Credits

@michaeleldar (@applejuiceproduc on scratch) for the code.
@UniqueName12345 (@DifferentDance8 on scratch) for ideas and problem solving.
@ScratchcatandGobo (on scratch) for ideas.
