# -*- coding: utf-8 -*-
from slacker import Slacker
import time
import logging

import os
import json
from ssl import SSLError

from websocket import create_connection, WebSocketException, WebSocketConnectionClosedException


logger = logging.getLogger(__name__)


class Brain(object):
    def __init__(self, token, slacker_client=None):
        self.slack = slacker_client if slacker_client else Slacker(token)

    def rtm_connect(self):
        reply = self.slack.rtm.start().body
        time.sleep(1)
        self.parse_slack_login_data(reply)

    def reconnect(self):
        while True:
            try:
                self.rtm_connect()
                logger.warning('reconnected to slack rtm websocket')
                return
            except Exception as e:
                logger.exception('failed to reconnect: %s', e)
                time.sleep(5)