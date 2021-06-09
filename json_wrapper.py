import requests


class JSon:
    """Objeto que devuelve un json a partir de una url en formato Dictionary"""
    def __init__(self, url):
        self.__json = None
        self.__set_json(url)

    def __del__(self):
        del self.json

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, data):
        self.__json = data

    @json.deleter
    def json(self):
        del self.__json

    """Setters and Getters"""
    def __set_json(self, url):
        headers = {
            "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Accept"     : "application/json, text/javascript, */*; q=0.01"
        }
        r = requests.get(url, headers=headers)
        data = r.json()
        self.json = data
