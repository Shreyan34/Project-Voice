from win32com.client import Dispatch

def speak(str):
    voice = Dispatch(("SAPI.SpVoice"))
    voice.Speak(str)

def deaf_and_mute_interact():
    while True:
        ask = input("Enter your statement: (type END to quit) \n")
        print(f"Statement: {ask}")
        if ask == 'END':
            break
        else:
            reply = input("Enter your reply: (type END to quit)\n")
            if reply == 'END':
                break
            else:
                print(f"Reply: {reply}")
                speak(reply)


def mute_interact():
    while True:
        ask = input("Enter your statement: (type END to quit) \n")
        print(f"Statement: {ask}")
        if ask == 'END':
            break
        else:
            speak(ask)


if __name__ == "__main__":
    option = input("For Deaf and Mute, press 1; for Mute, press 2: \n")
    if option == '1':
        deaf_and_mute_interact()
    elif option == '2':
        mute_interact()
    else:
        print("Oops! Something went wrong, please try again!")
