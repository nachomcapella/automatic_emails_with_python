import pandas as pd
from email.message import EmailMessage
import ssl
import smtplib

emails = pd.read_csv(
    '../credentials/emails.csv',
    sep=';',
    encoding='latin-1'
    )

sender_email = emails[emails['TYPE']=='Sender']['EMAIL_ADDRESS'].values[0]
sender_password = emails[emails['TYPE']=='Sender']['PASSWORD'].values[0]
receiver_email = emails[emails['TYPE']=='Receiver']['EMAIL_ADDRESS'].values[0]

subject = 'TO DO LIST NOTIFICATION'
body = """
Task: bla bla
Original date: bla bla
"""

em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['Subject'] = subject
em.set_content(body)

context_ssl = ssl.create_default_context()

with smtplib.SMTP_SSL(
    host='smtp.gmail.com',
    port=465,
    context=context_ssl
    ) as smtp:

    smtp.login(
        user=sender_email,
        password=sender_password
        )

    smtp.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg=em.as_string()
        )

    print('Email sent')