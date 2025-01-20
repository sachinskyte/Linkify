# LinkedIn Automation

This repository provides a professional and efficient way to automate LinkedIn tasks using Selenium WebDriver. The scripts handle tasks such as logging into LinkedIn, including OTP verification, and automatically accepting connection requests.

## How the Code Works

### Core Logic

1. **Login Automation**:
   - The `linkedin_login.py` script initiates a Chrome browser instance using Selenium.
   - It navigates to LinkedIn's login page and securely prompts for user credentials (email and password) via the console.
   - Once credentials are submitted, the script waits for OTP verification, which the user must input manually when prompted.
   - After successful login, session cookies are saved in a `linkedin_cookies.pkl` file for reuse in future sessions, reducing the need for repeated logins.

2. **Connection Management**:
   - The `auto_accept_connections.py` script reuses the session cookies saved during the login process.
   - It navigates to LinkedIn's "Invitation Manager" page and scans for pending connection requests.
   - Using Selenium, it identifies and clicks "Accept" buttons for each pending request, scrolling through the page as necessary to load more connections.
   - The script logs each accepted connection and stops when all visible requests have been processed.

3. **Optimizations**:
   - Headless Chrome is used by default for performance and to allow running the scripts on servers or CI/CD pipelines.
   - WebDriver Manager simplifies the handling of browser drivers.
   - Error handling is built in to manage unexpected issues, such as network delays or changes in LinkedIn's interface.

---

## Google Colab Integration

For a much better viewing and execution experience, you can use the provided Google Colab notebook:

[Run on Google Colab](https://colab.research.google.com/drive/19ZeOdAtX_dOJ3AXxbZ64NXwYnw1JpDbk?usp=sharing)

This Colab notebook comes pre-configured to install dependencies and execute the automation scripts with minimal setup. Simply open the link and follow the instructions in the notebook.

---

## Features

- **Login Automation**: Automates LinkedIn login, including handling OTP verification.
- **Connection Management**: Automatically accepts LinkedIn connection requests.
- **Headless Browser Support**: Optimized to run in headless mode for performance and scalability.
- **Reusable Sessions**: Saves session cookies for subsequent runs to reduce login friction.

---

## Setup and Installation

### Prerequisites

- **Python**: Ensure you have Python 3.8 or higher installed.
- **Google Chrome**: Install the latest version of Google Chrome.

### Step 1: Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/sachinskyte/LinkedIn-Auto-Connection.git
cd LinkedIn-Auto-Connection
```

### Step 2: Install Dependencies

Run the following commands to install the necessary libraries and set up your environment:

```bash
pip install selenium
pip install webdriver_manager
apt-get update
apt install chromium-chromedriver
```

### Step 3: Install Google Chrome

Download and install Google Chrome:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt-get -f install -y
```

### Step 4: Verify Chrome Installation

Ensure Google Chrome is correctly installed by checking its version:

```bash
google-chrome --version
```

### Step 5: Install WebDriver Manager

Install the WebDriver Manager for easier driver management:

```bash
pip install webdriver-manager
```

---

## Using the Scripts

### 1. LinkedIn Login Script

The login script automates the process of logging into LinkedIn, including handling OTP verification. It securely prompts for user credentials at runtime.

#### How to Run

```bash
python linkedin_login.py
```

1. Run the script in a Python environment.
2. Follow the on-screen prompts to input your LinkedIn email and password.
3. Enter the OTP received via email when prompted.
4. After successful login, session cookies are saved for reuse.

### 2. Auto-Accept Connections Script

The connection management script automatically accepts all pending LinkedIn connection requests.

#### How to Run

```bash
python auto_accept_connections.py
```

1. Ensure the `linkedin_cookies.pkl` file (generated after login) is available.
2. Run the script to process and accept pending connection requests.
3. The script logs details of accepted connections.


---

## File Structure

- `linkedin_login.py`: Script to handle LinkedIn login.
- `auto_accept_connections.py`: Script to automatically accept LinkedIn connections.
- `linkedin_cookies.pkl`: File where session cookies are stored after login.
- `README.md`: Documentation for the repository.

---

## Notes and Disclaimers

1. **Educational Purposes**: These scripts are intended for educational purposes only. Make sure to comply with LinkedIn's [Terms of Service](https://www.linkedin.com/legal/user-agreement).
2. **Headless Mode**: By default, the scripts use headless browser mode for improved performance. For debugging, remove the `--headless` argument from the Chrome options.
3. **Account Safety**: Avoid excessive use to prevent account flagging or restrictions.
4. **Dependencies**: Ensure all dependencies are installed and up to date before running the scripts.

---

## Support

For issues or questions, feel free to open an issue in this repository or contact the maintainer via GitHub.

---


