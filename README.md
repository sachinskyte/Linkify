# LinkedIn Automation

This repository provides a simple LinkedIn automation script using Selenium WebDriver. The scripts facilitate tasks such as logging into LinkedIn and automatically accepting connection requests.

## Features

- **Login Automation**: Automates LinkedIn login, including handling OTP verification.
- **Connection Management**: Automatically accepts LinkedIn connection requests.
- **Headless Browser Support**: Optimized to run in headless mode for efficient performance.

---

## Setup and Installation

Follow these steps to set up and run the scripts.

### Step 1: Install Required Dependencies

Run the following commands to install necessary Python libraries and Chromium browser:

```bash
!pip install selenium
!pip install webdriver_manager
!apt-get update
!apt install chromium-chromedriver
```

### Step 2: Download and Install Google Chrome

```bash
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
!dpkg -i google-chrome-stable_current_amd64.deb
!apt-get -f install -y
```

### Step 3: Verify Installation

```bash
!google-chrome --version
```

### Step 4: Install WebDriver Manager

```bash
!pip install webdriver-manager
```

---

## Scripts

### 1. LinkedIn Login Script

This script automates the process of logging into LinkedIn, including handling OTP verification. User credentials are provided securely at runtime.

#### Usage

1. Run the script in a Python environment.
2. Follow the prompts to input your LinkedIn email and password.
3. Enter the OTP received in your email when prompted.

#### Key Functionality:
- Waits for and interacts with LinkedIn login elements.
- Saves session cookies for reuse.

### 2. Auto-Accept Connections Script

This script automatically accepts all pending LinkedIn connection requests.

#### Usage

1. Ensure you have successfully logged in using the LinkedIn Login Script.
2. Run the script to accept pending connection requests.

#### Key Functionality:
- Loads previously saved cookies.
- Scrolls through the invitation manager and clicks the **Accept** button on connection requests.
- Logs the number of accepted requests.

---

## File Structure

- `linkedin_login.py`: Script to handle LinkedIn login.
- `auto_accept_connections.py`: Script to automatically accept LinkedIn connections.
- `linkedin_cookies.pkl`: File where session cookies are stored after login.

---

## Notes and Disclaimers

1. **Educational Purposes**: These scripts are intended for educational purposes. Make sure to comply with LinkedIn's [Terms of Service](https://www.linkedin.com/legal/user-agreement).
2. **Headless Mode**: The scripts use headless browser mode for performance. If debugging is needed, remove the `--headless` argument from Chrome options.
3. **Account Safety**: Avoid excessive use to prevent account flagging or restriction.
4. **Dependencies**: Ensure all dependencies are installed before running the scripts.

---

## Support

For issues or questions, please open an issue in this repository or contact the maintainer.

---

Happy Automating! 🚀
