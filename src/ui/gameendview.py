import tkinter
import data.datahandling

class GameEndView:
    def __init__(self, root, game, end, result, start):
        self._root = root
        self._show_game_view = game
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
        label = tkinter.Label(master=self._frame, text="This is a game end view")

        label_name = tkinter.Label(master=self._frame, text="Player: "+str(results[0]))
        label_size = tkinter.Label(master=self._frame, text="Size: "+str(results[1]))
        label_moves = tkinter.Label(master=self._frame, text="Moves :"+str(results[2]))
        label_biggest = tkinter.Label(master=self._frame, text="Biggest: "+str(results[3]))

        button = tkinter.Button(master=self._frame, text="Start", command=self._show_start_view)
        button2 = tkinter.Button(master=self._frame, text="Results", command=self._show_results_view)

        label.pack()
        label_name.pack()
        label_size.pack()
        label_moves.pack()
        label_biggest.pack()
        button.pack()
        button2.pack()