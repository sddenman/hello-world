import time

print("Hello, World!")
print("No doubt about it. This enhancement is just epic!")
time.sleep(1)
print("Gonna count from 1 to 10.")
time.sleep(1)
print("Buckle up!")
time.sleep(1)

print("Here we go... ", end='', flush=True)
for i in range(1,11):
    time.sleep(.5)
    print(i, " ", end='', flush=True)
time.sleep(.5)
print("Done!")