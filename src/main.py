from send_email import send_email
from check_to_do_list import check_to_do_list

print("Good morning")
print("Checking if there is any pending task...")
df_tasks_to_remind = check_to_do_list()

if df_tasks_to_remind.shape[0] > 0:
    print("Pending tasks found.")
    print("Preparing an email...")
    if send_email(df_tasks_to_remind):
        print("Email sent")
        print("Have a nice day!")
    else:
        print("Something wrong happened")
else:
    print("No pending tasks found.")
    print("Have a nice day!")

