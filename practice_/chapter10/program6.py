# Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” and see 



from random import randint

class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book (prachi, fro, to):
        print(f"Ticket is booked in train no: {prachi.trainNo} from{fro} to {to}")

    def getstatus(self):
        print(f"TrainNo: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to{to} is {randint(332, 4556)}" )

t = train(23234)
t.book("Amb" ,"Jalandhar")

t.getstatus()
t.getfare("Amb" ,"Jalandhar")