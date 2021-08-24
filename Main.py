import re, requests,smtplib, ssl, socket, datetime



port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "greenpizza0000@gmail.com"  # Enter your address
receiver_email = "aasedqiabedalhameed173@cit.just.edu.jo"  # Enter receiver address
password = "EasyPass00"
MyHost = socket.gethostname() 
current_time = datetime.datetime.now() 

url = requests.get("http://checkip.dyndns.com")
WebPage = url.text
IP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', WebPage )




MyIPFile =  open(r"LastOne.txt", "r")
Temp = MyIPFile.read()
MyIPFile.close
print(Temp)
MyIP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', Temp )


print(IP[0])
print(MyIP[0])

message = """\
Subject: IP Notification 

HostName: %s
IP Address has been changed to: %s

@%s""" %(MyHost,IP[0], current_time)

if IP[0] != MyIP[0]:
    MyIPFile =  open(r"LastOne.txt", "w")
    MyIPFile.write(IP[0])
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

