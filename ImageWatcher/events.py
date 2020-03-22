import os
from PIL import Image
from PIL.ImageOps import grayscale
from watchdog.events import RegexMatchingEventHandler

class ImagesEventHandler(RegexMatchingEventHandler):
    THUMBNAIL_SIZE = (750, 750)
    IMAGES_REGEX = [r".*[^_thumbnail]\.jpg$"]

    def __init__(self):
        super().__init__(self.IMAGES_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f'{filename}_thumbnail.jpg'

        image = Image.open(event.src_path)
        image.thumbnail(self.THUMBNAIL_SIZE)
        image.save(filename)
