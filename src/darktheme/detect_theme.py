##
## PERSONAL PROJECT, 2022
## YouTubeDownloader
## File description:
## detect theme of os and set the current screen according to the theme
##

import subprocess
import platform

def is_dark_theme_windows():
    print("check windows")
    return True

def is_dark_theme_macos():
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])

def is_dark_theme_linux():
    try:
        out = subprocess.run(
            ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],
            capture_output=True)
        stdout = out.stdout.decode()
    except Exception:
        return False
    theme = stdout.lower().strip()[1:-1]
    if '-dark' in theme.lower():
        return True
    else:
        return False

def check_dark_theme():
    match platform.system():
        case 'Windows':
            # chec if windows is supported
            return is_dark_theme_windows()
        case 'Linux':
            return is_dark_theme_linux()
        case 'Darwin':
            return is_dark_theme_macos()
        case _:
            print("Your os is not supported yet.")
            return False