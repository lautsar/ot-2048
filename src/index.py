import tkinter
import ui.ui

def main():
    window = tkinter.Tk()
    window.title('2048')

    new_ui = ui.ui.UI(window)
    new_ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()
