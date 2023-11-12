from abc import ABC, abstractmethod
import logging
import os
import shutil


class PhotoCollector(ABC):
    def __init__(self, photos_path: str, result_path: str) -> None:
        self.photos_path = photos_path
        self.result_path = result_path

    @abstractmethod
    def collect(self) -> None:
        ...


class SamsungPhotoCollector(PhotoCollector):
    def __init__(self, photos_path: str, result_path: str) -> None:
        super().__init__(photos_path, result_path)

    def collect(self) -> None:
        if not os.path.exists(self.result_path):
            os.mkdir(self.result_path)
            logging.log(logging.INFO, f"Creating a folder {self.result_path}")

        files = os.listdir(self.photos_path)

        for file in files:
            file_path = f"{self.photos_path}/{file}"

            data = file.split("_")[0]
            data = data[6:8] + "." + data[4:6] + "." + data[0:4]

            if not os.path.exists(f"{self.result_path}/{data}"):
                os.mkdir(f"{self.result_path}/{data}")

            shutil.copy(file_path, f"{self.result_path}/{data}")
            logging.log(logging.INFO, f"Moved file {file} to {self.result_path}/{data}")

        logging.log(logging.INFO, "Finished collecting photos")
