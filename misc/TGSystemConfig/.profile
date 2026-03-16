# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# START startup log
echo $(date +%F_%T) "OS("$(grep -E '^(ID|DEBIAN_VERSION_FULL|VERSION_CODENAME)=' /etc/os-release | tac | cut -d= -f2 | paste -sd " ")") started successfully." > Documents/TGLockSystem/logs/startup.log

# To set the system time from RTC
#if [ $(date +%Y) -lt 2026 ]; then
sudo hwclock -s
echo "- OS time restored from RTC (DS3231)." >> Documents/TGLockSystem/logs/startup.log
#fi

# Make TGLockSystem global system-wide
export PATH=$PATH:$TGLOCKSYS
echo "- TGLockSystem path has been add to global path" >> Documents/TGLockSystem/logs/startup.log
