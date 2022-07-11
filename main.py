from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('jagilren@gmail.com', 'ejqbvkhoujegsjui')

msg = MIMEMultipart()
msg['Subject'] = "Hola PyCharm"
msg.attach(MIMEText("Hola PyCharm"))

#Seccion de attachments
with open(one_attachment, 'rb') as f:
    file = MIMEApplication(
        f.read(), name=os.path.basename(one_attachment)
    )
    file['Content-Disposition'] = f'attachment; \
    filename="{os.path.basename(one_attachment)}"'
    msg.attach(file)

to = ["jagilren@outlook.com", "pythonforsendmail@gmail.com"]
smtp.sendmail(from_addr="jagilren@gmail.com",
              to_addrs=to, msg=msg.as_string())
smtp.quit()