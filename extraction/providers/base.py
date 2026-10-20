class ExtractionProvider:
    def __init__(self, config):
        self.config = config

    def extract(self, data):
        raise NotImplementedError("Subclasses must implement this method.")