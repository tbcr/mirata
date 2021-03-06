#Mirata v0.6 - The Linux setup utility for AlephOne
#by Brandon Clark and Chance Callahan

#    This file is part of mirata.

#    mirata is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    mirata is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with mirata.  If not, see <https://www.gnu.org/licenses/>.

#    This application downloads both snap images of the alephone source port (https://github.com/Aleph-One-Marathon/alephone)
#    and free-to-download scenario files that are property of Bungie LLC.
import os
import grabber
import time
import subprocess
import argparse
import sys
import requests

from tqdm import tqdm
from whichcraft import which


url = "http://174.109.47.119/files/alephone.snap"

act_os = 60
sup_os = ['Ubuntu', 'Fedora', 'Arch', 'Gentoo', 'openSUSE', 'Sabayon']


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--override-snap-bugout", help="Overrides sanity check for snapcraft.", action="store_true")
    parser.add_argument("--target-os", help="Select target OS, see --eligible-targets", action="store")
    parser.add_argument("--eligible-targets", help="Eligible Target Platforms: Ubuntu, Fedora, Arch, Gentoo, openSUSE, Sabayon")
    parser.add_argument("--refactor-override", help="No one in their sane mind would use this flag right now.", BaseException="store_true")
    args = parser.parse_args()

# This subroutine basically keeps some idiot from running the program in it's current state. Like us.

def refactor_safety(refactor_override):
    if refactor_override == True:
        print("Bless your heart, you stupid fool. Running as normal, and may God have mercy on your computer.")
        # At some point, we should add the call to the subrouting that runs this mess.
        print("SURPRISE! We haven't added the call for the actual code execution yet. Bye!")
        sys.quit()
    else:
        print("Just... don't even bother trying to run this code right now. You'll need to perform an exorcism if you do, and you probably can't afford both a technomancer and whatever the hourly rate right now the Catholic Church is charging.")
        sys.quit()

def os_preprocessing(act_os, target_os):
    if target_os == "Ubuntu":
        act_os=0
    elif target_os == "Fedora":
        act_os=1
    elif target_os == "Arch":
        act_os=2
    elif target_os == "Gentoo":
        act_os=3
    elif target_os == "openSUSE":
        act_os=4
    elif target_os == "Sabayon":
        act_os=5
    else:
        print("Fatal Error in the OS Preprocessing Subroutine. Good Night.")
    sys.quit()

def title_banner():
    os.system('clear')
    print("mirata, the Linux setup tool for AlephOne")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it under certain conditions.")
    print '-' * 20
    time.sleep(3)
    os_select()

def os_select(act_os, sup_os):
    if act_os == 60:
        print("Before we begin, please select your distro")
        print("------------------------------------------")
        print("1)Fedora")
        print("2)Ubuntu")
        print("3)Arch")
        print("4)Gentoo")
        print("5)openSUSE")
        print("6)Sabayon(Equo)")
        print("")
        act_os = input("Selection: ")
        act_os = act_os - 1
    else:
        print("I see you have selected " + sup_os[act_os] + " as your install target during runtime. Continuing unattended.")
    snap_dl()

def snap_dl(url):
    print('Downloading the snap file...')
    response = requests.get(url, stream=True)

    with open("alpehone.snap", wb) as handle:
        for data in tqdm(response.iter_content()):
    handle.write(data)

def check_for_snap():
    # Checks if snap is in the system PATH
    if which('snap') is not None:
        installmirata()
    else:
        bugout_nosnap()

def bugout_nosnap():
    #Checks if we are overriding the bugout
    if args.override-snap-bugout is True:
        installmirata()
    else:
        print("I can't seem to find snapcraft on this system. Either add it to your path, or use --override-snap-bugout to bypass this sanity check")
        #Sweet Dreams
    sys.exit()


refactor_safety(refactor_override)








