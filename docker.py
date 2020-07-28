from selenium.webdriver import Remote
import threading
from time import *


def test_gmaer(host, browser):
    print("開始：%s" % ctime())
    print(host, browser)
    dc = {'browserName': browser}
    driver = Remote(
        command_executor=host,
        desired_capabilities=dc
    )
    driver.get(r'https://www.gamer.com.tw/')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="BH-background"]/div[2]/div[1]/ul/li[6]/a/span[2]').click()
    sleep(4)
    #driver.get_screenshot_as_file(r'D:\testscreen\baidu.jpg')
    driver.quit()


if __name__ == '__main__':
    lists = {'http://192.168.30.128:5561/wd/hub': 'firefox',
             'http://192.168.30.128:5560/wd/hub': 'chrome'
             }
    threads = []
    files = range(len(lists))
    for host, browser in lists.items():
        t = threading.Thread(target=test_gmaer, args=(host, browser))
        threads.append(t)
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
