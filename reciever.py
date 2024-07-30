import socket
import datetime
import time 

# socket.AF_INET--> throuh thr internet
# socket.SOCK_STREAM--> TCP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #socket naem calss

# ip_address= "192.168.255.70"
ip_address="192.168.1.4"
port_no=2525  #random no  , range  is 0-65353 , 0-1023 are reserved

complete_address=(ip_address,port_no)
s.bind(complete_address)

# s.settimeout(20)



print(".......I am listining......")
while True:
        data= s.recvfrom(100)
        message=data[0]
        message=message.decode('ascii')
        sender_ip=data[1][0]
        sender_port=data[1][1]

        date=datetime.date.today()
        current_time=time.strftime("%H:%M:%S")
        message_with_Datetime=f"{date}  ({current_time}) : Message => {message}"
        file= open(sender_ip+'(S_to_R).txt','a')
        file.write(message_with_Datetime+"\n")
        # file.write("\n")
        file.close()
        print(message)
        target_address=(sender_ip,sender_port)
        
        condition=True
        while condition:
            option=input("Do you like to send message ")
            if option.lower()=='y':
                    message_to_send=input("Enter your message : ")
                    s.sendto(message_to_send.encode('ascii'),target_address)
            elif option.lower()=='n':
                    condition=False
                    print("I am listining....")
                    
                           
