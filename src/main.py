import pandas as pd

from send_email import send_email
from check_to_do_list import check_to_do_list

print("Good morning")
print("Checking if there is any pending task...")
df_to_do_list = check_to_do_list()

if df_to_do_list.shape[0] > 0:
    print("Pending tasks found.")
    print("Preparing an email...")
    send_email(df_to_do_list) 
else:
    print("No pending tasks found.")
    print("Have a nice day!")

