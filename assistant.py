import pyttsx3
import random
import speech_recognition  as sr
import datetime
import wikipedia
import webbrowser
import os, shutil
from pytube import YouTube
import speedtest as st
import smtplib
import pywhatkit


# sapi5 (Microsoft developed speech API) Voice in Windows, nss on Mac OS, espeak on every other platform
engine = pyttsx3.init("sapi5") # Helps in synthesis and recognition of voice
voices = engine.getProperty('voices') # getting details of current voice

# Printing a list of voice input devices
print("List of Microphones Available:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print('Microphone with name "{1}" found for `Microphone(device_index={0})`'.format(index, name))

# Voice id helps us to select different voices
engine.setProperty('voice', voices[1].id) # voice[0].id (Male voice) is used to declare the output voice language (In this case set to English)
# print("Communication language: ", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.

import datetime
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Mahendra Sai!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mahendra Sai!")
    else:
        speak("Good Evening Mahendra Sai!")
    
    speak("I am your Personal Assistance. Please tell me how may I help you!!!")

def takeCommand():
    """
    It takes microphone input from user and returns string output
    """
    r = sr.Recognizer() # Create a recognizer object
    my_mic = sr.Microphone(device_index=1)
    # Using a microphone as the audio source (can also use audio file as the audio source)
    with my_mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) # reduce noise from the input
        # r.pause_threshold = 1 # Seconds of non speaking audio before a phase is considered complete
        audio = r.listen(source, timeout=2)
        # take audio from the user
    
    try:
        print( "Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "None"
    return query

"""
Creating Dictionary to maintain emails
to send emails allow less secure apps & to login extract the details from the text file instead of displaying in the code for security concerns
"""

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587) # specifying the port number
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close() 

# Phone Book Dictionary
phoneNumberSet = {
    "mahendra": "+91 8297449455",
    "kalyan": "+91 9177195923",
    "ram" : "+91 9059625169",
    "surya" : "+91 9124005582",
    "gopi": "+91 9515820345",
    "bittu" : "+91 8291339557",
    "daddy" : "+91 8522089199",
    "mummy" : "+91 8309507258",
}

