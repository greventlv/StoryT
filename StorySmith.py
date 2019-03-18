# Dynamically construction sentences/paragraphs to help stimulate writing

#name = raw_input('What is your name?\n')
#print 'Hi, %s.' % name
#friends = ['john', 'pat', 'gary', 'michael']
#for i, name in enumerate(friends):
#    print "iteration {iteration} is {name}".format(iteration=i, name=name)

import win32com.client
import random
#print random.randint(0, 3)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

name = ['john', 'pat', 'gary', 'michael']
verb = ['gazes', 'runs', 'lays about', 'introspects']
noun = ['weather', 'state of the world', 'insects', 'Buddha']

name1 = random.choice(name)
verb1 = random.choice(verb)
noun1 = random.choice(noun)

print  (name1 + ' ' + verb1 + ' outside and thinks about the ' + noun1 + '.')
speaker.Speak(name1 + ' ' + verb1 + ' outside and thinks about the ' + noun1 + '.')
