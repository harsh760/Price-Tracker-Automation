import smtplib

def send_mail(name , diff , link):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Your email id' , "Your password")

    subject = "Price of " + name + " dropped by " + str(diff) + " !"

    body = "Check the amazon link \n We are glad to inform you that your " + name + "'s price is dropped by Rs. "+ str(diff) +"\n check This link \n" + link + "\n Thank You for Using our service!"

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'from email',
        'to email',
        msg
    )

    print("Mail successfully sent!")

    server.quit()