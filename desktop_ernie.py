import io
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime as dt
from images_creator import images_creator
from frontend.components import page


class DesktopErnie:
    def __init__(self) -> None:
        self.frontend = page.Page()
        self.window = self.frontend.getWindow()
        self.generate_image_futures = []  # 今後はgenerate_futuresごとに管理する必要があるので二次元配列かも
        self.generate_futures = []
        self.ic = None
        pass

    def main(self):
        self.write_log("main起動")
        #TODO: 非同期処理
        while True:
            event, values = self.window.read()
            generate_tpe = ThreadPoolExecutor(max_workers=3)
            if event == self.frontend.WIN_CLOSED:  # if user closes window or clicks cancel
                self.cancel_tpe()
                break
            if event == 'generate':
                self.generate_futures.append(generate_tpe.submit(
                    self.create_image, values['prompt'], values['style'], values['number_img']))
                print("generate_tpe submit")
        self.window.close()

    def create_image(self, prompt, style, number_img):
        if(prompt == '' or style == ''):
            return
        # 大受欢迎的二维动画角色，可爱女孩子，原神的新角色，金色头发少女，pixiv排名第一,纤细的双手
        self.window['generate'].update(disabled=True)
        tdatetime = dt.now()
        tstr = tdatetime.strftime('%Y%m%d%H_%M_%S')
        self.ic = images_creator()
        images = self.ic.get_image_list(number_img, prompt=prompt, style=style)
        self.save_image(images, tstr, number_img)
        self.write_prompt(tstr, prompt)
        print('You generated!')
        self.window['generate'].update(disabled=False)

    def write_prompt(datetime_str, prompt):
        f = open(f'./ernievilg_output/{datetime_str}/prompt.txt', 'w')
        f.write(f'{datetime_str}:{prompt}')
        f.close

    def write_log(self, message):
        tstr = dt.now().strftime('%Y-%m-%d-%H_%M_%S')
        f = open(f'./log/logger.txt', 'a')
        f.write(f'{tstr}:{message}\n')
        f.close

    def save_image(self, raw_images, datetime_str, number_img):
        print("save image start")
        images = raw_images[0:int(number_img)]
        print(images)
        print("create dir")
        os.makedirs(f"ernievilg_output/{datetime_str}")
        for idx, image in enumerate(images):
            sg_image = image
            sg_image.thumbnail([512, 512])
            sg_image.save(
                f"./ernievilg_output/{datetime_str}/{str(idx)}.png", format="PNG")
            #TODO: promptをメモできる機能
            bio = io.BytesIO()
            sg_image.thumbnail([256, 256])
            sg_image.save(bio, format="PNG")
            #self.frontend.update_imageLayout(idx, bio.getvalue())

    def cancel_tpe(self):
        for future in self.generate_futures:
            future.cancel()
        print(f"generate_futuresをキャンセル")
        if(self.ic is not None):
            self.ic.cancel_generating()
        print(f"generate_image_futuresをキャンセル")


os.makedirs(f"log", exist_ok=True)
tstr = dt.now().strftime('%Y-%m-%d-%H_%M_%S')
f = open(f'./log/logger.txt', 'a')
f.write(f'{tstr}\n')
f.close

hoge = DesktopErnie()
hoge.main()
