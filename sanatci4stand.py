from stand import Normal
#Normal bilet için sanatçı class'ı
class Singer4(Normal):   
    ticketno=[]
    for i in range(250):
        ticketno.append(i+1)
    def __init__(self, name, surname, age,singer):
        super().__init__(name, surname, age,singer)
