import PySimpleGUI as sg
from domain import hub_adaptor
from PIL import Image
import io

sg.theme('DarkAmber')   # Add a touch of color
ha = hub_adaptor.hub_adaptor()
# All the stuff inside your window.
layout = [[sg.Text('prompt'), sg.InputText(key='prompt')],
          [sg.Text('style'), sg.InputText(key='style')],
          [sg.Button('Generate!', key="generate")],
          [sg.Image(key='image0'), sg.Image(key='image1')],
          [sg.Image(key='image2'), sg.Image(key='image3')],
          [sg.Image(key='image4'), sg.Image(key='image5')],
          ]

# Create the Window
window = sg.Window('ERNIE-ViLG on Desktop', layout)
#TODO: 非同期処理
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'generate':
        prompt = values['prompt']  # 初音未来,pixiv
        style = values['style']  # 卡通
        images = ha.get_image(prompt=prompt, style=style)

        print(images)
        for idx, image in enumerate(images):
            sg_image = image
            sg_image.thumbnail([512, 512])
            sg_image.save("test_"+str(idx)+".png", format="PNG")
            bio = io.BytesIO()
            sg_image.thumbnail([256, 256])
            sg_image.save(bio, format="PNG")
            window['./ernievilg_output/image' +
                   str(idx)].update(data=bio.getvalue())

        print('You generated!')

window.close()
