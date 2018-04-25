import requests

# Change this as needed.
SERVER = "http://localhost:5000"

def getDailyData():
    films = getFilmDetails()
    tickets = getTicketData(films["films"])
    print(tickets)


def getFilmDetails():
    return requests.get(SERVER + "/api/films").json()


def getTicketData(films):
    tickets 
    for film in films:



def main():
    getDailyData()


if __name__ == '__main__':
    main()
