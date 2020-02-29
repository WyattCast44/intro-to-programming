from random import randint


def rollDice(sides=6):
    return randint(1, sides)


def main():

    DICE_SIDES = 6

    # Keep track of mathmatically possible values the user can enter
    reachableValues = list(range(2, (DICE_SIDES * 2) + 1))

    # Keep track of rolls
    attempts = []

    # Get the desired sum, convert to int
    desiredSum = int(input('\n> What is the sum we are going for? '))

    # Validate user input
    while not desiredSum in reachableValues:
        print('\nThat value is not attainable given the dice. Please try again\n')

        desiredSum = int(input('> What is the sum we are going for? '))

    # Get the first attempt
    attempts.append([
        rollDice(DICE_SIDES),
        rollDice(DICE_SIDES)
    ])

    # Loop while the last rolls sum is not equal to the desired sum
    while sum(attempts[-1:][0]) != desiredSum:
        attempts.append([
            rollDice(DICE_SIDES),
            rollDice(DICE_SIDES)
        ])

    print()

    # Print out attempts
    for attempt in attempts:
        print(
            f'Roll: {attempt[0]} and {attempt[1]}, sum is {sum(attempt)}')

    # Print the total number of rolls
    print(f'\nGot it in {len(attempts)} attempts!')


main()
