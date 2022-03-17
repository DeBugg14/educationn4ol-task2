import smtplib 

sender_email = input("Type your email and press enter: ");
receiver_email = input("Type receivers email and press enter: ")
password = input("Type your password and press enter: ")

subject = input('Enter your email subject and press Enter: ')
body = input("Enter your email body and press Enter: ")
msg = f'Subject: {subject}\n\n {body}'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email,password)
    smtp.sendmail(sender_email,receiver_email,msg)
    print('\nMessage successfully sent!')


