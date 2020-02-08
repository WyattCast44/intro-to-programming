# Header

"""
Week 1 Review - Part 3
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
Write a program that outputs the following fight song. Your program is required to have a function named `sing_fight_song`. When the `sing_fight_song` function is called it should "sing" the song below by printing it out.

You should create other functions to show structure and to eliminate redundancy in your program. More precisely, your `sing_fight_song` function should not consist solely of print statements printing each line of the song. That would be highly redundant. It should call other functions that print reusable parts of the song.
"""

# Solution 1 

song = """
Go, team, go!
Defeat your foe.

Go, team, go!
Defeat your foe.
Simply the best,
Better than the rest.
Go, team, go!
Defeat your foe.

Go, team, go!
Defeat your foe.
Simply the best,
Better than the rest.
Go, team, go!
Defeat your foe.

Go, team, go!
Defeat your foe.
"""

# Solution 2

uniqueSongLines = [
    "Go, team, go!",
    "Defeat your foe.",
    "Simply the best,",
    "Better than the rest.",
    ""
]

def printSongLines(*lines):
    for line in lines:
       print(uniqueSongLines[line])


def sing_fight_song():

    # Solution 1
    # print(song)

    # Solution 2
    printSongLines(
        # first stanze
        4, 0, 1, 4,

        # second stanza
        0, 1, 2, 3, 0, 1, 4,

        # third stanza
        0, 1, 2, 3, 0, 1, 4,

        # last stanze
        0, 1, 4
    )

sing_fight_song()