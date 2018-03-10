from GoogleSearch import GoogleSearch
from GoogleSearchScraper import GoogleSearchScraper

google = GoogleSearch()
res = google.Search('linux', num=50)
scraper = GoogleSearchScraper()
results = scraper.Scrape(res)
print(results)
print('===============================================')
for r in results:
    print(r['title'])
    print(' ', r['url'])
    #print(r['s'])
