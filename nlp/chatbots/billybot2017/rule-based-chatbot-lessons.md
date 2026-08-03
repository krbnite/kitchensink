# Rule-Based Chatbot Lessons

BillyBot is not an impressive chatbot: it is a testament to why chatbots are hard.

BillyBot is useful because it shows how quickly setting out to create a simple chatbot gets complicated -- or, in other words:
there is no such thing as a "good" simple chatbot!

The original goal was playful: make a small stateless bot with a distinctive voice. The implementation approach was traditional 
for the time (mid 2017): use TextBlob/NLTK to parse the user's sentence, extract a few grammatical features, and choose a 
rule/template-based response.

## What The Bot Tried To Do

- Normalize messy user input.
- Split text into sentences.
- Use part-of-speech tags to find pronouns, nouns, adjectives, and verbs.
- Detect greetings with a small keyword list.
- Detect comments directed at the bot.
- Construct a fallback response from the extracted grammatical pieces.
- Filter output so the bot did not emit obviously offensive words.

## Why It Got Hard

I just wanted to make a simple chatbot, and maybe iterate on it when I had time. The 
major lesson learned is that there is no way around the hard conversational design problems:

- The bot is stateless, so it cannot remember what was just said.
- The parser can produce unexpected parts-of-speech, or miss them entirely.
- Pronoun swapping is full of edge cases.
- Template responses break when the extracted words are missing or grammatically awkward.
- Random fallbacks can sound repetitive or unrelated.
- Persona is easy to overdo.
- Content filtering is more complicated than a word list.

## 2017 vs. 2026

In 2017, this kind of project taught the mechanics of a conversational pipeline:

```text
input text -> preprocessing -> parsing -> intent-ish rule -> response template -> filter -> output
```

In 2026, a local LLM chatbot moves much of that behavior into the model:

```text
input text -> chat template -> model generation -> decoding -> safety/runtime checks -> output
```

Models today are more flexible, but many of the same design questions remain:

- What should the bot know?
- What should it refuse?
- How much memory should it keep?
- What persona is useful rather than annoying?
- How does it recover when it misunderstands?
- What guardrails are deterministic?

