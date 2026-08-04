# IoT and Embedded Systems Notes

> Historical provenance and source-note details are at [Historical Provenance](#historical-provenance).

## Summary

These notes preserve a January-March 2020 pass through IoT and embedded systems fundamentals, started shortly after the Intel Edge AI scholarship material. The notes cover IoT definitions, privacy and security risks, embedded-system constraints, sensors, actuators, ADC/DAC, microcontrollers, development boards, memory, operating systems, RTOS ideas, Arduino/Raspberry Pi context, and networking basics.

This is especially useful as connective tissue between the OpenVINO / edge-AI articles and the later Udacity AI for IoT Developers Nanodegree archive. It shows the hardware-side learning path I was trying to build around edge deployment, not just model conversion.

## Contents

- [Context](#context)
- [Week 1: What Is the IoT?](#week-1-what-is-the-iot)
- [Week 2: Embedded Systems](#week-2-embedded-systems)
- [Week 3: Hardware and Software](#week-3-hardware-and-software)
- [Week 4: Networking and the Internet](#week-4-networking-and-the-internet)
- [Historical Provenance](#historical-provenance)

## Context

These notes came from a 2020 IoT / embedded systems learning thread around Raspberry Pi, Arduino, sensors, embedded constraints, and edge deployment. They are course-adjacent notes, but the preserved value is the working trail: what I was trying to understand before and during the edge-AI / IoT projects.

## Week 1: What Is the IoT?

Having completed Phase 1 of the Intel's Edge AI scholarship with quite some
time before Phase 2 begins, I figured I'd backtrack some and get my hands
dirty with the Rasberry Pi.  This interest led me to two relevant Coursera courses: (i)
[The Raspberry Pi Platform and Python Programming for the Raspberry Pi](https://www.coursera.org/learn/raspberry-pi-platform)
and [Interfacing with the Raspberry Pi](https://www.coursera.org/learn/raspberry-pi-interface). Both
courses are a part of the same specialization by UC-Irvine: 
[An Introduction to Programming the Internet of Things (IOT)](https://www.coursera.org/specializations/iot).  It
introduces embedded systems, C programming, networking, Arduino, Rasberry Pi, and -- well -- the general makeup of the 
Internet of Things (IoT).  I figured, "Why not back waaaay up!"  

So here I am, at the first week of the first course in the sequence:  [Introduction to the Internet of Things and Embedded Systems](https://www.coursera.org/learn/iot?specialization=iot).

In this course, we cover what IoT actually is, embedded systems (interface, hardware and software components),
IoT devices, IoT operating systems, networking, and something called "MANETs".  

Let's get started.

------------------------------------------------

We start by reading [The 2018 SANS Industrial IoT Security Survey](https://forescout-wpengine.netdna-ssl.com/wp-content/uploads/2018/07/2018-SANS-Industrial-IoT-Security-Survey.pdf).

"The digital transformation of industry, infrastructure and cities has clearly begun.
Whether it’s called Industrial Internet of Things (IIoT), Industry 4.0 or digitalization,
companies are developing new business improvement strategies based on analytics,
artificial intelligence (AI) and machine learning. These efforts are widespread and farreaching."

"The term IoT broadly refers to the connection of devices—other than the typical
computational platforms (workstations, tablets and smartphones)—to the Internet. IoT
encompasses the universe of connected physical devices, vehicles, home appliances
and consumer electronics—essentially any object with embedded electronics, software,
sensors, actuators and communications capabilities—that enable it to connect and
exchange data. Within this universe, Industrial IoT (IIoT) focuses specifically on industrial
applications that are often associated with critical infrastructure, including electricity,
manufacturing, oil and gas, agriculture, mining, water, transportation and healthcare."

"These IIoT efforts will invariably lead to violations of implicit cyber
security assumptions, including well-defined perimeters and architectures, which need
to be addressed."

"Predictive maintenance and operational improvements are the primary focus of
most of their IIoT efforts. Both involve broad-based connection of existing and new
plant sensors with cloud-based solutions and service providers. Cloud connectivity
is a concern, but most companies believe they can deal with this through network
segmentation and isolation of control networks. The security of new endpoints is clearly
more troublesome. Few organizations believe they can rely on the sensors’ original
equipment manufacturers (OEMs) in this emerging market to provide secure devices. "

"The individuals
probably the most knowledgeable about IIoT implementation, the OT team, appear the
least confident in their organization’s ability to secure these devices, while company
leadership and management, including department managers, appear the most assured." LOLOLOLOL.

Facts:
* "32% of IIoT devices connect directly to Internet, bypassing traditional IT security layers."


The Industrial Internet Consortium (IIC) Vocabulary
defines an endpoint as a “component that
has computational capabilities and network
connectivity.”6
IIoT endpoints support two basic connection types:
“Direct: where the [endpoint] can either talk as a
client ... to whatever remote online application it
interfaces with or where it can be seen online as a
server; and indirect, where communication to the
IIoT is mediated by some method other than IP.”


Major takeaway: the security and privacy risk is severe.

---------------------------

Internet of Things:
* Thing - anything besides acommon computer (laptop, desktop, tablet, etc)
* A refrigerator with an arduino has computational intelligence; add some network connectivity 
  (e.g., WiFi) and it's an "internet thing"
  - a regular fridge keeps stuff cold
  - a "smart fridge" does that and more (e.g., alerts you when door is ajar, when water filter
    needs replacement, when you're low on butter, recipes that match its contents); anything
    possible with local computational power and local sensors
  - a fridge "internet thing" can do all that and more (e.g., order food when stock is low, 
    lists lowest food prices from local grocers, anticipates meals and pre-emptively
    orders food, etc); anything made possible for a "smart fridge" w/ internet connectivity
* Modern cars are IoT devices
  - cars in 1950s had a simple interface (steering wheel, brakes, sound system buttons, etc)
  - modern cars have basically the same interface, but have so much computational intelligence
    "under the hood" (e.g., the anti-lock braking system has its own dedicated CPU, the
    fuel injection system, and so on)
  - this simple interface is characteristic of IoT devices
  - the most modern of cars are networked (e.g., you can remote start a car through the internet,
    call 911, etc)
 
Internet access gives simple devices access to computation and data not available on
the device itself (i.e., from the cloud).

RFID tags: improvement over barcodes.

An IoT device is a computer, but that's not its main point or main function: the computer
plays a supporting role.  Computers are general purpose, while IoT devices are very
purpose specific (both software and hardware).  A car does computation -- but only for
car-related tasks.  

IoT
* convergence of trends
  - cost of hardware (e.g., a computer in 1945 might have cost $0.5M, but a more capable
    laptop today might only run you $500; better, since IoT devices do not need the full
    general purpose power of a laptop, you'll pay much less;  this makes it easier today
    to say, "Hey, let's put a computer in this thing.")
  - size of hardware (again, the computer in 1945 might be the size of a room; now, it can
    be the size of a postage stamp)
  - computational throughput and speed (1945: 5k/s; now 18B/s)
  - internet access (1945: didn't exist; now: can access it almost anywhere)
  - wireless networking --> wireless internet access
  - data cost --> cheap, wireless internet access

Networking allows remote devices to have access to powerful servers, databases, and analytics.

What kind of IoT or smart devices are in your life:
* fridge
* microwave
* dvr
* tv
* game machine
* phone
* watch
* home automation systems
* motion sensors
* health trackers (Fitbit)
* medical devices (pace maker, insulin pump)
* RFID tags
* traffic lights
* security cameras


---------------------

Thermostats are important elements in the heating and cooling systems used to control the temperature in our houses.  The internal workings of a thermostat can vary quite a bit, but many heating systems use bimetallic switching thermostats.  However, from a user perspective, the inner workings are not so important: only the user interface.  This is similar to driving a car:  understanding what's under the hood is not essential.  Two cars can have very different engines, electrical systems, tire sizes, and so on, but still have the same user interface.   

The user interface for a thermostat is simple.  On a dial thermostat, the user simply rotates a numbered dial to set a desired temperature.  For a digital thermostat, a user inputs the desired temperature -- sometimes via keypad, but more often via up/down arrows or even a dial.   

Household thermostats were simple in the 1950s: one set the temperature on the device itself, mounted on some wall in the house.  By the 1980s, we had digital, programmable thermostats: one could set the temperature on the device itself, like the older thermostats, but could go a step further and put the set temperature on a regular, daily and/or weekly schedule.  Smart thermostats are now available: these allow you to put the set temperature on a regular schedule as well, if desirable, but has a few additional features: (i) it has the ability to learn what you like (e.g., over the first two weeks, it will learn your preferences as you manually increase and decrease the temperature throughout the day);  (ii) it has the ability to be monitored and manipulated from afar via your smartphone;  (iii) some have the ability to go into "eco" mode when you're out of the house;  (iv) some have the ability for voice control;  (v) some have the ability to be networked throughout the house using additional temperature sensors.

The ability to monitor and set your temperature from afar is certainly an improvement.  For example, if your thermostat is downstairs and you're already in bed upstairs -- it might be lazy, but it's super convenient to be able to pick up your phone from your nightstand and lower/raise the temperature.  Better, it's nice to be able to put the system into "eco mode" when you're away from the house and remember you left the heat on. 

The learning feature is of debatable importance.  For one, it isn't very difficult to develop a sensible weekly heating/cooling schedule.  It's also not clear that the learning feature truly makes things more convenient: in order for learning to take place, you do have to commit to manually tweaking the thermostat throughout the day and week.  The end result will probably look something like the schedule you would have programmed anyway.  Secondly, from an anecdotal perspective, I've personally found that it "over learns" and "over controls" the system.  For example, say at 4pm I usually have the heat in the dining room to 69*F, however one day I turn it down to 65*F because I'm feeling too hot:  I often find that after a certain amount of time, the system just kicks back to the "learned" temperature for that day and time.  

The various features of a smart thermostat allow for additional improvements not mentioned above, but these improvements come at a cost.  For example, allowing the mobile app to use location services on your phone in order to automatically have the system go into eco mode can become a privacy/security issue pretty quickly in the case of a data breach (which, let's face it, happens way too often).  

The cost of a simple dial thermostat these days is about $20-$40, while a smart thermostat can easily run $200-$400.  However, this price is not far off from what the dial thermostat cost in the 1950s:  a thermostat such as the Honeywell Round T832 day-night thermostat cost about $13 in 1950, which has the equivalent purchasing power of about $140 in 2020.  


-----------------------

If a smart speaker is hacked, prominent fears include being spied on by government ("Big Brother"), or by criminals who want to gain access to private conversations hoping to capture sensitive information, or by nefarious marketing firms with similar goals, or by hackers who want to stream your home life on internet sites for other perverted means (e.g., there are websites dedicated to streaming the footage of hacked security cameras hooked up to the internet; is there the same for smart speakers?).



SmartWatch:
The IoT watch has important features you missed, but which provide so much additional functionality (covered in next question).  Namely, an IoT Watch usually has:
* physical buttons and/or dials to navigate options and screens
* touchscreen capability

Sensors could have been fleshed out a bit:
* GPS
* accelerometer
* gyroscope
* magnetometer
* photoplethysmograph

The feature list is a bit short here.  Other features are worth mentioning:  pedometer (step counting), activity trackers (e.g., running performance), sleep monitoring and scoring, the ability to make calls or send/receive text messages, the ability to check the weather, the ability to use navigational features (e.g., find nearest restaurant and provide detailed directions), and so on.  

An important diminishment is "battery life":
* on an old, non-IoT battery-powered watch, the battery might last 2 years without any need for intervention
* on an IoT watch (e.g., Apple Watch), the battery needs to be charged every day; furthermore, if you go too long without charging (e.g., do not have access to), then the IoT watch doesn't even do the basic function of telling time

Location detection is a key concern, however the specifics can be fleshed out.  For example, by continuously recording location data, your highly personal and specific time tables and activity patterns can be leveraged against you in the case of a hacker/spy or data breach (e.g., it can be ascertained during which times of day and week are best for breaking into your house).

## Week 2: Embedded Systems

In this module, we take a look at embedded systems: what's the typical
interface of an embedded system?  What are its components?  Where are they 
used in the real world?

https://www.nytimes.com/2018/10/10/technology/future-internet-of-things.html

"...the economic and technical incentives of the internet-of-things industry do not align with security and privacy for society generally. Putting a computer in everything turns the whole world into a computer security threat — and the hacks and bugs uncovered in just the last few weeks at Facebook and Google illustrate how difficult digital security is even for the biggest tech companies. In a roboticized world, hacks would not just affect your data but could endanger your property, your life and even national security."

"business models for these devices don’t often allow for the kind of continuing security maintenance that we are used to with more traditional computing devices. Apple has an incentive to keep writing security updates to keep your iPhone secure; it does so because iPhones sell for a lot of money, and Apple’s brand depends on keeping you safe from digital terrors.  But manufacturers of low-margin home appliances have little such expertise, and less incentive. That’s why the internet of things has so far been synonymous with terrible security"


-----------

IoT devices are typically embedded systems -- computer-based systems that
do not appear to be computers (simple user interface hides any complexity).
* digital camera (same basic interface as an old camera, but lots more going on inside)
* TV
* cell phone

Some embedded systems do not directy interact with a human:
* USB stick 
* anti-lock breaking system

Embedded systems put a high emphasis on efficiency: it not only must
do what it's designed to do, but it must do so as efficiently as possible.  For example,
we might not fault the camera on your laptop for not being as memory efficient as
it could be, but in a low-resource device like a digital camera, inefficiency is
no longer a convenience: it must be fast, power efficient, memory efficient, etc.

Efficiency is important because these systems tend to be in cost-crticical or
power-critical devices...

The constraint set for an embedded system is much more stringent that systems deployed
on general purpose computers:
* manufacturing cost
* design cost
* performance
* power
* time-to-market

However, to offset a stringent constraint set, also note that an embedded system (like
an IoT device) is usually made to do one thing -- it is application specific.  Some
devices, like a cell phone, are exceptions to this rule.

For a GP computer, for almost any task, its potential is underutilized, e.g., you do
not need a quadcore CPU running at a few GHz to do a PowerPoint presentation.  This is
b/c the GP computer has to be ready for anything -- later on, you may be watching a movie,
while streaming on Google Hangouts and surfing the internet (with 23 tabs open).

Another aspect of embedded systems:  software and hardware co-design (GP systems usually
use hardware and software developed by different companies). So design is much harder: you
have to be both a SW and HW designer!

The embedded system diagram:
```
                     ___________________
[Sensors]-->[ADC]-->| [microcontroller] |-->[DAC]-->[Actuators]
        |__________>|   ^         ^     |______________|
                    |   v         v     |
                    | [IP] <--> [FPGA]  |
                     -------------------
```

* Sensors: Receive data from outside world
  - a microphone is a sensor
  - a webcam is a a sensor
  - a car's brake pedal is a sensor
* Actuators: Portray results or effects to outside world
  - a speaker is an actuator
  - a computer screen is an actuator
  - a car's brake lights are actuators
* IP: Intellectural Property Core
  - designed for very specific purpose
  - a reusable unit of logic or functionality 
  - expensive to make if you only need one, but cheap to mass produce
  - we won't design IP cores in this class, but what we will go over is buying ready-made ("off the shelf") IP cores
* FPGA: Field Programmable Gate Array
  - can be reconfigured for different purposes
  - complex; won't be used in this class

## Microcontrollers
A "microcontroller" can be thought of as a smaller, weaker "microprocessor".  The microcontroller
is used for specific purpose devices (embedded systems, IoT), so doesn't need to be as powerful:
usually it's slower than a microprocessor, has less memory, etc.  

Microcontrollers need to be programmed (usually in C); such programs are written on a regular 
computer (called the host, e.g., your MacBook Pro), then transferred from the host to 
the microcontroller (placed in `mctrlr` memory).


Some Components of Embedded Systems work
* development board - 
  - https://en.wikipedia.org/wiki/Microprocessor_development_board
* processors
  - GP: overdesigned; can do a little of everything; tends to be expensive
  - DSP: supports DSP functions; speed vector instructions (GPs usually have scalar instructions); cheaper, but limited https://en.wikipedia.org/wiki/Digital_signal_processor
* simple sensors
  - thermistor: reports temp
  - photoresistor: reports light intensity
  - potentiometer
* complex sensors
  - CMOS camera: captures images (special purpose light sensor)
  - ethernet controller: enables network communication (listens)
* simple actuators
  - LEDs, LCD displays
* complex actuators
  - servo motor (moves things)
  - ethernet controller:  enables network communication (output)
* ADC - Analog-to-Digital Converter
  - example: sound is an anolog quantity; when going into microphone, the pressure
    waves are converted to voltage waves, whose value are then digitized into discrete voltage 
    levels (this process is also happening with time too:  continuous time --> discrete time steps)
* DAC - Digital-to-Analog Converter
  - example: after a microphone's input has been digitized and processed (e.g., some reverb is added),
    then it must be "continuized" before blasting out of speaker
    
Things we'll be using in class:
* development board (has microcontroller w/ some code running on it)
  - Arduino
  - Rasberry Pi
  - might be interested in boards with cool things, like compasses, accelerometers,
    magnetometers, touch sensor screens, etc (though none of this is required)
* cables
  - USB cable
  - jumper wires
* inputs
  - potentiometer
  - photoresistor
  - keypad
  - buttons
* breadboard 
  - used for quick, impermanent wiring 
  - holes fit 24-gauge wiring
  - see diagram below
  
Breadboard
https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all

* all holes in leftside column are connected (this is your power supply and ground)
* all holes in a row are connected (this is how you connect components)
```
* *   * - * - * - * - *
| |
* *   * - * - * - * - *
| |
* *   * - * - * - * - *
| |
* *   * - * - * - * - *
```


------------------------

## HW

The Apple Watch (Series 4)
To a first approximation, the interface of an Apple Watch is fairly simple and familiar feeling: like a more traditional watch, it straps on the wrist and it has a screen that displays the time (and other information).  However, the similarities with a classical watch end rapidly after this superficial consideration of appearance.  

The Apple Watch has a screen that senses both touch and force, distinguishing between a light tap and a more firm press.  These sensing features provide context-dependent capabilities, from tapping in a security code to unlock the watch, to navigating through various screens, to tracing out alphanumeric characters and punctuation that are transcribed into digital text.  For additional control over screen navigation, the Apple Watch also has (i) a physical oblong button that serves different functions depending on how it's pressed (e.g., 1 press vs 2 quick presses) and (ii) a knob (called the "Digital Crown") that can be used to scroll through and/or zoom in and out of on-screen content, and which can also be pressed as a button for additional functionality (e.g, 1 press takes you to home screen).  The Apple Watch has a microphone that allows the user to issue voice commands (activated by holding down the digital crown), dictate text messages (an option provided by an on-screen button on the associated text messaging app screen), or take phone calls.  When issuing voice commands, a voice assistant (named "Siri") will provide cues and response outputs via the onboard speaker.  Both the text messaging and phone call functionality (as well as additional features and extensions) are enabled by pairing the Apple Watch with the user's iPhone via Bluetooth or WiFi.  The Apple Watch also supports Near Field Communication (NFC), which gives the device additional functionality, e.g., to be used in place of a credit card (via Apple Pay) or as a plane boarding ticket (via an airline's app).  A haptic feedback engine along with the speaker provide context-dependent tactile and auditory cues and feedback (e.g., for an incoming phone call, a notification, and so on). Onboard sensors (specifically, an accelerometer, gyroscope, and photoplethymograph) and built-in GPS track the user's activity and heart rate throughout the day, which is summarized and presented on screen as 3 rings surrounding the clock face of the watch (further details can be accessed by pressing on the rings to bring up the associated app).  The built-in GPS allows one to navigate their surroundings, especially when paired with the user's iPhone.  Due to the overwhelming amount of functionality, the Apple Watch has a relatively short battery life as far as fitness trackers go, often requiring daily instead of weekly (or better) charging.  Depending on the version of the Apple Watch one has, many more interface features may be provided (e.g., from Series 4 on, one may use the Apple Watch as an electrocardiogram (ECG) to monitor heart health; e.g., from Series 5 on, there is onboard compass functionality).  

iLife A4 Robot Vacuum Cleaner
For my second embedded system, I've went with something much simpler than an Apple Watch: the iLife A4 Vacuum Cleaner.  This smart vacuum is just a notch above a traditional "dumb" vacuum: like a traditional vacuum, it has a power button to turn it on and off.  However, once on, it finds its way around a room on its own -- and when it's running low on battery, it automatically navigates back to its charging station. Furthermore, the suction mechanism automatically adjusts depending on surface (e.g., carpet, tile, hardwood, and laminate).  Multiple smart sensors serve to help the robot avoid bumping too hard into walls or falling down stairs.  The user may manually control the vacuum wirelessly with a standard (infrared) remote control using forward, right, and left buttons (there is no "back" button).  The remote control is also used to: (i) change the cleaning mode using the various mode button (spot cleaning, edge cleaning, small room);  (ii) program in a cleaning schedule using the "plan" and "clock" buttons;  (iii) start a cleaning session using the "clean" button;  and (iv) initiate a deep cleaning session for carpets using the "max" button.  This particular model does not connect to the internet (no WiFi connectivity), nor does it learn its environment like smarter robot vacuums do.


The visual inputs/outputs to the Apple Watch include:
* ambient light (input)
* light variations indicative of changes in blood flow (inward facing optical sensor (photoplethysmography)) (input)
* information on screen (output)

The audio inputs/outputs to the Apple Watch include:
* microphone inputs (input)
* sounds from speaker (output)

The tactile inputs/outputs to the Apple Watch include:
* touches, taps, and swipes on the screen (input)
* physical button (input)
* physical knob turning signal (input)
* haptic feedback (vibrations) (output)

The electronic (and other sensory) inputs/outputs to the Apple Watch include:
* near field communication signals (radio frequency) (input/output)
* Bluetooth signal (communication with iPhone) (input/output)
* WiFi signal (input/output)
* GPS signal (input)
* accelerations (accelerometer) (input)
* rotations (gyroscope) (input)
* variations in electrical current associated with the heart (measured by resting a finger from the opposing hand on the knob ("digital crown"), which completes the arm-to-arm circuit with a sensor on the bottom of the watch face) (input)

-------------------------------------------------------------------------------

iLife A4 Robot Vacuum Cleaner
The visual inputs/outputs (including infrared sensors for environment understanding) to the iLife A4 Robot Vacuum Cleaner include:
* the front bumper houses infrared sensors for detecting walls (input)
* drop sensors are on the underside to help detect stairs, etc (input)
* on/off light indicator (output)
* battery charge state indicator (fully charged (green), middle range charge (orange), needs charging (red)) (output)
* the remote control itself is a separate embedded system, which has a screen for visual feedback (e.g., when programming in a cleaning schedule)

The audio inputs/outputs to the iLife A4 Robot Vacuum Cleaner include:
* beeps from speaker (for turning on/off, indicating it needs charging, and arriving at the charging station) (output)

The tactile inputs/outputs to the iLife A4 Robot Vacuum Cleaner include:
* has "auto clean" button to start a cleaning session (input)
* has power button to turn robot vacuum on/off (input)
* the remote control itself is a separate embedded system, which includes physical buttons to input commands (input)
* motion (transportation, spinning brushes) (output)

The electronic (and electromagnetic signal) inputs/outputs to the iLife A4 Robot Vacuum Cleaner include:
* receives infrared signal from IR remote control (input)
* state change (on/off) (output)
* the remote control itself is a separate embedded system, which outputs infrared signals to the robot cleaner (output)

https://www.pcmag.com/reviews/ilife-a4s-robot-vacuum-cleaner

----------------------

Gaming Console

Visual (for gaming console):  the content on the screen might be considered a visual output, but that's only if you consider the TV screen as a component of the video game console, which is true for handheld devices, like Game Boy.  However, for devices like X Box, the video game console itself does not visually output the content on the screen, but outputs an electronic signal that is received by the TV, which it then visually outputs, etc.  Visual outputs of a console that do exist for most consoles include things like lights to indicate if the console is on or off.

Audio (for gaming console):  similar to visual in that the gaming music and sound effects are often outputs of a TV speaker, though the speaker on handheld devices is responsible for this type of output.  That said, some audio outputs stemming from the console itself include beeps (e.g., errors on start up, etc).  

Tactile (gaming console):  if you consider the controller as a part of the console (and not itself a separate embedded system), then the physical buttons on the controller are tactile inputs to the system.

Electronic (gaming console):  this would include WiFi signals (connection to router), Bluetooth (connection to controller), etc.

* optical variations read off the DVD by an optical sensor

DVD Player

For example, take the DVD Player.  Audio outputs include beeps (e.g., due to an error on start up) and visual outputs include the on/off indicator light.  Tactile inputs include the various buttons to play, pause, rewind, etc.  Electronic inputs include infrared signals received from the remote control; you might also classify the optical variations read off the DVD as electronic inputs (though one could argue these are visual inputs).  The list goes on.

------------------


LG Smart Washing Machine + ThinQ app

* https://lgcommunity.us.com/discussion/3933/how-to-connect-wt7300cw-washer-to-your-wifi
  - I didn't have to check "front load" instead of "topload", but I did have to pull the plug out of the wall

I now have this washing machine connected to my iPhone.  Cool, but anti-climactic.  It's not like
the clothes are going to load themselves in, then from the comfort of my bed I click "go!"

The major use case for this that I can think of is when you've left the clothes in for a day or two,
and they've probably gotten that stank -- maybe I could tap a wash cycle on that (assuming the stank
vanishes without having to go put more soap in the machine).



-------------------

Some Smart Devices (& Related Stuff):
* [Home Assistant](https://www.home-assistant.io)
  - [Getting Started](https://www.home-assistant.io/getting-started/)
  - YouTube (TheHookUp): [Home Assistant Beginners Guide](https://www.youtube.com/watch?v=sVqyDtEjudk)
  - YouTube (DrZzs): [Intro to Home Assistant & Smart Home hubs: Hassio vs Alexa vs Google Home](https://www.youtube.com/watch?v=pVxoSXeC2Jw)
* [IFTTT (If This Then That)](https://ifttt.com/)
* [Arlo Security Cameras](https://www.arlo.com/en-us/default.aspx)
* [Philips Hue (Smart Lighting)](https://www2.meethue.com/en-us)
  - [Philips Hue White & Color Ambiance A19 LED Smart Bulb (Bluetooth & Zigbee Compatible)](https://www.amazon.com/dp/B07QWB3H1Q)
* [GE Enbrighten Z-Wave Plus Smart Dimmer](https://www.amazon.com/GE-Enbrighten-Repeater-SmartThings-14294/dp/B01MUCZA1C)
* [GE Enbrighten Z-Wave Plus Smart Switch](https://www.amazon.com/GE-Enbrighten-SimpleWire-SmartThings-46201/dp/B07RRBT6W5/)
* [Wyze Bulb](https://wyze.com/wyze-bulb.html)
* [Wyze Smart Home Plug](https://www.amazon.com/Wyze-Labs-WLPP1-Smart-Two-Pack/dp/B07XZT24B8)
* [Wyze Indoor Smart Home Camera](https://www.amazon.com/Wyze-1080p-Indoor-Camera-Vision/dp/B07DGR98VQ/)
* [Best smart bulbs for your connected home](https://www.techhive.com/article/3129887/best-smart-bulbs.html)
* [LampUX Smart LED WiFi Color Changing Light Bulbs](https://www.amazon.com/dp/B07PY5ZFM7/)
* [Magic Hue (RGBCW) Multicolor, Dimmable Smart Light (LED)](https://www.amazon.com/dp/B07VJL4MDH/)



* [How the Apple Watch Works](https://electronics.howstuffworks.com/gadgets/high-tech-gadgets/apple-watch2.htm)
* Quora: [What are the most popular embedded systems?](https://www.quora.com/What-are-the-most-popular-embedded-systems)
* [Understanding of Embedded Systems](https://www.edgefxkits.com/blog/embedded-systems-with-applications/)

## Week 3: Hardware and Software

In this module, we're covering the basic hardware used in IoT devices and embedded systems,
and how the hardware and software typically interact in these devices (hint: they are more
in sync and integrated than found in general purpose computers specifically due to their
"special purpose" nature).  We will also cover the role of operating systems in IoT devices,
and how these differ from more familiar general purpose OS's (e.g., Linux, Windows, MacOS, Android, etc).

In IoT design, you have to think about the hardware and software development 
process together -- in step.  

Whenever you start a project, you have to give careful thought to the hardware components.  The
software you write is sensitively dependent on the hardware you've chosen.  Unlike a GP computer,
for an IoT device you are not writing software that does a whole lot independent of the hardware -- the hardware
is NOT abstracted away as if it doesn't exist, while you train a model to classify cats and dogs (or
whatever!).  Instead, you are writing software for the sole purpose of breathing life into
the hardware.

It's advisable to look at hardware data sheets when planning a project:  What type of 
power draw is necessary? What size is just too large?  How much speed do you really need?  What
is the max current on a component?  Even with proper planning, you will get things wrong
and have to order a new part or two -- but you want to minimize that!  

> "In preparing for battle I have always found that plans are useless, but planning is indispensable."
- Dwight D. Eisenhower

You do not have to understand everything on a datasheet, and first starting out -- you won't.  But 
you should be able to pick things out.  For example, the size of the component or the pin spacings (e.g.,
if your board has pin holes spaced 1/10 of an inch, then your component should have a pin spacing that is
an integer multiple of that spacing, n/10).  

There is a lot of information you won't really need, e.g., the thermal parameters (unless you are hoping
to deploy your device in extreme conditions).  

Electrical information is important.  Understanding the min/max current and voltage for a device
is necessary in properly planning how to piece together your circuit.  For example, you might
find that a component comes in several voltage ranges -- then you would select the component 
that matches your needs.  If you could not find a component with the right voltage requirements,
you might have to plan in stepping the voltage down/up with a transformer.

Datasheets for integrated circuits (ICs) can be very complicated -- up to 100's of pages!  When
using Arduino and Rasberry Pi, a lot of this is abstracted away for you, so we needn't be too
concerned about it in this class.  


IoT systems are tightly constrained, which must be taken into account when selecting a microprocessor.  In
fact, these constraints can be helping in narrowing down the selection space, which is HUGE.  Professor's advice:
be cheap!  Look through the datasheets and find the components that just barely work for your needs.

Look at all these microcontrollers:
* https://www.sparkfun.com/categories/300

In this class, we use an Arduino -- and in the next class a Rasberry Pi.  So we will not have to
pick a microcontroller.  However, this info is important in the case that I want to make my
own IoT devices after the classes are over.

SparkFun is a cool website in general:
* https://www.sparkfun.com/


Terms
* Datapath Bitwidth
  - number of bits in each register (storage of number)
  - determines accuracy and data throughput
  - note that not all systems need high accuracy (i.e., 64-bit numbers); the various projects
    we work on in this class use 8-bit numbers -- and it's just fine
* Input/Output Pins
  - limited amount of pins stemming from a microcontroller is also the bottleneck in a system
  - you can easily create a circuit that requires more pins than the microcontroller has available
  - it's important to plan early on and sketch out your design so that you have an idea of how many pins
    will likely be necessary
  - for example, you might estimate a need of 38-40 pins, then look through some datasheets and find
    a 40-pin microcontroller
* Performance
  - clock times on microcontrollers are slower than desktop 
  - for many special purpose needs a fast processor is not necessary
  - consider audio: the highest frequency a human can hear is about 20kHz; if we interpret this
    through the lens of the Nyquist frequency, then it might be accurate to say that our internal
    auditory processing is running at 40kHz;  typical processors on GP computers are around 2GHz, 
    which is 50,000x faster than 40kHz;  in other words, a fairly limited processor (say 100kHz-1MHz)
    can process audio information much faster than a human
  - exception:  video processing (e.g., game-specific devices might higher than GP computers, e.g., 4GHz)
* Timers
  - needed for real-time applications
  - need to consider what timing accuracy you need and the bitwidth of the timer to determine which timers you should purchase/use
* Analog-to-Digital Converters
  - necessary for reading analog signals (e.g., sensors like accelerometers, gyroscope, thermometers, etc)
  - note that the Rasberry Pi doesn't come stock w/ an ADC
  - https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters
  - YouTube: Ralph S Bacon: [Analog inputs for your Raspberry Pi 🥧Model 3B+](https://www.youtube.com/watch?v=x_86hTwqEMk)
  - YouTube: rdagger68: [Raspberry Pi Analog Water Sensors ADC Tutorial](https://www.youtube.com/watch?v=wJgyszOSoQU)
* Low-Power Modes
  - modes where the microcontroller is not fully on, but not fully off
  - helps save power
  - will not cover in this class
* Communication Protocol Support
  - the microcontrollers must communicate with other ICs, and they do so via some protocol (certain ordering, timing, etc)
  - e.g., UART, I2C, SPI



-------------


Storing data inside and outside a microcontroller.

We look at an example microcontroller data sheet: AVR ATmega2560
* 8-bit microcontroller
* Up to 16 MHz
* 256kB of flash memory
  - a type of non-volatile memory (i.e., you can turn off power to the device and the memory
    remains intact)
  - technically, a type of EEPROM, though distinguished from typical EEPROM since flash is
    optimized for high speed and high density at the
    cost of large erase blocks (~ 512 bytes or more) and relatively short lifetime (~10k 
    write cycles), whereas what is referred to as "EEPROM" typically has much smaller
    erase blocks and much longer write-cycle lifetime
  - typically used in a microcontroller's firmware
* 4kB EEPROM
  - electrically erasable programmable read-only memory
  - a type of non-volatile memory
  - used to store relatively small amounts of data
  - individual bytes can be erased and reprogrammed
  - flash memory is technically a type of EEPROM, though in practice "EEPROM" is reserved for
    non-volatile memory with small erase blocks (down to 1 byte) and a long lifetime (on the 
    order of 1M cycles)
  - typically used for storing parameters and history (whereas flash is used in firmware)
* 8kB SRAM
  - static random access memory (as opposed to dynamic RAM - DRAM)
  - used with moderately slow processing speeds, SRAM draws very little power and can have
    a nearly negligible power draw when idle
* Pin Diagram
  - shows map of the microcontroller's pins (where they are located) and what each one is for

Here is a datasheet for a similar device: [AVRmega640](https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf)

Storage elements: you often have a speed/cost tradeoff and a power tradeoff with storage types.  For
example, you can have very fast access to memory, but it will be expensive and take up a lot of space
on the chip, whereas slower access to memory will take up very little room.  

The fastest (most expensive) storage is in a register, which stores only a single value, e.g.,
a 32-bit register stores a single 32-bit number.  A chip usually has a set of specific purpose
registers and a set of general purpose registers.  A [register file](https://en.wikipedia.org/wiki/Register_file) is a set of registers (e.g., 32 registers), which acts like memory.  

https://en.wikibooks.org/wiki/Microprocessor_Design/Register_File

Memories are meant to be much bigger than register files -- for storing a lot more, but with slower
access. 

Cache memory
* slower and cheaper than a register file
* but is still relatively fast and expensive as far as memories go in general 
* Cache memory stores like 10^5 more data than a register file, so it's relatively huge, but that 
  only amounts to about 1 Mbit of data, so not exactly "huge" in terms of other types of memory
* cache is usually on-chip memory (part of the integrated circuit)
  - in the [Harvard architecture](https://en.wikipedia.org/wiki/Harvard_architecture) we are using class, there is a data cache and an instruction cache
  - https://stackoverflow.com/questions/22394750/what-is-meant-by-data-cache-and-instruction-cache
* caches are generally used to avoid the von Neumann bottleneck 
  - system throughput is limited due to the relative ability of processors compared to top rates of data transfer
  - the limited throughput (data transfer rate) between the central processing unit (CPU) and memory compared to the amount of memory

Main memory
* very big (GBs)
* no in the CPU (not in-chip memory)
* connected to CPU via system bus
* relative to the cache and register file, memory access is slow (e.g., the difference between
  1 and 100 clock cycles for a task)


Machine Language: Processors understand machine language, e.g., x86 (Intel) processors understand x86 language.  At 
this level, the CPU instructions are in binary (or if looking at them in a text editor, you will see
them in hex). 

Assembly Language: This is a "human readable" version of machine language that employs simple mnemonics
to represent the CPU instructions (literally a one-to-one mapping between assembly and machine language). These 
are very simple instructions -- they do not include things like for loops that you may be used to from higher 
level languages (e.g., C, Python).

High Level Language:  these are the highly human readable, easy-to-use languages most of us are familiar with.
  - Compile language: code is translated once before running the code (e.g., C, C++); since code is compiled
    before runtime, everything is known at runtime and the code can run very fast; we'll be using C/C++ with
    the Arduino
  - Interpreted language: translate instructions while code is executed (e.g., Python); this translation occurs
    every time the code is run; often easier to use, but generally slower than a compiled script;  a lot is
    taken care of for you (e.g., memory management); we'll be using Python with the Rasberry Pi


Operating Systems

IoT devices do not always have an OS, e.g., the Rasberry Pi does have one, but the Arduino does not.

On a device without an OS, the code that you write (the "application") interacts directly with
the hardware; if you have multiple applications, you have to explicitly write how the hardware manages
its interactions with these applications -- but this is what an OS is for!  When a device has an OS,
the user can have many applications running, and the OS will orchestrate it.  Though it seems like
all the applications are running at the same time, this is not strictly true, e.g., the OS quickly
cycles through each running application in sequence, updating instructions, at a speed so fast it
seems like things are running simultaneously to the user.  An OS requires processing power and 
memory, and ultimately slows down the system a bit -- but it makes development way easier.

```
[ User ]
^    |
|    v
[ Application ]
^    |
|    v
[ OS ]
^    |
|    v
[ Hardware ]
```

The OS makes development much easier and more modular.  Instead of having to worry about how
different applications must work concurrently, the OS does this for you.  This means you can
develop applications independently of each other.  The main job of an OS is to support process
abstraction, where a process is an instance of a program (i.e., you can have one program that
is running for 10 users, thus have 10 processes).  Processes must have access to the CPU,
memory, and other resources (I/O, ADC, timers, network, etc).  There can be many processes running
on a system, so it's the job of the OS to manage resources fairly.

----------------------


Arduino OSs (not covered in HW)
* RTuinOS: 
  - [RTuinOS: A Real Time Operating System (RTOS) for Arduino 1.0.1](https://forum.arduino.cc/index.php?topic=138643.0)
  - [RTuinOS 1.0: Second Release of the Real Time Operating System (RTOS) for Arduino](https://forum.arduino.cc/index.php?topic=184593.0)
  - GitHub: https://github.com/PeterVranken/RTuinOS
* http://antipastohw.blogspot.com/2009/11/4-operating-systems-for-arduino.html
  - DuinOS
  - Pyxis OS
  - ArduinoMacOS
  - TaOS


Raspberry Pi OSs
* YouTube: Top 8 Raspberry Pi Distros
* [The 20 Best Raspberry Pi OS Available to Use in 2020](https://www.ubuntupit.com/best-raspberry-pi-os-available/)
* [The Best Operating Systems for Your Raspberry Pi Projects](https://lifehacker.com/the-best-operating-systems-for-your-raspberry-pi-projec-1774669829)
* [Raspberry PI Operating Systems (OS) – Which one to use in 2020?](https://www.seeedstudio.com/blog/2019/10/29/raspberry-pi-operating-systems-os-which-one-to-use/)

Misc
* [What is an ARM Processor](https://whatis.techtarget.com/definition/ARM-processor)


#### Microcontrollers


### HW Q1
What do the specs look like from one of the cheapest microcontrollers you can buy, and how do they compare to the specs from one of the most expensive microcontrollers you can buy?  To help answer this question, I specifically looked into AVR microcontrollers (originally developed by Atmel, now owned by Microchip as of 2016) and identified the cheapest and most expensive on the page: the ATtiny202 ($0.29/unit for 5000+ units; $0.40 for a single unit) vs the ATmega2561 ($8.51/unit for 5000+ units; $11.72 for a single uit).  


Clock Frequency
* ATtiny202: 20 MHz
* ATmega2561:  16 MHz

Bitwidth of the Datapath
* ATtiny202: 8 bit
* ATmega2561:  8 bit

Size of Flash Memory
* ATtiny202:  2KB
* ATmega2561:  256KB

Number of Pins
* ATtiny202:  8
* ATmega2561:  64

Analog-to-Digital Converter
* ATtiny202: Yes, 12-Channel 10-bit ADC
* ATmega2561:  Yes, 8-Channel 16-bit ADC

Comparing these 5 properties certainly gives some motivation for the price differential (e.g., the ATmega2561 has over 100x the Flash memory, and 8x more pins).  Other specs of interest might include:
* EEPROM: 64B (ATtiny202) vs 4KB (ATmega2561)
* SRAM: 128B (ATtiny202) vs 8KB (ATmega2561)
* Timers:  2x16-bit (ATtiny202) vs 2x8-bit + 4x16-bit (ATmega2561)

#### General References 
* Definition of "bitwidth datapath" given by Professor Harris in Lecture 1.3 (Microcontroller Properties @ 3:22):  "Okay. Datapath bitwidth. Bitwidth, what that means is, it's a number of bits in each register. A register storage element to store as a number. So, the bitwidth basically tells you the size of most numbers in your system."
* AVR Microcontrollers:  https://www.microchip.com/design-centers/8-bit/avr-mcus

#### ATtiny202 References
* https://www.microchip.com/wwwproducts/en/ATTINY202
* http://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny202-402-AVR-MCU-with-Core-Independent-Peripherals_and-picoPower-40001969A.pdf

#### ATmega2561 References
* https://www.microchip.com/wwwproducts/en/ATmega2561
* https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf

------------------------------

### HW Q2

Both the Arduino and Rasberry Pi have multiple operating systems (OSs) available for use.

The use of an OS in an Arduino Uno appears to be fairly controversial since many Arduino developers consider an OS to be overkill within the typical Arduino Uno use cases.  However, controversial or not, OSs have been created for and used on the Arduino Uno.

ChibiOS (open source under GPL3/Apache2.0)
Website:  http://www.chibios.org/
Licensing:  http://www.chibios.org/dokuwiki/doku.php?id=chibios:licensing:start
Arduino port of ChibiOS:  https://github.com/greiman/ChibiOS-Arduino
Semi-recent article about ChibiOS:  https://hackaday.com/2016/09/22/arduino-sketch-the-next-generation/
YouTube Tutorial:  Arduino Real Time OS (ChibiOS):  https://www.youtube.com/watch?v=JXy86GrjVso&list=PL-VRW4ibM-f20B-dXzf6ogiwSzexkAPxY
Code to follow along with YouTube tutorial:  https://github.com/ItKindaWorks/sketches/tree/master/ChibiOS


FreeRTOS (open source under MIT open source license)
Website:  https://www.freertos.org
Licensing:  https://www.freertos.org/a00114.html
Feilipu's Arduino port of FreeRTOS (https://github.com/feilipu/Arduino_FreeRTOS_Library) and overview (https://feilipu.me/2015/11/24/arduino_freertos/) 
Several examples using Feilipu's Arduino port:  (i) https://create.arduino.cc/projecthub/feilipu/using-freertos-multi-tasking-in-arduino-ebc3cc;  (ii) https://www.mepits.com/tutorial/576/arduino/using-free-rtos-multi-tasking-in-arduino
Greiman's Arduino port of FreeRTOS:  https://github.com/greiman/FreeRTOS-Arduino


DuinOS (open source under a modified GNU General Public License (GPL))
Based on FreeRTOS
Most recent version:  https://github.com/DuinOS/DuinOS
Older versions:  https://code.google.com/archive/p/duinos/

If one considers Arduino platforms beyond the Uno, then there exist more OSs.  For example, the Arduino 101 has the Intel Arduino 101 RTOS (might be open source under LGPL, but I cannot find an exact statement on this):
Article about this: https://www.infoq.com/news/2016/04/arduino-101-fw-open-source/
Intel's blog about it: https://blog.arduino.cc/2016/04/21/intel-releases-the-arduino-101-firmware-source-code/
Source code for the Arduino 101 (referred to as ArduinoCore-arc32 in the repo), which Intel's Arduino 101 RTOS runs on: https://github.com/arduino/ArduinoCore-arc32
Licensing (LGPL) for the Arduino 101: https://github.com/arduino/ArduinoCore-arc32/blob/master/LICENSE

There exist other OS efforts on the Arduino I saw mentioned on webpages published 9+ years ago (e.g., 2009-2011), but no longer have much of a digital presence (e.g., several listed on one webpage I visited include Pyxis OS, ArduinoMacOS, and TaOS;  http://antipastohw.blogspot.com/2009/11/4-operating-systems-for-arduino.html).


Raspberry Pi Operating Systems

There are countless OS options on the Raspberry Pi -- so many, that articles dedicate themselves to the "top 10", "top 15", and even "top 20" operating systems (e.g., https://www.ubuntupit.com/best-raspberry-pi-os-available/).  This is not surprising: unlike the Arduino, the Rasberry Pi was intended to have an OS -- which OS to use depends strongly on the use case (and, of course, user preference).

Raspian (open source under GPL)
* The "official OS" of Raspberry Pi, based on Debian
* Website: https://www.raspbian.org/
* Download:  https://www.raspberrypi.org/downloads/

DietPi (open source under GPL 2.0)
* Very lightweight Debian
* Website: https://dietpi.com/
* Source Code: https://github.com/MichaIng/DietPi

LibreELEC (open source under GPL 2.0)
* This is a fork of OpenELEC, another (now defunct) open source OS available for Raspberry Pi 
* Basically, LibreELEC (and OpenELEC before it) turns Raspberry Pi into a Kodi media center 
* Website: https://libreelec.tv/
* What is Kodi (hint: formerly known as XBox Media Center):  https://www.tomsguide.com/us/what-is-kodi,review-4160.html

OSMC (open source under GPL 2.0)
* Like LibreELEC, OSMC turns Raspberry Pi into a Kodi media center
* However, unlike LibreELEC, OSMC is a fully featured OS (not ONLY a Kodi media center)
* Based on Debian
* Website: https://osmc.tv/

RISC OS (open source under Apache 2.0)
* A very idiosyncratic OS (not based on Linux or Windows) that has been used on ARM processors since 1987
* Poking around the internet, it seems like the user base is biased towards older engineers that learned this OS as a kid, or used it professionally early in their career
* Website: https://www.riscosopen.org/content
* Formerly closed, now open source:  https://itsfoss.com/risc-os-is-now-open-source/
* Who uses RISC OS (1):  https://www.raspberrypi.org/forums/viewtopic.php?t=162004
* Who uses RISC OS (2): https://www.riscosopen.org/forum/forums/5/topics/3008

Windows IoT Core (not open source)
* Very Windows-oriented; you need a Windows computer for this
* ARM compatible
* Does not appear to be open source (basically a stripped down version of Windows 10)
* About:  https://docs.microsoft.com/en-us/windows/iot-core/windows-iot-core
* Hooking up a Raspberry Pi with Windows IoT Core:  https://docs.microsoft.com/en-us/windows/iot-core/tutorials/rpi

Lakka (open source)
* Retro gaming-oriented lightweight Linux OS 
* Website: https://www.lakka.tv/

RaspBSD (open source under FreeBSD)
* Customized build of FreeBSD for single-board computers like Raspberry Pi
* Possible reason to use:  MacOS and PS4 are based off FreeBSD, so you can tinker with something similar

RetroPie (open source under GPL)
* Retro gaming-oriented OS that can be installed on top of other OSs
* Website: https://retropie.org.uk/

Ubuntu Core
* Download:  https://ubuntu.com/download/raspberry-pi

Kali Linux
* Security- and forensics-oriented OS (ethical hacking)

Kano (open source under GPLv2)
* This is an educationally-oriented OS designed specifically for teaching children how a computer works, how to write code, and how to put together some basic projects
* What is Kano OS: https://help.kano.me/hc/en-us/articles/360001546340-What-is-Kano-OS-

Chromium OS (open source)
* If all you plan on doing is browsing the web, this will basically turn your Rasberry Pi into something like a Chromebook 

HassOS (open source)
* Stripped down Linux OS for Raspberry Pi intended to run Home Assistant (i.e., this is SmartHome-focused OS)
* Home Assistant Website:  https://www.home-assistant.io/

Mozilla WebThings (open source)
* This OS also has a SmartHome focus
* https://iot.mozilla.org/


SO MANY MORE operating systems are available for Raspberry Pi:
* Ubuntu Mate (open source)
* Ubuntu Server (open source)
* PiNet (open source)
* Linutop (open source)
* OpenMediaVault (open source)
* Gentoo (open source)
* Rokos (open source, MIT)
* Minibian (open source, GPLv2)
* Chromium OS (open source)
* Alpine Linux (open source)

And this list can go technically go on and on (e.g., many more on this page alone:  https://elinux.org/RPi_Distributions).  However, it should also be noted that it seems many of the OSs you can learn and read about, including a few listed above, have become "dead projects" (no further updates or support).

-----------------------------

## Misc

Some Arduino videos I've watched/skimmed:
* [You can learn Arduino in 15 minutes](https://www.youtube.com/watch?v=nL34zDTPkcs)
* YouTube: Eli the Computer Guy: [Arduino Introduction](https://www.youtube.com/watch?v=bY03PJihDMw)
  - playlist: https://www.youtube.com/watch?v=5rr-UmADohs&list=PLJcaPjxegjBUGZ6ao0JRoUwRlYmG9XWKf

More Playlists from Eli the Computer Guy:
* [Arduino Introduction](https://www.youtube.com/watch?v=5rr-UmADohs&list=PLJcaPjxegjBUGZ6ao0JRoUwRlYmG9XWKf)
* [Arduino](https://www.youtube.com/playlist?list=PLJcaPjxegjBUsCc8PDvalF9j9dvc1RpUh)
* [Arduino Sensors](https://www.youtube.com/watch?v=KjJFf_DnKeA&list=PLJcaPjxegjBWG6w_2uccJpXHQa3N6W-P2)
* [Arduino Vehicle](https://www.youtube.com/watch?v=l2WCKQoVdcU&list=PLJcaPjxegjBU9LLgF9dGiIhVTPHrh82N5)
* There a bunch of playlists...

* RPi Projects:  https://www.ubuntupit.com/20-best-raspberry-pi-projects-that-you-can-start-right-now/

### Some Home Assistant Stuff
* https://github.com/home-assistant/operating-system
* https://www.reddit.com/r/homeassistant/comments/9z3nrr/whats_the_difference_between_hassio_hassbian/
* https://community.home-assistant.io/t/hass-vs-hass-io-vs-hassos/130174
* https://community.home-assistant.io/t/homeassistant-for-newcomers-what-it-is-what-is-hassio-hassos-hassbian-101-and-cookies/123004

----------------------------


AVR XMEGA: http://ww1.microchip.com/downloads/en/DeviceDoc/doc7925.pdf
https://www.kanda.com/blog/microcontrollers/avr-xmega-microcontroller-family/

Beetle: https://www.dfrobot.com/product-1075.html

## Week 4: Networking and the Internet

MANet: Mobile Adhoc Network


Why is networking needed?  Easy: to access data or compute not available in a single device.  

For example, imagine all cars were networked: they could plan efficient routes as a holistic organism!

More common example: connecting to Netflix for access to nigh-unlimited media content.

Client-Server Model
* single server, one-to-many clients
* server manages a resource, responds to client requests
```
 ________      request         ________                      __________
|        | -----------------> |        |   handle request   |          |
| CLIENT |                    | SERVER | <----------------> | RESOURCE |
|________| <----------------- |________|                    |__________|
               response
```

LAN: Local Area Network.  Typically spans a building or campus (relatively small network).  You 
hook in through an ethernet cable (or WiFi). 

WAN: Wide Area Network. This is a huge network which you wouldn't call "localized."  For example,
the internet is a WAN.  Basically, it's a network of many LANs. 

MANET:  Mobile Ad Hoc Network.  Continually changing, typicall short-range network composed of wireless, mobile 
devices.  Most common for IoT devices.  (Example: you walk through a MANET area, your cell connects, network
reconfigures to accept connection, you walk out of area, cell disconnects, etc.)


## Historical Provenance

- Historical note: Curated in 2026 from IoT and embedded systems notes originally committed in `krbnite.github.io` from 2020-01-30 to 2020-04-04. The source-note histories were imported into this repository before consolidation.
- Date note: The first source note began in Git on 2020-01-30 and was later standardized under a 2020-02-05 filename. This merged article uses 2020-02-05 to match the original dated course-note sequence.
- Curation note: Four week-level notes were merged into this one article so the IoT learning path reads as a single historical artifact.

### Source Notes

- `2020-02-05-IoT-and-Embedded-Systems-Week-1-What-is-the-IoT.md`
- `2020-02-13-IoT-and-Embedded-Systems-Week-2Embedded-Systems.md`
- `2020-02-13-IoT-and-Embedded-Systems-Week-3-Hardware-and-Software.md`
- `2020-03-12-IoT-and-Embedded-Systems-Week-4-Networking-and-the-Internet.md`
