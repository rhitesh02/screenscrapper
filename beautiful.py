import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup

#import URL data here
url = "http://www.hubertiming.com/results/2018MLK"
html = urlopen(url)

#extract website tags
soup = BeautifulSoup(html, features="html.parser")

# get column headers 
header_list = []
col_headers = soup.find_all('th')
for col in col_headers:
    header_list.append(col.text)

# get all data from table
data = []

allrows = soup.find_all("tr")
for row in allrows:
    row_list = row.find_all("td")
    dataRow = []
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
data = data[5:]

df = pd.DataFrame(data).dropna(axis=0, how='any')
# add headers to rows
df.columns = header_list


print(df.head(5))
print(df.tail(5))



