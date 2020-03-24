def odd_number(x):
    result = []
    for ele in range(x):
        result.append(2*ele+1) # 2x+1
    return result

# Number of samples calculated. Precession increases with increase in value
elements = odd_number(200) 
# Leibniz formula
odd_position, even_position, result = 0, 0, 0
for x in range(len(elements)):
    if x % 2 == 0:
        odd_position = odd_position + (1/elements[x])
    else:
        even_position = even_position + (1/elements[x])
result = (4*(odd_position-even_position))
pre = int(input("Enter the precession value: "))
print(round(result,pre))