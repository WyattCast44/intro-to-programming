import os
import sys
import time


def clearConsole():
    try:
        os.system('clear')
    except:
        os.system('cls')


def sleep(seconds):
    time.sleep(seconds)


def main():
    consoleWidth = 50
    printDelay = 0.10

    introCrawl = """

            STAR WARS
            ORDER 66

    Battles rage across known space.
    The Galactic Republic is crumbling
    under the continuous attacks by
    the Separatist droid army.

    The Jedi council is in turmoil.
    The Dark side has clouded a 
    plot to destroy the Jedi.

    In his hunt for the evil General 
    Grevious, General Kenobi and the
    501st Legion find themselves on 
    the bare planet of Utapau.

    Commander Cody of the 501st has 
    found himself facing his own 
    battle within the war...

    """

    for letter in introCrawl:
        sleep(0.065)
        sys.stdout.write(letter)
        sys.stdout.flush()


main()
