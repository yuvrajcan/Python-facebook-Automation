# Facebook Automation Suite

Automate your Facebook workflow with Python!  
This toolkit enables you to post text, images, and even bulk-share content to multiple Facebook groups — all programmatically.

## 🚀 Features

- **Automated Feed Posting:**  
  Post text and images directly to your Facebook timeline using the Facebook Graph API.

- **Bulk Group Sharing:**  
  Share messages and images to multiple Facebook groups at once via Selenium browser automation.

- **CSV-Driven Posting:**  
  Read post content from CSV files for batch or scheduled posting (great for campaigns and challenges).

- **Commenting, Liking, and Deleting:**  
  Automate engagement actions such as commenting on, liking, or deleting posts.

## 🛠 Tech Stack

- Python 3.x
- Facebook Graph API (`facebook-sdk`)
- Selenium WebDriver
- Pandas

## 📦 Setup

1. **Clone the repository**
2. **Install dependencies**
3. **Configure:**
- Set your Facebook access token in `fb_auto.py`.
- Update ChromeDriver and Chrome path in `sharing_fb_groups.py` as needed.
- Prepare your CSV file (`day.csv`) for batch posting.

4. **Run the scripts**
- For posting to feed:  
  `python fb_auto.py`
- For group sharing:  
  `python sharing_fb_groups.py`
- For CSV-driven posting:  
  `python uploading_on_fb.py`

## ⚠️ Notes

- **Facebook API access**: You need a valid access token with appropriate permissions.
- **Selenium automation**: Requires Chrome browser and ChromeDriver installed.
- **Usage**: Intended for personal or educational use. Respect Facebook's terms of service.

## 📄 License

MIT License

---

*Automate your social presence and save hours every week!*


