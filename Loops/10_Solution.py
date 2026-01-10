import time

Wait_time =1
max_retries =5
attempts =0

while attempts<max_retries:
    print("Attempts",attempts+1,"Wait_time",Wait_time)
    time.sleep(Wait_time)
    Wait_time *=2
    attempts+=1