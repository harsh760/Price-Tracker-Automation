import json
import json.decoder
from scraper import check_product
from product import Product

# URLs = ['https://www.amazon.in/Test-Exclusive-646/dp/B07HGJKDRR/ref=br_msw_pdt-2?_encoding=UTF8&smid=A1EWEIV3F4B24B&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=9J82R4R8JVP3KXBF4N1G&pf_rd_t=36701&pf_rd_p=3ee7fd98-e85f-47bb-91a5-7de85fe7ede5&pf_rd_i=desktop',
# 'https://www.amazon.in/FX505DT-Graphics-5-3550H-Windows-FX505DT-AL202T/dp/B07RRQBC1S/ref=sr_1_3?keywords=gaming+laptop&qid=1578569252&s=electronics&smid=A14CZOWI0VEHLG&sr=1-3']

URLs = []

with open("file.txt" , "r") as read_file:
    for line in read_file.readlines():
        URLs.append(line)

# print(URls)        

products = []

for url in URLs:
    name , price = check_product(url)
    product = Product(name, price ,url)

    products.append(product)

with open("products.json" , "w") as json_file:
    data = {}

    data["Products"] = []

    for prod in products:
        data["Products"].append(prod.serialize())
    json.dump(data , json_file , sort_keys= 4,indent=True)    
