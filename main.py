import PySimpleGUI as sg

class Application:
    def __init__(self):
        self.window = None
        self.recommender = None
        self.movies = None

    def run(self):
        layout = [
            [sg.Text("Enter user_id: "), sg.InputText(), sg.Button('OK')],
            [sg.MLine(size=(60, 10), key="-OUTPUT-")],
        ]
        self.window = sg.Window("Recommender", layout)


        while True:
            event, values = self.window.read()
            if event is None:
                break

            if event == "OK":
                pass
                # something something


        self.window.close()


def main():
    Application().run()


if __name__ == '__main__':
    main()
else:
    print("ERROR: Try running from main")
