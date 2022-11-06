from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains



class Javascripttry():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("https://letskodeit.teachable.com/pages/practice")
        # baseUrl = "https://the-internet.herokuapp.com/"
        baseurl = "https://courses.letskodeit.com/practice"
        driver.get(baseurl)

        driver.implicitly_wait(3)  #ignore for now , will discuss in next class


        # time.sleep(5)
        # #scrolling down by 1000 pixels
        # driver.execute_script("window.scrollBy(0, 1000);")
        #
        # time.sleep(10)
        # # scrolling up by 500 pixels
        # driver.execute_script("window.scrollBy(0, -500);")
        # time.sleep(5)


        # # driver find element alternative
        # # element = driver.find_element(By.ID, "name")
        # element = driver.execute_script("return document.getElementById('name');")
        # element.send_keys("Chaitenya")

        #scrolll in to view utilising javascript
        #our target is to get mouse hover into view

        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, -150);")

        time.sleep(10)




        driver.quit()

    def alert(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("https://letskodeit.teachable.com/pages/practice")
        # baseUrl = "https://the-internet.herokuapp.com/"
        baseurl = "https://courses.letskodeit.com/practice"
        driver.get(baseurl)

        #moving to mouse hover element
        actions = ActionChains(driver)
        mousehover_element = driver.find_element(By.ID, "mousehover")
        #moving into view
        driver.execute_script("arguments[0].scrollIntoView(true);", mousehover_element)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, -150);")

        actions.move_to_element(mousehover_element).perform()
        time.sleep(5)

        driver.quit()

    def dragdrop(self) :
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(5)
        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(fromElement, toElement)
            # actions.drag_and_drop(fromElement, toElement).perform()
            actions.drag_and_drop_by_offset(fromElement,200,0).perform()   #moving right
            time.sleep(5)
            actions.drag_and_drop_by_offset(fromElement,0,200).perform()   #moving down
            time.sleep(5)
            actions.drag_and_drop_by_offset(fromElement,-200,-200).perform()   #moving  left and up
            time.sleep(5)
            # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag And Drop Element Successful")

        except:
            print("Drag And Drop failed on element")


    def slider(self) :
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 150, 0).perform()
            print("Sliding Element Successful")
            time.sleep(10)
        except:
            print("Sliding failed on element")


jaa = Javascripttry()
# jaa.alert()
# jaa.dragdrop()
jaa.slider()