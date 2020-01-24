# function to notify about:
#  1. houses
#  2. errors
# parameters

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# TODO setup email 
def email_notif(receiver, cc, subject, msg):
  sender_email = "bot.prodej.majetku@gmail.com"
  password = "enth364+!0N"

  message = MIMEMultipart("alternative")
  message["Subject"] = subject
  message["From"] = sender_email
  message["To"] = receiver
  message['Cc'] = cc

  text = f"""\
  """
  html = f"""\
        {msg}
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, [receiver, cc], message.as_string()
      )
      server.quit()
