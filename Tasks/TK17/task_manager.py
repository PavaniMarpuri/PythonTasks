# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password

# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


def reg_user():
    # - Request input of a new username
    new_username = input("New Username: ")
    # check if the username is already exists
    while new_username in username_password.keys():
        new_username = input("User already exist. Please enter a new username for user registration ")
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            data = []
            for k in username_password:
                data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


def write_to_file(list_of_tasks):
    # writing task data to the file
    try:
        with open("tasks.txt", "w") as file:
            task_list_to_write = []
            for t in list_of_tasks:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            file.write("\n".join(task_list_to_write))
        print("Task successfully added/Modified.")
    except FileNotFoundError as e:
        print("Your text file doesnt exists ")


def add_task():

    task_username = input("Name of person assigned to task: ")

    while task_username not in username_password.keys():
        task_username = input("User does not exist. Please enter a valid username for task assignment")
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)

    write_to_file(task_list)


def view_all():

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def edit_task_status(task_to_modify):

    task_status = input("Please enter the task status as Yes/No ").lower()

    while task_status not in ("yes", "no"):
        edit_task_status(task_to_modify)

    task_list.remove(task_to_modify)
    task_to_modify["completed"] = True if task_status == "yes" else False
    task_list.append(task_to_modify)

    write_to_file(task_list)


def edit_task(task_to_edit):

    if not task_to_edit["completed"]:
        while True:
            assignee_due_date = input("""Please enter your choice from below options 
                    a.  Edit Assignee
                    dd. Edit Due Date
                    e.  Go to Main menu """).lower()

            if assignee_due_date == "a":
                task_list.remove(task_to_edit)
                task_to_edit["username"] = input("Please enter name of the assignee ")
                task_to_edit["assigned_date"] = date.today()
                task_list.append(task_to_edit)
                write_to_file(task_list)
            elif assignee_due_date == "dd":
                while True:
                    try:
                        task_due_date = input("Please Enter Due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified ")
                task_list.remove(task_to_edit)
                task_to_edit["due_date"] = due_date_time
                task_to_edit["assigned_date"] = date.today()
                task_list.append(task_to_edit)
                write_to_file(task_list)
            elif assignee_due_date == 'e':
                break
    else:
        print("The task you have selected to edit is already Completed ")


def user_task_choice(tasks):

    try:
        task_choice = int(input("Please Enter task number to edit/modify a task or enter '-1' to go to main menu "))
    except ValueError as e:
        print("You have entered wrong input type")
        task_choice = int(input("Please Enter task number to edit/modify a task or enter '-1' to go to main menu "))

    if task_choice > len(tasks):
        print("You have entered wrong task number")
        user_task_choice(tasks)
    elif task_choice != -1 and task_choice <= len(tasks):
        selected_task = tasks[task_choice]
        edit_modify_choice = input('''Please select one of the below two options
        mc - To mark task as complete 
        mo - To edit a task ''').lower()
        if edit_modify_choice == 'mc':
            edit_task_status(selected_task)
        elif edit_modify_choice == 'mo':
            edit_task(selected_task)
        else:
            print("You have made a wrong choice, Please Try again")


def view_mine():

    count = 0
    user_tasks = {}

    for t in task_list:
        if t['username'] == curr_user:
            count += 1
            disp_str = f"{count} \t Task: \t\t {t['title']}\n"
            disp_str += f"\t Assigned to: \t {t['username']}\n"
            disp_str += f"\t Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"\t Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"\t Task Description: \t {t['description']}\n"
            print(disp_str)
            user_tasks[count] = t

    print(f"User tasks: {user_tasks}")

    user_task_choice(user_tasks)


def task_reports(today):

    total_tasks = len(task_list)
    completed_tasks, incomplete_perc, over_due_tasks, incomplete_tasks, overdue_perc = 0, 0, 0, 0, 0

    for t in task_list:
        if t['completed']:
            completed_tasks += 1
        if (not t['completed']) and (t["due_date"].strftime(DATETIME_STRING_FORMAT) < today):
            over_due_tasks += 1

    if not total_tasks == 0:
        incomplete_tasks = total_tasks - completed_tasks
        incomplete_perc = (incomplete_tasks / total_tasks) * 100
        overdue_perc = (over_due_tasks / total_tasks) * 100
    try:
        with open("task_overview.txt", "w") as file:
            file.writelines("The total number of tasks that have been generated "
                            f"""and tracked using the task_manager.py : {total_tasks}
The total number of completed tasks : {completed_tasks}
The total number of uncompleted tasks : {incomplete_tasks}
The total number of tasks that haven’t been completed and that are overdue : {over_due_tasks}
The percentage of tasks that are incomplete : {incomplete_perc}
The percentage of tasks that are overdue : {overdue_perc}""")
    except FileNotFoundError as e:
        print("Your text file doesnt exists ")


def user_reports(today):
    
    total_users = len(username_password)
    total_tasks = len(task_list)

    try:
        with open("user_overview.txt", "w") as file:
            file.writelines(f"The total number of users registered with task_manager.py : {total_users}"
                            "\nThe total number of tasks that have been generated "
                            f"and tracked using the task_manager.py : {total_tasks}")
    except FileNotFoundError as e:
        print("Your text file doesnt exists ")

    for user_name in username_password:

        total_user_tasks, completed_tasks_user, over_due_tasks_user, user_task_per, user_complete_task_per = 0, 0, 0, 0, 0
        incomplete_perc_user, overdue_perc_user = 0, 0

        for t in task_list:
            if user_name == t["username"]:
                total_user_tasks += 1
                if t['completed']:
                    completed_tasks_user += 1
                if (not t['completed']) and (t["due_date"].strftime(DATETIME_STRING_FORMAT) < today):
                    over_due_tasks_user += 1
        if (not total_user_tasks == 0) and (not total_tasks == 0):

            user_task_per = (total_user_tasks / total_tasks) * 100
            user_complete_task_per = (completed_tasks_user / total_user_tasks) * 100
            incomplete_tasks_user = total_user_tasks - completed_tasks_user
            incomplete_perc_user = (incomplete_tasks_user / total_user_tasks) * 100
            overdue_perc_user = (over_due_tasks_user / total_user_tasks) * 100

        try:
            with open("user_overview.txt", "a") as file:
                file.writelines(f"""\nUser Name : {user_name}
\t\tThe total number of tasks assigned to that user : {total_user_tasks}
\t\tThe percentage of the total number of tasks that have been assigned to that user :{user_task_per}
\t\tThe percentage of the tasks assigned to that user that have been completed : {user_complete_task_per}
\t\tThe percentage of the tasks assigned to that user that must still be completed : {incomplete_perc_user}
\t\tThe percentage of the tasks assigned to that user that has not """
                                f"yet been completed and are overdue : {overdue_perc_user}")
        except FileNotFoundError as e:
            print("Your text file doesnt exists ")


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        reg_user()

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        add_task()

    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all()

    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine()

    elif menu == 'gr' and curr_user == 'admin':
        '''If the user is an admin they can generate reports about number of users
                    and tasks.
        '''
        date_today = date.today().strftime(DATETIME_STRING_FORMAT)

        task_reports(date_today)
        user_reports(date_today)

    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
