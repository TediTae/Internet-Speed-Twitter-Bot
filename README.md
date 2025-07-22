# Internet Speed Twitter Bot

This Python bot automatically checks your internet speed using [Speedtest.net](https://www.speedtest.net/) and tweets at your internet service provider (ISP) if the speeds are below your promised thresholds. It's a fun and practical way to let your ISP know you're watching! 😄

---

## 🚀 Features

- Uses Selenium to automate browser actions.
- Measures download and upload speeds.
- Logs into your Twitter account and tweets your speed.
- Customizable promised speed thresholds.

---

## 🛠️ Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver (match your Chrome version)

---

## 📦 Installation
1. Clone the repository
2. Install the required libraries
   - pip install selenium
3. Download ChromeDriver and place it in your PATH.

4. 🧠 Usage
- Update the following constants with your own info inside the Python file:

  - TWITTER_EMAIL = "your@email.com"
  - TWITTER_PASSWORD = "yourPassword"
  - PROMISED_DS = 100  # Promised Download Speed
  - PROMISED_US = 100  # Promised Upload Speed
5. Then run the script

## It will:
1. Open SpeedTest.
2. Run the speed test.
3. If your speed is less than promised, open Twitter and post a tweet.

---

## ⚠️ Disclaimer
- This bot automates login and tweet processes, which might violate Twitter's Terms of Service. Use it responsibly and for educational purposes only.

---

## 📄 License
- This project is licensed under the MIT License.

---


## 📬 Contact
- If you have any questions, suggestions, or just want to say hi, feel free to reach out:
- 📧 tolgayilmaz1377@gmail.com
