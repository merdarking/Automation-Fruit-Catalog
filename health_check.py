#! /usr/bin/python3

import psutil
import shutil
import socket
import emails

'''Check the CPU usage'''
def cpu_usage():
    usage = psutil.cpu_percent(1)
    # Check if CPU usage is not over 80%
    return usage < 80

'''Check the available disk space'''
def avail_disk_space(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    # Check if disk space is not lower than 20%
    return round(free,2) > 20

'''Check the available memory'''
def avail_memory():
    memory = psutil.virtual_memory()
    # Memory in MB
    mega = 2**20
    available_memory = memory.available / mega
    # Ensure available memory is not less than 500 MB
    return round(available_memory,2) > 500

'''Resolve hostname "localhost"'''
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    # Check if hostname 'localhost' is '127.0.0.1'
    return localhost == '127.0.0.1'

'''Send email when the problem occurs'''
def send_email(error_code):
    sender = 'automation@example.com'
    receiver = 'username@example.com'
    subject_list = [None]*4
    subject_list[0] = 'Error - CPU usage is over 80%'
    subject_list[1] = 'Error - Available disk space is less than 20%'
    subject_list[2] = 'Error - Available memory is less than 500MB'
    subject_list[3] = 'Error - localhost cannot be resolved to 127.0.0.1'
    subject = subject_list[error_code]
    body = 'Please check your system and resolve the issue as soon as possible'

    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send(message)
    return '{}. Email has been send'.format(subject)

def main():
    get_cpu_usage = cpu_usage()
    get_disk_space = avail_disk_space("/")
    get_memory = avail_memory()
    host_ip_address = check_localhost()
    status = get_cpu_usage, get_disk_space, get_memory, host_ip_address
    if False in status:
        code = status.index(False)
        print(send_email(code))
    else:
        print("Everything is find")
    
if __name__ == '__main__':
    main()