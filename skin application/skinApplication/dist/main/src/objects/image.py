# This Python file uses the following encoding: utf-8
from .data_object import *
import PIL.Image as PImage
from PIL.ExifTags import TAGS

class Image(DataObject):
    def __init__(self, src, img_type):
        self.src = src
        self.image = PImage.open(src)

        # both parameters are also outside for filtering
        self.name_extension = util.get_file_name_extension(src)
        self.name = util.get_file_name(src)
        self.ceartion_date = "0"



        self.info_dict = {
            "filename": self.name,
            "type": img_type,
            "image_height": self.image.height,
            "image_width": self.image.width,
            "image_format": self.image.format,
            "image_mode": self.image.mode,
            "ceartion_date": self.ceartion_date
#            "image_is_animated": getattr(self.image, "is_animated", False),
#            "frames_in_image": getattr(self.image, "n_frames", 1)
        }
#        exifdata = self.image.getexif()
#        print(exifdata)
#        for tag_id in exifdata:
#            print(tag_id)
#            # get the tag name, instead of human unreadable tag id
#            tag = TAGS.get(tag_id, tag_id)
#            data = exifdata.get(tag_id)
#            # decode bytes
#            if isinstance(data, bytes):
#                data = data.decode()
#            print(f"{tag:25}: {data}")

    def __hash__(self):
        return hash(self.src)

    def __eq__(self, obj):
#        return obj.src == self.src
        return list(self.image.getdata()) == list(obj.image.getdata())

    def get_size(self):
        return (self.info_dict["image_width"], self.info_dict["image_height"])

    def get_resized_size(self, maxWidth, maxHeight=0):
        if maxHeight == 0:
            maxHeight = maxWidth
        ratio = min(maxWidth / self.get_size()[0], maxHeight / self.get_size()[1])
        return (self.get_size()[0]*ratio, self.get_size()[1]*ratio)
