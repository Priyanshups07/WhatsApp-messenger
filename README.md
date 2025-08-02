# 📱 WhatsApp Messenger - Scheduled Message Sender

> **Automate your WhatsApp messaging with Python and Twilio**

A powerful Python application that enables you to schedule and send WhatsApp messages automatically using Twilio's WhatsApp API. Perfect for birthday wishes, reminders, notifications, and automated messaging workflows.

## ✨ Features

- **🕐 Scheduled Messaging**: Set messages to be sent at specific dates and times
- **📞 Multi-Platform**: Send to any WhatsApp number with country code support
- **🛡️ Secure**: Environment variable support for API credentials
- **📝 User-Friendly**: Simple command-line interface with clear prompts
- **⚡ Real-time**: Immediate message delivery through Twilio's API
- **🔧 Easy Setup**: Minimal configuration required

## 🚀 Use Cases

- **🎂 Birthday Wishes**: Schedule birthday messages in advance
- **⏰ Reminders**: Set up appointment or meeting reminders
- **📢 Notifications**: Automated notifications for events
- **💼 Business**: Customer service and marketing messages
- **👥 Personal**: Stay in touch with friends and family

## 📋 Prerequisites

- **🐍 Python 3.6+** - Modern Python with async support
- **📱 Twilio Account** - WhatsApp API access required
- **🔑 API Credentials** - Account SID and Auth Token

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Priyanshups07/WhatsApp-messenger.git
cd WhatsApp-messenger
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚙️ Setup

1. **Create Twilio Account**: Sign up at [https://www.twilio.com](https://www.twilio.com)
2. **Get API Credentials**: Find your Account SID and Auth Token in the Twilio Console
3. **Configure Environment Variables** (Recommended):
   ```bash
   export TWILIO_ACCOUNT_SID='your_account_sid'
   export TWILIO_AUTH_TOKEN='your_auth_token'
   ```
   
   Or update directly in `main.py`:
   ```python
   account_sid = 'YOUR_ACCOUNT_SID'
   auth_token = 'YOUR_AUTH_TOKEN'
   ```

## 🚀 Usage

**Run the application:**
```bash
python main.py
```

**Follow the interactive prompts:**
1. 📝 **Recipient Name** - Who you're sending to
2. 📞 **Phone Number** - WhatsApp number with country code (e.g., +1234567890)
3. 💬 **Message Content** - What you want to send
4. 📅 **Date** - When to send (YYYY-MM-DD format)
5. ⏰ **Time** - What time to send (HH:MM in 24-hour format)

## 📝 Example

```bash
$ python main.py

Enter the recipient name: John
Enter the recipient WhatsApp number with country code (e.g., +1234567890): +1234567890
Enter the message you want to send to John: Happy Birthday! 🎉
Enter the date to send the message (YYYY-MM-DD): 2024-01-15
Enter the time to send the message (HH:MM in 24-hour format): 09:00

Message scheduled to be sent to John at 2024-01-15 09:00:00.
```

## ⚠️ Important Notes

- **🔗 Sandbox Required**: Recipients must join the Twilio WhatsApp Sandbox to receive messages
- **📱 Sandbox Number**: Messages are sent using Twilio's WhatsApp Sandbox number
- **🚀 Production**: For production use, get your WhatsApp number approved by Twilio
- **💳 Credits**: Twilio requires credits for sending messages

## 🔒 Security

⚠️ **Important**: Never commit your actual Twilio credentials to version control. Use environment variables or a secure configuration file for production applications.

**Best Practices:**
- Use environment variables for API credentials
- Never share your auth tokens publicly
- Regularly rotate your API keys
- Use `.env` files (added to `.gitignore`)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**How to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

⭐ **Star this repository if you find it helpful!**

## 🏷️ Trending Topics & Hashtags

This project is tagged with the following trending topics for better discoverability:

### 🔥 Trending Topics
- `#python` - Python programming language
- `#whatsapp` - WhatsApp messaging platform
- `#twilio` - Twilio API integration
- `#automation` - Automated messaging
- `#scheduled-messaging` - Message scheduling
- `#api` - API integration
- `#messaging` - Messaging applications
- `#bot` - Automated bots
- `#webhook` - Webhook integration
- `#notifications` - Notification systems

### 🚀 Popular Categories
- `#automation-tools` - Tools for automation
- `#messaging-api` - Messaging API projects
- `#python-projects` - Python-based projects
- `#twilio-integration` - Twilio service integration
- `#whatsapp-api` - WhatsApp API projects
- `#scheduled-tasks` - Task scheduling
- `#communication-tools` - Communication utilities
- `#developer-tools` - Tools for developers

### 📱 Related Technologies
- `#python3` - Python 3.x
- `#twilio-api` - Twilio API usage
- `#whatsapp-business` - WhatsApp Business API
- `#message-automation` - Message automation
- `#api-integration` - API integration patterns
- `#python-automation` - Python automation scripts
- `#messaging-platform` - Messaging platform development
- `#scheduled-automation` - Scheduled automation tasks

---

**🔍 Search these hashtags on GitHub to find similar projects and connect with the community!**
