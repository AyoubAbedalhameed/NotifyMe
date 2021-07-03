# NotifyMe
Python Script, send notification emails whenever the machine IP addree changes. Designed to run as a Cron Job 


  This is version 1.0 , the sender email address password are stored in plain text, no decryption, the notifications can be send to only one email, there may be a gap between the notification email and the actual change time of the IP since the script is running as a cron, and no mechanism of run/wake once the IP changes. 
This Gap can be reduced according to the cron scheduling time. 
