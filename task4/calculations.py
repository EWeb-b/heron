import tickets2money
# these functions are used to handle Graemes data an convert it into a form the app can use

## hard coded data
# INCdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
INCtakings = ['120','120','300','200','180','240','150']

INCdaily = [[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[10,2,3,5,1],[0,0,0,0,0],[2,1,3,5,0],[0,0,0,0,0]]
def calc_takings_list(list_of_lists):
    # list_of_lists: weekly ticket data breakdown
    takings_list = []
    for i in range(7):
        daily_list = tickets2money.Total(list_of_lists[i])
        takings_list.append(str(daily_list))
    return takings_list
print(calc_takings_list(INCdaily))
