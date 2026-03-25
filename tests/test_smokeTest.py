from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

class TestSmoke:

    def setup_method(self, method):
        opts = Options()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_home_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/teton/1.6/index.html")

        assert "Teton Idaho CoC" in driver.title

    def test_directory_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/teton/1.6/index.html")

        driver.find_element(By.LINK_TEXT, "Directory").click()
        driver.find_element(By.ID, "directory-grid").click()

        text = driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text
        assert "Teton Turf and Tree" in text

    def test_join_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/teton/1.6/index.html")

        driver.find_element(By.LINK_TEXT, "Join").click()

        fname = driver.find_element(By.NAME, "fname")
        fname.send_keys("Angelique")

        lname = driver.find_element(By.NAME, "lname")
        lname.send_keys("Legaspi")

    def test_admin_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/teton/1.6/index.html")

        driver.find_element(By.LINK_TEXT, "Admin").click()

        username = driver.find_element(By.ID, "username")
        username.send_keys("Angelique")

        password = driver.find_element(By.ID, "password")
        password.send_keys("Legaspi")

        driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()

        error = driver.find_element(By.CSS_SELECTOR, ".errorMessage").text
        assert "Invalid username and password" in error