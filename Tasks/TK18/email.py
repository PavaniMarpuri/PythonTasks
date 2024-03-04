# Creating a class called Email
class Email:
    # Class variable with default value
    has_been_read = False

    # Parameterized Constructor
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Class method to change the class variable value
    def mark_as_read(self):
        self.has_been_read = True


# Declaring an empty list
inbox = []


# Function to create Email object and add to list and populate the list items to the user
def populate_inbox():

    email_obj1 = Email("andry@gmail.com", "andry's email subject line",
                       "This mail is used to populate andry's inbox with email")
    inbox.append(email_obj1)

    email_obj2 = Email("jhon@gmail.com", "jhon's email subject line",
                       "This mail is used to populate jhon's inbox with email")
    inbox.append(email_obj2)

    email_obj3 = Email("jessy@gmail.com", "jessy's email subject line",
                       "This mail is used to populate jessy's inbox with email")
    inbox.append(email_obj3)

    print("\033[1mEMAIL INBOX \033[0m")

    for item in inbox:

        print(f"\t\033[1mEmail From\033[0m :- {item.email_address}, \033[1mSubject\033[0m :- {item.subject_line}")


# Function to populate the subject line of unread emails with count to the user
def list_emails():

    for count, email_obj in enumerate(inbox, 0):

        if not email_obj.has_been_read:

            print(f"{count}\t{email_obj.subject_line}")


# Function to show the selected email to the user and mark the email as read.
def read_email(choice):

    for count, email_obj in enumerate(inbox, 0):

        if count == choice:

            print(f"Subject Line:- {email_obj.subject_line}")
            print(f"\tEmail Content:- {email_obj.email_content}")

            Email.mark_as_read(email_obj)

            # Assigning selected email object to temporary object
            temp_obj = email_obj
            # Removing selected object from inbox list and adding temporary object to the list
            """
                This is to show the sequential count again when we select option 1 from main menu
            """
            inbox.remove(email_obj)
            inbox.append(temp_obj)

            print(f"\nEmail from {email_obj.email_address} marked as read.\n")


# Calling function to populate inbox items
populate_inbox()

# Displaying user menu
while True:

    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:

        list_emails()
        # taking user choice from the displayed list of emails
        email_choice = int(input("Please enter the email number that you wanted to read "))

        if email_choice < len(inbox):

            read_email(email_choice)

        else:
            print("You have entered wrong choice. ")

    elif user_choice == 2:

        for item in inbox:

            if not item.has_been_read:

                print(f"\t\t\033[1mEmail From\033[0m :- {item.email_address}, \033[1mSubject\033[0m :- "
                      f"{item.subject_line}")

    elif user_choice == 3:

        print('Goodbye!!!')
        exit()

    else:
        print("Oops - incorrect input.")
