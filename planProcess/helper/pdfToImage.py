import base64
import os
import shutil
from pathlib import Path

from pdf2image import convert_from_path


class Decoded:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.pdf_file_name = self.pdf_file.strip(".pdf", "")
        self.images_directory = ""
        self.all_images = ""
        self.all_encoded_images = []
        self.url_list = []

        self.make_directory(self.pdf_file_name)

        self.save_images()

        self.encode_images(self.all_images)

        self.delete_images(self.images_directory)

    def make_directory(self, pdf_file_name):
        try:
            os.mkdir(pdf_file_name)
        except FileExistsError:
            pass
        self.images_directory = Path(pdf_file_name)

    def save_images(
        self,
    ):
        self.all_images = convert_from_path(self.pdf_file)
        for i, page in enumerate(self.all_images):
            image_path = f"{self.pdf_file_name}/page{i + 1}.jpg"
            page.save(image_path, "JPEG")

    def encode_images(self, images):
        for image in images:
            encoded_image = base64.b64encode(open(image, "rb").read()).decode("utf-8")
            self.all_encoded_images.append(encoded_image)
        self.url_list = [
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{item}"},
            }
            for item in self.all_encoded_images
        ]

    def delete_images(self, images_directory):
        shutil.rmtree(images_directory)
