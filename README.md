# NotifyMe
Python Script, sends notification emails whenever the machine IP address changes. Designed to run as a Cron Job on linux. 


  This is version 1.0 , it has many limitations, the sender email address password are stored in plain text, no decryption, the notifications can be send to only one email address, The script use one website only to fetch current  IP address which is  "http://checkip.dyndns.com", if it fails there are no "spare" or a list of websites to use.
  
There may be a gap between the notification email and the actual change time of the IP since the script is running as a cron, and no mechanism of run/wake once the IP changes, this Gap can be reduced according to the cron scheduling time. 
