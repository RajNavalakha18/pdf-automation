# ***************************************************************
# TASKS
# 1. Download all the (only) attachments into the same folder 
# 2. Ask if the company wise downloading is the requirement
# 3. Date filtering 
# 4. If invoice number is same, don't write the data in the excel 
# *****************************************************************

# requirements
# Windows pc, Pywin32 does mot work with mac

from pathlib import Path  #core python module
import win32com.client  #pip install pywin32
from datetime import datetime

# Create output folder
print(Path.cwd())
output_dir = Path.cwd() / "Output"
output_dir.mkdir(parents=True, exist_ok=True)

# Connect to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Connect to folder
#inbox = outlook.Folders("youremail@provider.com").Folders("Inbox")
inbox = outlook.GetDefaultFolder(6)
# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

# print(dir(inbox))
# Get messages
messages = inbox.Items

date_time_str_start = '2001/08/07 11:55:02'
date_time_str_end = '2001/08/07 11:55:02'
start_time = datetime.strptime(date_time_str_start, '%Y/%m/%d %H:%M:%S').strftime('%Y-%m-%d %H:%M %p')
end_time = datetime.strptime(date_time_str_end, '%Y/%m/%d %H:%M:%S').strftime('%Y-%m-%d %H:%M %p')

messages = messages.Restrict("[ReceivedTime] >= '" + start_time
+ "' And [ReceivedTime] <= '" + end_time + "'")

messages.Sort("[ReceivedTime]", Descending=True)

for message in messages:
    subject = message.Subject
    # body = message.body
    attachments = message.Attachments
    #date
    date_email = message.ReceivedTime

    print('Mail with subject : ',subject, 'has ', len(attachments), 'attachments')

    # Save attachments
    for attachment in attachments:
        if str(attachment).endswith(".pdf"):
          attachment.SaveAsFile(output_dir / str(attachment))

    # Create separate folder for each message
    # target_folder = output_dir / str(subject)
    # target_folder.mkdir(parents=True, exist_ok=True)

    # # Write body to text file
    # Path(target_folder / "EMAIL_BODY.txt").write_text(str(body))

    # # Save attachments
    # for attachment in attachments:
    #     attachment.SaveAsFile(target_folder / str(attachment))