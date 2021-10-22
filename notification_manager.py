from email.utils import formataddr
from email.message import EmailMessage
from email.mime.text import MIMEText
import smtplib
import requests

SHEETY_USER_END_POINT = "https://api.sheety.co/b946898b0f13306711bf82e72272d307/flightDeals/users"
class NotificationManager:
    def __init__(self, send_message):
        self.my_email = "email"
        self.password = "password"
        # customers_emails = []
        customers = requests.get(SHEETY_USER_END_POINT)
        customers_data = customers.json()['users']
        for data in customers_data :
            email_data = data['email']
            print(email_data)
            # customers_emails.append(email_data)
            msg = EmailMessage()
            msg['From'] = formataddr(('Ram', self.my_email))
            msg['To'] = email_data
            # msg['To'] = ", ".join(customers_emails)
            msg['Subject'] = "Flight deal alert!"
            msg.set_content(send_message)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                # connection.set_debuglevel(1)
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.send_message(msg)
                print("email sent")
                print("\n")




# notification_manager = NotificationManager("CHECKING TODAY SEP")