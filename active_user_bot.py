#! /usr/bin/python3

# Imports
import praw
import time
import csv
import datetime as dt
import matplotlib.pyplot as plt

class OnlineUserBot:
    """A simple bot that finds the number of users online a specifc Subreddit."""

    def __init__(self, subreddit_name, interval, lengthOfTime, client_id, client_secret, password, user_agent, username):
        self.subreddit_name = subreddit_name
        self.interval = interval
        self.lengthOfTime = lengthOfTime
        self.client_id = client_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.password = password
        self.user_agent = user_agent
        self.username = username

    def auth(self):
        self.reddit = praw.Reddit(client_id = self.client_id,
                                  client_secret = self.client_secret,
                                  password = self.password,
                                  user_agent = self.user_agent,
                                  username = self.username)

        self.subreddit = self.reddit.subreddit(self.subreddit_name)

    def findNumberOnlineUsers(self):
        return self.subreddit.accounts_active

    def write_information_to_CSV(self, _online_users, _readable_time):
        with open('data.csv', "a") as csvFile:
            filewriter = csv.writer(csvFile)
            filewriter.writerow([_online_users, _readable_time])
            csvFile.close()

    def activateBot(self):

        elapsed_time = time.clock()

        while elapsed_time < self.lengthOfTime:

            self.auth()

            readable_time = str(dt.datetime.now().time().strftime("%H-%M-%S"))
            elapsed_time = time.clock()
            online_users = self.findNumberOnlineUsers()

            self.write_information_to_CSV(online_users, readable_time)

            print(elapsed_time)
            time.sleep(self.interval)


# Plot data
def plotData(subreddit_name):
    # create list holders for our data.
    number_of_online_users = []
    dateAndTime= []

    with open('data.csv', "r") as csv_file:

        csv_reader = csv.reader(csv_file, delimiter = ',')

        for row in csv_reader:
            try:
                number_of_online_users.append(int(row[0]))
                time = row[1]
                dateAndTime.append(time)
            except Exception as e:
                if e == IndexError:
                    pass


    # Print data
    print(number_of_online_users)
    print(dateAndTime)

    plt.plot(dateAndTime, number_of_online_users)
    plt.xlabel('Time')
    plt.ylabel('Online Users')
    plt.title('Subreddit: ' + subreddit_name)

    ax = plt.subplot()

    every_nth = 40
    for i, tick in enumerate(ax.xaxis.get_ticklabels()):
        if i % every_nth != 0:
            tick.set_visible(False)

    for i, line in enumerate(ax.xaxis.get_ticklines()):
            if i % every_nth != 0:
                line.set_visible(False)

    plt.xticks(fontsize=8, rotation=60)

    plt.show()

if __name__ == '__main__':

    # Change the input to this class with your information from the Reddit API (See README.md for instructions)
    bot = OnlineUserBot('SUBREDDIT_NAME', INTERVAL, TOTAL_TIME, 'CLIENT_ID','CLIENT_SECRET','PASSWORD','USER_AGENT','USERNAME')

    bot.activateBot()
    plotData('SUBREDDIT_NAME')
