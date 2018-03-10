import requests
#import bs4
from bs4 import BeautifulSoup
import json
class GoogleSearchScraper:
    def __init__(self):
        pass

    def Scrape(self, res: requests.Response) -> dict:
        soup = BeautifulSoup(res.text, 'html.parser')
        search_res = soup.select('.g')
        res_list = []
        for res_one in search_res:
            d = self.ResultToDict(res_one)
            if d is not None: res_list.append(d)
        return res_list
            
    def ResultToDict(self, res_one) -> dict:
        res_dict = {}
        title = res_one.select_one('h3.r a')
        if title is None: return None
        detail = res_one.select_one('div.s')
        if detail is None: return None
        res_dict['url'] = title['href']
        res_dict['title'] = title.text
        res_dict['s'] = detail.contents
        return res_dict
