import tkinter
import gamelogic.gamemotor

class StartView:
    def __init__(self, root, end, result, start):
        self._root = root
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
        label = tkinter.Label(master=self._frame, text="Welcome to 2048 game",
                                font="Helvetica 16 bold")
        label2 = tkinter.Label(master=self._frame, text="Start a new game",
                                font="Helvetica 12 bold")
        name_label = tkinter.Label(master=self._frame, text="Player name (optional):")
        name_entry = tkinter.Entry(master=self._frame, textvariable=self._name)
        size_label = tkinter.Label(master=self._frame, text="Select grid size:")
        radiobutton = tkinter.Radiobutton(master=self._frame, text="3x3",
                                          value=3, variable=self._size)
        radiobutton2 = tkinter.Radiobutton(master=self._frame, text="4x4",
                                           value=4, variable=self._size)
        radiobutton3 = tkinter.Radiobutton(master=self._frame, text="5x5",
                                           value=5, variable=self._size)
        start_game_button = tkinter.Button(master=self._frame, text="Start",
                                            command=self._start_new_game, width=15)

        label4 = tkinter.Label(master=self._frame, text="Check top 10 results",
                                font="Helvetica 12 bold")
        button2 = tkinter.Button(master=self._frame, text="View", command=self._show_results_view,
                                width=15)

        label.grid(row=0, columnspan=4, padx=5, pady=5)
        label2.grid(row=1, columnspan=4, padx=5, pady=5)

        name_label.grid(row=2, padx=5, pady=5)
        name_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        size_label.grid(row=3, padx=5, pady=5)
        radiobutton.grid(row=3, column=1, padx=5, pady=5)
        radiobutton2.grid(row=3, column=2, padx=5, pady=5)
        radiobutton3.grid(row=3, column=3, padx=5, pady=5)

        start_game_button.grid(row=4, columnspan=4, padx=5, pady=5)

        label4.grid(row=5, columnspan=4, padx=5, pady=5)
        button2.grid(row=6, columnspan=4, padx=5, pady=5)

    def _start_new_game(self):
        motor = gamelogic.gamemotor.GameMotor(self._name.get(), self._size.get())
        motor.start()
        self._show_game_end_view()
