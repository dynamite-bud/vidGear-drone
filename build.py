import time

animation = "|/-\\"
idx = 0
while True:
    print("Building...",animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)