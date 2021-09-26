from win32com.client import Dispatch

def speak(str):
    '''
        This function takes a string as a parameter and then speaks it
    '''
    voice = Dispatch(("SAPI.SpVoice")) # calling the Windows SAPI API for voice (depends upon different computer systems)
    voice.Speak(str) # the voice speaks the string which the function takes as the parameter

def deaf_and_mute_interact():
    '''
        This is the function that helps for Deaf and Mute people to interact
    '''
    while True:
        ask = input("Enter your statement: (type END to quit) \n") # asking for the statement
        print(f"Statement: {ask}") # printing the statement
        if ask == 'END': # if the statement is END then the loop breaks
            break
        else: # the else part
            reply = input("Enter your reply: (type END to quit)\n") # asking for the reply
            if reply == 'END': # if reply is END then the loop breaks
                break
            else: # the else part
                print(f"Reply: {reply}") # printing the reply
                speak(reply) # using the speak function to speak the reply


def mute_interact():
    '''
        This is the function that helps for Mute people to interact
    '''
    while True:
        ask = input("Enter your statement: (type END to quit) \n") # asking for statement
        print(f"Statement: {ask}") # printing the statement
        if ask == 'END': # if the statement is END then the loop breaks
            break
        else: # the else part
            speak(ask) # the statement is spoken by the computer


if __name__ == "__main__": # the main method
    option = input("For Deaf and Mute, press 1; for Mute, press 2: \n") # asks for the option
    if option == '1': # if option is 1 then the deaf_and_mute_interact function is called
        deaf_and_mute_interact()
    elif option == '2': # else if option is 2 then the mute_interact function is called
        mute_interact()
    else: # if by mistake, something else is typed, then an error message is printed
        print("Oops! Something went wrong, please try again!")
