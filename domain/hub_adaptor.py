import paddlehub as hub


class hub_adaptor:
    def __init__(self) -> None:
        self.model = hub.Module(name='ernie_vilg')
        pass

    def __inference(self, text_prompts, style):
        try:
            results = self.model.generate_image(
                text_prompts=text_prompts, style=style, visualization=False)
            return 'Success', results[:6]
        except Exception as e:
            error_text = str(e)
            return error_text, None
        return

    # returnでは配列でPILImageが返ってくる
    def get_image(self, prompt, style):
        print("get image!")
        ret = self.__inference(prompt, style)
        if ret[0] != 'Success':
            raise ValueError(ret[0])
        print(ret)
        images = ret[1]
        return images
