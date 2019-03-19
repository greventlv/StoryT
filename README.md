# StoryT
Dynamically construction sentences/paragraphs to help stimulate writing and a create your own story mode
StoryTime: User creates story by inutting custom nouns, verbs, etc
StorySmith: AI composes sentences with data

# Requirements
Made in Python 3.7.2

Windows: Don't forget to "pip install pywin32" in administrator cmd line in windows for t2s, to test t2s write:
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Qaplah!")

Linux: pip install pyttsx3
import pyttsx
engine = pyttsx.init()
engine.say('Qaplah!')
engine.runAndWait()

# Todo
Need to make menu to choose the mode between two scripts
Need to add module to take in census data on favored words from MBTI groups and associate types with spawn data to create bias spoken word statements (*NT*: Conceptual, Intrinsic, emergent. *SF*: Loyal, Stellar, traditional)
Need to create survery for harvesting of such data from MBTI groups
