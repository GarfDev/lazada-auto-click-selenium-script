import time
import datetime
import random
import warnings
import threading
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def drag_slider(driver):
    slider = driver.find_element_by_id('nc_2_n1z')
    slider.click()
    ac = ActionChains(driver)
    ac.move_to_element(slider)
    ac.click_and_hold(slider)
    xoffset = 0
    while xoffset < 350:
        xmove = random.randint(10, 40)
        ymove = random.randint(-1, 1)
        ac.move_by_offset(xmove, ymove)
        xoffset += xmove
    ac.release()
    ac.perform()

    time.sleep(3)

    element = driver.find_element_by_class_name('nc-lang-cnt')
    print(element.text)


def runner(chrome_driver, index):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.headless = True
    # options.add_argument(f'user-agent={generate_user_agent()}')

    warnings.filterwarnings('ignore')
    driver = webdriver.Chrome(chrome_driver, chrome_options=options)

    driver.set_window_size(1366, 768)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })

    for x in range(1000):
        print(f"[{datetime.datetime.now()}] Go to product page..")
        driver.get("https://www.lazada.vn/products/deal-huy-diet-tai-nghe-bluetooth-nhi-s530-am-thanh-to-ro-chat-am-chuan-chong-on-xuyen-am-pin-trau-dam-thoai-suot-4-tieng-tai-nghe-bluetooth-mau-moi-chat-luong-tai-nghe-nhet-tai-tai-nghe-gia-re-i673262058-s1638182628.html")
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "container")))

        if "captcha" in driver.title:
            print(f"[Thread-{index}] Resolving captcha..")
            drag_slider(driver)

        try:
            time.sleep(random.randint(4, 6))
            element = driver.find_element_by_class_name(
                'add-to-cart-buy-now-btn')
            time.sleep(random.randint(10, 20))
            print(f"[Thread-{index}] Back to main page..")
            driver.get(
                "https://www.lazada.vn/products/chinh-hang-lan-khu-mui-scion-giai-phap-dut-hoi-nach-hoi-chan-tan-goc-i675798593-s1646658028.html?search=store&mp=3")
            time.sleep(random.randint(10, 20))
        except:
            print(
                f"[{datetime.datetime.now()}] Failed to load product page, sleep for 300 sec..")
            driver.save_screenshot(
                f"./screenshots/{datetime.datetime.now()}.png")
            time.sleep(300)

    driver.quit()


if __name__ == "__main__":
    threads = []

    chrome_driver = ChromeDriverManager().install()

    for index in range(50):
        x = threading.Thread(target=runner, args=(chrome_driver, index))
        threads.append(x)
        time.sleep(random.randint(1, 3))
        x.start()
