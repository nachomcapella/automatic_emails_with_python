import pandas as pd
from email.message import EmailMessage
import ssl
import smtplib

def get_credentials():
    emails = pd.read_csv(
        '../credentials/emails.csv',
        sep=';',
        encoding='latin-1'
        )

    sender_email = emails[emails['TYPE']=='Sender']['EMAIL_ADDRESS'].values[0]
    sender_password = emails[emails['TYPE']=='Sender']['PASSWORD'].values[0]
    receiver_email = emails[emails['TYPE']=='Receiver']['EMAIL_ADDRESS'].values[0]

    return sender_email, sender_password, receiver_email

def compose_email(sender_email, receiver_email, df_to_do_list):
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

    return em.as_string()


def send_email(df_to_do_list):
    with smtplib.SMTP_SSL(
        host='smtp.gmail.com',
        port=465,
        context=ssl.create_default_context()
        ) as smtp:

        sender_email, sender_password, receiver_email = get_credentials()

        smtp.login(
            user=sender_email,
            password=sender_password
            )

        smtp.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=compose_email(
                sender_email=sender_email,
                receiver_email=receiver_email,
                df_to_do_list=df_to_do_list
                )
            )

        print('Email sent')