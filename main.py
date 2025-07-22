from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_EMAIL = "YOUR EMAIL ADDRESS"
TWITTER_PASSWORD = "YOUR PASSWORD"
PROVIDER_HANDLE = "@YourISP"
PROMISED_DS = 100
PROMISED_US = 100

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/"
                                                            "div[2]/div[2]/div/div[2]/a/span[4]")
        go_button.click()
        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/"
                                                        "div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/"
                                                        "div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/"
                                                         "div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/"
                                                         "div[2]/span").text
        print(self.down)
        print(self.up)


    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        time.sleep(10)
        sign_in_button = self.driver.find_element(By.XPATH, "//a[@data-testid='loginButton' and contains(., 'Sign in')]")
        sign_in_button.click()
        time.sleep(10)

        email_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        time.sleep(2)
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
        time.sleep(2)
        next_button.click()
        time.sleep(10)
        password_input = self.driver.find_element(By.XPATH, "//input[@name='password' and @type='password']")
        time.sleep(2)
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        log_in_button = self.driver.find_element(By.XPATH,"//button[@role='button' and @data-testid='LoginForm_Login_Button'"
                                                          " and @type='button' and contains(., 'Log in')]")
        time.sleep(2)
        log_in_button.click()
        time.sleep(10)
        send_tweet = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0' and @role='textbox']")
        send_tweet.send_keys(f"Dear {PROVIDER_HANDLE}, I have {self.down}mbps download and {self.up}mbps upload currently while i promised {PROMISED_DS}download and"
                             f"{PROMISED_US}upload. Please help me to fix it.")
        time.sleep(2)
        send_tweet_button = self.driver.find_element(By.XPATH, "//button[@role='button' and @data-testid='tweetButtonInline']")
        send_tweet_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if float(bot.down) < float(PROMISED_DS) or float(bot.up) < float(PROMISED_US):
    bot.tweet_at_provider()
