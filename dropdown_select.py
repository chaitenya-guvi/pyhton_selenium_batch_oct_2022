from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select ## import select class


class DropdownSelect():

    def test(self):
        """
        Select class - only interactable with select tag
        select by : -index  -------
                    - value
                    - visible text

        :return:
        """

        baseUrl = "https://the-internet.herokuapp.com/dropdown"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        # driver.implicitly_wait(10)
        time.sleep(5)

        xpath_id_to_dropdown = "dropdown"
        element = driver.find_element(By.ID,xpath_id_to_dropdown)
        # passed web elements in the select class

        sel = Select(element)
        time.sleep(5)
        #Returns a list of all options belonging to this select tag
        print(sel.options)
        #iterating over web elements list and printing the text of options
        for values in sel.options :
            print(values.text)


        driver.quit()
        # sel.select_by_value("benz")
        # print("Select Benz by value")
        # time.sleep(2)
        #
        # sel.select_by_index("2")
        # print("Select Honda by index")
        # time.sleep(2)
        #
        # sel.select_by_visible_text("BMW")
        # print("Select BMW by visible text")
        # time.sleep(2)
        #
        # sel.select_by_index(2)
        # print("Select Honda by index")


ff = DropdownSelect()
ff.test()
