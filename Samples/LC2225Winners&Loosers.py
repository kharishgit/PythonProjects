# You are given an integer array matches where matches[i] = [winneri, loseri] indicates
# that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
#
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]


from collections import Counter
matches = [[2,3],[1,3],[5,4],[6,4]]
winners=[]
losers=[]
win=[]
res = []
for lst in matches:
    winners.append(lst[0])
    losers.append(lst[1])
for i in winners:
    if not i in losers:
        win.append(i)
chk=set(win)
print(sorted(list(chk)))
cnt = Counter(losers)
oneLoose=list(item for item in cnt if cnt[item]==1 )
print(sorted(oneLoose))






