import threading


class PluginThread(threading.Thread):
    def run(self):
        raise NotImplementedError
