

class ReceiveTrigger(object):
    """
    Trigger function that gets triggered after
    a new request is received
    """
    def __init__(self):
        self._subject_code = None
        self._group_media = None
        self._observers = []

    @property
    def group(self):
        return (self._subject_code, self._group_media)

    @group.setter
    def group(self, value):
        self._subject_code, self._group_media = value
        for callback in self._observers:
            callback(self._subject_code, self._group_media)

    def bind_to(self, callback):
        self._observers.append(callback)
