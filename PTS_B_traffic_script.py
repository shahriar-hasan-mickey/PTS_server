#!/usr/bin/python3
from selenium import webdriver
import time
#from PIL import Image
#import numpy
#import os
import threading

def repeater(url):
    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    driver.get(url)
    print("here\n")
    time.sleep(10)
    traffic_level = driver.find_element("xpath", "/html/body/div[3]/div[9]/div[3]/div[3]/div/div/div/div/div[2]/button/div[2]/div[1]")
    traffic_motion_state = driver.find_element("xpath", "/html/body/div[3]/div[9]/div[3]/div[3]/div/div/div/div/div[2]/button/div[2]/div[2]")
    temperature = driver.find_element("xpath", "/html/body/div[3]/div[9]/div[3]/div[3]/div/div/div/div/div[1]/div[2]/div")
    print(traffic_level.get_property("innerHTML"))
    print(traffic_motion_state.get_property("innerHTML"))
    print(temperature.get_property("innerHTML"))
    driver.close()


map1 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808312,90.4005565,21z/data=!5m1!1e1"])
map2 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808533,90.3999832,21z/data=!5m1!1e1"])
map3 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808172,90.3993145,21z/data=!5m1!1e1"])
map4 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7808172,90.3993145,21z/data=!5m1!1e1"])
map5 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7807955,90.4006015,21z/data=!5m1!1e1"])
map6 = threading.Thread(target=repeater, args=["https://www.google.com/maps/@23.7807832,90.4013022,21z/data=!5m1!1e1"])

map1.start()
map2.start()
map3.start()
map4.start()
map5.start()
map6.start()


#time.sleep(2)
#image = Image.open('map1.png')

#width, height = image.size

#image = numpy.array(image, dtype=numpy.uint8)
#print(image.shape)
#image[]
#print(width, height)
#os.system("gopen map.png")
