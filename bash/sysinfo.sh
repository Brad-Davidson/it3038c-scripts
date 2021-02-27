#!/bin/bash
#This script will email the ip, hostname, date, and user of a computer
emailaddress=davidsbw@mail.uc.edu #this is my school email
today=$(date) #today's date and time
ipv4=$(ip a|grep 'dynamic ens192'|awk '{print $2}') #gets ip address
user=$USER
hostname=$HOSTNAME
content="User $USER
Server Name is $hostname
IP address is $ipv4
Date and Time is $today"
echo "Email will contain $content" #msg that the email will send
mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)


