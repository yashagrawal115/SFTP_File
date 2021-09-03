#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:18:21 2020

@author: yashaggrawal
"""




import paramiko 
import sys 
local_path = sys.argv[1] 
report_path =  sys.argv[2] 
    
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='yash.yashonline.com',username='yashagrawal',password='Mtc%sredf3Aw5',port =22)

sftp_client=ssh.open_sftp()
print(sftp_client.getcwd())
print('connection established')


sftp_client.chdir('')
print(sftp_client.getcwd())
print('1')
#sftp_client.put("/home/yashaggrawal/Desktop/testing_sftp.txt",'/CODESET/ready/testing_sftp_file.txt')
sftp_client.put(local_path,report_path)
sftp_client.close()

ssh.close()
