#define class
class chatbot:
    #constructor
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loogedin = False
        #call the menu function as well within the constructor
        self.menu()
    
    #function -> provide input options for user
    def menu(self):
        user_input = input("""Welcome to Chatbot !! How would you like to proceed?
                           1. Enter 1 to Sign Up
                           2. ENter 2 to Sign In
                           3. Enter 3 to Write a Post
                           4. Enter 4 to Message a Friend
                           5. Press any other key to Exit
                           """)
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

#create object of the chatbot class
chatbot_obj = chatbot()
        
