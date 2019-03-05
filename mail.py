import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(to_email, subject, text):
    from_email = 'p.j.schietvereniging@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    mail = smtplib.SMTP(host='smtp.gmail.com', port=587)
    mail.ehlo()
    mail.starttls()
    mail.login(from_email, '!Password123')
    mail.sendmail(from_email, to_email, msg.as_string())
    mail.close()
