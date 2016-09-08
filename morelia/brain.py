# -*- coding: utf-8 -*-
import time
import asyncio
import logging
import functools
import os
import signal

logger = logging.getLogger(__name__)


def ask_exit(sig_name, loop):
    print("got signal %s: exit" % sig_name)
    loop.stop()


def _populate_dict(d, l):
    for i in l:
        d[i.name] = i


class Brain(object):
    def __init__(self, sensors, effectors, interpreters):
        self._sensors = {}
        self._effectors = {}
        self._interpreters = {}

        _populate_dict(self._sensors, sensors)
        _populate_dict(self._effectors, effectors)
        _populate_dict(self._interpreters, interpreters)

    def process(self):
        # read each sensor
        sensor_data = {}
        for sensor in self._sensors:
            sensor_data[sensor.name] = sensor.read()

        # provide each interpreter with all sensor data
        for interpreter in self._interpreters:

            # gather the desired effects
            effects = interpreter.activate(sensor_data)

            # pass effect payloads to effectors
            for effector_name, payload in effects.iteritems():
                self._effectors[effector_name].activate(payload)

        time.sleep(0.1)
        # asyncio.ensure_future(self.process())

    def import_subroutines(self):
        pass

    def start(self):
        self.import_subroutines()
        while True:
            self.process()

    def start_asyncio(self):
        loop = asyncio.get_event_loop()
        for sig_name in ('SIGINT', 'SIGTERM'):
            loop.add_signal_handler(getattr(signal, sig_name),
                                    functools.partial(ask_exit, sig_name, loop))

        asyncio.ensure_future(self.process())

        print("Event loop running forever, press Ctrl+C to interrupt.")
        print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())
        try:
            loop.run_forever()
        finally:
            loop.close()
