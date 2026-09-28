# -----------------------------------------------------------------------------------------------
# =========================================Question 13: ==========================================
# -----------------------------------------------------------------------------------------------

# 13.
# Take a number representing a day:

# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# Display Other for any other value.

day=int(input("Enter a number (1-5): "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
else:
    print("Other")