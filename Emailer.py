import smtplib
import ssl
from email.message import EmailMessage


def emailSender(br):
    emails = ['Numbers:   ', 'ksenija.dimitrijevic@gmail.com',
              'dimitrijevic.zarko@gmail.com', 'mita.mitric2013@gmail.com', 'dimitrijevic.jelica@gmail.com']
    print(emails)
    subject = "Hi Mummy"
    body = "Peppa here hehehehhehehehhehehehhehehhehehehhe!!!!!!!!!!!!!!"
    sender_email = "vasilije.dimitrijevic10@gmail.com"
    receiver_email = emails[br]
    # if br == 0:
    # receiver_email = "mita.mitric2013@gmail.com"
    # if br == 1:
    # receiver_email = "ksenija.dimitrijevic@gmail.com"
    # if br == 2:
    # receiver_email = "dimitrijevic.zarko@gmail.com"
    password = 'Vasa201020'

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = """
    <html>
        <body>
            <h1>
                "Hi Mummy"
            </h1>
            <p>
                Peppa here hehehehhehehehhehehehhehehhehehehhe!!!!!!!!!!!!!!
            </p>
            <h3>
                Do you remember Thissssssssss
            </h3>
            <a href = https://www.youtube.com/watch?v=NW_niwvZdXs>
                <button style="color:blue;">
                    Hello There Mummy Pig
                </button>
            </a>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("Sending Email!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Success")

emailSender(2)
