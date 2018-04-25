def adult(num):
    return num*5.0
def student(num):
    return num*4.0
def child(num):
    return num*4.0
def OAP(num):
    return num*4.0
def VIP(num):
    return num*6.0

def Total(tickets_sold):
    # takes list of length 5. Each index corresponds to the type of ticket, the int inside is quantity
    # index0: adult
    # index1: student
    # index2: child
    # index3: OAP
    # index4: VIP
    #total = adult(tickets_sold[0]) + student(tickets_sold[1]) + child(tickets_sold[2]) + OAP(tickets_sold[3]) + VIP(tickets_sold[4])
    total = OAP(tickets_sold[0]) + adult(tickets_sold[1]) + student(tickets_sold[2]) + child(tickets_sold[3]) + VIP(tickets_sold[4])
    return total


#print(Total([1,1,1,1,1]))
