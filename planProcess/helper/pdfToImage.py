import base64
import os
import shutil
from pathlib import Path

from pdf2image import convert_from_path


class Decoded:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.pdf_file_name = self.pdf_file.replace(".pdf", "")
        self.directory = ""
        self.all_images = ""
        self.all_decoded_images = []
        self.url_list = []

        self.create_directory(self.pdf_file_name)

        self.create_images(self.pdf_file)

        self.save_images(self.all_images)

        self.create_urls()

        self.delete_directory(self.directory)

    def create_directory(self, pdf_file_name):
        try:
            os.mkdir(pdf_file_name)
        except FileExistsError:
            pass
        self.directory = Path(self.pdf_file_name)

    def create_images(self, pdf_file):
        self.all_images = convert_from_path(pdf_file)

    def save_images(self, images):
        for i, page in enumerate(images):
            image = f"{self.pdf_file_name}/page{i + 1}.jpg"
            page.save(image, "JPEG")

    def create_urls(self):
        for image in self.directory.iterdir():
            encoded_string = base64.b64encode(open(image, "rb").read()).decode("utf_8")
            self.all_decoded_images.append(encoded_string)

        self.url_list = [
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{item}"},
            }
            for item in self.all_decoded_images
        ]

    def delete_directory(self, directory):
        shutil.rmtree(directory)
