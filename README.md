<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_OnlineUsers/master/Images/Reddit_Logo.png" alt="Reddit" width="200">
  </br>
  RedditBot: Subreddit Online Users
  <br>
</h1>

<p align="center">
  <a href="#instructions">Instructions</a> •
  <a href="#instructions-getting-started">Getting Started</a> •
  <a href="#instructions-subreddit_onlineusers_collector_py">Online Users</a> •
  <a href="#future-features">Future Features</a>
</p>

<h3 align="center">
  <br>
  Example of Output
  </br>
  <img src="https://i.redd.it/7mwm5u63qaw21.png" alt="gatechOnlineUserGraph">
</h2>

# Purpose
Track the amount of online users for a given subreddit you provide every time interval, and save that data to display on a graph.

## Getting Started
  1.) Download the zip file and extract the contents.  
  2.) Open the active_user_bot.py module

## Getting Started - Required
  First, you'll want to set up your credentials to use the Reddit API. At the the bottom of active_user_bot.py you will notice:
  ~~~~
  bot = OnlineUserBot('SUBREDDIT_NAME', INTERVAL, TOTAL_TIME, 'CLIENT_ID','CLIENT_SECRET','PASSWORD','USER_AGENT','USERNAME')
  ~~~~
  You can watch this video made by Sentdex to help you set this up! https://www.youtube.com/watch?v=NRgfgtzIhBQ

  <hr>

  Once you've set up your credentials, you need to change 3 more things.

  * SUBREDDIT_NAME
    1. Should be in the form of whatever comes after the r/. For example r/__gatech__ should become __gatech__.  
    2. _This is case sensitive, so be careful!_
    3. type = str. Keep the parentheses
  * INTERVAL
    1. This is the number of seconds between each call to the api for data. I find that about 10-30 seconds is good because the number of users only updates about every 20-30 seconds.
    2. The type must be just an integer
  * TOTAL_TIME
    1. This is the total time in seconds that you want the program to run.
    2. The type must also be an integer

<hr>
Once this is done, you are all set. As long as the dependencies are installed, you should be able to run it just nicely.

## Additional Instructions
  This script will collect the online user count of the given subreddit you provide, and store the data in a csv file. You will notice it'll create file in this directory *titled data.csv*  
  In this file you will see data in the form of
  ~~~~
  248,21-33-03
  249,21-33-14
  249,21-33-24
  249,21-33-35
  ~~~~
  It includes the time that the data was collected at, and the online user count at that time.
<hr>

## Libraries Used
active_user_bot.py
```
praw
time
csv
datetime
matplotlib.pyplot
```

## Future Features
<hr>
  * Predict the best time to post something for maximum view potential.
  * Two separate files, one for graphing and one for api calling.
  * Really anything that can make it better, I will try to do. I am open to any suggestions if you would like to help me.

## Special Thanks
  * [r/gatech](https://www.reddit.com/r/gatech/ "Subreddit for Georgia Tech Students")
  * [r/python](https://www.reddit.com/r/Python/ "Subreddit for python users")
  * https://github.com/TinyQubit/RedditBot_OnlineUsers - For .md help and how to format graph. Litaraly coded the whole thing by myself and then searched to see if someone else had done won and walah, one ten times better than mine.
