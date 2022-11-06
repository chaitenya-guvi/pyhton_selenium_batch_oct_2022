from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class  DropdownExample2():

    def  test1(self):

        baseurl = "https://courses.letskodeit.com/practice"

        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseurl)


        xpath_to_carselect_dropdown = 'carselect'
        element = driver.find_element(By.ID,xpath_to_carselect_dropdown)
        time.sleep(4)
        sel = Select(element)

        # select ing by value
        sel.select_by_value("honda")
        time.sleep(5)

        # selecting by index
        sel.select_by_index(0)
        time.sleep(5)


        # selecting by text
        sel.select_by_visible_text("Benz")
        time.sleep(5)

        # selecting by index - 2
        sel.select_by_index("1")

        driver.quit()


ff = DropdownExample2()
ff.test1()

