floors="<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>><>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<><><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><><><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><<>><<>><<>><"


def getFloor(flooors):
    """ Checks the floor a person is on """
    counter =0
    for i in floors:
        if i == '<':
            counter+=1
        else:
            counter-=1
    return counter

print("Which floor did John end up on? ")
print("John ended on the {}th Floor." .format(getFloor(floors)))
