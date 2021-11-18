import game

def main():
    new_game = game.Game(3)

    command = ""

    while new_game.game_continues():
        print(new_game)
        print("1 left, 3 right, 5 up, 2 down, q quit")
        command = input("Command: ")
        if command == "1":
            print("Move left")
            if new_game.move_left() is True:
                new_game.new_tile()
        elif command == "3":
            print("Move right")
            if new_game.move_right() is True:
                new_game.new_tile()
        elif command == "5":
            print("Move up")
            if new_game.move_up() is True:
                new_game.new_tile()
        elif command =="2":
            print("Move down")
            if new_game.move_down() is True:
                new_game.new_tile()
        elif command == "q":
            print("Game ends")
            break
        else:
            print("Unknown command")
            print("1 left, 3 right, 5 up, 2 down, q quit")
    
    print(new_game)
    print("Game ended")

if __name__ == '__main__':
    main()