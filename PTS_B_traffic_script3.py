#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import threading
import time

traffic_level_element = "/html/body/div[3]/div[9]/div[3]/div[3]/div/div/div/div/div[2]/button/div[2]/div[1]"
traffic_motion_state_element = "/html/body/div[3]/div[9]/div[3]/div[3]/div/div/div/div/div[2]/button/div[2]/div[2]"
temperature_element = "/html/body/div[3]/div[9]/div[3]/div[3]/div/div/div/div/div[1]/div[2]/div"

data = []


def wait_function(driver, xpath):
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    
file = open("/home/slave/cse470/cse489/project/mapInfo.txt", "w")

def repeater(url):
    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    driver.get(url)
    driver.maximize_window()

    wait_function(driver, traffic_level_element)
    traffic_level = driver.find_element("xpath", traffic_level_element)

    wait_function(driver, traffic_motion_state_element)
    traffic_motion_state = driver.find_element("xpath", traffic_motion_state_element)

    wait_function(driver, temperature_element)
    temperature = driver.find_element("xpath", temperature_element)

#    data.append((traffic_level.get_property("innerHTML"), traffic_motion_state.get_property("innerHTML"), temperature.get_property("innerHTML")))
 #   print(data)
    file.write(traffic_level.get_property("innerHTML") + "," + traffic_motion_state.get_property("innerHTML") + "," + temperature.get_property("innerHTML") + "\n")
    driver.close()


#map1 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808312,90.4005565,21z/data=!5m1!1e1"])
#map2 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808533,90.3999832,21z/data=!5m1!1e1"])
#map3 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808172,90.3993145,21z/data=!5m1!1e1"])
#map4 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808172,90.3993145,21z/data=!5m1!1e1"])
#map5 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7807955,90.4006015,21z/data=!5m1!1e1"])
#map6 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7807832,90.4013022,21z/data=!5m1!1e1"])


while(True):
    map1 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808312,90.4005565,21z/data=!5m1!1e1"])
    map2 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808533,90.3999832,21z/data=!5m1!1e1"])
    map3 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808172,90.3993145,21z/data=!5m1!1e1"])

    map1.start()
    map2.start()
    map3.start()
    time.sleep(25)
#map4.start()
#map5.start()
#map6.start()

file.close()
#print(data)
print("TERMINATING SCRIPT")
