from context.domain import Dataset
import pandas as pd


class Model:
    def __init__(self):
        self.ds = Dataset()
        this = self.ds
        this.dataName = './data/'
        this.saveName = './save/'

    def get_saveName(self):
        return self.ds.saveName

    def new_model(self, fileName) -> object:
        this = self.ds
        return pd.read_csv(f'{this.dataName}{fileName}', index_col=0)
