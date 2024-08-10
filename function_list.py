from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def start(is_headless):
    global driver
    if is_headless:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        driver.get_screenshot_as_file("screenshot.png")  # getting screenshot

    else:
        driver = webdriver.Chrome()
        driver.get('https://web.whatsapp.com/')
    input("Press Enter after scanning QR code")
    # Uncomment that if you want to use headless mode cuz you cant see the UI while that mean you cant scan QR code either


def send_keys(keys):
    try:
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(keys)
        ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
    except:
        pass


def unread():
    UnSeen = driver.find_element(By.XPATH, '//*[@id="side"]/div[2]/button[2]')
    UnSeen.click()
    # click the Unread menu


def group():
    group = driver.find_element(By.XPATH, '//*[@id="side"]/div[2]/button[3]')
    group.click()
    # click group menu


def click_2nd_row():
    try:
        second_row = driver.find_element(By.CSS_SELECTOR, "div[style*='transform: translateY(72px);']")
        second_row.click()
    except:
        pass


def lastchat():
    try:
        last_msg = driver.find_element(By.CSS_SELECTOR, "div[style*='transform: translateY(0px);']")
        last_msg.click()
        # click most top message

        try:
            find_last_chat = driver.find_element(By.XPATH,
                                                 '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div[1]/span/span[2]')
            find_last_sender = driver.find_element(By.XPATH,
                                                   '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div[1]/span/div/span')

            last_chat = find_last_chat.text
            sender = find_last_sender.text
            print("last chat: ", last_chat, "\nsender: ", sender)
            return [last_chat, sender]
            # im sure everyone know what this gonna do
        except:
            try:
                find_last_chat = driver.find_element(By.XPATH,
                                                     '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/span/span')
                find_last_sender = driver.find_element(By.XPATH,
                                                       '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/span')
                last_chat = find_last_chat.text
                sender = find_last_sender.text
                print("Sender: ", last_chat,"\nChat: ", sender)
                return [last_chat, sender]
            except:
                print("Someone is typing...")
                # you cant get last_chat while someone is typing,sadly... i didnt know how to fix this
    except:
        pass


def send(msg):
    try:
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(msg)
        message_box.send_keys(Keys.ENTER)
        # fast way to send message
    except:
        pass


def enter():
    try:
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(Keys.ENTER)
    except:
        pass


def shift_enter():
    try:
        ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
    except:
        pass
    # you cant just use /n function, so i make this instead and using it every new line is needed


def click_first_row():
    try:
        first_row = driver.find_element(By.CSS_SELECTOR, "div[style*='transform: translateY(0px);']")
        first_row.click()
    except:
        pass


def search_contact(name):
    try:
        search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div')
        search_box.click()
        search_box.send_keys(name)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)
        time.sleep(0.5)
    except:
        print("Error while searching...")


webdriver.Chrome().close()
