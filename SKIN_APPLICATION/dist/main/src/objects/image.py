# @autor: Agustin CARTAYA

# class modeling an image

from .data_object import *
import PIL.Image as PImage
from PIL.ExifTags import TAGS

class Image(DataObject):
    def __init__(self, src, img_type):
        self.src = src
        p_image = PImage.open(src)

        # both parameters are also outside for filtering
        self.name_extension = util.get_file_name_extension(src)
        self.name = util.get_file_name(src)
        self.ceartion_date = "0"

        self.info_dict = {
            "filename": self.name,
            "type": img_type,
            "image_height": p_image.height,
            "image_width": p_image.width,
            "image_format": p_image.format,
            "image_mode": p_image.mode,
            "ceartion_date": self.ceartion_date
        }
        exifdata = p_image.getexif()
        for tag_id in exifdata:
            try:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()
                self.info_dict[tag] = data
            except:
                print("problem decoding ", tag_id, " for " + self.name_extension)


        p_image.close()

    def __hash__(self):
        return hash(self.src)

    def __eq__(self, obj):
        p_self = PImage.open(self.src)
        p_other = PImage.open(obj.src)
        eq = list(p_self.getdata()) == list(p_other.getdata())
        p_self.close()
        p_other.close()
        return eq


    def get_size(self):
        return (self.info_dict["image_width"], self.info_dict["image_height"])

    def get_resized_size(self, maxWidth, maxHeight=0):
        if maxHeight == 0:
            maxHeight = maxWidth
        ratio = min(maxWidth / self.get_size()[0], maxHeight / self.get_size()[1])
        return (self.get_size()[0]*ratio, self.get_size()[1]*ratio)
