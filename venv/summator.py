import requests
from bs4 import BeautifulSoup
import time



class Currency:
	DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

	current_converted_price = 0

	def __init__(self):
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))


	def get_currency_price(self):

		full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)


		soup = BeautifulSoup(full_page.content, 'html.parser')


		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text



summ = 0.
values = open("values.txt", "r")

try:
	while True:
		line = values.readline()
		lineR = ''.join(i for i in line if not i.isalpha())
		if not line:
			break
		point = lineR.find('-') + 2
		summ += float(lineR[point:lineR.rfind(" ") ])
		print(summ)
	values.close
except:

	values.close

	summ = round(summ, 2)

	currency = Currency()

	buff = currency.get_currency_price()

	currentC = float(buff.replace(",", "."))

	summR = round(summ*currentC, 2)

	with open('values.txt', 'a') as file:
		file.write('\nSumm - ' + str(summ) + "$\n")
		file.write('Summ - ' + str(summR) + "р\n")

	print(summ)


# q = "Хуu - 30 $"
#
# q = ''.join(i for i in q if not i.isalpha())
#
# q = q[3:len(q) - 1]


