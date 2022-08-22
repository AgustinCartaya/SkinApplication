from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QFrame, QRadioButton, QGridLayout, QButtonGroup

from .label import Label
import src.util.util as util

from src.objects.timeline import Timeline


class TimelinePointsContainer(QFrame):

    s_switch_point = Signal(int)
    def __init__(self, parent):
        QFrame.__init__(self, parent)

        self.timeline = None
        self.points = []
        self.__create()

    def __create(self):
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(50)

        self.qbt_group = QButtonGroup()
        self.qbt_group.buttonClicked.connect(self.__switch_point)

    def create_points(self, timeline, switch_poit_receaver):
        self.s_switch_point.connect(switch_poit_receaver)
        self.timeline = timeline
        counter = 0
        for tilp in timeline.timeline_points:
            lb_point_date = Label(self)
            lb_point_date.setText(tilp.date.strftime('%d-%m-%Y'))
            self.layout.addWidget(lb_point_date, 0, counter, 1, 1, Qt.AlignHCenter)

            i_point = QRadioButton(self)
            self.layout.addWidget(i_point, 1, counter, 1, 1, Qt.AlignHCenter)

            self.points.append([i_point, lb_point_date])
            self.qbt_group.addButton(i_point, counter)
            counter = counter + 1

        if len(self.points) > 0:
            self.points[counter-1][0].setChecked(True)
            self.__switch_point(self.points[counter-1][0])

    @Slot(QRadioButton)
    def __switch_point(self, i_point):
        self.s_switch_point.emit(self.qbt_group.checkedId())

