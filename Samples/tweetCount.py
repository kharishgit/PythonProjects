import pandas as pd
from collections import OrderedDict
total = {}
testCase = int(input())  # Getting No of Test Case From User
for i in range(testCase):
    subSet = {}
    tweetList = []
    nosEntries = int(input())  # Getting entries in each test cases
    for j in range(nosEntries):
        tweets = input()  # Getting Tweets from user in Specified Format
        tweetList.append(tweets.split()[0])  # Avoiding the data after Space
    count = pd.Series(tweetList).value_counts()  # To get each Tweet Owner and corresponding Tweet Count
    totalCount = dict(count)    # Type Conversion into Dictionary
    maxVal = max(totalCount.values())  # Get max value of tweet Counts
    for name, key in totalCount.items():
        if key == maxVal:
            subSet[name] = key  # Appending all the values to a dictionary with Tweeter name with max tweets
    total[i] = subSet  # Appending the previous dictionary to new dict for all case sets
for name, nos in total.items():
    res = OrderedDict(sorted(nos.items())) # Sorting Dictionary in Alphabetic Order
    for key, val in res.items():
        print(key, val)
