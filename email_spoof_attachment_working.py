import base64
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='',
    to_emails='',
    subject='email attachment',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

file_path = 'IET.pdf'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/pdf')
attachment.file_name = FileName('File_notice.pdf')
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('Example Content ID')
message.attachment = attachment
try:
    sendgrid_client = SendGridAPIClient('')
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)