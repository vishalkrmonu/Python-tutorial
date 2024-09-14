print("hello world")

print('''The last days of the summer: bright and clear
    Shines the warm sun down on the quiet land,
Where corn-fields, thick and heavy in the ear,
    Are slowly ripening for the laborer’s hand;
Seed-time and harvest — since the bow was set,
Not vainly has man hoped your coming yet!''')



import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()



import os
# Specify the directory you want to list
directory = "/Python tutorial"  # Change this to your desired path


    # List all files and directories in the specified path
contents = os.listdir(directory)
print(f"Contents of '{directory}':")
for item in contents:
        print(item)

