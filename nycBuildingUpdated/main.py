from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as BS

from time import sleep

import pandas as pd

import csv

import warnings
warnings.filterwarnings('ignore')



# Start the Selenium WebDriver
path = r'chromedriver.exe'
driver = webdriver.Chrome(path)

# url = "https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=15&allcount=0071&licensetype=G&licname=b&licstatus=&requestid=1"

# Navigate to the URL containing the data you want to scrape
urlList = ["https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=b&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=15&allcount=0071&licensetype=G&licname=b&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=20&allcount=0141&licensetype=G&licname=b&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=12&allcount=0211&licensetype=G&licname=b&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=13&allcount=0281&licensetype=G&licname=b&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=11&allcount=0351&licensetype=G&licname=b&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=11&allcount=0421&licensetype=G&licname=b&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=13&allcount=0491&licensetype=G&licname=b&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=11&allcount=0561&licensetype=G&licname=b&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=12&allcount=0631&licensetype=G&licname=b&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=16&allcount=0701&licensetype=G&licname=b&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=15&allcount=0771&licensetype=G&licname=b&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=28&next.y=9&allcount=0841&licensetype=G&licname=b&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=15&allcount=0911&licensetype=G&licname=b&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=15&allcount=0981&licensetype=G&licname=b&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=15&allcount=1051&licensetype=G&licname=b&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=8&allcount=1121&licensetype=G&licname=b&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=16&allcount=1191&licensetype=G&licname=b&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=17&allcount=1261&licensetype=G&licname=b&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=11&allcount=1331&licensetype=G&licname=b&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=13&allcount=1401&licensetype=G&licname=b&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=16&allcount=1471&licensetype=G&licname=b&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=23&allcount=1541&licensetype=G&licname=b&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=10&allcount=1611&licensetype=G&licname=b&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=14&allcount=1681&licensetype=G&licname=b&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=22&next.y=14&allcount=1751&licensetype=G&licname=b&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=15&allcount=1821&licensetype=G&licname=b&licstatus=&requestid=26",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=13&allcount=1891&licensetype=G&licname=b&licstatus=&requestid=27",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=12&allcount=1961&licensetype=G&licname=b&licstatus=&requestid=28",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=c&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=16&allcount=0071&licensetype=G&licname=c&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=28&next.y=10&allcount=0141&licensetype=G&licname=c&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=16&allcount=0211&licensetype=G&licname=c&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=23&next.y=14&allcount=0281&licensetype=G&licname=c&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=22&allcount=0351&licensetype=G&licname=c&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=27&next.y=13&allcount=0421&licensetype=G&licname=c&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=5&allcount=0491&licensetype=G&licname=c&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=9&allcount=0561&licensetype=G&licname=c&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=14&allcount=0631&licensetype=G&licname=c&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=56&next.y=11&allcount=0701&licensetype=G&licname=c&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=10&allcount=0771&licensetype=G&licname=c&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=8&allcount=0841&licensetype=G&licname=c&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=16&allcount=0911&licensetype=G&licname=c&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=12&allcount=0981&licensetype=G&licname=c&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=4&allcount=1051&licensetype=G&licname=c&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=11&allcount=1121&licensetype=G&licname=c&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=8&allcount=1191&licensetype=G&licname=c&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=10&allcount=1261&licensetype=G&licname=c&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=12&allcount=1331&licensetype=G&licname=c&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=56&next.y=17&allcount=1401&licensetype=G&licname=c&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=19&allcount=1471&licensetype=G&licname=c&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=7&allcount=1541&licensetype=G&licname=c&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=13&allcount=1611&licensetype=G&licname=c&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=14&allcount=1681&licensetype=G&licname=c&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=16&allcount=1751&licensetype=G&licname=c&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=3&allcount=1821&licensetype=G&licname=c&licstatus=&requestid=26",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=25&next.y=10&allcount=1891&licensetype=G&licname=c&licstatus=&requestid=27",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=3&allcount=1961&licensetype=G&licname=c&licstatus=&requestid=28",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=2031&licensetype=G&licname=c&licstatus=&requestid=29",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=16&allcount=2101&licensetype=G&licname=c&licstatus=&requestid=30",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=6&allcount=2171&licensetype=G&licname=c&licstatus=&requestid=31",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=9&allcount=2241&licensetype=G&licname=c&licstatus=&requestid=32",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=5&allcount=2311&licensetype=G&licname=c&licstatus=&requestid=33",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=16&next.y=12&allcount=2381&licensetype=G&licname=c&licstatus=&requestid=34",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=d&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=11&allcount=0071&licensetype=G&licname=d&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=7&allcount=0141&licensetype=G&licname=d&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=24&next.y=14&allcount=0211&licensetype=G&licname=d&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=3&allcount=0281&licensetype=G&licname=d&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=71&next.y=18&allcount=0351&licensetype=G&licname=d&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=27&next.y=11&allcount=0421&licensetype=G&licname=d&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=8&allcount=0491&licensetype=G&licname=d&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=13&allcount=0561&licensetype=G&licname=d&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=17&allcount=0631&licensetype=G&licname=d&licstatus=&requestid=9", 
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=15&allcount=0701&licensetype=G&licname=d&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=15&allcount=0771&licensetype=G&licname=d&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=6&allcount=0841&licensetype=G&licname=d&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=14&allcount=0911&licensetype=G&licname=d&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=15&allcount=0981&licensetype=G&licname=d&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=12&allcount=1051&licensetype=G&licname=d&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=29&next.y=8&allcount=1121&licensetype=G&licname=d&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=10&allcount=1191&licensetype=G&licname=d&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=13&allcount=1261&licensetype=G&licname=d&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=1331&licensetype=G&licname=d&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=9&allcount=1401&licensetype=G&licname=d&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=10&allcount=1471&licensetype=G&licname=d&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=e&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=11&allcount=0071&licensetype=G&licname=e&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=8&allcount=0141&licensetype=G&licname=e&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=9&allcount=0211&licensetype=G&licname=e&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=7&allcount=0281&licensetype=G&licname=e&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=11&allcount=0351&licensetype=G&licname=e&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=17&allcount=0421&licensetype=G&licname=e&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=f&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=12&allcount=0071&licensetype=G&licname=f&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=16&allcount=0141&licensetype=G&licname=f&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=6&allcount=0211&licensetype=G&licname=f&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=67&next.y=7&allcount=0281&licensetype=G&licname=f&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=15&allcount=0351&licensetype=G&licname=f&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=15&allcount=0421&licensetype=G&licname=f&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=56&next.y=13&allcount=0491&licensetype=G&licname=f&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=16&allcount=0561&licensetype=G&licname=f&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=13&allcount=0631&licensetype=G&licname=f&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=13&allcount=0701&licensetype=G&licname=f&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=3&allcount=0771&licensetype=G&licname=f&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=16&allcount=0841&licensetype=G&licname=f&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=16&allcount=0911&licensetype=G&licname=f&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=14&allcount=0981&licensetype=G&licname=f&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=8&allcount=1051&licensetype=G&licname=f&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=12&allcount=1121&licensetype=G&licname=f&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=12&allcount=1191&licensetype=G&licname=f&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=g&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=16&allcount=0071&licensetype=G&licname=g&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=7&allcount=0141&licensetype=G&licname=g&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=7&allcount=0211&licensetype=G&licname=g&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=15&allcount=0281&licensetype=G&licname=g&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=7&allcount=0351&licensetype=G&licname=g&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=13&next.y=11&allcount=0421&licensetype=G&licname=g&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=17&allcount=0491&licensetype=G&licname=g&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=15&allcount=0561&licensetype=G&licname=g&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=67&next.y=17&allcount=0631&licensetype=G&licname=g&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=12&allcount=0701&licensetype=G&licname=g&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=5&allcount=0771&licensetype=G&licname=g&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=10&allcount=0841&licensetype=G&licname=g&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=17&next.y=16&allcount=0911&licensetype=G&licname=g&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=7&allcount=0981&licensetype=G&licname=g&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=15&allcount=1051&licensetype=G&licname=g&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=29&next.y=20&allcount=1121&licensetype=G&licname=g&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=16&next.y=20&allcount=1191&licensetype=G&licname=g&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=20&allcount=1261&licensetype=G&licname=g&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=15&allcount=1331&licensetype=G&licname=g&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=9&allcount=1401&licensetype=G&licname=g&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=7&allcount=1471&licensetype=G&licname=g&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=1541&licensetype=G&licname=g&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=63&next.y=10&allcount=1611&licensetype=G&licname=g&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=13&allcount=1681&licensetype=G&licname=g&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=9&allcount=1751&licensetype=G&licname=g&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=h&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=21&next.y=11&allcount=0071&licensetype=G&licname=h&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=11&allcount=0141&licensetype=G&licname=h&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=16&allcount=0211&licensetype=G&licname=h&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=60&next.y=17&allcount=0281&licensetype=G&licname=h&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=14&allcount=0351&licensetype=G&licname=h&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=10&allcount=0421&licensetype=G&licname=h&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=8&allcount=0491&licensetype=G&licname=h&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=14&allcount=0561&licensetype=G&licname=h&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=8&allcount=0631&licensetype=G&licname=h&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=10&allcount=0701&licensetype=G&licname=h&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=21&next.y=11&allcount=0771&licensetype=G&licname=h&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=12&allcount=0841&licensetype=G&licname=h&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=15&allcount=0911&licensetype=G&licname=h&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=14&allcount=0981&licensetype=G&licname=h&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=8&allcount=1051&licensetype=G&licname=h&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=24&next.y=18&allcount=1121&licensetype=G&licname=h&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=12&allcount=1191&licensetype=G&licname=h&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=13&allcount=1261&licensetype=G&licname=h&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=i&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=69&next.y=9&allcount=0071&licensetype=G&licname=i&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=11&allcount=0141&licensetype=G&licname=i&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=9&allcount=0211&licensetype=G&licname=i&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=10&allcount=0281&licensetype=G&licname=i&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=j&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=7&allcount=0071&licensetype=G&licname=j&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=17&allcount=0141&licensetype=G&licname=j&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=3&allcount=0211&licensetype=G&licname=j&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=63&next.y=11&allcount=0281&licensetype=G&licname=j&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=22&next.y=3&allcount=0351&licensetype=G&licname=j&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=12&allcount=0421&licensetype=G&licname=j&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=10&allcount=0491&licensetype=G&licname=j&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=k&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=8&allcount=0071&licensetype=G&licname=k&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=12&allcount=0141&licensetype=G&licname=k&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=18&allcount=0211&licensetype=G&licname=k&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=3&allcount=0281&licensetype=G&licname=k&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=11&allcount=0351&licensetype=G&licname=k&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=14&allcount=0421&licensetype=G&licname=k&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=65&next.y=10&allcount=0491&licensetype=G&licname=k&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=3&allcount=0561&licensetype=G&licname=k&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=7&allcount=0631&licensetype=G&licname=k&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=18&allcount=0701&licensetype=G&licname=k&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=6&allcount=0771&licensetype=G&licname=k&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=17&allcount=0841&licensetype=G&licname=k&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=56&next.y=17&allcount=0911&licensetype=G&licname=k&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=10&allcount=0981&licensetype=G&licname=k&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=17&allcount=1051&licensetype=G&licname=k&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=7&allcount=1121&licensetype=G&licname=k&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=27&next.y=13&allcount=1191&licensetype=G&licname=k&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=3&allcount=1261&licensetype=G&licname=k&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=19&allcount=1331&licensetype=G&licname=k&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=19&allcount=1401&licensetype=G&licname=k&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=27&next.y=13&allcount=1471&licensetype=G&licname=k&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=23&next.y=13&allcount=1541&licensetype=G&licname=k&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=18&allcount=1611&licensetype=G&licname=k&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=14&allcount=1681&licensetype=G&licname=k&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=11&allcount=1751&licensetype=G&licname=k&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=64&next.y=8&allcount=1821&licensetype=G&licname=k&licstatus=&requestid=26",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=l&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=14&allcount=0071&licensetype=G&licname=l&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=7&allcount=0141&licensetype=G&licname=l&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=16&allcount=0211&licensetype=G&licname=l&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=24&next.y=8&allcount=0281&licensetype=G&licname=l&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=4&allcount=0351&licensetype=G&licname=l&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=14&allcount=0421&licensetype=G&licname=l&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=19&allcount=0491&licensetype=G&licname=l&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=10&allcount=0561&licensetype=G&licname=l&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=9&allcount=0631&licensetype=G&licname=l&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=22&next.y=20&allcount=0701&licensetype=G&licname=l&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=20&next.y=13&allcount=0771&licensetype=G&licname=l&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=6&allcount=0841&licensetype=G&licname=l&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=15&allcount=0911&licensetype=G&licname=l&licstatus=&requestid=13",    
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=8&allcount=0981&licensetype=G&licname=l&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=2&allcount=1051&licensetype=G&licname=l&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=8&allcount=1121&licensetype=G&licname=l&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=8&allcount=1191&licensetype=G&licname=l&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=23&allcount=1261&licensetype=G&licname=l&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=7&allcount=1331&licensetype=G&licname=l&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=17&allcount=1401&licensetype=G&licname=l&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=12&allcount=1471&licensetype=G&licname=l&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=10&allcount=1541&licensetype=G&licname=l&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=11&allcount=1611&licensetype=G&licname=l&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=29&next.y=18&allcount=1681&licensetype=G&licname=l&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=m&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=63&next.y=13&allcount=0071&licensetype=G&licname=m&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=13&allcount=0141&licensetype=G&licname=m&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=16&allcount=0211&licensetype=G&licname=m&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=0281&licensetype=G&licname=m&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=16&allcount=0351&licensetype=G&licname=m&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=10&allcount=0421&licensetype=G&licname=m&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=15&allcount=0491&licensetype=G&licname=m&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=15&allcount=0561&licensetype=G&licname=m&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=17&allcount=0631&licensetype=G&licname=m&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=14&allcount=0701&licensetype=G&licname=m&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=6&allcount=0771&licensetype=G&licname=m&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=21&allcount=0841&licensetype=G&licname=m&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=14&allcount=0911&licensetype=G&licname=m&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=0981&licensetype=G&licname=m&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=13&allcount=1051&licensetype=G&licname=m&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=13&allcount=1121&licensetype=G&licname=m&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=13&allcount=1191&licensetype=G&licname=m&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=16&allcount=1261&licensetype=G&licname=m&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=56&next.y=20&allcount=1331&licensetype=G&licname=m&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=8&allcount=1401&licensetype=G&licname=m&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=15&allcount=1471&licensetype=G&licname=m&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=13&allcount=1541&licensetype=G&licname=m&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=18&allcount=1611&licensetype=G&licname=m&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=17&allcount=1681&licensetype=G&licname=m&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=17&allcount=1751&licensetype=G&licname=m&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=15&allcount=1821&licensetype=G&licname=m&licstatus=&requestid=26",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=13&allcount=1891&licensetype=G&licname=m&licstatus=&requestid=27",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=17&allcount=1961&licensetype=G&licname=m&licstatus=&requestid=28",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=6&allcount=2031&licensetype=G&licname=m&licstatus=&requestid=29",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=1&allcount=2101&licensetype=G&licname=m&licstatus=&requestid=30",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=18&allcount=2171&licensetype=G&licname=m&licstatus=&requestid=31",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=20&allcount=2241&licensetype=G&licname=m&licstatus=&requestid=32",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=20&allcount=2311&licensetype=G&licname=m&licstatus=&requestid=33",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=6&allcount=2381&licensetype=G&licname=m&licstatus=&requestid=34",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=10&allcount=2451&licensetype=G&licname=m&licstatus=&requestid=35",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=15&allcount=2521&licensetype=G&licname=m&licstatus=&requestid=36",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=8&allcount=2591&licensetype=G&licname=m&licstatus=&requestid=37",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=5&allcount=2661&licensetype=G&licname=m&licstatus=&requestid=38",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=5&allcount=2731&licensetype=G&licname=m&licstatus=&requestid=39",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=29&next.y=12&allcount=2801&licensetype=G&licname=m&licstatus=&requestid=40",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=n&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=14&allcount=0071&licensetype=G&licname=n&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=15&allcount=0141&licensetype=G&licname=n&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=23&next.y=11&allcount=0211&licensetype=G&licname=n&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=20&allcount=0281&licensetype=G&licname=n&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=65&next.y=16&allcount=0351&licensetype=G&licname=n&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=17&allcount=0421&licensetype=G&licname=n&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=16&next.y=20&allcount=0491&licensetype=G&licname=n&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=14&allcount=0561&licensetype=G&licname=n&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=19&allcount=0631&licensetype=G&licname=n&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=o&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=8&allcount=0071&licensetype=G&licname=o&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=14&allcount=0141&licensetype=G&licname=o&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=13&allcount=0211&licensetype=G&licname=o&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=14&allcount=0281&licensetype=G&licname=o&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=5&allcount=0351&licensetype=G&licname=o&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=64&next.y=12&allcount=0421&licensetype=G&licname=o&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=p&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=10&allcount=0071&licensetype=G&licname=p&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=62&next.y=19&allcount=0141&licensetype=G&licname=p&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=10&allcount=0211&licensetype=G&licname=p&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=11&allcount=0281&licensetype=G&licname=p&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=11&allcount=0351&licensetype=G&licname=p&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=13&allcount=0421&licensetype=G&licname=p&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=17&allcount=0491&licensetype=G&licname=p&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=17&allcount=0561&licensetype=G&licname=p&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=11&allcount=0631&licensetype=G&licname=p&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=16&allcount=0701&licensetype=G&licname=p&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=64&next.y=12&allcount=0771&licensetype=G&licname=p&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=20&allcount=0841&licensetype=G&licname=p&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=11&allcount=0911&licensetype=G&licname=p&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=7&allcount=0981&licensetype=G&licname=p&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=15&allcount=1051&licensetype=G&licname=p&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=8&allcount=1121&licensetype=G&licname=p&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=28&next.y=10&allcount=1191&licensetype=G&licname=p&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=14&allcount=1261&licensetype=G&licname=p&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=14&allcount=1331&licensetype=G&licname=p&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=23&allcount=1401&licensetype=G&licname=p&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=9&allcount=1471&licensetype=G&licname=p&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=10&allcount=1541&licensetype=G&licname=p&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=18&allcount=1611&licensetype=G&licname=p&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=18&allcount=1611&licensetype=G&licname=p&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=42&next.y=11&allcount=1681&licensetype=G&licname=p&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=8&allcount=1751&licensetype=G&licname=p&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=17&allcount=1821&licensetype=G&licname=p&licstatus=&requestid=26",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=q&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=7&allcount=0071&licensetype=G&licname=q&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=r&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=67&next.y=14&allcount=0071&licensetype=G&licname=r&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=58&next.y=8&allcount=0141&licensetype=G&licname=r&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=52&next.y=2&allcount=0211&licensetype=G&licname=r&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=12&allcount=0281&licensetype=G&licname=r&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=10&allcount=0351&licensetype=G&licname=r&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=53&next.y=21&allcount=0421&licensetype=G&licname=r&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=52&next.y=17&allcount=0491&licensetype=G&licname=r&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=12&allcount=0561&licensetype=G&licname=r&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=10&allcount=0631&licensetype=G&licname=r&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=7&allcount=0701&licensetype=G&licname=r&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=15&allcount=0771&licensetype=G&licname=r&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=11&allcount=0841&licensetype=G&licname=r&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=8&allcount=0911&licensetype=G&licname=r&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=71&next.y=9&allcount=0981&licensetype=G&licname=r&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=4&allcount=1051&licensetype=G&licname=r&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=16&allcount=1121&licensetype=G&licname=r&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=16&allcount=1191&licensetype=G&licname=r&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=9&allcount=1261&licensetype=G&licname=r&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=14&allcount=1331&licensetype=G&licname=r&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=14&allcount=1401&licensetype=G&licname=r&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=9&allcount=1471&licensetype=G&licname=r&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=40&next.y=13&allcount=1541&licensetype=G&licname=r&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=18&allcount=1611&licensetype=G&licname=r&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=s&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=22&next.y=11&allcount=0071&licensetype=G&licname=s&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=14&allcount=0141&licensetype=G&licname=s&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=20&allcount=0211&licensetype=G&licname=s&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=4&allcount=0281&licensetype=G&licname=s&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=69&next.y=18&allcount=0351&licensetype=G&licname=s&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=7&allcount=0421&licensetype=G&licname=s&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=63&next.y=10&allcount=0491&licensetype=G&licname=s&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=13&allcount=0561&licensetype=G&licname=s&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=3&allcount=0631&licensetype=G&licname=s&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=4&allcount=0701&licensetype=G&licname=s&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=69&next.y=12&allcount=0771&licensetype=G&licname=s&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=10&allcount=0841&licensetype=G&licname=s&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=14&allcount=0911&licensetype=G&licname=s&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=52&next.y=3&allcount=0981&licensetype=G&licname=s&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=12&allcount=1051&licensetype=G&licname=s&licstatus=&requestid=15",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=16&allcount=1121&licensetype=G&licname=s&licstatus=&requestid=16",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=1191&licensetype=G&licname=s&licstatus=&requestid=17",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=24&next.y=6&allcount=1261&licensetype=G&licname=s&licstatus=&requestid=18",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=13&allcount=1331&licensetype=G&licname=s&licstatus=&requestid=19",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=63&next.y=12&allcount=1401&licensetype=G&licname=s&licstatus=&requestid=20",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=51&next.y=17&allcount=1471&licensetype=G&licname=s&licstatus=&requestid=21",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=9&allcount=1541&licensetype=G&licname=s&licstatus=&requestid=22",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=28&next.y=13&allcount=1611&licensetype=G&licname=s&licstatus=&requestid=23",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=27&next.y=9&allcount=1681&licensetype=G&licname=s&licstatus=&requestid=24",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=19&allcount=1751&licensetype=G&licname=s&licstatus=&requestid=25",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=11&allcount=1821&licensetype=G&licname=s&licstatus=&requestid=26",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=52&next.y=20&allcount=1891&licensetype=G&licname=s&licstatus=&requestid=27",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=14&allcount=1961&licensetype=G&licname=s&licstatus=&requestid=28",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=9&allcount=2031&licensetype=G&licname=s&licstatus=&requestid=29",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=32&next.y=13&allcount=2101&licensetype=G&licname=s&licstatus=&requestid=30",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=15&allcount=2171&licensetype=G&licname=s&licstatus=&requestid=31",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=21&allcount=2241&licensetype=G&licname=s&licstatus=&requestid=32",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=76&next.y=10&allcount=2311&licensetype=G&licname=s&licstatus=&requestid=33",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=13&allcount=2381&licensetype=G&licname=s&licstatus=&requestid=34",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=34&next.y=8&allcount=2451&licensetype=G&licname=s&licstatus=&requestid=35",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=6&allcount=2521&licensetype=G&licname=s&licstatus=&requestid=36",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=8&allcount=2591&licensetype=G&licname=s&licstatus=&requestid=37",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=13&allcount=2661&licensetype=G&licname=s&licstatus=&requestid=38",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=16&next.y=3&allcount=2731&licensetype=G&licname=s&licstatus=&requestid=39",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=15&allcount=2801&licensetype=G&licname=s&licstatus=&requestid=40",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=66&next.y=17&allcount=2871&licensetype=G&licname=s&licstatus=&requestid=41",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=12&allcount=2941&licensetype=G&licname=s&licstatus=&requestid=42",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=24&allcount=3011&licensetype=G&licname=s&licstatus=&requestid=43",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=65&next.y=8&allcount=3081&licensetype=G&licname=s&licstatus=&requestid=44",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=41&next.y=13&allcount=3151&licensetype=G&licname=s&licstatus=&requestid=45",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=18&next.y=18&allcount=3221&licensetype=G&licname=s&licstatus=&requestid=46",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=1&allcount=3291&licensetype=G&licname=s&licstatus=&requestid=47",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=8&allcount=3361&licensetype=G&licname=s&licstatus=&requestid=48",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=75&next.y=7&allcount=3431&licensetype=G&licname=s&licstatus=&requestid=49",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=13&allcount=3501&licensetype=G&licname=s&licstatus=&requestid=50",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=t&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=20&allcount=0071&licensetype=G&licname=t&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=14&allcount=0141&licensetype=G&licname=t&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=64&next.y=10&allcount=0211&licensetype=G&licname=t&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=10&allcount=0281&licensetype=G&licname=t&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=13&allcount=0351&licensetype=G&licname=t&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=57&next.y=14&allcount=0421&licensetype=G&licname=t&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=33&next.y=5&allcount=0491&licensetype=G&licname=t&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=23&next.y=4&allcount=0561&licensetype=G&licname=t&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=37&next.y=15&allcount=0631&licensetype=G&licname=t&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=16&allcount=0701&licensetype=G&licname=t&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=67&next.y=18&allcount=0771&licensetype=G&licname=t&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=6&allcount=0841&licensetype=G&licname=t&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=36&next.y=6&allcount=0911&licensetype=G&licname=t&licstatus=&requestid=13",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=39&next.y=17&allcount=0981&licensetype=G&licname=t&licstatus=&requestid=14",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=u&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=60&next.y=16&allcount=0071&licensetype=G&licname=u&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=v&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=5&allcount=0071&licensetype=G&licname=v&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=49&next.y=19&allcount=0141&licensetype=G&licname=v&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=43&next.y=8&allcount=0211&licensetype=G&licname=v&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=7&allcount=0281&licensetype=G&licname=v&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=35&next.y=15&allcount=0351&licensetype=G&licname=v&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=11&allcount=0421&licensetype=G&licname=v&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=50&next.y=9&allcount=0491&licensetype=G&licname=v&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=52&next.y=10&allcount=0561&licensetype=G&licname=v&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=38&next.y=10&allcount=0631&licensetype=G&licname=v&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=w&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=15&allcount=0071&licensetype=G&licname=w&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=4&allcount=0141&licensetype=G&licname=w&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=44&next.y=15&allcount=0211&licensetype=G&licname=w&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=48&next.y=9&allcount=0281&licensetype=G&licname=w&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=10&allcount=0351&licensetype=G&licname=w&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=55&next.y=5&allcount=0421&licensetype=G&licname=w&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=12&allcount=0491&licensetype=G&licname=w&licstatus=&requestid=7",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=26&next.y=17&allcount=0561&licensetype=G&licname=w&licstatus=&requestid=8",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=65&next.y=14&allcount=0631&licensetype=G&licname=w&licstatus=&requestid=9",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=31&next.y=13&allcount=0701&licensetype=G&licname=w&licstatus=&requestid=10",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=54&next.y=9&allcount=0771&licensetype=G&licname=w&licstatus=&requestid=11",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=47&next.y=13&allcount=0841&licensetype=G&licname=w&licstatus=&requestid=12",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=x&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=y&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=59&next.y=19&allcount=0071&licensetype=G&licname=y&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=60&next.y=12&allcount=0141&licensetype=G&licname=y&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=52&next.y=1&allcount=0211&licensetype=G&licname=y&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=19&next.y=14&allcount=0281&licensetype=G&licname=y&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?licname=z&licensetype=G&go1=+GO+&requestid=0",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=30&next.y=18&allcount=0071&licensetype=G&licname=z&licstatus=&requestid=1",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=45&next.y=18&allcount=0141&licensetype=G&licname=z&licstatus=&requestid=2",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=20&next.y=8&allcount=0211&licensetype=G&licname=z&licstatus=&requestid=3",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=61&next.y=10&allcount=0281&licensetype=G&licname=z&licstatus=&requestid=4",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=18&next.y=10&allcount=0351&licensetype=G&licname=z&licstatus=&requestid=5",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=46&next.y=10&allcount=0421&licensetype=G&licname=z&licstatus=&requestid=6",
"https://a810-bisweb.nyc.gov/bisweb/ResultsByNameServlet?next.x=60&next.y=12&allcount=0491&licensetype=G&licname=z&licstatus=&requestid=7"]

