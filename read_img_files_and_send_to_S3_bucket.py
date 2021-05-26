import os

class ImageHandler:
    def __init__(self, img_path):
        self.img_path = img_path
        self.ucode_list = []

    def read_img_files(self):
        # print(img_path)
        for img in os.listdir(img_path):
            ucode = img.split('-')[1].split('.')[0]
            print(ucode)
            self.ucode_list.append(ucode)


    def connect_and_send_to_S3_bucket(self):
        pass



if __name__ == '__main__':
    img_path = 'ucode_S3_bucket/Images'

    obj = ImageHandler(img_path)

    obj.read_img_files()
    obj.connect_and_send_to_S3_bucket()