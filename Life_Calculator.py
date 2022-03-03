age = int( input("Enter Your age : ") )
left = int( 100 - age )
month = (left * 12)
week = (left * 52)
day =  (left * 365)

print(f"You have {day} days, {week} weeks, and {month} months, {left} year left.")
