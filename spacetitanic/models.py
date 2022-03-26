import context.models
from context import models, domain
from context.domain import Dataset
from context.models import Model
from icecream import ic


class TitanicModel:
    model = Model()
    dataset = Dataset()

    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        ic(f'트레인 컬럼 {self.train.columns}')

    def preprocess(self):
        this = self.dataset
        that = self.model
        feature = ['PassengeId', 'HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP',
                   'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'Name',
                   'Transported']
