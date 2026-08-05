---
title: "Convert your Markdown to Beautiful Presentations with Markdown Slides"
layout: post
created-on: 2021-03-12
author: Kevin Urban
tags: markdown presentations workflow revealjs
---


Recently, I figured out how to use Beamer, a LaTex package for making "PowerPoint"
presentations (i.e., slides).  I chose a decent style and colors to match CVB
branding, but overall I wasn't impressed.  The slides have a distinctly "1980s"
vibe to them.  Plus, anytime I resort to using LaTex I think, "Someone must've figured
out how to do this with Markdown by now."

And they did!  Many of them.  

Now, honestly, a great choice would probably be using RMarkdown files with 
RStudio.  Several years ago, I almost exclusively used R and would have likely
made this choice.  These days I use Bash and Python for almost all my programming
needs, so I haven't been using RStudio for a while (though I did see somewhere
that it finally built in support for python development, which is pretty 
enticing).

I am not always coding, so this isn't really a Python-vs-R thing anyway.  However,
I'm almost always using Markdown: I use it when I code, for sure, but also when 
taking notes during a lit review or a meeting, for organizing my references, for 
managing my projects.  At any point, I'm probably using Markdown and Git (or 
GitLab). 

Anyway, I tried the first thing that came up when I googled something like 
"markdown slides gitlab."  Should be no surprise then that what I found is 
called "Markdown Slides" or that its codebase is located on GitLab.

