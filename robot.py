

# TODO: Decompose into functions
def move_forward(length):
    '''
    Function to specify amount to move forward by

    parameters:
        length: The number of steps to move forward
    '''
    print("* Move Forward "+str(length))

def turn_right(degrees):
    '''
    Function for specified how much to turn by

    Parameters:
        degrees: amount to turn by specified in degrees
    '''
    print("* Turn Right "+str(degrees)+" degrees")
def move_square():
    '''
    Function for moving in a square of size 'size'
    '''
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        move_forward(size)
        turn_right(degrees)
def move_rectangle():
    '''
    Function for moving in a rectangleof size 'length'
    '''
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        move_forward(length)
        turn_right(degrees)
        move_forward(width)
        turn_right(degrees)

def move_circle():
    '''
    Function for moving in a circle
    '''
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        move_forward(length)
        turn_right(degrees)

def square_dancing():
    '''
    Function displays 4 squares of side size 20
    '''
    print("Square dancing - 3 squares of size 20")
    length = 20
    size = 20
    degrees = 90
    for i in range(3):
        move_forward(length)
        print("Moving in a square of size 20")
        for j in range(4):
            move_forward(size)
            turn_right(degrees)
            
def crop_circle():
    '''
    Function display 4 cropped circles
    '''
    print("Crop circles - 4 circles")
    length = 20
    degrees = 1
    for i in range(4):
        print("* Move Forward "+str(20))
        print("Moving in a circle")
        length = 1
        for k in range(360):
            move_forward(length)
            turn_right(degrees)
            
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
