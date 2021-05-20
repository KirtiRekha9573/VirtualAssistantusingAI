import smtplib

content = 'example emails stuff here'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('kirtichaudhari070495@gmail.com', 'KirtiC@95')

mail.sendmail('kirtichaudhari070495@gmail.com', 'krchaudharib4u@gmail.com ', content)

mail.close()