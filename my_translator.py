import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  


def getHindiText(english_text=''):
    hindi_text = ''
    with webdriver.Chrome(chrome_options=chrome_options) as driver:
        driver.get('https://www.easyhindityping.com/english-to-hindi-translation')
        driver.find_element_by_id('SourceTextarea').clear()
        driver.find_element_by_id('SourceTextarea').send_keys(english_text)
        driver.find_element_by_id('SubmitTranslation').click()
        #
        time.sleep(10)
        hindi_text = driver.find_element_by_id('TargetTextarea').get_property("value")
        driver.close()
        driver.quit()
    return hindi_text


def googleTranslate(hindi_text = ''):
    english_text = ''
    with webdriver.Chrome(chrome_options=chrome_options) as driver:
        driver.get("https://translate.google.co.in/?sl=auto&tl=en&text="+hindi_text+"&op=translate")
        time.sleep(10)
        english_text = driver.find_element_by_xpath(
            '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]'
            ).text
        driver.close()
        driver.quit()
    return english_text


def hindiToEnglish(english_text=''):
    # english_text = 'Tu aaja bhi insan hai vah bhi kuchh 4 5 10 15 20 ko gadi kar payenge 121 ab 1200 kar payenge to aapko dimag lagana hai aapko kab jana hai to bahut sahi hai mujhe. Aur.'
    hindi_text = getHindiText(english_text)
    english_text = googleTranslate(hindi_text)
    return english_text

