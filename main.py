from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ua = UserAgent()
random_user_agent = ua.random
print(random_user_agent)

driver = webdriver.Chrome()
driver.get(url = "https://www.kiwi.com/en/search/results/yerevan-armenia/riyadh-saudi-arabia/anytime/no-return?stopNumber=1%7Etrue")
try:
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#cookies_accept").click()
    time.sleep(5)
    f = 0
    info = []
    my_list = []
    for i in range(1, 37):
        if i == 4:
            continue
        try:
            driver.find_element(By.CSS_SELECTOR , fr"#react-view > div.flex.min-h-screen.flex-col > div.grow.bg-cloud-light > div > div > div > div > div > div.min-w-0.flex-grow.p-400.de\:p-0.de\:pb-600.de\:ps-600.de\:pt-600 > div > div > div > div > div > div > div:nth-child({i})").click()
            f += 1
            try:
                # Print the page source for debugging
                print(driver.page_source)
                
                # Wait for the price element to be present using a more general XPath
                price_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'AMD')]"))  # Adjust based on the expected text
                )
            
                # Extract the text from the price element
                price_text = price_element.text
                 # Add the price to your list
                print(f"Price found: {price_text}")
                # my_list.append(price_text)
            except Exception as e:
                print(f"Error finding price element: {e}") 
            time.sleep(2)
            try:
                modal_button = driver.find_element(By.CSS_SELECTOR, r"body div:nth-child(69) section div div.px-400.py-300.tb\:pt-300")
            except:
                modal_button = driver.find_element(By.CSS_SELECTOR, ".px-400.py-300.tb\\:pt-300")
            if modal_button:
                modal_button.click()
            time.sleep(3)
#-----------------------------------------------------------------------=
            try:
                flight_info = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='pt-300']"))
                )
                flight_info.click()
                time.sleep(2)
            except Exception as e:
                print(f"Error clicking flight info: {e}")
#------------------------------------------------------------------------
            try:
                country1 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mb-800 div.pt-300 div:nth-child(1) div.items-start div.orbit-text.text-primary-foreground"))
                )
                if country1:
                    my_list.append(country1.text)
            except Exception as e:
                print(f"Error retrieving country1: {e}")

            try:
                airport1 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mb-800 div.pt-300 div:nth-child(1) div.items-start div.orbit-text.text-secondary-foreground"))
                )
                if airport1:
                    my_list.append(airport1.text)
            except Exception as e:
                print(f"Error retrieving airport1: {e}")

            try:
                airline1 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.flex.flex-col.items-center.mb-400 > div:nth-child(1) > div.grow-0.text-wrap.break-all > div"))
                )
                if airline1:
                    my_list.append(airline1.text)
            except Exception as e:
                print(f"Error retrieving airline1: {e}")

            try:
                time1 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mb-800 div.pt-300 div.relative.box-border div.flex.justify-end"))
                )
                if time1:
                    my_list.append(time1.text)
            except Exception as e:
                print(f"Error retrieving time1: {e}")

            try:
                layover = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mb-800 div.pt-300 div.flex.py-0.mb-300 div.items-start div.orbit-text"))
                )
                if layover:
                    my_list.append(layover.text)
            except Exception as e:
                print(f"Error retrieving layover: {e}")

            try:
                layover_airport = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mb-800 div.pt-300 div.py-0.mb-300 div.items-start div.orbit-text.text-secondary-foreground"))
                )
                if layover_airport:
                    my_list.append(layover_airport.text)
            except Exception as e:
                print(f"Error retrieving layover_airport: {e}")

            try:
                wait_layover = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'orbit-itinerary-badge-list')]//li[1]//span//time"))
                )
                if wait_layover:
                    my_list.append(wait_layover.text)
            except Exception as e:
                print(f"Error retrieving wait_layover: {e}")

            try:
                duration = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'safe-space-x-300')]//time"))
                )
                if duration:
                    my_list.append(duration.text)
                time.sleep(2)
            except Exception as e:
                print(f"Error retrieving duration: {e}")
#-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mb-800 > div > div:nth-child(4) > div > div"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", element)

                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mb-800 > div > div:nth-child(4) > div > div"))
                )
                element.click()
                time.sleep(2)  # Wait for the action to complete

            except Exception as e:
                print(f"Error while scrolling or clicking: {e}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

            try:
                airline2 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='flex flex-col items-center mb-400']//div[contains(@class, 'grow-0 text-wrap break-all')]"))
                )
                my_list.append(airline2.text if airline2 else 'N/A')
            except Exception as e:
                print(f"Error retrieving airline2: {e}")

            try:
                time2 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'relative box-border w-full')]//div[contains(@class, 'flex justify-end')]//div"))
                )
                my_list.append(time2.text if time2 else 'N/A')
            except Exception as e:
                print(f"Error retrieving time2: {e}")

            try:
                time2 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'relative box-border w-full')]//div[contains(@class, 'flex justify-end')]//div"))
                )
                if time2:
                    my_list.append(time2.text)
            except Exception as e:
                print(f"Error retrieving time2: {e}")

            try:
                city2 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'orbit-text') and contains(text(), 'Riyadh')]"))
                )
                if city2:
                    my_list.append(city2.text)
                    print(f"City found: {city2}")
            except Exception as e:
                print(f"City not found: {e}")

            try:
                airport2 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'orbit-text') and contains(text(), 'King Khalid International')]"))
                )
                if airport2:
                    my_list.append(airport2.text)
                    print(f"Airport found: {airport2}")
            except Exception as e:
                print(f"Airport not found: {e}")
        except Exception as ex:
            print(f"FIRST LOCAL ERROR ***********************************{ex}***********************************")
        time.sleep(1)
        driver.back()
        time.sleep(1)
        if i == 11:
            driver.find_element(By.CSS_SELECTOR , r"#react-view > div.flex.min-h-screen.flex-col > div.grow.bg-cloud-light > div > div > div > div > div > div.min-w-0.flex-grow.p-400.de\:p-0.de\:pb-600.de\:ps-600.de\:pt-600 > div > div > div > div > div > button").click()
            for _ in range(2):
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                time.sleep(5)
            time.sleep(10)
        if i % 10 == 1 and i != 1:
            driver.find_element(By.CSS_SELECTOR , r"#react-view > div.flex.min-h-screen.flex-col > div.grow.bg-cloud-light > div > div > div > div > div > div.min-w-0.flex-grow.p-400.de\:p-0.de\:pb-600.de\:ps-600.de\:pt-600 > div > div > div > div > div > button").click()
            time.sleep(10)
        time.sleep(1)
        my_list.append(duration)
        my_list.append(price_text)
        if len(my_list) == 13:
            info.append(my_list)

except Exception as exx:
    print(f"GLOBAL ERROR*****************************************{exx}*****************************************")
finally:
    driver.close()
    driver.quit()