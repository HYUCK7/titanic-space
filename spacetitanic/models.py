
import context.models
from context import models, domain
from context.domain import Dataset
from context.models import Model
from icecream import ic


class TitanicModel:
    model = Model()
    dataset = Dataset()

    def __init__(self, train_fname, test_fname):
        this = self.dataset
        that = self.model

        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # ic(f'트레인 타입 {type(self.train)}')
        # ic(f'트레인 컬럼 {self.train.columns}')
        # ic(f'트레인 헤드 {self.train.head()}')

        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.label = this.train['Transported']  # 실제값
        ic(f'라벨 확인{this.label}')
        this.id = this.test['PassengerId']
        ic(f'아이디 확인{this.id}')
        this.train = this.train.drop('Transported', axis=1)
        ic(f'중간 확인{this.train}')


    def preprocess(self, train_fname, test_fname):
        pass
    # __init__에서 해보고 옮기기

    @staticmethod
    def drop_feature(self):
        pass

    @staticmethod
    def HomePlanet():
        pass

    @staticmethod
    def CryoSleep():
        pass

    @staticmethod
    def Cabin():
        pass

    @staticmethod
    def Destination():
        pass

    @staticmethod
    def Age():
        pass

    @staticmethod
    def VIP():
        pass

    @staticmethod
    def RoomService():
        pass

    @staticmethod
    def FoodCourt():
        pass

    @staticmethod
    def ShoppingMall():
        pass

    @staticmethod
    def Spa():
        pass

    @staticmethod
    def VRDeck():
        pass

    @staticmethod
    def Name():
        pass
    


