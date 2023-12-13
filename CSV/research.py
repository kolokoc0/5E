with open('WHO-COVID-19-global-data.csv') as file:
    file = file.readlines()
new_file = ""
def own_percentage(country):
    count = 0
    digits = {str(i):0 for i in range(1,10)}
    exp_values = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]
    chi_square= []
    chi_val = 15.51 #this is the value in chi square distribution table with 8 degrees of freedom and probability of large x squared value 0.05
    for line in file:
        if country in line:
            line = line.strip().split(",")
            digit = line[-2][0]
            if digit in digits:
                count +=1
                digits[digit] = digits.get(digit,0)+1
    for key in digits:
        print(f'{key} - {digits[key]/count*100:.2f}%')
        obs = float("{:.2f}".format(digits[key]/count*100))
        chi_square.append(((obs-exp_values[int(key)-1])**2)/exp_values[int(key)-1])
        print(sum(chi_square))
    if sum(chi_square)<=chi_val:
        print('Uninfluenced')
    else:
        print('Influenced')

own_percentage("Egypt")





