import time

def timer(h, m, s):
    
    t = (3600*h) + (60*m) + (s)

    while (t > 0):
        print(t)
        time.sleep(1)
        t = t-1
    print("TIMER STOP")


hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

timer(hours, minutes, seconds)




