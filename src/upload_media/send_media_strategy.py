import strategies

class SendMediaStrategy:

    def __init__(self, destination_address, strategy = None):

        self.destination_address = destination_address

        if strategy is not None:
            self.strategy = getattr(strategies, strategy)()
        else:
            self.strategy = getattr(strategies, 'PostRequest')()
    
    def send(self, subject_code, media_path):
        self.strategy.execute(self.destination_address, subject_code, media_path)