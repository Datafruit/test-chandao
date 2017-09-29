from selenium import  webdriver

def browser():
    # driver=webdriver.PhantomJS()
    driver=webdriver.Chrome()
    #driver=webdriver.Firefox()
    return driver



    #driver.get("http://www.baidu.com")
if __name__ == '__main__':
    browser()