import time

length = int(input("Enter the length of the countdown in seconds: "))

while length:
    mins, secs = divmod(length, 60)
    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    length -= 1

print("Fire in the hole!")
