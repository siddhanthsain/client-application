import socket
import datetime
import time 

date=datetime.date.today()
current_time=time.strftime("%H:%M:%S")
# socket.AF_INET--> throuh thr internet
# socket.SOCK_STREAM--> TCP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #to create ports

# targert_id= "192.168.255.70"
target_id="192.168.1.4"
target_port=2525

target_address=(target_id,target_port)

# s.settimeout(10)  # Set a timeout of 5 seconds for the recvfrom method
s.settimeout(20)

def rec():
    data = s.recvfrom(100)
    rec_message=data[0]
    receiver_ip=data[1][0]
    rec_message=rec_message.decode('ascii')
    print("Received message:", rec_message) 
    message_with_Datetime=f"{date}  ({current_time}) : Rec_Message => {rec_message}" 
    file= open(receiver_ip+'(R_to_S).txt','a')
    file.write(message_with_Datetime+"\n")
    # file.write("\n")
    file.close()

condition = True
while condition==True:
    message=input("plz enter msg : ")
    message_encrypted=message.encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("your message is sent\nResponse limit 20sec")
    try:
        rec()
    except socket.timeout:
        
        print("No response received.")
    choice=input("Do you want to send more message y/N")
        
    if choice.lower() == 'y':
        continue
    elif choice.lower() == 'n':
        print("Sending stoped....")
        condition = False

while True:
    rec()