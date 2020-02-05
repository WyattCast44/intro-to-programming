# Header

"""
Week 4 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
A mad lib is a game where you take a sentence and fill in some of the words to make a (typically) silly story. For example, you might make up a sentence "She ate the [noun] and [past_tense_verb]." Then someone else picks a noun and a past tense verb at random, like "alarm clock" and "smiled", and they are put into the sentence to make "She ate the alarm clock and smiled." Usually the mad libs are a much longer story, but this is the general idea.

You are to create your own mad lib. Here is an example:

Madlib Maker
name: Paul
place: airport
verb: wait

Old Mc-Paul had a airport, E-I-E-I-O
And on that airport he liked to wait, E-I-E-I-O
With a wait wait here, and a wait wait there, everywhere a wait wait
I picked part of a song, and you could too, but your mad lib should:

have at least three lines or sentences
have at least three and no more than eight replacements (mine are name, place, and verb) and two of them must be present in more than one sentence (e.g., in the example note how `airport` is lines 1 and 2, and `wait` is in lines 2 and 3)
not use the concatenation operator: +. Why? Because although it is straightforward to do so, your solution would very likely be tedious and would not work for more than just your sentences. String methods exist to make work with Strings more efficient than that. You can solve this simply with sequences and some String methods (maybe string formatting?).
HINT: If you find yourself devising an elaborate algorithm involving programming content we have not yet covered (e.g., conditionals), you are overthinking it.
"""

# Solution

from helpers import *

template = """
The wheels on the [VEHICLE] go round and round
Round and round
The wheels on the [VEHICLE] go round and round
Round and round
All through [PLACE]

The wipers on the [VEHICLE] go Swish, swish, swish
Swish, swish, swish
The wipers on the [VEHICLE] go Swish, swish, swish
Swish, swish, swish
All through [PLACE]

[NAME] in the [VEHICLE] says "[GREETING], [GREETING], [GREETING]",
[NAME] in the [VEHICLE] says "[GREETING], [GREETING], [GREETING]"
All through [PLACE]

The doors on the [VEHICLE] go open and close
Open and close
The doors on the [VEHICLE] go open and close
Open and close
All through [PLACE]
"""

def main():
    # Welcome
    print(success('\nMadLib Maker 1000 - v0.1.0'))
    print(success('----------------------------'))
    print(info('- Give me a couple of words and I\'ll give you a MadLib\n\n'))
    
    # Name
    print('Let\'s start with a name:')
    name = bold(input('> '))

    # Place
    print(f'\nOkay {name}, how about a place?')
    place = bold(input('> '))

    # Vehicle
    print('\nQuick think a vehicle, something with wheels!')
    vehicle = bold(input('> '))

    # Greeting
    print('\nAlright last one... we need a greeting:')
    greeting = bold(input('> '))

    # Print Result
    print(success('\nHere you go!'))
    print(success('------------------------------------------'))

    print(template.replace('[NAME]', name).replace('[PLACE]', place).replace('[VEHICLE]', vehicle).replace('[GREETING]', greeting))

    print(success('------------------------------------------'))
    print(success('Thanks for playing!'))

main()