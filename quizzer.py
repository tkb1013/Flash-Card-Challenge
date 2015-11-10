import random
import argparse
import sys  

#prompts the user to enter file name if missing
if len (sys.argv) != 2 :
    print "Please supply the file name."
    sys.exit(0)
    
# argument parsing for file name
parser = argparse.ArgumentParser()
parser.add_argument("FILE", help="file that contains questions and answers")
args = parser.parse_args()
f = args.FILE

mynewhandle = open(f, "r")

wordList = mynewhandle.readlines()   # Try to read next line

q_a = dict(line.strip().split(',') for line in wordList) #dictionary: questions = key , answers = value


# user answers questions until they enter "exit"
while 1<2:
    question = random.choice(q_a.keys())
    print "%s?" % (question),
    answer = raw_input()
    
    #the user's answer is case-insensitive
    if(answer.lower().strip() == q_a[question].lower()):
        print "Correct! Nice job."
    elif(answer.lower().strip() == "exit"):
        print "Goodbye"
        break
    else:
        print "Incorrect. The correct answer is %s." % (q_a[question])
        
        
#close file resources
mynewhandle.close()
