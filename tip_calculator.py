print("Welcome to the tip calculator")

total_bill = int(input("What was the Total bill?:$"))
tip_amt = int(input("How much would you like to tip?:$"))      
split_bill = int(input("How many people do you want to split the bill?:"))

bill_pay = round((total_bill + tip_amt)/split_bill)
print(f"Each person will have to pay ${bill_pay}")
                
                       