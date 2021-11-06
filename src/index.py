import game

def main():
    new_game = game.Game(4)

    command = ""

    while True:
        print(new_game)
        command = input("Command: ")
        if command == "1":
            print("Move left")
            new_game.move_left()
        elif command == "3":
            print("Move right")
            new_game.move_right()
        elif command == "5":
            print("Move up")
            new_game.move_up()
        elif command =="2":
            print("Move down")
            new_game.move_down()
        elif command == "q":
            print("Game ends")
            break
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()