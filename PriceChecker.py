import requests
from bs4 import BeautifulSoup
import smtplib
import config

URL="https://www.bajaao.com/products/fender-squier-affinity-series-stratocaster-hss-electric-guitar-olympic-white?variant=16329076605000"
header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

def check_price():
    page = requests.get(URL, headers=header)  # get contents of page

    soup = BeautifulSoup(page.content, 'html.parser')  # make code look cool

    title = soup.find(class_="product-title").get_text()
    price = soup.find(class_="price--main").get_text().strip()
    # print(title.strip())
    # print(price.strip())
    real_price = price[4:]
    real_price = int(real_price.replace(',', ''))
    # print(real_price)
    if (real_price < 19000):
        send_email()
    else:
        send_price(real_price)

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        subject = "Price fell down for Guitar dude!!!"
        body = "Check the link : https://www.bajaao.com/products/fender-squier-affinity-series-stratocaster-hss-electric-guitar-olympic-white?variant=16329076605000"
        # msg = f"Subject: {subject}\n\n{body}"
        msg = 'Subject: {}\n\n{}'.format(subject, body)

        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS_B, msg)
        print("Hey Email Has Been Sent!!!")
    except:
        print("Email sent failed")

def send_price(rp):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        subject = "Today's price for Fender Affinity Stratocaster is Rs. " + str(rp)
        body = "Check the link : https://www.bajaao.com/products/fender-squier-affinity-series-stratocaster-hss-electric-guitar-olympic-white?variant=16329076605000"
        # msg = f"Subject: {subject}\n\n{body}"
        msg = 'Subject: {}\n\n{}'.format(subject, body)

        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS_B, msg)
        print("Hey Email Has Been Sent!!!")
    except:
        print("Email sent failed")

check_price()






