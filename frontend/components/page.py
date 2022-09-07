import PySimpleGUI as sg


class Page:
    WIN_CLOSED = sg.WIN_CLOSED
    STYLES = ['油画', '水彩', '粉笔画', '卡通', '儿童画', '蜡笔画', '探索无限']

    def __init__(self) -> None:
        sg.theme('DarkAmber')   # Add a touch of color
        self.window = sg.Window('ERNIE-ViLG on Desktop', self.getLayout())

        pass

    def getLayout(self):
        return [[sg.Text('prompt'), sg.InputText(key='prompt')],
                [sg.Text('style'), sg.Combo(
                    self.STYLES, key='style', default_value='卡通', expand_x=True, readonly=True)],
                [sg.Text('number of images'), sg.Slider(
                    key='number_img', range=(1, 20), orientation='h')],
                [sg.Button('Generate!', key="generate")],
                [sg.Image(key='image0'), sg.Image(key='image1')],
                [sg.Image(key='image2'), sg.Image(key='image3')],
                [sg.Image(key='image4'), sg.Image(key='image5')],
                ]

    def getWindow(self):
        return self.window

    def update_imageLayout(self, idx, image_data):
        self.window['image'+str(idx)].update(data=image_data)

    def disabled_generate_button(self):
        self.window['generate']
