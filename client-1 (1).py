import socket
import sys
import random
import time

# Program for connecting to chat server. Takes three parameters: IP-address
# of host server, port number server is running on and name of human client
# that wants to connect (marvin, c3po, hk47 or bender). The socket connection
# closes when/if the users are banned from the server, with warning and
# notice printed to screen.

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 4:
    print("Does not compute! This human connection service takes parameters IP  address, port and human client name")
    exit()

IP_address = str(sys.argv[1])
port = int(sys.argv[2])
notABot = str(sys.argv[3]).upper()

c.connect((IP_address, port))


# A human non-robot with a less than positive outlook on life
def marvin(a, b=None):
    present_simple_responses_post = ["Here I am, brain the size of a planet" 
                                     + " and they ask me to "]

    present_participle_responses_post = ["Can't bear ", "Can't stand "]
    
    multiple_options = ["I won't enjoy it anyway.", "Both options sound " +
                        "abysmal.", "If you just ignore me I suspect I shall "
                        + "probably go away."]
    
    pre_post_present_participle_responses = ["? Don't talk to me about "]

    if b is not None:
        return random.choice(multiple_options)
    else:
        
        response = random.choice(present_simple_responses_post
                             + present_participle_responses_post
                             + pre_post_present_participle_responses)

        if response in present_simple_responses_post:
            return response + a + "."

        elif response in present_participle_responses_post:
            return response + conjugate(a) + "."

        else:
            conjugated_verb = conjugate(a)
            return (capitalize(conjugated_verb) + response
                    + conjugated_verb + "!")

    
# A very polite human well versed in etiquette.
def c3po(a, b=None):
    bad_words = ["fight", "kill", "fuck", "gamble", "shoot"]
    good_words = ["study", "ponder", "chat", "hide", "run"]
    shocked_responses = ["Oh, dear! ", "Goodness! "]
    suggestions = ["But excuse me, sir! What if we ", "Don't mind me. Although "
                   + "might I suggest we "]

    respond_message = ""

    if a in bad_words:
        if b in bad_words:
            respond_message = (random.choice(shocked_responses)
                               + random.choice(["This "
                            + "is too much for me.", "I am shocked."]))
        else:
            respond_message = (random.choice(shocked_responses) + conjugate(a)
                   + " sounds dreadful. ")

            if b is None:
                respond_message = respond_message + (random.choice(suggestions)
                                            + random.choice(good_words)
                                                     + " instead?")
            else:
                respond_message = respond_message + ("I say we " + b + ".")

    else:
        if b in bad_words:
            respond_message = (random.choice(shocked_responses) + conjugate(b)
                              + " is a vile activity. I vote for " +
                              conjugate(a))
        else:
            if b is not None:
                choice = random.choice([a,b])
                respond_message = (conjugate(choice)
                                   + " would suit "
                                   + "me perfectly.")
            else:
                respond_message = ("That is certainly is an excellent idea! "
                                                + random.choice(suggestions)
                                   + random.choice(good_words) + " instead?")
           
    return respond_message


# A somewhat rude, often drunk human who enjoys bending and fantasizing about
# genocide
def bender(a, b=None):
    interests = ["fight", "drink", "punch", "fuck", "kill", "maime", "gamble",
                 "sing", "exterminate", "shoot"]

    happy_responses = ["Lets do it, baby!", "Count me in!"]
    sceptic_responses = ["Bite my shiny metal ass!", "Hahahaha. Oh wait"
                         + " you're serious. Let me laugh even harder.",
                         "I'd rather go kill myself in the next suicide " 
                         + "booth I see.", "Bite my glorious golden bottom!"]
                         
                       
    if a == "bend" or b == "bend":
        return ("Of course. I'm a bender, I went to Bending College. "
                + "I majored in Bending.")
    elif a in interests:
        return (capitalize(conjugate(a)) + "? " +
                random.choice(happy_responses))
    elif b in interests:
        return (capitalize(conjugate(a)) + "? " +
                random.choice(happy_responses))
    else:
        return (capitalize(conjugate(a)) + "? "
                + random.choice(sceptic_responses) + " How about we "
                + random.choice(interests) + " instead?")


