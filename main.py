import pyttsx3

if __name__ == '__main__':
    print("Welcome")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "stop":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
