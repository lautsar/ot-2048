import game

def main():
    new_game = game.Game(4)

    command = ""

    while True:
        print(new_game)
        command = input("Command: ")
        if command == "1":
            print("Move left")
        elif command == "3":
            print("Move right")
        elif command == "5":
            print("Move up")
        elif command =="2":
            print("Move down")
        elif command == "q":
            print("Game ends")
            break
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()