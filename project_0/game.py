import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input("Input number"))
    if predict_number > number:
        print("smaller!")
    elif predict_number < number:
        print("bigger!")
    else:
        print(f"Number = {number}, count = {count}")
        break 