# driver.get(url)

# page = driver.page_source

# soup = BS(page, "lxml")
# body = soup.find('body')
# center = body.find('center')
# table = center.find_all('table')

# for i, tbl in enumerate(table):
#     print(i)
#     print(tbl)
#     print("************************************************************")

allPersonlinks = pd.DataFrame(columns=['Name', 'Link'])

# allPersonlinks

# for url in urlList:
#     print(url)

for url in urlList[:2]:
    sleep(2)
    
    # Start the Selenium WebDriver
    path = r'chromedriver.exe'
    driver = webdriver.Chrome(path)
    
    
    driver.get(url)
    sleep(2)
    
    page = driver.page_source
    soup = BS(page, "lxml")
    body = soup.find('body')
    center = body.find('center')
    table = center.find_all('table')

    for i, tbl in enumerate(table):
        if(i == 4):

            intbody = tbl.find('tbody')
            intr = intbody.find_all('tr')

            for k, tr in enumerate(intr):
                if(k !=0):

                    inintd = tr.find_all('td', class_='content')

                    combinefirsturl = "https://a810-bisweb.nyc.gov/bisweb"

                    for j, td in enumerate(inintd):

                        if(j == 0):

                            link = td.find("a")
                            # print(link.text)
                            Name = link.text
                            href = link["href"]
                            combine = combinefirsturl + "/" + href
                            # print(combine)   
                            Link = combine

                            row = [Name, Link]

                            # Convert the row to a dataframe
                            row_df = pd.DataFrame([row], columns=allPersonlinks.columns)

                            # Concatenate the row dataframe to the existing dataframe
                            allPersonlinks = pd.concat([allPersonlinks, row_df], ignore_index=True)

