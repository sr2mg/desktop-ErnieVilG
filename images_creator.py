from concurrent.futures import ThreadPoolExecutor
from domain import hub_adaptor


class images_creator:

    def __init__(self) -> None:
        self.return_image_list = []
        self.generate_images_tpe = ThreadPoolExecutor(max_workers=5)
        self.generate_image_futures = []
        self.ha = hub_adaptor.hub_adaptor()

    def get_image_list(self, number, prompt, style):  # create_image_listのスレッド管理
        set = int(-(-number//6))  # 切り上げで何回回せばいいかを決める
        for idx in range(set):
            self.generate_image_futures.append(
                self.generate_images_tpe.submit(self.create_image_list, prompt, style))
        self.generate_images_tpe.shutdown()
        return self.return_image_list

    def create_image_list(self, prompt, style):  # 6枚生成する
        ret = self.ha.get_image(prompt=prompt, style=style)
        self.return_image_list.extend(ret)

    def cancel_generating(self):
        for future in self.generate_image_futures:
            future.cancel()
