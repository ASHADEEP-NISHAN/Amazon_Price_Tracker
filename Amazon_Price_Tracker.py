import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

my_email="SENDAR EMAIL"
password="PASSWORD"

url = "https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_2?" \
      "keywords=ps5&qid=1683515726&sr=8-2&th=1"

headers = {
    "User-Agent": "Defined",
    "Accept-Language": "en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
}

response = requests.get(url=url, headers=headers)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
# soup = BeautifulSoup(webpage, "lxml")

price_tag = soup.find(name="span", class_="a-offscreen").get_text().strip()
price = float(price_tag.split("$")[1])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 500
if price < BUY_PRICE:
    message = f"{title} is now {price}"
    email="YOUR EMAIL"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))