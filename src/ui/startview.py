import tkinter
import gamelogic.gamemotor

class StartView:
    def __init__(self, root, game, end, result, start):
        self._root = root
        self._show_game_view = game
        self._show_game_end_view = end
        self._show_results_view = result
        self._show_start_view = start
        self._frame = None
        self._name = tkinter.StringVar()
        self._size = tkinter.IntVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=tkinter.constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = tkinter.Frame(master=self._root)

        self._size.set(4)
        self._name.set("")
        label = tkinter.Label(master=self._frame, text="Welcome")
        label2 = tkinter.Label(master=self._frame, text="Start a new game")
        name_label = tkinter.Label(master=self._frame, text="Player name (optional)")
        name_entry = tkinter.Entry(master=self._frame, textvariable=self._name)
        size_label = tkinter.Label(master=self._frame, text="Select grid size:")
        radiobutton = tkinter.Radiobutton(master=self._frame, text="3x3",
                                          value=3, variable=self._size)
        radiobutton2 = tkinter.Radiobutton(master=self._frame, text="4x4",
                                           value=4, variable=self._size)
        radiobutton3 = tkinter.Radiobutton(master=self._frame, text="5x5", 
                                           value=5, variable=self._size)
        start_game_button = tkinter.Button(master=self._frame, text="Start", command=self._start_new_game)

        label4 = tkinter.Label(master=self._frame, text="Or watch previous results")
        button2 = tkinter.Button(master=self._frame, text="View", command=self._show_results_view)

        label.pack()
        label2.pack()

        name_label.pack()
        name_entry.pack()
        size_label.pack()
        radiobutton.pack()
        radiobutton2.pack()
        radiobutton3.pack()

        start_game_button.pack()

        label4.pack()
        button2.pack()
    
    def _start_new_game(self):
        self._show_game_view()
        motor = gamelogic.gamemotor.GameMotor(self._name.get(), self._size.get())
        motor.start()
        self._show_game_end_view()
