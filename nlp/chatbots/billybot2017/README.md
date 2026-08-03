# BillyBot Legacy
BillyBot is not an impressive chatbot: it is a testament to why chatbots are hard.

BillyBot was a 2017 rule-based chatbot learning experiment. It is preserved here as a historical reference 
of my early NLP/chatbot exploration (it is not a polished chatbot implementation).

The useful lesson here is how designing a simple chatbot quickly runs into hard conversational design problems: 
intent detection, part-of-speech parsing, persona, content filtering, fallback behavior, 
and brittle edge cases.

## Historical Status

- Original work dates: July 25, 2017 (`7a88e7d`) through August 5, 2017 (`c6e2d5c`).
- Original local repo remote: `git@github.com:krbnite/BillyBot.git` (but I intend to delete that repo as I clean up my GitHub account).
- Preserved into kitchensink: August 1, 2026.

## Attribution

This project was heavily adapted from Liza Daly's Brobot sample code and chatbot tutorial:

- https://github.com/lizadaly/brobot
- https://apps.worldwritable.com/tutorials/chatbot/

The upstream Brobot repository is MIT licensed. A copy of the Brobot MIT license is included in `BROBOT-MIT-LICENSE.txt`.

The BillyBot notebook is essentially a tutorial-derived adaptation with personalized notes, examples, and persona-response 
experiments layered on top. My intent was to create a hillbilly persona based on my dad's quotes, but the design was 
intentionally exaggerated for fun. See `original-2017-notes.md` for the original design notes.

## Files

- `billybot-legacy.ipynb`: output-cleared historical notebook with a provenance header.
- `original-2017-notes.md`: preserved design notes from the old BillyBot repo.
- `rule-based-chatbot-lessons.md`: reflection on what the old experiment demonstrates.
- `BROBOT-MIT-LICENSE.txt`: upstream Brobot MIT license.
- `.gitignore`: ignores local envs, notebook checkpoints, caches, and generated scratch output.

The notebook is historical and may not run end-to-end without additional cleanup. It still contains some incomplete 
2017-era experimentation, including references to helper names that were not fully wired together.

## Why Keep Any of This at All?

BillyBot is not valuable because it works well! It's useful because it gives some historical context to
how hard it is to design a chatbot by hand and how far we've come in 2026 with local LLM chatbots. 