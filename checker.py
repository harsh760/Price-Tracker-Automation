import json
import json.decoder
from scraper import check_product
from mail import send_mail

data = []

with open("products.json" , "r") as json_file:
    data = json.load(json_file)

current_name = []
current_price = []
for prod in data["Products"]:
    c_name , c_price = check_product(prod["link"])
    current_name.append(c_name)
    current_price.append(c_price)

current_price = [9000 , 3500]

i = 0
for prod in data["Products"]:
    try:
        if(prod['price'] > current_price[i]):
            diff = prod['price'] - current_price[i]
            diff = abs(diff)

            if(diff != prod['price']):
                send_mail(current_name[i],diff,prod['link'])
            else:
                print("No mail to send")    
        else:
            print("No changes!")        
    except:
        Exception()
    i += 1        

