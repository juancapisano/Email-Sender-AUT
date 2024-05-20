# Bulk Email Sender Script

## Overview

This script is designed to send a series of emails to multiple recipients individually. It is particularly useful for tasks such as sending job applications, newsletters, or any type of bulk communication where each recipient needs to receive their own separate email.

## Features

- Sends emails to a list of recipients individually.
- Attaches multiple PDF files to each email.
- Configurable email subject and body content.
- Uses plain text for email content and attachments for added flexibility.

## Requirements

- Python 3.x
- `smtplib` module (standard library)
- `email` module (standard library)
- An SMTP server to send emails (configured with your email account details)

## Setup

1. **Install Python 3.x** if it is not already installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Configure your email account**:
   - Open the script and locate the email configuration section.
   - Replace the placeholder email and password with your actual email credentials.
   - Set the SMTP server and port (e.g., for Gmail, use `smtp.gmail.com` and port `587`).

3. **List of Recipients**:
   - Update the `destinatarios` list with the email addresses of your recipients.

4. **Email Content**:
   - Set your email subject and body content within the script.

5. **Attachments**:
   - Ensure the PDF files you want to attach are in the same directory as the script or provide the correct file path.

## Usage

1. **Run the script**:
   - Execute the script using a Python interpreter.
   - Each recipient in the `destinatarios` list will receive an individual email with the specified content and attachments.

## Example

Here's an example snippet from the script:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email account credentials
email_address = 'your_email@example.com'
email_password = 'your_password'

# List of recipients
destinatarios = [
    'example1@example.com',
    'example2@example.com',
    # Add more emails as needed
]

# Email content
subject = 'Your Subject Here'
body = 'Your email body content here.'

# Attachments
attachments = ['file1.pdf', 'file2.pdf']

for destinatario in destinatarios:
    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = destinatario
    msg['Subject'] = subject

    # Attach the body
    msg.attach(MIMEText(body, 'plain'))

    # Attach each file
    for file in attachments:
        attachment = open(file, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file)
        msg.attach(part)

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, destinatario, text)
        server.quit()
        print(f'Email sent to {destinatario}')
    except Exception as e:
        print(f'Failed to send email to {destinatario}. Error: {str(e)}')
