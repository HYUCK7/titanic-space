from icecream import ic

from context.models import Model
from spacetitanic import models
from spacetitanic.models import TitanicModel

if __name__ == '__main__':
    while 1:
        models = TitanicModel(train_fname='train.csv', test_fname='test.csv')
        models.__init__(train_fname='train.csv', test_fname='test.csv')
        break
