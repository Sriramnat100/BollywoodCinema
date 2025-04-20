from selenium import webdriver
from selenium.webdriver.common.by import By
import time




def scrape_website(link):
    driver = webdriver.Chrome()
    driver.get(link)

    driver.implicitly_wait(3)
    time.sleep(4)

    button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div[3]/button')
    button.click()

    search = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div[2]/div/form/div/input')
    search.send_keys("year:193")

    submit_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div[2]/div/form/button[2]')
    submit_btn.click()
    time.sleep(3)
    driver.quit()



scrape_website("https://new.giitaayan.com/")