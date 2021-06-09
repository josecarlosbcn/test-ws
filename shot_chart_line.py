from decimal import Decimal


class SCLine:
    def __init__(self, data):
        self.__id = None
        self.__x = None
        self.__y = None
        self.__scored = None
        self.__txt = None
        self.__home = None
        self.__set_data(data)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @property
    def x(self):
        return round(self.__x, 2)

    @x.setter
    def x(self, x):
        self.__x = Decimal(x)

    @x.deleter
    def x(self):
        del self.__x

    @property
    def y(self):
        return round(self.__y, 2)

    @y.setter
    def y(self, y):
        self.__y = Decimal(y)

    @y.deleter
    def y(self):
        del self.__y

    @property
    def scored(self):
        return self.__scored

    @scored.setter
    def scored(self, scored):
        self.__scored = scored

    @scored.deleter
    def scored(self):
        del self.__scored

    @property
    def txt(self):
        return self.__txt

    @txt.setter
    def txt(self, txt):
        self.__txt = txt

    @txt.deleter
    def txt(self):
        del self.__txt

    @property
    def home(self):
        return self.__home

    @home.setter
    def home(self, home):
        self.__home = home

    @home.deleter
    def home(self):
        del self.__home

    def __set_data(self, data):
        style = data['style'].split(";")
        x = style[2].split(":")[1] if len(style) == 5 else style[1].split(":")[1]
        y = style[3].split(":")[1] if len(style) == 5 else style[2].split(":")[1]
        x = x.split("%")[0]
        y = y.split("%")[0]
        self.id = data['data-shooter']
        self.scored = True if 'made' in data['class'] else False
        self.txt = data['data-text']
        self.home = True if data['data-homeaway'] == 'home' else False
        self.x = x
        self.y = y
