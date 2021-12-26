import tkinter
import data.datahandling

class ResultsView:
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
        results = self._datahandler.get_top_ten()
        self._frame = tkinter.Frame(master=self._root)
        label = tkinter.Label(master=self._frame, text="All time top 10",
                                font="Helvetica 12 bold")
        label2 = tkinter.Label(master=self._frame, text="Name \t Size \t Moves \t Biggest",
                                font="Helvetica 10 bold")
        result1 = tkinter.Label(master=self._frame, text=results[0])
        result2 = tkinter.Label(master=self._frame, text=results[1])
        result3 = tkinter.Label(master=self._frame, text=results[2])
        result4 = tkinter.Label(master=self._frame, text=results[3])
        result5 = tkinter.Label(master=self._frame, text=results[4])
        result6 = tkinter.Label(master=self._frame, text=results[5])
        result7 = tkinter.Label(master=self._frame, text=results[6])
        result8 = tkinter.Label(master=self._frame, text=results[7])
        result9 = tkinter.Label(master=self._frame, text=results[8])
        result10 = tkinter.Label(master=self._frame, text=results[9])

        button = tkinter.Button(master=self._frame, text="Back to start view",
                                command=self._show_start_view)

        label.pack()
        label2.pack()
        result1.pack()
        result2.pack()
        result3.pack()
        result4.pack()
        result5.pack()
        result6.pack()
        result7.pack()
        result8.pack()
        result9.pack()
        result10.pack()

        button.pack()
