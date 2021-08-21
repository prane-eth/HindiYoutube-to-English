from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
# with webdriver.chrome() as driver:
driver.get('https://www.typingbaba.com/translator/english-to-hindi-translation.php')
driver.find_element_by_id('english_text').clear()
driver.find_element_by_id('english_text').send_keys('Tu aaja bhi insan hai vah bhi kuchh 4 5 10 15 20 ko gadi kar payenge 121 ab 1200 kar payenge to aapko dimag lagana hai aapko kab jana hai to bahut sahi hai mujhe. Aur.')
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/a').click()
driver.find_element_by_id('_trans').click()

hindi_text = driver.find_element_by_id('hindi_text')

driver.close()

