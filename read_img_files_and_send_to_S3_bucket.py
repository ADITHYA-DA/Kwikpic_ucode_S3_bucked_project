import os.path as osp

class ImageHandler:
    def __init__(self, img_path):
        self.img_path = img_path

    def read_img_files(self):
        for img in os.path.listdir(img_path):
            ucode = img.split('-')[1].strip('.jpg')
            print(ucode)

    def connect_and_send_to_S3_bucket(self):



if __name__ == '__main__':
    img_path = osp('Images')

    obj = ImageHandler(img_path)
    
    obj.read_img_files()
    obj.connect_and_send_to_S3_bucket()