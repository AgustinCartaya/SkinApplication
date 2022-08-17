# This Python file uses the following encoding: utf-8

import src.config as cfg
import src.util.util as util

from .timeline_point import TimelinePoint
from operator import attrgetter


class Timeline:
    def __init__(self, skin_lesion):
        self.skl = skin_lesion
        self.timeline_points = []
        self.__charge_timeline_points()

        # for test
#        TimelinePoint.create_test_points(skin_lesion)

    def __charge_timeline_points(self):
        for tlp_file_name in util.get_file_list(self.skl.get_timeline_folder_path()):
            tlp = TimelinePoint.read_point(self.skl.get_timeline_folder_path(), tlp_file_name)
            self.timeline_points.append(tlp)
        self.timeline_points.sort(key=attrgetter("date"), reverse=False)

