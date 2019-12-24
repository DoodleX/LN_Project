from selenium import webdriver as wd

driver = wd.Firefox()

driver.get('https://www.imdb.com/?ref_=nv_home')

driver.find_element_by_xpath('/html/body/div[2]/nav/div[2]/label[2]/div').click()

driver.find_element_by_xpath('/html/body/div[2]/nav/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[4]').click()

driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[6]/td[2]/a').click()


from selenium.webdriver.common.by import By

all_elements = driver.find_elements(By.TAG_NAME, 'tr')
element6 = all_elements[6].text
name = element6.split('\n')[0]
print(name)