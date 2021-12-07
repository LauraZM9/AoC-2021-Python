

def get_final_position(steps: list) -> int:
    """Calculates the coordinates of the postion of the submarine, returns their product.

    Args:
        steps (list): list of instructions for the submarine (strings)

    Returns:
        (int): product of x and depth
    """

    x = 0
    depth = 0
    for coo in steps:
        coo = coo.split(" ")
        if coo[0] == "forward":
            x += int(coo[1])
        elif coo[0] == "down":
            depth += int(coo[1])
        else:
            depth -= int(coo[1])
    return x * depth


# print(get_final_position(data))


def get_correct_position(instructions: list) -> int:
    """Calculates the coordinates of the postion of the submarine with the correct formula and returns their product

    Args:
        instructions (list): list of instructions for the submarine (strings)

    Returns:
        int: product of x and depth
    """
    x = 0
    depth = 0
    aim = 0
    for coo in instructions:
        coo = coo.split(" ")
        if coo[0] == "forward":
            x += int(coo[1])
            depth += aim * int(coo[1])
        elif coo[0] == "down":
            aim += int(coo[1])
        else:
            aim -= int(coo[1])
    return x * depth


# print(get_correct_position(data))
