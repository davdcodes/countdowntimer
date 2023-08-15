import time

retime = "n"

while retime != "q":

    option = input("Would you like to count in (s)econds, (m)inutes, or (h)ours: ")

    timer = int(input("Enter how long would you like your timer to be set for: "))

    currtime = 0
    starttime = time.time()
    endtime = 1

    if option == "s":
        endtime = starttime + timer
    elif option == "m":
        endtime = starttime + (timer*60)
    elif option == "h":
        endtime == starttime + (timer*360)

    while currtime < endtime:
        currtime = time.time()

    print("Time Finished!")

    retime = input("Enter any key if you'd like to time again, or 'q' to quit: ")

print("Thank you for using my countdown timer!")