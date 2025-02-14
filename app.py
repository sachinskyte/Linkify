from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import time
import logging
import pickle
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a secure secret key

def init_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    return webdriver.Chrome(options=chrome_options)

def wait_and_find_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        logger.error(f"Timeout waiting for element: {value}")
        return None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/connections')
def connections():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('connections.html')

@app.route('/process-connections', methods=['POST'])
def process_connections():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Session expired. Please login again.'})
    
    try:
        driver = init_driver()
        cookie_path = os.path.join('cookies', f"linkedin_cookies_{session['username']}.pkl")
        
        if not os.path.exists(cookie_path):
            return jsonify({'success': False, 'message': 'No valid session found. Please login again.'})
        
        # Load cookies and process connections
        connections_accepted = accept_connections(driver, cookie_path)
        
        return jsonify({
            'success': True,
            'message': f'Successfully processed {connections_accepted} connection requests!'
        })
    except Exception as e:
        logger.error(f"Error processing connections: {str(e)}")
        return jsonify({'success': False, 'message': f'Error processing connections: {str(e)}'})
    finally:
        if 'driver' in locals():
            driver.quit()

def accept_connections(driver, cookie_path):
    """Handle accepting connection requests"""
    connections_accepted = 0
    try:
        # Load cookies
        driver.get('https://www.linkedin.com')
        with open(cookie_path, 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        
        # Navigate to Connection Requests Page
        driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')
        time.sleep(5)

        max_scrolls = 5
        scroll_count = 0

        while scroll_count < max_scrolls:
            connections_in_current_scroll = 0

            # Find accept buttons
            accept_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label*='Accept']")
            if not accept_buttons:
                accept_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'artdeco-button--secondary')]")
            if not accept_buttons:
                accept_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Accept')]")

            if not accept_buttons:
                break

            # Process each button
            for button in accept_buttons:
                try:
                    if not button.is_displayed():
                        continue

                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                    time.sleep(1)

                    initial_button_count = len(driver.find_elements(By.CSS_SELECTOR, "button[aria-label*='Accept']"))
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(1)

                    new_button_count = len(driver.find_elements(By.CSS_SELECTOR, "button[aria-label*='Accept']"))
                    if new_button_count < initial_button_count:
                        connections_accepted += 1
                        connections_in_current_scroll += 1

                    time.sleep(2)
                except Exception as e:
                    logger.error(f"Failed to process button: {str(e)}")
                    continue

            if connections_in_current_scroll == 0:
                break

            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(3)
            scroll_count += 1

        return connections_accepted

    except Exception as e:
        logger.error(f"Error in accept_connections: {str(e)}")
        raise

@app.route('/submit-password', methods=['POST'])
def submit_password():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required'})
    
    driver = init_driver()
    try:
        driver.get('https://www.linkedin.com/login')
        
        username_field = wait_and_find_element(driver, By.ID, 'username')
        if not username_field:
            return jsonify({'success': False, 'message': 'Could not find username field'})
        username_field.send_keys(username)

        password_field = wait_and_find_element(driver, By.ID, 'password')
        if not password_field:
            return jsonify({'success': False, 'message': 'Could not find password field'})
        password_field.send_keys(password)

        sign_in_button = wait_and_find_element(driver, By.CSS_SELECTOR, 'button[type="submit"]')
        if not sign_in_button:
            return jsonify({'success': False, 'message': 'Could not find sign in button'})
        sign_in_button.click()

        time.sleep(3)
        
        session['username'] = username
        session['password'] = password
        session['cookies'] = driver.get_cookies()
        
        otp_field = wait_and_find_element(driver, By.CSS_SELECTOR, 'input[name="pin"]')
        if otp_field:
            return jsonify({'success': True, 'redirect': '/otp'})

        # If no OTP field, save cookies and proceed
        cookie_dir = 'cookies'
        if not os.path.exists(cookie_dir):
            os.makedirs(cookie_dir)
        
        cookie_path = os.path.join(cookie_dir, f"linkedin_cookies_{username}.pkl")
        with open(cookie_path, 'wb') as file:
            pickle.dump(driver.get_cookies(), file)
        
        return jsonify({'success': True, 'redirect': '/connections'})

    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({'success': False, 'message': f'Login error: {str(e)}'})
    finally:
        driver.quit()

@app.route('/otp')
def otp_page():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('otp.html')

@app.route('/submit-otp', methods=['POST'])
def submit_otp():
    if 'username' not in session or 'password' not in session:
        return jsonify({'success': False, 'message': 'Session expired. Please login again.'})

    otp = request.form.get('otp')
    skip_otp = request.form.get('skip_otp')

    if not otp and not skip_otp:
        return jsonify({'success': False, 'message': 'OTP is required'})

    driver = init_driver()
    try:
        driver.get('https://www.linkedin.com/login')
        
        for cookie in session.get('cookies', []):
            driver.add_cookie(cookie)
        
        driver.get('https://www.linkedin.com')

        if not skip_otp:
            otp_field = wait_and_find_element(driver, By.CSS_SELECTOR, 'input[name="pin"]')
            if otp_field:
                otp_field.send_keys(otp)
                verify_button = wait_and_find_element(driver, By.CSS_SELECTOR, 'button[type="submit"]')
                if verify_button:
                    verify_button.click()
                    time.sleep(3)

        cookies = driver.get_cookies()
        cookie_dir = 'cookies'
        if not os.path.exists(cookie_dir):
            os.makedirs(cookie_dir)
            
        cookie_path = os.path.join(cookie_dir, f"linkedin_cookies_{session['username']}.pkl")
        with open(cookie_path, 'wb') as file:
            pickle.dump(cookies, file)
        
        return jsonify({'success': True, 'redirect': '/connections'})

    except Exception as e:
        logger.error(f"OTP verification error: {str(e)}")
        return jsonify({'success': False, 'message': f'OTP verification error: {str(e)}'})
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=False)