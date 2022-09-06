from PIL import Image
import io

from domain import hub_adaptor
from frontend.components import page


ha = hub_adaptor.hub_adaptor()
# Create the Window
frontend = page.Page()
window = frontend.getWindow()
#TODO: 非同期処理
while True:
    event, values = window.read()
    if event == frontend.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    if event == 'generate':
        prompt = values['prompt']  # 初音未来,pixiv
        style = values['style']  # 卡通
        images = ha.get_image(prompt=prompt, style=style)

        print(images)
        for idx, image in enumerate(images):
            sg_image = image
            sg_image.thumbnail([512, 512])
            sg_image.save("./ernievilg_output/test_" +
                          str(idx)+".png", format="PNG")
            bio = io.BytesIO()
            sg_image.thumbnail([256, 256])
            sg_image.save(bio, format="PNG")
            frontend.update_imageLayout(idx, bio.getvalue())
        print('You generated!')
window.close()
