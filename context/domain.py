from dataclasses import dataclass


@dataclass
class Dataset:
    dataName: object
    saveName: object
    fileName: object
    train: object
    test: object
    id: object
    label: object

    @property
    def dataName(self) -> object: return self._dataName

    @dataName.setter
    def dataName(self, dataName) -> object: self._dataName = dataName

    @property
    def saveName(self) -> object: return self._saveName

    @saveName.setter
    def saveName(self, saveName) -> object: self._saveName = saveName

    @property
    def fileName(self) -> object: return self._fileName

    @fileName.setter
    def fileName(self, fileName) -> object: self._fileName = fileName

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train) -> object: self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test) -> object: self._test = test

    @property
    def id(self) -> object: return self._id

    @id.setter
    def id(self, id) -> object: self._id = id

    @property
    def label(self) -> object: return self._label

    @label.setter
    def label(self, label) -> object: self._label = label
