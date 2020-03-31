import unittest
from time import sleep
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from faker import Faker
from faker_e164.providers import E164Provider


class ForFriends(unittest.TestCase):

    def setUp(self):
        #chrome_options = Options()
        #chrome_options.add_argument('--window-size=1360,768')
        #self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
        firefox_options = Options()
        firefox_options.add_argument('--window-size=1360,768')
        #firefox_options.headless = True
        #print("Headless Firefox Initialized")
        self.driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver', firefox_options=firefox_options)
        driver = self.driver
        driver.get("http://4friends.space/en")

    def test_admin_registration_first_step(self):
        f = Faker()
        f.add_provider(E164Provider)
        driver = self.driver
        self.assertIn("4Friends", driver.title)
        driver.find_element(By.XPATH, '//a[contains(text(),"Register Now")]').click()
        self.assertIn("Who are you?", driver.title)
        driver.find_element(By.XPATH, '//a[contains(text(),"Start Fundraising")]').click()
        self.assertIn("Register as Admin", driver.title)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/div/div[3]/button[2]').click()
        self.assertIn("Register as Admin", driver.title)
        # TO DO: ADD RANDOM ADMIN COUNTRY
        admin_organization = driver.find_element(By.ID, 'organizationInput')
        admin_organization.click()
        admin_organization.send_keys(f.company())
        admin_name = driver.find_element(By.ID, 'firstNameInput')
        admin_name.click()
        admin_name.send_keys(f.first_name())
        admin_lname = driver.find_element(By.ID, 'lastNameInput')
        admin_lname.click()
        admin_lname.send_keys(f.last_name())
        admin_phone = driver.find_element(By.ID, 'phoneInput')
        admin_phone.click()
        admin_phone.send_keys(f.safe_e164(region_code="US"))
        admin_email = driver.find_element(By.ID, 'emailInput')
        admin_email.click()
        admin_email.send_keys(f.email())
        admin_password = driver.find_element(By.ID, 'passwordInput')
        admin_password.click()
        admin_password.send_keys('Qwerty12345')
        admin_agreement = driver.find_element(By.ID, 'agreementCheckbox')
        admin_agreement.click()
        admin_continue_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div[2]/button[2]').click()

   # def tearDown(self):
      #  self.driver.close()


if __name__ == "__main__":
    unittest.main()