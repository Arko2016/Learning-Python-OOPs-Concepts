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
            self.writepost()
        elif user_input == "4":
            self.sendmsg()
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
                #this is changed to True if user is able to log in successfully
                self.loggedin = True
            else:
                print("Please input correct sign-in credentials")
        
        print("\n")
        #call the menu function for next user input
        self.menu()

    #create a post
    def writepost(self):
        if self.loggedin == True:
            txt = input("Enter your post here: ")
            print(f"Following post has been posted:\n{txt}")
        else:
            print("Please sign in first using option 2 from main menu")
        
        print("\n")
        #call the menu function for next user input
        self.menu()
    
    #message a friend
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter message for friend: ")
            frnd = input("Enter name of friend to message: ")
            print(f"Your sent the below message to {frnd}:\n{txt}")
        else:
            print("Please sign in first using option 2 from main menu")
        
        print("\n")
        #call the menu function for next user input
        self.menu()


#create object of the chatbot class
chatbot_obj = chatbot()
        
