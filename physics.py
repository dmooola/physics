'''
This program will take user input for acurrent value. It will then use the current value squared multiplied by the resistance to find power. The output will be displayed in a chart.
'''
resistance = [12, 16, 27, 39, 56, 81]

current = []
power = []

for i in range(6):
    while True:
        user_input = input("Enter current value #{}: ".format(i + 1))
        try:
            current_value = float(user_input)
            if current_value <= 0:
                print("Enter a number greater than 0.")
            else:
                current.append(current_value)
                break
        except ValueError:
            print("Enter a number.")

for i in range(6):
    power.append((current[i] ** 2) * resistance[i])

total_resistance = sum(resistance)

print("{:<10} {:<10} {:<10}".format("Resistance:", "Current:", "Power:"))
print("-" * 30)
total_current = total_power = 0
for i in range(6):
    print("{:<10} {:<10.2f} {:<10.2f}".format(resistance[i], current[i], power[i]))
    total_current += current[i]
    total_power += power[i]

print("-" * 30)
print("{:<10} {:<10.2f} {:<10.2f}".format("Total:", total_current, total_power))
print("{:<10} {:<10}".format("Resistance", total_resistance))
