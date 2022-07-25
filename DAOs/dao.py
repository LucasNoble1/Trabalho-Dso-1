from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        self.__cache2 = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, obj):
        self.__cache2.append(obj)
        self.__dump()

    def update(self, obj):
        for i in self.get_all():
            if i.codigo == obj.codigo:
                self.__cache2.remove(i)
                self.__cache2.append(obj)
                self.__dump()

    def get(self, key):
        for i in self.get_all():
            if i.codigo == key:
                return i
        return None

    def remove(self, key):
        for i in self.get_all():
            if i.codigo == key:
                self.__cache2.remove(i)
                self.__dump()

    def get_all(self):
        return self.__cache2
