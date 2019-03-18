# Dynamically construction sentences/paragraphs to help stimulate writing

#name = raw_input('What is your name?\n')
#print 'Hi, %s.' % name
#friends = ['john', 'pat', 'gary', 'michael']
#for i, name in enumerate(friends):
#    print "iteration {iteration} is {name}".format(iteration=i, name=name)

from tkinter import *
import win32com.client
import random
#print random.randint(0, 3)

master = Tk()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
###

# Button click
def randomSentence():
    name = ['John', 'Pat', 'Jessi', 'Michelle', 'Ben', 'Rosa', 'Sean', 'Mari', 'Patricio', 'Brian', 'Annie', 'Alvaro']
    verb = ['gazes', 'runs', 'lays about', 'introspects', 'plays', 'cleans', 'cuts', 'drives', 'eats', 'flies', 'reads', 'stops', 'swims', 'throws', 'trips', 'walks', 'washes', 'writes', 'admires', 'adopts', 'beats', 'buys', 'counts', 'doubts', 'discovers', 'desires', 'meditates']
    noun = ['weather', 'state of the world', 'insects', 'Buddha', 'milk', 'rice', 'snow', 'rain', 'water', 'food', 'music', 'luggage', 'President', 'orangessnail', 'spring', 'idea', 'mouth', 'sea', 'mountain', 'day', 'mice', 'pail', 'bulb', 'cemetery']

    name1 = random.choice(name)
    verb1 = random.choice(verb)
    verb2 = random.choice(verb)
    noun1 = random.choice(noun)

    print  (name1 + ' ' + verb1 + ' outside and ' + verb2 + ' the ' + noun1 + '.')
    speaker.Speak(name1 + ' ' + verb1 + ' outside and ' + verb2 + ' the ' + noun1 + '.')

# Gui

label1 = Button(master, text="Say something", command=randomSentence)
label1.pack()
