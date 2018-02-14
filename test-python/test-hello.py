# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=1&s=1&click=0"

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

# 模拟下滑到底部操作
for i in range(1, 5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# 将加载好的页面源码给bs4解析
soup = BeautifulSoup(driver.page_source, "html.parser")

# 进行信息的抽取（商品名称，价格）
goods_info = soup.select(".gl-item")
for info in goods_info:
    title = info.select(".p-name.p-name-type-2 a")[0].text.strip()
    price = info.select(".p-price")[0].text.strip()
    print title
    print price

driver.close()


import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 5

