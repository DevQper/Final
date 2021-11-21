from bs4 import BeautifulSoup
# from bs4.element import ResultSet
import requests


class news_scraper():

    urls = []

    def find_coin_news(self, query):
        
        url = 'https://www.coingecko.com/en/coins/' + query + '/news'

        page = requests.get(url)

        news_parser = BeautifulSoup(page.content, 'html.parser')

        page_currency_news_title2 = news_parser.find_all("div", class_ = "my-4")

        # page_currency_news_title = news_parser.find_all("h2", class_ = "tw-text-xl")


        # page_currency_news_title_link = news_parser.find_all("h2", class_ = "tw-text-xl")

        # page_currency_news = news_parser.find_all("div", class_ = "post-body")

        # print(page_currency_news_title.text)
        # print(page_currency_news.text)
        # print(page_currency_news_title_link.find('a', href=True)["href"])
        # print("Latest News:")
        # for news in page_currency_news_title2:
        #     self.urls.append(news.find('a', href=True)["href"])
        #     print("------------------------------------------------------------------------------------")
        #     print(news.find("h2", class_ = "tw-text-xl").text.strip())
        #     print(news.find("div", class_ = "post-body").text.strip())
        #     print(news.find('a', href=True)["href"])
        #     print("------------------------------------------------------------------------------------")
        # print(page_currency_news_title2)
        return page_currency_news_title2

    def ScrapTheLink(self, link):
        url = link

        page = requests.get(url)

        news_parser = BeautifulSoup(page.content, 'html.parser')
        results = []
        linkPageScraper = news_parser.find_all("p")
        for news in linkPageScraper:
            results.append(news.text.strip() + '\n')
        return results



        