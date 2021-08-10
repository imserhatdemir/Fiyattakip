import requests as rq
from bs4 import BeautifulSoup
import time
import smtplib

url = 'https://www.hepsiburada.com/silver-crest-sc-190-19-inch-vga-hdmi-led-monitor-p-HBCV00000DG8Z2?magaza=citybilisim' #ürünün linki
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275'} #my user agent

def check_price():
    page = rq.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:20]
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print(price)

    if (price >700):
        send_mail(title)

def send_mail(title):
    sender = '******' #kullanılacak mail
    receiver = 'zarokile@gmail.com' #iletilecek mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender,'#kullanılacak mail şifresi')
        subject = title + 'İstediğin fiyata düştü!'
        body = 'Bu Linkten Gidebilirsin =>' + url
        mailcontent = f"To:{receiver}\nFrom:{sender}\nSubject{subject}\n\n{body}"
        server.sendmail(sender,receiver,mailcontent)
        print("Mail Gönderildi")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

        while (1):
            check_price()
            time.sleep(60*60)