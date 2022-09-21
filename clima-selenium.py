from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
													#luism - Luis Mario
driver = webdriver.Chrome(executable_path=r"C:\Users\luism\OneDrive\Documentos\AA Trabajos 7to Parcial 22_2\Prueba Aseg Calidad Soft\ChromeDriver\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.clima.com/")
driver.find_element(By.XPATH, '//li[@class="m_list_countrys_mx"]/a').click()

search = driver.find_element(By.ID, "term")
search.send_keys("querétaro")
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.XPATH, '//ul[@class="m_search_results"]/li[1]/a').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/section/ul/li[2]/h2/a').click()
time.sleep(5)

txt_colums = driver.find_element(By.XPATH, '//*[@id="cityTable"]/div[1]/ul')
txt_colums = txt_colums.text
#print(txt_colums)

todays_weather = txt_colums.split('Hoy')[0].split('\n')[1:-1]
#print(todays_weather)

horas = list()
temp = list()
v_viento = list()

for i in range(0, len(todays_weather),3):
	horas.append(todays_weather[i])
	temp.append(todays_weather[i+1])
	v_viento.append(todays_weather[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Viento(km/h)': v_viento})
print(df)

df.to_csv('tiempo_hoy.cvs', index=False)
driver.quit()
