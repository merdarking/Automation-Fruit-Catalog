#! /usr/bin/python3

import os
import sys
import emails

def main():
    path = os.path.join(os.path.dirname(sys.argv[0]),"processed.pdf")
    sender = 'automation@example.com'
    receiver = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'
    
    message = emails.generate(sender, receiver, subject, body, path)
    emails.send(message)

if __name__ == '__main__':
    main()