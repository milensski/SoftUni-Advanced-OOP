def rectangle(lenght,width):

    if not isinstance(lenght,int) or not isinstance(width,int):
        return "Enter valid values!"

    def area():
        return f'Rectangle area: {lenght*width}'

    def perimeter():
        return f'Rectangle perimeter: {2*lenght+ 2*width}'

    return f"{area()}\n{perimeter()}"


print(rectangle(2, 10))

print(rectangle('2', 10))