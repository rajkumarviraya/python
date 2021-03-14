count_start = 0
count_stop = 5
started = False

while count_start < count_stop:

    i = input(">")

    count_start += 1

    if i == "help":

        start = print("start - start the car")
        stop = print("stop  - stop the car")
        quit = print("quit - to exit")

    elif (i == "start"):

        if started:

            print("car already started")

        else:

            started = True
            print("car started")


    elif i == "stop":

        if not started:

            print("car already stoped")

        else:

            started = False

            print("car stoped")


    elif i == "quit":

        print("exit")

        break
    else:

        print("i cant understard")