# allPersonlinks

allPersonlinks.to_csv('personLinks.csv', index=False)



import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as BS

from time import sleep

import csv

import warnings
warnings.filterwarnings('ignore')



df = pd.read_csv('personLinks.csv')

# df.head()

# Start the Selenium WebDriver
path = r'chromedriver.exe'
driver = webdriver.Chrome(path)



allFinalData = []


# for firstName, link in zip(df['Name'], df['Link']):
for firstName, link in zip(df['Name'][:2], df['Link'][:2]):
    
#     sleep(1)
    driver = webdriver.Chrome(path)
    sleep(2)
    
    driver.get(link)

    page = driver.page_source

    soup = BS(page, "lxml")
    body = soup.find('body')
    center = body.find('center')
    table = center.find_all('table')
    
    for index, item in enumerate(table):

        if (index == 3):

            safetyarr = []
            tablearr = []
            endorsementarr = []

            tbody = item.find('tbody')
            tr = tbody.find_all('tr')
            
            name = ""

            for idx, row in enumerate(tr):

                if(idx == 1):
                    rawName = row.find_all('td', class_='centercolhdg')

                    for itemName in rawName:
                        name = itemName.text
#                         safetyarr.append(name)
#                         print(name)
#                         print("++++++++++++++")
        
#                 print(name)
                if(name == ""):
