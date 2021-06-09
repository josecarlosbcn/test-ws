from bs4 import BeautifulSoup
import urllib.request


class BS:
    """Objeto a través del cual una vez le pasadmos la url obtenemos todo el código HTML de la página que le hemos pasado"""
    def __init__(self, url):
        self.__url = url
        self.__soup = None
        self.__set_soup()

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @url.deleter
    def url(self):
        del self.__url

    @property
    def soup(self):
        return self.__soup

    @soup.setter
    def soup(self, soup):
        self.__soup = soup

    @soup.deleter
    def soup(self):
        del self.__soup

    def __set_soup(self):
        req = urllib.request.Request(self.url)
        page = urllib.request.urlopen(req)
        html = page.read()
        self.soup = BeautifulSoup(html, 'html.parser')
