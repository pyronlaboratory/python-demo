from urllib import request
import requests
from bs4 import BeautifulSoup

def x_spider(max_pages):

 page = 1

 while page < max_pages:

   url = r'https://buckysroom.org/trade/search.php?page=' + str/(page)
   source_code = request.get(url)
   plain_text = source_code.text

   for link in soup.findAll('a', {'class':'item-name'}):

    href = "https://buckysroom.org" + link.get('href');
    title = link.string;
    print(title)

   page += 1
			
x_spider(1)


goog_url = r"https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1532959698&period2=1535638098&interval=1d&events=history&crumb=tsx7n5.mtzf"

def web_crawler(download_url):

  source_code = requests.get(download_url)
  
  plain_text = source_code.text
  
  print(plain_text)
  print("")
  print(source_code)
  csv = str(source_code.text)
  
  lines = csv.split("\\n")
  
  dest_url = r'goog.csv'



  fx = open(dest_url,"w")

  
  for line in lines:
    fx.write(line + "\n")

  fx.close()

#web_crawler(goog_url)





        
