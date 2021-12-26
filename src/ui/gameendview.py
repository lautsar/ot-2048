import tkinter
import data.datahandling

class GameEndView:
    def __init__(self, root, end, result, start):
        self._root = root
        self._show_game_end_view = end
        self._show_results_view = result
        self._show_start_view = start
        self._frame = None
        self._datahandler = data.datahandling.DataHandling()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=tkinter.constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        results = list(self._datahandler.get_latest_result().values())
        self._frame = tkinter.Frame(master=self._root)

        if results[3] == 2048:
            label = tkinter.Label(master=self._frame, text="You won!",
                                    font="Helvetica 12 bold")
        else:
            label = tkinter.Label(master=self._frame, text="Game ended",
                                    font="Helvetica 12 bold")

        label2 = tkinter.Label(master=self._frame, text="Here are your results",
                                font="Helvetica 10 bold")
        label_name = tkinter.Label(master=self._frame, text="Player name:")
        label_size = tkinter.Label(master=self._frame, text="Size:")
        label_moves = tkinter.Label(master=self._frame, text="Made moves:")
        label_biggest = tkinter.Label(master=self._frame, text="Biggest:")
        label_name2 = tkinter.Label(master=self._frame, text=str(results[0]))
        label_size2 = tkinter.Label(master=self._frame, text=str(results[1]))
        label_moves2 = tkinter.Label(master=self._frame, text=str(results[2]))
        label_biggest2 = tkinter.Label(master=self._frame, text=str(results[3]))

        button = tkinter.Button(master=self._frame, text="Back to start page", command=self._show_start_view)
        button2 = tkinter.Button(master=self._frame, text="View top 10 results",
                                command=self._show_results_view)

        label.grid(row=0, columnspan=2, padx=5, pady=5)
        label2.grid(row=1, columnspan=2, padx=5, pady=5)

        label_name.grid(row=2, column=0, padx=5, pady=5)
        label_size.grid(row=3, column=0, padx=5, pady=5)
        label_moves.grid(row=4, column=0, padx=5, pady=5)
        label_biggest.grid(row=5, column=0, padx=5, pady=5)
        label_name2.grid(row=2, column=1, padx=5, pady=5)
        label_size2.grid(row=3, column=1, padx=5, pady=5)
        label_moves2.grid(row=4, column=1, padx=5, pady=5)
        label_biggest2.grid(row=5, column=1, padx=5, pady=5)

        button.grid(row=6, columnspan=2, padx=5, pady=10)
        button2.grid(row=7, columnspan=2, padx=5, pady=10)
