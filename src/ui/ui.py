import ui.startview
import ui.gameendview
import ui.resultsview

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = ui.startview.StartView(
            self._root,
            self._show_game_end_view,
            self._show_results_view,
            self._show_start_view
        )

        self._current_view.pack()

    def _show_game_end_view(self):
        self._hide_current_view()

        self._current_view = ui.gameendview.GameEndView(
            self._root,
            self._show_game_end_view,
            self._show_results_view,
            self._show_start_view
        )

        self._current_view.pack()

    def _show_results_view(self):
        self._hide_current_view()

        self._current_view = ui.resultsview.ResultsView(
            self._root,
            self._show_game_end_view,
            self._show_results_view,
            self._show_start_view
        )

        self._current_view.pack()
