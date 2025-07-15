# LinkedIn Auto-Connection

Automate LinkedIn tasks efficiently using Selenium WebDriver and Flask. This project provides a web interface for secure login (with OTP support) and automatic acceptance of LinkedIn connection requests.

---

## Features

- **Automated Login**: Handles LinkedIn login, including OTP verification.
- **Connection Management**: Accepts all pending connection requests automatically.
- **Headless Browser Support**: Runs in headless mode for speed and CI/CD compatibility.
- **Session Persistence**: Saves and reuses session cookies to minimize repeated logins.
- **Web Interface**: Manage automation from your browser.

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/sachinskyte/LinkedIn-Auto-Connection.git
cd LinkedIn-Auto-Connection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

### 4. Open in Browser
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the web interface.

---

## File Structure

```
LinkedIn-Auto-Connection/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── scripts/
│   ├── linkedin_login.py   # Script for LinkedIn login
│   └── accept_connections.py # Script to accept connections
├── cookies/
│   └── linkedin_cookies.pkl # Session cookies
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
└── README.md               # Project documentation
```

---

## Best Practices & Safety

- **Educational Use Only**: Use responsibly and comply with [LinkedIn's Terms of Service](https://www.linkedin.com/legal/user-agreement).
- **Headless Mode**: For debugging, remove the `--headless` option in the Chrome setup.
- **Account Safety**: Avoid excessive automation to prevent account restrictions.
- **Dependencies**: Keep all dependencies up to date.

---

## Support

For questions or issues, open an issue on GitHub or contact the maintainer.