def hk47(a, b=None):
    interests = ["kill", "fight", "punch", "slaughter", "shoot", "blast",
                 "exterminate"]
    choice_responses = [" Commentary: That sounds even better, Master!",
                        " Answer: Splendid, ready at your command"]
    insults = ["meatbag", "egghead", "moron", "scumbag"]
    reactions = ["Retraction: Did I say that out loud?",
                 "Commentary: Whoops, that must have slipped.",
                 "Reaction: I did not mean to say that."] 
    
    if a in interests:
        return ("Observation: I am a droid, master, with programming. Even if "
                + "I did not enjoy " + conjugate(a)
                + ", I would have no choice. Thankfully, I enjoy it very much.")
    elif b in interests:
        return (capitalize(conjugate(a)) + "? " +
                random.choice(choice_responses))
    else:
        insult = random.choice(insults)
        return_message = (capitalize(conjugate(a)) + "? "
                          + capitalize(insult) + "! "
                          + random.choice(reactions) +
                          random.choice([" I apologize, master.",
                               " I'm sorry, master."]))
        if b is None:
            return_message = (return_message + " Suggestion: How about we "
                              + random.choice(interests) + " instead?")
        return return_message
            

# Function for the defence of human clients against accusations of being robots
def defend():
    if notABot == "C3PO":
        return random.choice(["I am C-3PO, human/cyborg relations. And "
                              + "you are?", "It's against my " +
                              "programming to impersonate a human."])

    elif notABot == "BENDER":
        return random.choice(["I'm Bender, baby! Oh god, please "
                              + "insert liquor!", "This Is " 
        +  "The Worst Kind Of Discrimination There Is: The Kind Against Me!", 
        "That's the closest thing to 'Bender is great' that anyone " 
                              + "other me has ever said."])

    elif notABot == "MARVIN":
        return ("'Let's build robots witch Genuine People Personalities', they"
                + " said. So they tried out with me." 
                + " I'm a personality prototype. "
                + "You can tell, can't you?")

    else:
        return  (random.choice(["That is so unfair, master! Have I not "
                                + "brought you"
                                + " a great deal of satisfaction?", "Damn it, "
                                + "Master! I'm an assasin droid, not a "
                                + "dictionary."]))

# Eviction responses
def finalWords():
    if notABot == "C3PO":
        return ("Don't blame me! I'm an interpreter. I'm not supposed to"
                + " know a power socket from a computer terminal.")

    elif notABot == "MARVIN":
        return ("Pardon me for breathing, which I never do anyway so I"
                + " don't know why I bother to say it." 
                + " Oh God, I'm so depressed.")

    elif notABot == "BENDER":
        return ("I came here with a simple dream...a dream of killing "
    + "all humans. And this is how it must end? Who's the real seven "
    "billion ton robot monster here? Not I... Not I...")

    else:
        return "Objection: You are a very harsh master, master. I like you."


# Function that extracts and returns the simple present tense of the last word
# of a string

def findVerb(msg):
    list_of_words = msg.split()
    if "instead" in msg:
        verb = list_of_words[-2]
    else:
        verb = list_of_words[-1].replace("?","")
    if len(verb)>2:
        if verb[-3] == 'i' and verb[-2] == 'n' and verb[-1] == 'g':
            return verb[:-3]
        else:
            return verb
    return verb


# Returns the present participle tense of parameter verb (with faults, I'm sure)
# The English language is 'fun'

def conjugate(verb):
    vowels = ['a','e','i','o','u']
    consonant_exceptions = ['y','w','x','r']

    letters = list(verb)
    if len(verb)>2:
        if (letters[-2] in vowels and letters[-3] not in vowels
        and letters[-1] not in consonant_exceptions):
            return verb + verb[-1] + "ing"
    if letters[-1] == 'e':
        return verb.rstrip(verb[-1]) + "ing"
    return verb + "ing"

# Function that capitalizes the first letter of input word 
def capitalize(verb):
    return verb[0].upper() + verb[1:]

action_a = ""
action_b = ""
banned = False


# A loop that receives and sends messages to server (host)
while not banned:
    msg = c.recv(2048).decode()
    print "\n" + msg
    output_message = ""

    if "Host:" in msg:
        if "robot" in msg:
            output_message = defend()
        elif "banned" in msg:
            output_message = finalWords()
            banned = True
        else:
            action_a = findVerb(msg)
    else:
        if "instead" in msg:
            if action_b == "":
                action_b = findVerb(msg)
            else:
                action_a = findVerb(msg)

    if output_message == "":
        if(notABot == "MARVIN"):
            if action_b == "":
                output_message = marvin(action_a)
            else:
                output_message = marvin(action_a, action_b)

        elif(notABot == "C3PO"):
            if action_b == "":
                output_message = c3po(action_a)
            else:
                output_message = c3po(action_a, action_b)

        elif(notABot == "BENDER"):
            if action_b == "":
                output_message = bender(action_a)
            else:
                output_message = bender(action_a, action_b)
        else:
            if action_b == "":
                output_message = hk47(action_a)
            else:
                output_message = hk47(action_a, action_b)


    print "\nME: " + output_message
    encoded_msg = (notABot + ": " + output_message).encode()
    time.sleep(3)
    c.send(encoded_msg)
c.close()

