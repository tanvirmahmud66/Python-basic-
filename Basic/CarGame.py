q = False
started = False
while not q:
    command = input("Enter Command: ")
    if command.lower() == "help":
        print("Start -> to Start the car")
        print("Stop -> to Stop the car")
        print("Quit -> to quit the game")
    elif command.lower() == 'start':
        if not started:
            started = True
            print("Car Engine started..Ready to go!!")
        else:
            print("Car Engine already started")
    elif command.lower() == 'stop':
        if started:
            started = False
            print("Car engine stopped")
        else:
            print("Car engine already stopped")
    elif command.lower() == 'quit':
        q = True
        print("Exited from the Game")
        break
    else:
        print("wrong command  :(")
