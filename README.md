# WhatsApp Messenger - Scheduled Message Sender

A Python application that allows you to schedule and send WhatsApp messages using Twilio's WhatsApp API.

## Features

- Schedule WhatsApp messages for future delivery
- Send messages to any WhatsApp number with country code
- Simple command-line interface
- Error handling and validation

## Prerequisites

- Python 3.6 or higher
- Twilio account with WhatsApp API access
- Twilio credentials (Account SID and Auth Token)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/whatsapp-messenger.git
cd whatsapp-messenger
```

2. Install required dependencies:
```bash
pip install twilio
```

## Setup

1. Sign up for a Twilio account at [https://www.twilio.com](https://www.twilio.com)
2. Get your Account SID and Auth Token from the Twilio Console
3. Update the credentials in `main.py`:
   ```python
   account_sid = 'YOUR_ACCOUNT_SID'
   auth_token = 'YOUR_AUTH_TOKEN'
   ```

## Usage

Run the application:
```bash
python main.py
```

Follow the prompts to:
1. Enter recipient name
2. Enter recipient WhatsApp number (with country code, e.g., +1234567890)
3. Enter your message
4. Enter the date (YYYY-MM-DD format)
5. Enter the time (HH:MM in 24-hour format)

## Example

```
Enter the recipient name: John
Enter the recipient WhatsApp number with country code (e.g., +1234567890): +1234567890
Enter the message you want to send to John: Happy Birthday!
Enter the date to send the message (YYYY-MM-DD): 2024-01-15
Enter the time to send the message (HH:MM in 24-hour format): 09:00
```

## Important Notes

- The recipient must join the Twilio WhatsApp Sandbox to receive messages
- Messages are sent using Twilio's WhatsApp Sandbox number
- For production use, you'll need to get your WhatsApp number approved by Twilio

## Security

⚠️ **Important**: Never commit your actual Twilio credentials to version control. Use environment variables or a secure configuration file for production applications.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 