from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import schedule
from email.mime.text import MIMEText
import time



def main(URL):
	File = open("out.csv", "a")

	HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

	webpage = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(webpage.content, "lxml")

# title
	try:
		title = soup.find("span",attrs={"id": 'productTitle'})
		title_value = title.string
		title_string = title_value.strip().replace(',', '')

	except AttributeError:
		title_string = "NA"
	
	print("product Title = ", title_string)

# price

	try:
		price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '').replace('₹', 'Rs.')
	except AttributeError:
		price = "NA"
	
	print("Products price = ", price)


	notify(URL,title_string,price)
	

	
	print("\n---------------------------------------------------------------\n")




                
	File.close()

#PRICE ALERT
def notify(URL,title_string,price):
        SMTP_SERVER="smtp.gmail.com" 
        PORT=587
        EMAIL_ID="slowwhite219@gmail.com"
        PASSWORD="lqjoxiueylvzpdkt"
        EMAIL_ID1="padhyansh01@gmail.com"
        PASSWORD1="ptgpqgqajccnuczk"
        server=SMTP(SMTP_SERVER,PORT)
        server.starttls()
        server.login(EMAIL_ID,PASSWORD)
        server.login(EMAIL_ID1,PASSWORD1)

        subject="Product Notification!"
        body=title_string+" is available for "+price+"\nGo buy it now at:\n" + URL
        msg=f"Subject: {subject} \n\n{body} "


        server.sendmail(EMAIL_ID,EMAIL_ID1,msg)
        print("Email sent successfully")
        server.quit()





## MAIN 
file = open("notify.txt", "r")

for links in file.readlines():
        for i in range(0,5):
                main(links)
                time.sleep(1)
    

    

    