#                     print("here")
                    flag = 1
                    flaggyy = 0
                else:
#                     print("there")
                    flag = 0
                    flaggyy = -1
                    

                if(idx == (4+flag)):
                    dateCont = row.find_all('td', class_='content')

                    for i, itemDateCont in enumerate(dateCont):
                        if(i == 0):
                            date = itemDateCont.text
                            safetyarr.append(date)
                            # print(date)
                        if(i == 1):
                            contId = itemDateCont.text
                            safetyarr.append(contId)
                        #     print(contId)
                        #
                        # print("+++++++++++++++")


                if (idx == (5+flag)):
                    statusExp = row.find_all('td', class_='content')

                    for i, itemstatusExp in enumerate(statusExp):
                        if (i == 0):
                            status1 = itemstatusExp.text
                            safetyarr.append(status1)
                            # print(status1)
                        if (i == 1):
                            expiration = itemstatusExp.text
                            safetyarr.append(expiration)
                        #     print(expiration)
                        #
                        # print("+++++++++++++++")

                if (idx == (6+flag)):
                    cityEmpRaw = row.find_all('td', class_='content')

                    for i, itemcityEmp in enumerate(cityEmpRaw):
                        if (i == 0):
                           cityEmp  = itemcityEmp.text
                           safetyarr.append(cityEmp)
                        #    print(cityEmp)
                        #
                        # print("+++++++++++++++")

                if (idx == (7+flag)):
                    officeAddressRaw = row.find_all('td', class_='content')

                    for i, itemofficeAdd in enumerate(officeAddressRaw):
                        if (i == 0):
                           officeAdd  = itemofficeAdd.text
                           safetyarr.append(officeAdd)
                        #    print(officeAdd)
                        #
                        # print("+++++++++++++++")

                if (idx == (8+flag)):
                    bussinessPhoneRaw = row.find_all('td', class_='content')

                    for i, itembussinessPhone in enumerate(bussinessPhoneRaw):
                        if (i == 0):
                           bussPhone  = itembussinessPhone.text
                           safetyarr.append(bussPhone)
                        #    print(bussPhone)
                        #
                        # print("+++++++++++++++")

                if (idx == (12+flag)):
                    bussRaw = row.find_all('td', class_='content')

                    for i, itembuss in enumerate(bussRaw):
                        if (i == 0):
                           business1  = itembuss.text
                           safetyarr.append(business1)
                        #    print(business1)
                        #
                        # print("+++++++++++++++")

                if (idx == (13+flag)):
                    doingbussRaw = row.find_all('td', class_='content')

                    for i, itemdoingbuss in enumerate(doingbussRaw):
                        if (i == 0):
                           doingBussiness = itemdoingbuss.text
                           safetyarr.append(doingBussiness)
                        #    print(doingBussiness)
                        #
                        # print("+++++++++++++++")


                if (idx == (16+flaggyy) or idx == (17+flaggyy) or idx == (18+flaggyy)):
                    insidearr = []
                    alltd = row.find_all('td', class_='content')
                    alltdcenter = row.find_all('td', class_='centercontent')

                    for item in alltd:
                        output = item.text
                        insidearr.append(output)
                        # print(item.text)

                    for item in alltdcenter:
                        output = item.text
                        insidearr.append(output)
                        # print(item.text)
                    tablearr.append(insidearr)

                    # print(tablearr)
                    # print("+++++++++++")
#
                if (idx == (23) or idx == (24) or idx == (25)):
                    alltdrow = row.find_all('td', class_='content')

                    for item in alltdrow:
                        output = item.text
                        endorsementarr.append(output)
                    # print(endorsementarr)
#
#             print(safetyarr)
#             print(tablearr)
#             print(endorsementarr)

            finalarr = []
    
            finalarr.append(firstName)

            for i in safetyarr:
                finalarr.append(i)

            for i in tablearr:
                finalarr.append(i)

            for i in endorsementarr:
                finalarr.append(i)
                
                
#             print(finalarr)

            cleaned_data = []
            for item in finalarr:
                if isinstance(item, str):
                    cleaned_item = item.replace('\t', '').replace('\xa0', '').replace('\n', '')
                else:
                    cleaned_item = item
                cleaned_data.append(cleaned_item)
                
            allFinalData.append(cleaned_data)

            sleep(1)
            
    sleep(1)

firstPage = pd.DataFrame(allFinalData)

firstPage.to_csv("delte.csv", index=False)




