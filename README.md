# AstroPhoto Plus Desktop

This project is a thin wrapper around Chromium (using Qt WebEngine) to provide a native application for AstroPhoto Plus.

It's functionally identical to the browser version, but it offers the following advantages:

 - Native notifications (with sounds)
 - Server autodiscovery
 - Simple and minimal user interface

## Download and run

Currently the app is built for Linux (using AppImage universal package) and Windows (64 bit).

OSX should be available as well soon.

### Linux (AppImage)

 - Download one of the AppImage files from the [releases](https://github.com/GuLinux/AstroPhoto-Plus-Desktop/releases) page.
 - Move the file wherever you prefer
 - Right click on the AppImage file and, depending on your desktop environment, mark it as executable. If you prefer using a shell, just use `chmod a+x AstroPhoto_Plus_Desktop*.AppImage`.
 - Now just click or double click the file to launch the application.

### Windows

 - Download one of the Setup `exe` files from the [releases](https://github.com/GuLinux/AstroPhoto-Plus-Desktop/releases) page.
 - Double click the installer
 - Just follow the installer instructions. The installer will setup an icon in your Windows menu.
 - Launch _AstroPhoto Plus Desktop_. If the Windows firewall asks you about app network permissions, please allow everything.
