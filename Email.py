import imaplib

import os

import time

from email.parser import HeaderParser

obj = imaplib.IMAP4_SSL('imap.mail.yahoo.com','993')        															#Gmail IMAP server address: imap.gmail.com, leave port 993.
username = "USERNAME"																								#Enter your own username, everything before the @ sign.
password = "PASSWORD"																								#Your email password.
obj.login(username, password)
first_loop = True
update = False
buf_new_mails = 0

while True:
        
        obj.select()
        emailamount = str(len(obj.search(None, 'UnSeen')[1][0].split()))
        
        emailamount = int(emailamount)

        if emailamount != buf_new_mails or first_loop == True:													
                buf_new_mails = emailamount
                first_loop = False
                update = True
        
        
        time.sleep(1)
                
        if update == True:																							#Only update when the number of unread emails change.
                
                        print ("You have " + str(emailamount) + " new emails.\n")
                        for n in range(0, int(emailamount)):
                        
                                data = obj.search(None, 'ALL')
                                id_list = data[-1]
                                last_id = str(id_list).split()[-2 - n]
                                last_id = int(last_id)
                                data = obj.fetch(last_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT FROM)] FLAGS)')
                                header_data = data[1][0][1]
                                parser = HeaderParser()
                                msg = parser.parsestr(header_data)
                                msg = str(msg).splitlines()
                                subject = msg[1]
                                from_who = msg[2]
                                from_who = from_who.split()
                                print str(n+1) + ": "
                                print (from_who[0] + " " + from_who[1] + "\n")
                                time.sleep(2)
                                print(subject + "\n")
                                time.sleep(2)
        update = False
