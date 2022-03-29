"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

you are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

[7,2, 5,3,1, 3]

"""


l = 0       #buy
r = len(list1) -1       #sell

for r in range(len(list1)):
	if list1[l] > list1[r] :
		l = r
	else: 
	profit = list1[r] - list1[l]
	maxprofit = max (maxprofit  - profit)
  
#===============================================


for buy_index in range(len(list1)):
	for sell_index in range(buy_index + 1, len(list1)):
		newdiff = list1[sell_index] - list1[buy_index] 
		
		diff = max (diff, newdiff)
  
  
  # https://www.youtube.com/watch?v=1pkOgXD63yU
