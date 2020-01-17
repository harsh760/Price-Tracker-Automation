import requests
from bs4 import BeautifulSoup
from product import Product


headers = {"User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# URL = 'https://www.amazon.in/Test-Exclusive-646/dp/B07HGJKDRR/ref=br_msw_pdt-2?_encoding=UTF8&smid=A1EWEIV3F4B24B&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=9J82R4R8JVP3KXBF4N1G&pf_rd_t=36701&pf_rd_p=3ee7fd98-e85f-47bb-91a5-7de85fe7ede5&pf_rd_i=desktop'


def con_price(price):
    price = price.split('₹')[1]

    try:
        price = price.split('\n')[0] + "." + price.split('\n')[1]
    except:
        Exception()

    try:
        price = price.split(",")[0] + price.split(",")[1]
    except:
        Exception()

    return float(price)                


def check_product(URL):
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").text.strip()
    
    try:
        gprice = soup.find("span",id = "priceblock_dealprice").get_text()
        print(gprice)
        if(gprice == ""):
            gprice = soup.find("span",id = "priceblock_ourprice").get_text()
    except:
        gprice = '₹ 0'
    # print(gprice)
    price = con_price(gprice)            
    print(price)
    return title , price
  