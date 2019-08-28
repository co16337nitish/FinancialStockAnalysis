import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

#Download the mailing list in .csv format and paste its directory in this function argument
df = pd.read_csv("/home/Dittu/Documents/TPC/Alumni Mailing List - Sheet1.csv")

#For Statistics
failed = sent = duplicates_sent = 0
lastemail = " "

#Enter the Gmail id and password here
gmail_user = 'alumnitpc@gmail.com'
gmail_password = 'alumni@ccet'

sent_from = gmail_user
#Check if the column names are correct. Also you can add extra columns as required (seperate them by ,)
# l = [list(x) for x in df[["First Name", "Email ID"]].values]
l = [['Dittu', 'nitishrocks88@gmail.com'], ['Nitish', 'nitish.cse2020@gmail.com']]
i=l[1]
for i in l:
    to = i[1]

    #Write the subject here
    subject = 'Alumni Meet Date Preference Collection'


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to




# Create the body of the message (a plain-text and an HTML version).
    #Plain text body part (Comment if body in html)
    text = ''' May God gift you all the colours of life, colours of joy, colours of happiness, colours of friendship, colours of love and all other colours you want to paint in your life. Wishing our Alumni and their families a very Happy Holi... Hoping all of you Have a colourful Holi !!!

Regards
TPC
CCET'''
    partBODY = MIMEText("Dear "+i[0]+",\n"+text, 'plain')
    #PLain text body part ends

    #HTML body part (Comment if body in Plain text)
    # html = """\
    # <html>
    # <head></head>
    # <body>
    #     <img src="https://gdurl.com/lDJP" alt="Smiley face" height="42" width="42">
    # </body>
    # </html>
    # """
    # partBody = MIMEText(html, 'html')
    # #HTML body part
    msg.attach(partBODY)
# Creation of the body of the message ends here.




#For attaching file
    """partATTACHMENT = MIMEBase('application', "octet-stream")
    #Edit first argument for open() for the directory of file to be attached
    partATTACHMENT.set_payload(open("/home/Dittu/Documents/TPC/ccet ny.png", "rb").read())
    encoders.encode_base64(partATTACHMENT)
    #Edit filename and keep it same as the actual file name (especially the file extension)
    partATTACHMENT.add_header('Content-Disposition', 'attachment; filename="ccet ny.png"')
    msg.attach(partATTACHMENT)"""
#File attachment block ends here (Make duplicates to Attach more than 1 files)


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.close()

        print('Email sent! to %s' % (to))
        if lastemail.lower() == i[1].lower():
            duplicates_sent +=1
        else:
            sent += 1
        lastemail = i[1]
    except:
        print('Something went wrong...')
        failed += 1


#Print Stats
print("Total records processed: "+ str(failed+sent+duplicates_sent))
print("Successfully sent: "+ str(sent))
print("Duplicates Sent: "+ str(duplicates_sent))
print("Failed attempts: "+ str(failed))
