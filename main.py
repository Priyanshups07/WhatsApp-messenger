# Step 1: Import required libraries
from twilio.rest import Client
from datetime import datetime
import time
from threading import Thread
import os

# Step 2: Twilio credentials (use environment variables for security)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

if not account_sid or not auth_token:
    print("❌ Error: Twilio credentials not found!")
    print("Please set the following environment variables:")
    print("  export TWILIO_ACCOUNT_SID='your_account_sid'")
    print("  export TWILIO_AUTH_TOKEN='your_auth_token'")
    exit(1)

client = Client(account_sid, auth_token)

# Step 3: Define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio Sandbox number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred:', e)

# Step 4: User input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +1234567890): ')
message_body = input(f'Enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

def schedule_message(recipient_number, message_body, schedule_datetime, name=None):
    current_datetime = datetime.now()
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()
    if delay_seconds <= 0:
        print('The specified time is in the past. Please enter a future date and time.')
        return False, 'The specified time is in the past.'
    else:
        print(f'Message scheduled to be sent to {name or recipient_number} at {schedule_datetime}.')
        time.sleep(delay_seconds)
        send_whatsapp_message(recipient_number, message_body)
        return True, 'Message sent successfully.'

if __name__ == '__main__':
    try:
        schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
        schedule_message(recipient_number, message_body, schedule_datetime, name)
    except ValueError:
        print('Invalid date or time format. Please use the correct format (YYYY-MM-DD for date and HH:MM for time).') 