import serial, struct
from time import sleep
ser=serial.Serial('COM5', 9600)
points=0
val = '0'
i = 0
checknumber = 0
delay = 0
def testsequence(val, ser, points, checknumber, delay):# this is a simple strech to test out the code, it works great the goal is to just step on squares 2 and 6
#and bend and touch your hands on 3 and 7
    delay = 0
    checknumber = 0
    print("I will give you a square to step on, and you will be given 3 seconds to do so.")
    sleep(2)
    print("The quicker you step, the more points you earn.")
    sleep(2)
    print("Please put your left leg on square number 4.")
    sleep(1)
    print('Go!')
    val = '4'
    checknumber = 3
    delay = 1
    points = points+check(val, ser, i,checknumber, delay)
    print('Keep your left leg on square 2 and put your right leg on square 5')
    sleep(2)
    print('Go!')
    val = '5'
    checknumber = 3
    delay = 1
    points = points + check(val, ser, i, checknumber, delay)
    print("You should be standing up straight now.")
    print("Bend down and touch your left hand to square 7")
    sleep(2)
    print('Go!')
    val = '7'

    delay = 1
    checknumber = 3
    points = points + check(val, ser, i, checknumber, delay)
    print("Now touch your right hand to sqaure 8")
    print('Go!')
    val = '8'
    delay = 1
    checknumber = 3
    points = points + check(val, ser, i, checknumber, delay)
    print("Good job, no stand back up and put your feet on squares 5 and 8 facing square 4 and 7")
    sleep(2)
    print("Now lets do a little bit of dance")
    sleep(1)
    print("Put your right leg on square 11, touch your left leg on square 8 and then move it to square 2")
    sleep(2)
    print("Now touch your right leg on square 5 and move it back to square 11.")
    print("We'll repeat this circuit 3 times. You'll have a half second delay between each step.")
    sleep(3)
    print("Ready")
    sleep(1)
    print("Lets go")
    for x in range(2):
        print("11")
        val = '11'
        delay = 0.5
        checknumber = 1
        points = points + check(val, ser, i, checknumber, delay)
        print("8")
        val = '8'
        delay = 0.5
        checknumber = 1
        points = points + check(val, ser, i, checknumber, delay)
        print("2")
        val = '2'
        delay = 0.5
        checknumber = 1
    points = points + check(val, ser, i, checknumber,delay)

    print("5")
    val = '5'
    delay = 0.5
    checknumber = 1
    points = points + check(val, ser, i, checknumber, delay)
    print("Great job, test sequence succesfully completed")
    print("Your points are:", points)

def check(val, ser, i, checknumber, delay): # This is the checking function. Communication and point tracking happends here
    i =0
    y = checknumber
    incorrects = 0
    ser.write(val.encode())
    b = ser.readline()
    b = b.decode()
    b = b.strip()
    sleep(delay)
    for i in range(checknumber):# this loop checks the giving squar(val) a number(checknumber) of times
        if (b=="incorrect"):
            print(b)
            incorrects = incorrects+1
            ser.write(val.encode())
            sleep(delay)
            y = y-1
            b = ser.readline()
            b = b.decode()
            b = b.strip()
        else:
            print("correct")
            break
    sleep(y)
    points = checknumber - incorrects
    return(points)
    sleep(0.1) # wait (sleep) 0.1 seconds

testsequence(val, ser, points, checknumber, delay)