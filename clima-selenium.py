from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Luis Mario\Documents\AA Trabajos 7to Parcial 22_2\Prueba Aseg Calidad Soft\ChromeDriver\chromedriver.exe")

driver.get("https://www.clima.com/")
driver.find_element(By.XPATH, '//li[@class="m_list_countrys_mx"]/a').click()

search = driver.find_element(By.ID, "term")
search.send_keys("querétaro")
time.sleep(2)
search.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//ul[@class="m_search_results"]/li[1]/a').click()

driver.find_element(By.XPATH, '//article[@class="m_tables"]/section/ul/li[2]/h2/a').click()