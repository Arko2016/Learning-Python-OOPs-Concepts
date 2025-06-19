#define class
class chatbot:
    #constructor
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        #call the menu function as well within the constructor
        self.menu()
    
    #provide input options for user
    def menu(self):
        user_input = input("""Welcome to Chatbot !! How would you like to proceed?
                           1. Enter 1 to Sign Up
                           2. Enter 2 to Sign In
                           3. Enter 3 to Write a Post
                           4. Enter 4 to Message a Friend
                           5. Press any other key to Exit
                           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    #get signup details from user
    def signup(self):
        email = input("enter your email address: ")
        pwd = input("enter your password: ")
        #assign the above inputs to class attributes username and password
        self.username = email
        self.password = pwd
        print("You have successfully signed up")
        
        print("\n")
        #call the menu function for next user input
        self.menu()
    
    #sign in the user to account
    def signin(self):
        #check if user has an account
        if self.username == "" and self.password == "":
            print("Please sign up first by pressing 1 in main menu")
        else:
            #get username and password for signing in to account
            email = input("enter your email address: ")
            pwd = input("enter your password: ")
            #check if user enter correct sign in details
            if self.username == email and self.password == pwd:
                print("You have logged in successfully")
                #update class attribute loggedin variable
                self.loggedin = True
            else:
                print("Please input correct sign-in credentials")
        
        print("\n")
        #call the menu function for next user input
        self.menu()

#create object of the chatbot class
chatbot_obj = chatbot()
        
