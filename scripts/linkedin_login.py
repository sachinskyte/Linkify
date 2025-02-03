from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging
import pickle
import sys

def login_linkedin(username, password, otp):
    """Handle LinkedIn login with OTP verification"""
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

    try:
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        logging.info("Chrome WebDriver initialized successfully")

        # Navigate to LinkedIn login page
        driver.get('https://www.linkedin.com/login')
        logging.info("Navigating to LinkedIn login page")

        # Enter username
        username_field = wait_and_find_element(driver, By.ID, 'username')
        if username_field:
            username_field.send_keys(username)
            logging.info("Username entered")
        else:
            raise Exception("Could not find username field")

        # Enter password
        password_field = wait_and_find_element(driver, By.ID, 'password')
        if password_field:
            password_field.send_keys(password)
            logging.info("Password entered")
        else:
            raise Exception("Could not find password field")

        # Click Login
        submit_button = wait_and_find_element(driver, By.XPATH, '//button[@type="submit"]')
        if submit_button:
            submit_button.click()
            logging.info("Login button clicked")
        else:
            raise Exception("Could not find submit button")

        # Enter OTP
        otp_field = wait_and_find_element(driver, By.ID, 'input__email_verification_pin')
        if otp_field:
            otp_field.send_keys(otp)
            logging.info("OTP entered")

            # Submit OTP
            verify_button = wait_and_find_element(driver, By.ID, 'email-pin-submit-button')
            if verify_button:
                verify_button.click()
                logging.info("OTP submitted")
            else:
                raise Exception("Could not find OTP submit button")
        else:
            raise Exception("Could not find OTP input field")

        # Wait for login to complete
        time.sleep(5)

        # Save cookies after successful login
        cookies = driver.get_cookies()
        with open('linkedin_cookies.pkl', 'wb') as file:
            pickle.dump(cookies, file)
        logging.info("Cookies saved successfully")

        return True

    except Exception as e:
        logging.error(f"An error occurred during login: {str(e)}")
        return False

    finally:
        try:
            driver.quit()
            logging.info("Browser closed successfully")
        except Exception as e:
            logging.error(f"Error closing browser: {str(e)}")

def wait_and_find_element(driver, by, value, timeout=10):
    """Helper function to wait for and find an element"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        logging.error(f"Timeout waiting for element: {value}")
        return None