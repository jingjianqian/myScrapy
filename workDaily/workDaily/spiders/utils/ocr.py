import ddddocr


class MyOcr:

    def __init__(self, image_path):
        self.ocr = ddddocr.DdddOcr()
        self.image_path = image_path
        self.image = None

    def OcrOneImage(self):
        try:
            with open(self.image_path, 'rb') as f:
                self.image = f.read()
                print(self.image)
                return self.ocr.classification(self.image)
        except IOError:
            print("没有找到文件")
            return None


if __name__ == '__main__':
    my_ocr = MyOcr('../images/catpath.png')
    print(my_ocr.image_path)
    result = my_ocr.OcrOneImage()
    print(result)
