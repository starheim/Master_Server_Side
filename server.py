import zmq
import chatserver

context = zmq.Context()
visualEducator = context.socket(zmq.REP)
subject = context.socket(zmq.REP)

visualEducator.bind("tcp://*:5555")
subject.bind("tcp://*:5556")

visualEducatorConnected = visualEducator.recv()
visualEducator.send(b"Connected to the server.")
visualEducatorReady = visualEducator.recv()

subjectConnected = subject.recv()
subject.send(b"Connected to the server.")
subjectReady = subject.recv()

visualEducator.send(b"Both parties are connected.")
subject.send(b"Both parties are connected.")
subjectReady = subject.recv()

#Command from visual educator to start examination
visualEducatorStartExamination = visualEducator.recv()

#Command is forwarder to the subject
subject.send(b"Starting examination.")

#Sending confrimation to visual educator
visualEducator.send(b"Examination has started.")

#Awaiting test completion
visualEducatorAwaiting = visualEducator.recv()

#Confirming completion of examination
examnationCompleted = subject.recv()

#Sending confirmation to visual educator
visualEducator.send(b"Examination has been completed.")



