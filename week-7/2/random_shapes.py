from ShapeGenerator import ShapeGenerator


def main():

    ###
    # Get the desired file name
    ###
    fileName = input("\n> Enter a name for the generated shape file data: ")

    ###
    # Get the desired shape count
    ###
    shapeCount = int(input("> How many shapes shoud we create? "))

    lines = []

    current = 1

    while current <= shapeCount:

        shape = ShapeGenerator().random()

        lines.append(shape)

        current = current + 1

    f = open("myfile.txt", "w")

    for line in lines:

        f.write(f'{line}\n')

    f.close()


main()
