# -*- coding: utf-8 -*-
"""
Created on 2020-05-05 22:30

bank-product-tool

@author: Tianyu
"""

from selenium import webdriver  # 导入库
from lxml import etree
import time
import json
import warnings

warnings.filterwarnings('ignore')


# 启动模拟浏览器
def ini_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #     options.add_argument('User-Agent={}'.format(UserAgent().random))
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    #    prefs = {"profile.managed_default_content_settings.images": 2}
    #    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_options=options)
    browser.get('http://www.baidu.com')
    return browser


# 加载页面
def load_page(browser, load_cnt, sleep_time):
    i = 0
    while i < load_cnt:
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        i += 1
    time.sleep(sleep_time)


# 单页信息爬取
def single_page_scraper(browser1, browser2, json_file):

    tree1 = etree.HTML(browser1.page_source)  # 获取源码

    link_list = tree1.xpath(
        "//*[@class='c_content']/div[@id='cList']//div[@class='prdBlock']")

    # 开始爬取并保存全部产品信息
    n = 0
    all_prod = []
    while n < len(link_list):
        try:
            info = {}  # 单个产品的信息字典
            #     print(link.xpath("//table[@class='buyArea']/tbody/tr/td/a[@class='viewMore']//@href")[0])
            print(n)
            link = tree1.xpath(
                "//table[@class='buyArea']/tbody/tr/td/a[@class='viewMore']//@href")[n]
            prod_url = 'http://www.cmbchina.com' + link
            #     print(sub_link)
            browser2.get(prod_url)
            tree2 = etree.HTML(browser2.page_source)  # 获取源码

            # 爬每个产品的详细信息
            i = 1
            while i <= len(tree2.xpath("//*[@id='content_panel']/div/table/tbody//tr")):

                info_key = tree2.xpath("//*[@id='content_panel']/div/table/tbody/tr[{i}]/td[1]/p/span[1]".format(i=i))[
                    0].text
                print(info_key)

                desc = ''

                for s in tree2.xpath("//*[@id='content_panel']/div/table/tbody/tr[{i}]/td[2]/p//span".format(i=i)):
                    #             print(type(s.text))
                    desc += str(s.text)

                # print(tmp)
                info[info_key] = desc

                i += 1

            print(info)
            with open(json_file, 'a', encoding="utf-8") as f:
                json.dump(info, f, ensure_ascii=False, indent=4)
                f.write('\n')

        except Exception as e:
            print(e)

        all_prod.append(info)
        n += 1


# 多页信息爬取
def multi_page_scraper(browser1, browser2):

    # 产品列表页面链接
    base_url = 'http://www.cmbchina.com/cfweb/personal/ProdBySeries.aspx?code=010011'
    browser1.get(base_url)

    p = 1
    while p <= 10:
        # 加载产品列表页面
        load_page(browser1, 5, 10)
        single_page_scraper(browser1, browser2, 'cmb_dep_prd.json')

        p += 1
        browser1.execute_script("javascript:loadpage({p})".format(p=p))
        time.sleep(5)


if __name__ == '__main__':
    # 开启两个模拟器
    browser1 = ini_browser()
    browser2 = ini_browser()

    multi_page_scraper(browser1, browser2)
