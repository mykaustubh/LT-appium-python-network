from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
import http.client
import json

desired_caps = {
    "deviceName": "iPhone 12",
    "platformName": "ios",
    "platformVersion": "14",
    "isRealMobile": True,
    "app": "lt://proverbial-ios",  # Enter app_url here
    "build": "Python Vanilla iOS",
    "name": "Sample Test - Python",
    # "fixedIP": "Sample Test - Python",
    # "network": True,
    # "visual": True,
    # "video": True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    gridURL = "@mobile-hub.lambdatest.com/wd/hub"
    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+gridURL)
        time.sleep(3)

        url = "https://mobile-api.lambdatest.com/mobile-automation/api/v1/sessions/" + \
            driver.session_id + "/update_network"
        payload = json.dumps({
            "mode": "offline"
        })
        headers = {
            'Authorization': 'Basic a2F1c3R1YmhkOm5xZHVIMXBQRExydEZpV1pyZDBMQkx6cmt0WVpobWJGRElUZWowTkZ4ZmttTWRpM2lN',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        gridURL = "https://mobile-api.lambdatest.com/mobile-automation/api/v1/sessions/" + \
            driver.session_id+"/update_network"
        time.sleep(30)
        print(url)
        print(payload)

        colorElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "color")))
        colorElement.click()
        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text")))
        textElement.click()
        toastElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "toast")))
        toastElement.click()
        notification = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "notification")))
        notification.click()
        time.sleep(3)
        geolocation = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "geoLocation")))
        geolocation.click()
        time.sleep(5)
        driver.back()
        home = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Home")))
        home.click()
        time.sleep(10)

        #Python - http.client
        # conn = http.client.HTTPSConnection("mobile-api.lambdatest.com")
        # payload = json.dumps({
        #     "mode": "offline"
        # })
        # headers = {
        #     'Authorization': 'Basic a2F1c3R1YmhkOm5xZHVIMXBQRExydEZpV1pyZDBMQkx6cmt0WVpobWJGRElUZWowTkZ4ZmttTWRpM2lN',
        #     'Content-Type': 'application/json'
        # }
        # url = "https://mobile-api.lambdatest.com/mobile-automation/api/v1/sessions/" + \
        #     driver.session_id + "/update_network"
        # conn.request("POST", url, payload, headers)
        # res = conn.getresponse()
        # data = res.read()
        # print(data.decode("utf-8"))
        # print(payload)
        # print(url)
        # time.sleep(30)

        # url = "https://mobile-api.lambdatest.com/mobile-automation/api/v1/sessions/" + \
        #     a+"/update_network"
        # payload = json.dumps({
        #     "mode": "online"
        # })
        # headers = {
        #     'Authorization': 'Basic a2F1c3R1YmhkOm5xZHVIMXBQRExydEZpV1pyZDBMQkx6cmt0WVpobWJGRElUZWowTkZ4ZmttTWRpM2lN',
        #     'Content-Type': 'application/json'
        # }
        # response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        # print("Kaustubh Online")
        # print(driver.session_id)

        speedTest = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "speedTest")))
        speedTest.click()
        time.sleep(5)
        driver.back()
        browser = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Browser")))
        browser.click()
        url = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "url")))
        url.send_keys("https://www.lambdatest.com")
        find = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "find")))
        find.click()
        driver.quit()
    except:
        driver.quit()


startingTest()
