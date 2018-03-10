import requests
import bs4

class GoogleSearch:
    def __init__(self):
        pass
    def Search(self, q, num=50):
        res = requests.get(f'https://www.google.co.jp/search?q={q}&num={num}')
        res.raise_for_status()
        return res
