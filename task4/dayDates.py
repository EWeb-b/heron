from datetime import *

def dayDates(day):
    # takes datetime
    # returns list1 of dates for the days of the current week
    # print(datetime.date.today().strftime("%d"))
    # print(datetime.date.today() - 15)
    # print(datetime.date.today().strftime("%A"))

    list1 = []

    # day = datetime.date.today()

    # past = day - datetime.timedelta(days = 15)
    #
    # print(past)
    if datetime.today().weekday() == 1:
        for i in range(6):
            list1.append(day + timedelta(days = i))
    elif datetime.today().weekday() == 2:
        for i in range(-2,5):
            list1.append(str(day + timedelta(days = i)))
    elif datetime.today().weekday() == 3:
        for i in range(-3,4):
            list1.append(str(day + timedelta(days = i)))
    elif datetime.today().weekday() == 4:
        for i in range(-4,3):
            list1.append(str(day + timedelta(days = i)))
    elif datetime.today().weekday() == 5:
        for i in range(-5,2):
            list1.append(str(day + timedelta(days = i)))
    elif datetime.today().weekday() == 6:
        for i in range(-6,1):
            list1.append(str(day + timedelta(days = i)))
    else:
        for i in range(-7,0):
            list1.append(str(day + timedelta(days = i)))

    # for i in range(len(list1)):
    #     print(i)
    #     # list1[i].strftime('%m-%d-%Y')
    #     str(list1[i])
    #     print(list1[i])
    #     #print(type(list1[i]))
    for i in range(7):
        if i == 0:
            list1[i] = 'Monday\n'+str(list1[i])
        elif i == 1:
            list1[i] = 'Tuesday\n'+str(list1[i])
        elif i == 2:
            list1[i] = 'Wednesday\n'+str(list1[i])
        elif i == 3:
            list1[i] = 'Thursday\n'+str(list1[i])
        elif i == 4:
            list1[i] = 'Friday\n'+str(list1[i])
        elif i == 5:
            list1[i] = 'Saturday\n'+str(list1[i])
        else:
            list1[i] = 'Sunday\n'+str(list1[i])
    print(list1)
    return list1
# day = date.today()
# dayDates(day)
