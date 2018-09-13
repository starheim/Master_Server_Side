import zmq
import time
import threading

def VEThread():
        context1 = zmq.Context()

        VEReceiveSocket = context1.socket(zmq.REP)
        VEForwardSocket = context1.socket(zmq.REP)

        VEReceiveSocket.bind("tcp://*:5560")
        VEForwardSocket.bind("tcp://*:5561")

        VEReceiveSocketConnected = VEReceiveSocket.recv()
        VEForwardSocketConnected = VEForwardSocket.recv()

        print(VEReceiveSocketConnected)
        print(VEForwardSocketConnected)

        #Sending socket back to retrieve message
        VEReceiveSocket.send(b"Chat established.")

        while True:
                message = VEReceiveSocket.recv()

                VEForwardSocket.send(b"Visual educator: %s" % message)

                VEForwardSocketReturned = VEForwardSocket.recv()

                VEReceiveSocket.send(b"")

def SThread():
        context2 = zmq.Context()

        SubjectReceiveSocket = context2.socket(zmq.REP)
        SubjectForwardSocket = context2.socket(zmq.REP)

        SubjectReceiveSocket.bind("tcp://*:5562")
        SubjectForwardSocket.bind("tcp://*:5563")

        SubjectReceiveSocketConnected = SubjectReceiveSocket.recv()
        SubjectForwardSocketConnected = SubjectForwardSocket.recv()

        print(SubjectReceiveSocketConnected)
        print(SubjectForwardSocketConnected)

        #Sending socket back to retrieve message
        SubjectReceiveSocket.send(b"Chat established.")

        while True:
                message = SubjectReceiveSocket.recv()

                SubjectForwardSocket.send(b"Subject: %s" %message)