* [Markdown Slides on GitLab](https://gitlab.com/da_doomer/markdown-slides)


# Set up
To test out the `markdown-slides` software, I created a new Miniconda environment
and installed pip.  
```
conda create --name mdslides -y
conda activate mdslides 
conda install pip 
```

Then I downloaded the `mdslides` software:
```
python -m pip install git+https://gitlab.com/da_doomer/markdown-slides.git
```

To compile slides, I had to download Chromium (just google it for the download link).

And that's it for setup!

# Basic Usage 
## The Markdown File 
Let's say you are working on a presentation: you create a Markdown file, make 
a few section headers and add a few notes, lists, and images.   Nothing fancy
or complicated, but enough to get started.  Believe it or not, you're 98% the 
way to an extremely beautiful-looking presentation.  

```markdown
# My Wonderful Presentation
![](images/flattering-pic-of-me.png)
Kevin Urban | 2021-03-12

# The Hook
On this slide, I do 3 things
* make you laugh
* make you cry
* patiently wait for the tears to stop

# The Pitch
On this slide, I make you feel smart and business
savvy before subtly implying anyone who didn't 
agree with my idea is going to lose out big time!

![](images/photoshopped-pic-of-me-shaking-famous-peoples-hands.png)
```

You just have to add some header info to the top of the Markdown file 
and a "slide break" anywhere you think a new slide should start.  

Editing the Markdown example from above, we now have this:

```markdown
[comment]: # (This presentation was made with markdown-slides)
[comment]: # (This is a CommonMark compliant comment. It will not be included in the presentation.)
[comment]: # (Compile this presentation: mdslides --include images/ README.md)
[comment]: # (----------------------------------------------------------------)
[comment]: # (----------------------------------------------------------------)
[COMMENT]: # (SET THE THEME:                                                  )
[comment]: # (THEME = white                                                   )
[comment]: # (CODE_THEME = zenburn                                            )
[comment]: # (The list of themes is at https://revealjs.com/themes/           )
[comment]: # (The list of code themes is at https://highlightjs.org/          )
[comment]: # (----------------------------------------------------------------)
[comment]: # (----------------------------------------------------------------)
[COMMENT]: # (PASS OPTIONAL SETTINGS TO REVEAL.JS:                            )
[comment]: # (controls: false                                                 )
[comment]: # (keyboard: true                                                  )
[comment]: # (markdown: { smartypants: true }                                 )
[comment]: # (hash: false                                                     )
[comment]: # (respondToHashChanges: false                                     )
[comment]: # (----------------------------------------------------------------)
[comment]: # (----------------------------------------------------------------)
[COMMENT]: # (OTHER SETTINGS:                                                 )
[comment]: # (    Documented at https://revealjs.com/config/                  )
[comment]: # (COMMENTS:                                                       )
[comment]: # (    A comment starting with three or more !!! marks a slide     )

# My Wonderful Presentation

![](images/flattering-pic-of-me.png)
Kevin Urban | 2021-03-12

[comment]: # (!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)


# The Hook
On this slide, I do 3 things
* make you laugh
* make you cry
* patiently wait for the tears to stop

[comment]: # (!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)


# The Pitch
On this slide, I make you feel smart and business
savvy before subtly implying anyone who didn't 
agree with my idea is going to lose out big time!

![](images/photoshopped-pic-of-me-shaking-famous-peoples-hands.png)
```

That's it!  

## The Interactive Slides 
Now, to get slides you just have to issue a simple command:

```
mdslides --include images my-wonderful-presentation.md 
```

The slides that are generated are actually dynamic, web-based slides you 
interactively view in your favorite browser.  You will notice that a 
new directory has been created in your current working directory.  This new 
directory will have the same name as your Markdown file.  To view the slides, 
just open up the file called `index.html`:

```
open my-wonderful-presentation/index.html 
```

And that's it!

Without much work at all, your simple Markdown file should look pretty 
dang beautiful.  This beauty rests on the `markdown-slides` software being built
with `Reveal-JS`.  

## PDF Slides 
It might be cumbersome to send the entire webpage directory to someone over email as 
opposed to a PDF (though you could always zip the directory to do so easily).  However, 
some people will still just prefer to look over your slides as a PDF (and some people won't 
know what to do with the zip file).  

To create a PDF is simple:
```
mdslides --include images --pdf my-wonderful-presentation.md 
```

# The Good, The Bad, and The Ugly
Ok, here is where I let you know it's not all sunshine and puppies.

As an initial exploration into creating slides from Markdown files, the `markdown-slides` 
software was well worth it.  If you like creating simple slides with just a few words or 
items on them, it will work fine.  You'll especially be happy if you are not nitpicky 
about how big or small things are and where they get placed.  

However, I felt that weaknesses arose the second that I wanted to customize the 
appearance of a slide -- even just a little bit.  

To be fair as possible, I finished an entire presentation using this software (well, not so 
much to be fair as I was already using it and had very little time to pivot before go-time).  Below,
you can see a better example of what to expect if you have any concern at all 
about customizability.  

I'll just show you the HTML I used for the first two slides.  Just know that there were many 
more slides!  (Also, skipping out on the header info since I already showed that above.)

```markdown
<!-- SLIDE 1 -->
<!-- TITLE (TOP) -->
<div style="float:top; height:30%;">
  <div style="float:center; font-size:50%;">
    Kevin Urban, Roozbeh Atri, Lee Lancashire | Cohen Veterans Bioscience | March 11, 2021
  </div>
  <div style="float:middle; font-size:100%; margin-top:2%;">
    24/7 Sensor-Driven Support for Parkinson's Disease 
  </div>
  <div style="float:bottom; font-size:70%; margin:2%; color:#800000;">
    Tools to Aid and Assist in Diagnosis, Symptom Tracking, Disease Progresion, and More!
  </div>
</div> 
<!-- GRRAPHICS (BOTTOM) -->
<div style="float:right; vertical-align:bottom; width:100%; display:flex; flex-direction: row;">
<div style="order:0; width:50%;">
  <img src="images/time-series-spaghetti-1_spilled-pot.png">
</div>
<div style="order:1; width:30%; position:relative;">
  <img src="images/right-arrow.png">
</div>
<div style="order:2; width:40%; position:relative;">
  <img src="images/HAR_clinician-friendly-monitor.png">
</div>
</div>


<!-- SLIDE 2 -->
[comment]: # (!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
## Raw Sensor Data is Like a Scary Slop of Spaghetti
<!--LEFT (FULL)-->
<div style="float:left; width:55%; position:relative;">
  <img src="images/time-series-spaghetti-1_spilled-pot.png">
</div>
<!--RIGHT (TOP)-->
<div style="float:right; vertical-align:top; width:30%; position:relative;">
  <img src="images/quote_what-is-this-thing.png">
</div>
<!--RIGHT (bottom)-->
<div style="float:right; vertical-align:bottom; width:35%; display:flex; flex-direction: row;">
<div style="order:0; width:55%; position:relative; left:8%;">
  <img src="images/time-series_squiggly-lines.png">
</div>

<div style="order:1; width:45%; position:relative; right:8%">
  <img src="images/character_angry-confused-doctor.png">
</div>
</div>
```

Fortunately (or perhaps unfortunately for me), I know enough HTML, JS, and CSS to be dangerous, so 
I was able to make things work.  

But -- dang!  Doesn't that beat the spirit of the endeavor into a bloody pulp?!  I was looking for a 
way to convert Markdown files into slides.  Though the code above indeed comes from a Markdown file, 
you might as well call it HTML.  Only someone with web dev experience is going to be able to 
finagle something similar.  

# Conclusion
It was a fun experience and I'm glad that I dove in and had some fun with it, but I don't 
think the specific software called `markdown-slides` is the best way to do Markdown slides.  While 
developing my presentation and running into various customizability issues, I learned of several 
other software packages that puport to do the same thing (including a way to do it using RMarkdown).  
Many of them look to be more powerful than the one I reviewed here.  

I'll keep y'all posted.  
