import smtplib

gmail_user = 'exampleuser@mail.com'
gmail_password = 'xxxxxx'

sent_from = 'example@mail.com'
to = ['email_one', 'email_two']
subject = 'Test email'
body = 'This is a email.'


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
    
""" with google Less secure app access """
