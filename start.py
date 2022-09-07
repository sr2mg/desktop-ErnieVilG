from asyncio.windows_events import NULL
from faulthandler import disable
from PIL import Image
import io

from domain import hub_adaptor
from frontend.components import page


class webappErnie:
    def __init__(self) -> None:
        self.ha = hub_adaptor.hub_adaptor()
        self.frontend = page.Page()
        self.window = self.frontend.getWindow()
        pass

    def main(self):
        # Create the Window

        #TODO: 非同期処理
        while True:
            event, values = self.window.read()
            if event == self.frontend.WIN_CLOSED:  # if user closes window or clicks cancel
                break
            if event == 'generate':
                self.create_image(values['prompt'],
                                  values['style'], values['number_img'])
        self.window.close()

    def create_image(self, prompt, style, number_img):
        if(prompt == '' or style == ''):
            return
        # 大受欢迎的二维动画角色，可爱女孩子，原神的新角色，金色头发少女，pixiv排名第一,纤细的双手
        self.window['generate'].update(disabled=True)
        images = self.generate_images(number_img, prompt=prompt, style=style)
        self.save_image(images)
        print('You generated!')
        self.window['generate'].update(disabled=False)

    def save_image(self, images):
        for idx, image in enumerate(images):
            sg_image = image
            sg_image.thumbnail([512, 512])
            sg_image.save("./ernievilg_output/test_" +
                          str(idx)+".png", format="PNG")
            bio = io.BytesIO()
            sg_image.thumbnail([256, 256])
            sg_image.save(bio, format="PNG")
            #self.frontend.update_imageLayout(idx, bio.getvalue())

    def generate_images(self, number, prompt, style):
        set = int(-(-number//6))  # 切り上げで何回回せばいいかを決める
        ret_images = []
        for idx in range(set):
            images = self.ha.get_image(
                prompt=prompt, style=style)
            ret_images.extend(images)
        return ret_images


main = webappErnie()
main.main()
