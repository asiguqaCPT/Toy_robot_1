

# TODO: Decompose into functions
def move_square():
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def square_dancing():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        size = 20
        for j in range(4):
            degrees = 90
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")

def crop_circle():
    print("Crop circles - 4 circles")
    length = 20
    degrees = 1
    for i in range(4):
        print("* Move Forward "+str(20))
        print("Moving in a circle")
        length = 1
        for k in range(360):
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")



def move():
    '''
    move_in_shapes()

    The name explicitly states that the function is for moving in shapes
    '''
    move_square()
    move_rectangle()
    move_circle()
    square_dancing()
    crop_circle()

def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
