import smtplib
import ssl
from email.message import EmailMessage
import schedule
import time
from datetime import date

# Email configuration
email_sender = 'k.gbenga234@gmail.com'
email_password = 'password'
email_receivers = {
    'oguntadetoluwalope678@gmail.com': '14:19',  
    'kajolagbenga@gmail.com': '14:19',  
    'olatujaopeoluwa@gmail.com': '14:20',  
    'kajolagbengaprodigy@gmail.com': '14:20',
    'kajolaolasubomi@gmail.com': '14:21',
    'ibroheemabdullah@gmail.com': '14:22',
    'kajolasundayoluwafemi@gmail.com': '14:23'
}

subject = 'Email Automation Model'
body = """
From UMeRA's ICT Department..... We are just testing it......
"""

def send_email(email_receiver, email_time):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f"Email sent successfully to {email_receiver} at {email_time}!")

# Schedule email sending for today
today = date.today().strftime("%Y-%m-%d")
print(f"Today's date: {today}")

# Different time schedules for each email receiver
for email_receiver, email_time in email_receivers.items():
    schedule.every().day.at(email_time).do(send_email, email_receiver, email_time)

while True:
    schedule.run_pending()
    time.sleep(1)