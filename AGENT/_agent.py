class Agent(object):
    '''BASE AGENT CLASS'''

    def __init__(self, identifier):
        self._name = identifier

    def _run(self):
        return True