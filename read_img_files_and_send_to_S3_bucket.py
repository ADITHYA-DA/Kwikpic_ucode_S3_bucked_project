import os
import boto3

class ImageHandler:
    def __init__(self, img_path):
        self.img_path = img_path
        self.file_name_ucode_list = []

    def read_img_files(self):
        # print(img_path)
        for full_file_name in os.listdir(img_path):
            file_name = full_file_name.split('-')[1]
            ucode = file_name.split('.')[0]
            # print(ucode)
            self.file_name_ucode_list.append(tuple(full_file_name, file_name, ucode))


    def connect_and_send_to_S3_bucket(self):
        s3 = boto3.resource(
            # kwikpic_selfies
            service_name='s3',
            region_name='us-east-2',
            aws_access_key_id='mykey',
            aws_secret_access_key='mysecretkey'
        )

        for full_file_name, file_name, ucode in self.file_name_ucode_list:
            s3.Bucket('cheez-willikers').upload_file(Filename=full_file_name, Key=file_name)



if __name__ == '__main__':
    img_path = 'ucode_S3_bucket/Images'

    obj = ImageHandler(img_path)

    obj.read_img_files()
    obj.connect_and_send_to_S3_bucket()