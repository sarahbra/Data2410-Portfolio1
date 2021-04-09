import socket
from thread import *
import threading
import random
import sys
import time

# This program hosts a chat server for human users. It takes a single parameter:
# port number. Every client gets their own thread so as not to disrupt other
# users. The server is always open once the program is run (quit with
# ctrl+alt+c). Users are banned if they use bad language or are secretely
# robots.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 2:
    print("This server takes port as input parameter. Try again!")

port = int(sys.argv[1])

s.bind(('0.0.0.0',port))

s.listen(4)

human_client_list = []
message_log = []
lock = threading.Lock()

def clientThread(con,address):
    while True:
        message = con.recv(2048).decode()
        name = message.split(":")[0]
        lock.acquire()
        if message:
            if badLanguage(message):
                removeClient(con,"language",name)
            else:
                sendToAll(message, con)
                print "\n" + message
                if message in message_log:
                    accuseOfBoting(con,name)

            message_log.append(message)
        else:
            removeClient(con,"nonresponsive",name)
        lock.release()

# Checks language for potential bad words
def badLanguage(message):
    list_of_bannable_phrases = ["kill", "maim", "decapitat", "bomb", "shoot",
                                "tortur", "exterminat"]
    for phrase in list_of_bannable_phrases:
        if phrase in message:
            return True
        else:
            return False


#Accuse client of being a robot
def accuseOfBoting(con,name):
    if con in human_client_list:
        output_message = ("Host: Warning: This channel is for "
                          + "human users only. Are you a robot?")

        con.send(output_message.encode())
        defence = con.recv(2048).decode()
        removeClient(con,"bot",name)
        
#removes non-cooperative humans or bad robots        
def removeClient(con, reason, name):
    if con in human_client_list:
        if reason == "bot":
            kick_message = ("Host: You have been banned for suspicion of "
            + "bot-usage.")
        else:
            kick_message = "Host: You have been banned for bad language usage." 

        con.send(kick_message.encode())
        last_words = con.recv(2048).decode()
        human_client_list.remove(con)
        #info_message = name + " is no longer with us."
        #sendToAll(info_message, None)


#broadcasts message to all except sender
def sendToAll(msg, con):
    for human in human_client_list:
        if human != con:
            try:
                human.send(msg.encode())
            except:
                human.close()
                removeClient(human)

# suggests new action to clients
def newAction():
    actions = ["play", "eat", "gamble", "dance", "drink", "bend", "volunteer"]
    requests = ["How about we begin to", "Would you like to", "Wanna"]

    return random.choice(requests) + " " + random.choice(actions) + "?"

output_message = ""

while True:
    connection, address = s.accept()
    human_client_list.append(connection)
    if len(human_client_list) == 1:
        output_message = "Host: " + newAction()
        message_log.append(output_message)
        print "\n" + output_message

    connection.send(output_message.encode())
    start_new_thread(clientThread,(connection,output_message)) 
    
connection.close()
s.close()
