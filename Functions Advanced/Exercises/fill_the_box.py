def fill_the_box(heihgt, length, width, *args):

    volume = heihgt * length * width

    left_cubes = 0

    for item in args:

        if item == "Finish":
            break

        if item <= volume:
            volume -= item
        else:
            left_cubes += item - volume
            volume = 0



    if volume > 0:
        return f'There is free space in the box. You could put {volume} more cubes.'
    else:
        return f'No more free space! You have {left_cubes} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))