import zmq
import time
import json

def RunServer(rep_socket,address):

    rep_socket.bind(address) 
    time.sleep(1)
    print("listen...")
    while True:
        
        recv_message = rep_socket.recv_string()
        print("recive massage is： "+repr(recv_message))
        message = json.loads(recv_message)

        ProcessMessage(rep_socket,message)


def ProcessMessage(rep_socket,message):
    if (message["Name"] == "register"):
        Demo3dAddress = Register(message["Object"])
        msg = {
                "Name":"register",
                "Object": "finished",
            }
        json_msg = json.dumps(msg,sort_keys=True,indent=4)
        rep_socket.send_string(json_msg)
        print("send to demo3d : register finished")
    elif(message["Name"] == "load_arrived"):
        str_list = str.split(message["Object"])
        print("split: ",str_list)
        Box_Type = str_list[0]
        NB_PE1 = str_list[4]
        print("NB_PE1: ",NB_PE1)
        print("Box_Type：",Box_Type)
        if(Box_Type == "Cardboard" and NB_PE1 == "Main.PE1"):
            msg = {
                "Name":"action",
                "Object": "release",
                "ID":message["ID"]
            }

        elif(Box_Type == "Bule" and NB_PE1 == "Infeed.PE1"): 
            msg = {
                "Name":"action",
                "Object": "delete",
                "ID":message["ID"]
            }
        else: # main to PE2
            msg = {
                "Name":"action",
                "Object": "delete",
                "ID":message["ID"]
            }
        json_msg = json.dumps(msg,sort_keys=True,indent=4)
        rep_socket.send_string(json_msg)
    else:
        rep_socket.send_string('Nothing')
        print("waiting...")


def Register(returnAddress):
    Demo3dAddress = returnAddress
    print("Demo3d address is "+ Demo3dAddress)
    return Demo3dAddress



#-------------------------------------------#
#                   Main                    #
#-------------------------------------------#

address = "tcp://127.0.0.1:5556"
context = zmq.Context()

rep_socket = context.socket(zmq.REP)

RunServer(rep_socket,address)
#-------------------------------------------#
#                   End                     #
#-------------------------------------------#



