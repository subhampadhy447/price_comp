from bs4 import BeautifulSoup
import requests


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
	File.write(f"{title_string},")

# price

	try:
		price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
	except AttributeError:
		price = "NA"
	
	print("Products price = ", price)
	File.write(f"{price.replace('₹', 'Rs.')},")
# rating
	try:
		rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

	except AttributeError:
		try:
			rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
		except:
			rating = "NA"
			
	print("Overall rating = ", rating)
	File.write(f"{rating},")

	try:
		review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

	except AttributeError:
		review_count = "NA"
		
	print("Total reviews = ", review_count)
	File.write(f"{review_count},")

# availablility
	try:
		available = soup.find("div", attrs={'id': 'availability'})
		available = available.find("span").string.strip().replace(',', '')

	except AttributeError:
		available = "NA"
	
	print("Availability = ", available)
	File.write(f"{available},\n")

	print("\n---------------------------------------------------------------\n")
	

                
	File.close()

	file = open('out.txt', 'a')
	file.write("Title: "+title_string+"\n\n")
	file.write("Price: "+price.replace('₹', 'Rs.')+"\n")
	file.write("Rating: "+rating+"\n")
	file.write("Available: "+available+"\n\n")
	file.write("URL: "+URL+"\n------------------------------------------\n")
	file.close()


## MAIN 
file = open("url.txt", "r")

for links in file.readlines():
    main(links)
