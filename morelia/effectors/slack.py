# -*- coding: utf-8 -*-
from contracts import ContractsMeta, contract
from morelia.effectors.base import Effector


class Slack(Effector):
    """Publishes messages to slack
    """

    @contract(input_data='dict')
    def activate(self, input_data):
        raise NotImplementedError
