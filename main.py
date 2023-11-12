import logging
import sys

from photo_collector import SamsungPhotoCollector


def main():
    logging.basicConfig(level=logging.INFO)

    photo_collector = SamsungPhotoCollector(
        photos_path=sys.argv[1], result_path=sys.argv[2]
    )
    photo_collector.collect()


if __name__ == "__main__":
    main()
