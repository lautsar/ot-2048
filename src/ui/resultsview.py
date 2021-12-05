import tkinter

class ResultsView:
    def __init__(self, root, game, end, result, start):
        self._root = root
        self._show_game_view = game
        self._show_game_end_view = end
        self._show_results_view = result
        self._show_start_view = start
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=tkinter.constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tkinter.Frame(master=self._root)
        label = tkinter.Label(master=self._frame, text="This is a result view")
        label2 = tkinter.Label(master=self._frame, text="Nothing to see here, yet")
        button = tkinter.Button(master=self._frame, text="Back to start view", command=self._show_start_view)

        label.pack()
        label2.pack()
        button.pack()