def file_manager(file_source_dir, file_destination_dir):
    source_dir = file_source_dir
    destination_dir = file_destination_dir
    deleteFiles = []

    file_names = os.listdir(source_dir)
    print("Files List", file_names)

    """
    Creating Folders if not present
    """
    # checking if the directory Audios exist or not.
    if not os.path.exists(source_dir + "\\Audios"):
        # if the Audios directory is not present then create it.
        os.makedirs(source_dir + "\\Audios")

    if not os.path.exists(source_dir + "\\Videos"):
        os.makedirs(source_dir + "\\Videos")
    
    if not os.path.exists(source_dir + "\\Zip"):
        os.makedirs(source_dir + "\\Zip")

    if not os.path.exists(source_dir + "\\Pictures"):
        os.makedirs(source_dir + "\\Pictures")
    
    if not os.path.exists(source_dir + "\\Documents"):
        os.makedirs(source_dir + "\\Documents")


    """
    Transferring files to respective folders based on the file extension
    """
    for file_name in file_names:
        if os.path.join(source_dir, file_name).endswith('.mp3'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Audios'))

        if os.path.join(source_dir, file_name).endswith('.mp4'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Videos'))

        if os.path.join(source_dir, file_name).endswith('.zip'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Zip'))

        if os.path.join(source_dir, file_name).endswith('.jpg'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Pictures'))

        if os.path.join(source_dir, file_name).endswith('.png'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Pictures'))

        if os.path.join(source_dir, file_name).endswith('.jpeg'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Pictures'))

        if os.path.join(source_dir, file_name).endswith('.pdf'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Documents'))

        if os.path.join(source_dir, file_name).endswith('.docx'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Documents'))
        
        if os.path.join(source_dir, file_name).endswith('.txt'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Documents'))
        
        if os.path.join(source_dir, file_name).endswith('.pptx'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Documents'))

        if os.path.join(source_dir, file_name).endswith('.exe'):
            deleteFiles.append(file_name)
        
        if os.path.join(source_dir, file_name).endswith('.msi'):
            deleteFiles.append(file_name)
        
        if os.path.join(source_dir, file_name).endswith('.iso'):
            deleteFiles.append(file_name)

    print("Delete Files", deleteFiles)
    for deleteFile in deleteFiles:
        os.remove(source_dir + "\\"+ deleteFile)
        # os.unlink(source_dir + "\\" + deleteFile)
    
    return

if __name__ == "__main__":
    wishMe()
    while True:
        print("\n\n")
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            print(query)
            results = wikipedia.summary(query, auto_suggest=False, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")     

        elif 'play music' in query:
            music_dir = 'C:\\Users\\pogo\\Music'
            songs = os.listdir(music_dir)
            song = random.randint(0, len(songs))
            print("Playing Song:", songs[song])
            try:
                os.startfile(os.path.join(music_dir, songs[0]))
            # handling the FileNotFoundError exception
            except FileNotFoundError as not_found:
                print("The directory was not found and handled exceptions successfully." )
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\I587835\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'email to mahendra' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mahendrayouremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, Couldn't send the email")

        elif 'download youtube video' in query:
            speak("Enter the link of the video in terminal")
            link = input("Enter the link of the video you want to download: ")
            print("Link Entered: ", link)
            try:
                video_download = YouTube(link)
                print("Video Title:", video_download.title)
                video_download.streams.get_highest_resolution().download()
                speak("Video Downloaded Successfully")
                # Video downloaded in the folder where the current code is present
            except Exception as e:
                print(e)
                speak("Please Re-Check the URL Provided")

        elif 'speed test' in query:
            # Internet Speed Tester
            speak("Performing Speed Test")

            # Set Best Server
            server = st.Speedtest()

            # Test Download Speed
            down = server.download()
            print("Download Speed: ", down, "Mbps")
            speak(f"Download Speed: {down} Mbps")

            # Test Upload Speed
            up = server.upload()
            print("Upload Speed: ", up, "Mbps")
            speak(f"Upload Speed: {up} Mbps")

            # Test Ping
            server = server.results.ping
            print("Ping: ", server, "ms")
            speak(f"Ping: {server} ms")
        
        elif 'whatsapp' in query:
            flag, names = False, []

            # Need to optimize the code here as all the values are hardcoded
            
            while(1):
                for key in phoneNumberSet.keys():
                    if key in query:
                        flag = True
                        names.append(key)
                    
                if flag == False:
                    speak("Person not found in phone book! Try speaking again")
                    query = takeCommand().lower()
                    print("Person log search", query)
                else:
                    break

            """
            while flag == False:
                if "kalyan" in query:
                    flag = True
                    names.append("kalyan")
                if "surya" in query:
                    flag = True
                    names.append("surya")
                if "gopi" in query:
                    flag = True
                    names.append("gopi")
                if "ram" in query:
                    flag = True
                    names.append("ram")

                if flag == False:
                    speak("Person not found in phone book! Try speaking again")
                    query = takeCommand().lower()
                    print("Person log search", query)
            """
            
            """
            # For Scheduling the messages, Fetch the current time and add 2-3 minutes to it and then pass it to the sendwhatmsg function
            current_time = datetime.datetime.now()
            x_minutes = 3 # we need to provide at least 2-3 minutes future time from the current time while running the script, because if you will set the time 1-2 minutes from the current time, then the module will give an error.
            schedule_datetime = current_time + datetime.timedelta(minutes=x_minutes)
            hour, minutes = schedule_datetime.hour, schedule_datetime.minute
            """
            speak("What message should I pass on?")
            message = takeCommand()

            for i in range(len(names)):
                personName, personNumber = names[i], phoneNumberSet[names[i]]
                pywhatkit.sendwhatmsg_instantly( phone_no=phoneNumberSet[names[i]],  message=message,)
                # pywhatkit.sendwhatmsg(personNumber, message, hour, minutes) # This will send the message at the specified time
            speak("Message sent successfully")
        elif 'organise files' in query:
            file_manager('C:\\Users\\pogo\\Downloads', 'C:\\Users\\pogo\\Downloads') # Source and Destination directory
            speak("Files organized successfully")
        elif 'thank you' in query:
            break

    
    # End of listening
    speak("Thank you sir! Have a nice Day")

"""
Can create chatbots, scikit learn, tensorflow can be included to
"""
