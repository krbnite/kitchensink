This bot is based on the tutorial at [apps.worldwritable.com](https://apps.worldwritable.com/tutorials/chatbot/).

Objective: To motivate design and engineering challenges of conversational bots.

## Bot Boundaries
For any bot, two fundamental design questions should be answered first:
* What should this bot be expected to understand?
* What tone, vocabulary, and personality do you hope this bot to portray?

### Domain of Expertise
This bot is going to answer questions about coffee, fishing, hunting, whether or not
something is gluten free, ...

### Personality
A rule-of-thumb is to not personify your bot b/c it can be insulting... But, uh, this bot
will be different: it will speak like a hillbilly -- based on quotes from my dad.  
Is my dad a hillbilly?  Good question.  He is a fisherman extraordinaire and legendary
deerslayer.  He likes to smoke and drink coffee all day long.  Coffee does not go bad:
a cup left in the garage yesterday is a stroke of good luck today!  Most importantly,
my dad says some funny-ass shit, to put it technically. Of course, this bot is going
to exaggerate it to the extreme.  But just know: this is all for fun. 

> So, if it sounds sarcastic, don't take it seriously.
> If it sounds dangerous,
> Do not try this at home or at all.
> And if it offends you, just don't listen to it.

## Simple Bot
This bot is completely stateless... So, it won't really remember what you said.  

## High-Level NLP Library
We will be using [TextBlob](http://textblob.readthedocs.io/en/dev/), which wraps over the
[NLTK](http://www.nltk.org/) library.



