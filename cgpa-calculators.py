n = int(input("Enter number of Subjects:"))

total_credits = 0
weighed_sum = 0

for i in range(1, n+1):
    credit = float(input(f"Enter credits for Subjects {i}:"))
    grade_points = float(input(f"Enter grade points for Subjects {i}:"))
    
    weighed_sum +=grade_points * credit
    total_credits += credit
    
cgpa = weighed_sum / total_credits

print("\nYour cgpa is:", round(cgpa , 28))
