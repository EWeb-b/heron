import tickets2money
# these functions are used to handle Graemes data an convert it into a form the app can use

## hard coded data
# INCdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
# INCtakings = ['120','120','300','200','180','240','150']
#
# INCweekly = [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]]
#
# week_data = [[[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]],
#             [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]]]
def calc_takings_list(list_of_lists):
    # list_of_lists: weekly ticket data breakdown
    takings_list = []
    for i in range(7):
        daily_list = tickets2money.Total(list_of_lists[i])
        takings_list.append(str(daily_list))
    return takings_list
#print('weekly takings for inception, broken down by days',calc_takings_list(INCweekly))

def calc_weekly_takings(list_of_lists_of_lists):
    # list of legnth 9, then
    # list of length 7, then
    # list of legnth 5(ticket types)
    takings_buffer = []
    for i in range(9):
        #print(calc_takings_list(list_of_lists_of_lists[i]))
        takings_buffer.append(calc_takings_list(list_of_lists_of_lists[i]))
    weekly_buffer = [0,0,0,0,0,0,0]
    for i in range(7):
        for j in range(9):
            weekly_buffer[i] += float(takings_buffer[j][i])
    return weekly_buffer
# print(calc_weekly_takings(week_data))
