temperature = float(input())
if temperature >= 35.01:
    print("unknown")
elif temperature >= 26.00:
    print("Hot")
elif temperature >= 20.1:
    print("Warm")
elif temperature >= 15.00:
    print("Mild")
elif temperature >= 12.00:
    print("Cool")
elif temperature >= 5.00:
    print("Cold")
elif temperature <= 4.99:
    print("unknown")
