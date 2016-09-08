# -*- coding: utf-8 -*-
from morelia.sensors.base import Sensor
from contracts import contract


class Slack(Sensor):
    """Emits messages read from slack
    """

    def activate(self):
        raise NotImplementedError
