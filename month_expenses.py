#A program that shows expenses of user in a particular month
month= input("NAME OF THE CURRENT MONTH:")
money= int(input("ENTER MONEY FOR THIS MONTH:"))
expenses ={
    "food" : int(input("ENTER ESTIMATED MONEY TO SPENT FOR FOOD:")),
    "travel":int(input("ENTER ESTIMATED MONEY TO SPENT FOR TRAVEL:")),
    "shopping":int(input("ENTER ESTIMATED MONEY TO SPENT FOR SHOPPING:")),
    "other":int(input("ENTER ESTIMATED MONEY TO SPENT FOR MISCELLANEOUS:"))
}
total = sum(expenses.values())
save = (money-total)
print()
print("TOTAL MONEY FOR" , month,":" ,money)
print("TOTAL MONEY SPEND FOR" ,month, ":", total)
print("TOTAL MONEY SAVED:",save)
