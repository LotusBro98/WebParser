import requests as rq
from lxml import html
from BeautifulSoup import BeautifulSoup as bs
import xlsxwriter

def pretty_print(elem):
    print(bs(html.tostring(elem, encoding="utf-8", pretty_print=True)).prettify())

url = "https://www.chipdip.ru/catalog/smd-leds"
response = rq.get(url)

tree = html.fromstring(response.content)

items = tree[1][1][0][2][1][2][0][1][0]

workbook = xlsxwriter.Workbook('goods.xlsx')
worksheet = workbook.add_worksheet()

pretty_print(items[0])
i = 0
for item in items:
    data = (item[0][0][0].text, item[0][0][1][1][0].text)
    worksheet.write_row(i, 0, data, )
    i = i + 1

workbook.close()

