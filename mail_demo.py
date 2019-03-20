# An application to send email using python

import os
import smtplib
import imghdr
from email.message import EmailMessage

# EMAIL_USER & EMAIL_PASSWORD are save to my system environment user variable
# so as to hide it from my code and it's accessed using os
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# people I want to sent the email to
contacts = ['segwuonwu@gmail.com', 'solomon.egwuonwu@wsu.edu']

# composing a plain_text message
# msg = EmailMessage()
# msg['Subject'] = 'Grab dinner this weekend!'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = ', '.join(contacts)
# msg.set_content('How about dinner at 6pm this Saturday?')

# composing a plaintext message with an attachment
msg = EmailMessage()
msg['Subject'] = 'Check out my new pic!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'solomon.egwuonwu@wsu.edu'
msg.set_content('The attached image is my recent pic!')

# storing multiple images in a list
files = ["C:\\Users\\solo4\\OneDrive\\Pictures\\Saved Pictures\\DSCN0006.JPG",
         "C:\\Users\\solo4\\OneDrive\\Pictures\\Saved Pictures\\IMG_3899.jpg"]

# looping through the files an attaching them to the email
for file in files:
    # formatting your image
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)

    # adding the attached image to your email
    msg.add_attachment(file_data, maintype='image', subtype=file_type)

# Accessing the server port
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

