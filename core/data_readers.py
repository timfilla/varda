import json
import pandas as pd

class _Reader:
    def __init__(self):
        pass

class JsonReader(_Reader):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def produce_df(self):
        df = pd.read_json(self.path)
        return df