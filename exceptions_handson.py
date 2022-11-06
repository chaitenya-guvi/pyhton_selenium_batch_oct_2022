from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExceptionsExample():
    def hidden_element(self):
        #elementNotinteractable
        driver = webdriver.Chrome()
        base_url = "http://www.omayo.blogspot.com/"

        driver.get(base_url)

        xpath_of_hidden = "//input[@id='hbutton']"
        hidden_ele = driver.find_element(By.XPATH,xpath_of_hidden)
        hidden_ele.click()
        time.sleep(10)

    def webdriver_wait_example(self):

        driver = webdriver.Chrome()
        # base_url = "http://www.omayo.blogspot.com/"
        base_url = "https://courses.letskodeit.com/practice"

        driver.get(base_url)

        xpath_of_disable = "disabled-button"
        xpath_of_enable = "enabled-button"
        xpath_of_enable_input = "enabled-example-input"
        #explicit wait
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         xpath_of_enable_input)))

        time.sleep(10)



    def frame_example(self):

        driver = webdriver.Chrome()
        base_url = "http://www.omayo.blogspot.com/"

        driver.get(base_url)
        xpath_of_frame = "//iframe"
        time.sleep(1)
        try :
            driver.switch_to.frame(4)
        except NoSuchFrameException :
            print("Frame is not present ,please check the frame .")
        else :
            pass
        finally :
            driver.save_screenshot("example.png")
            print("into the final block . ")

        print("switch successfull")

        time.sleep(10)


    def window_example(self):

        driver = webdriver.Chrome()
        base_url = "http://www.omayo.blogspot.com/"

        driver.get(base_url)
        driver.get(base_url)

        driver.switch_to.window(4)
        print("switch successfull")

text_area = ExceptionsExample()
# text_area.hidden_element()
text_area.frame_example()
