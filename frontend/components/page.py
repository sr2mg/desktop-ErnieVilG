import PySimpleGUI as sg


class Page:
    WIN_CLOSED = sg.WIN_CLOSED

    def __init__(self) -> None:
        sg.theme('DarkAmber')   # Add a touch of color
        self.window = sg.Window('ERNIE-ViLG on Desktop', self.getLayout())

        pass

    def getLayout(self):
        return [[sg.Text('prompt'), sg.InputText(key='prompt')],
                [sg.Text('style'), sg.InputText(key='style')],
                [sg.Button('Generate!', key="generate")],
                [sg.Image(key='image0'), sg.Image(key='image1')],
                [sg.Image(key='image2'), sg.Image(key='image3')],
                [sg.Image(key='image4'), sg.Image(key='image5')],
                ]

    def getWindow(self):
        return self.window

    def update_imageLayout(self, idx, image_data):
        self.window['image'+str(idx)].update(data=image_data)
