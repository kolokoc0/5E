with open('WHO-COVID-19-global-data.csv') as file:
    file = file.readlines()
count = 0
new_file = ""
digits = {str(i):0 for i in range(1,10)}
for line in file:
    if 'Philippines' in line:
        line = line.strip().split(",")
        digit = line[-2][0]
        if digit in digits:
            count +=1
            digits[digit] = digits.get(digit,0)+1
        else:
            count -=1

for key in digits:
    print(f'{key} - {digits[key]/count*100:.2f}%')





print(digits)

