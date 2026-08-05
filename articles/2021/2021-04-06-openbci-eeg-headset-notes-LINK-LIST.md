
---
title: OpenBCI EEG Headset Notes (LINK-LIST)
layout: post
tags: eeg openbci brainflow digital-health sensors link-list
---

# OpenBCI EEG Headset Notes (LINK-LIST)

These are 2021 setup notes and reading links from a first pass through OpenBCI Ganglion, the OpenBCI GUI, BrainFlow, and EEG headset resources.




Today, I'm following along with some intro tutorials:
* [Getting Started - GanglionGS](https://docs.openbci.com/docs/01GettingStarted/01-Boards/GanglionGS)
* [Installing the OpenBCI GUI](https://docs.openbci.com/docs/06Software/01-OpenBCISoftware/GUIDocs#installing-the-openbci-gui-as-a-standalone-application)
* [OpenBCI EEG Headband Kit Guide](https://docs.openbci.com/docs/04AddOns/01-Headwear/HeadBand)
* [OpenBCI EEG Setup](https://docs.openbci.com/docs/01GettingStarted/02-Biosensing-Setups/EEGSetup)
* [OpenBCI GUI Widgets](https://docs.openbci.com/docs/06Software/01-OpenBCISoftware/GUIWidgets)
* [OpenBCI Downloads](https://openbci.com/downloads)
  - this is where to get the GUI, but has many other downloads available, such as Ganglion 
    firmware updates and the 3D-print instructions for the Ultrcortex EEG Headset 


Probably won't get to...
* BrainFlow
  - BrainFlow is OpenBCI's recommended software library, which is a universal BCI package that 
    OpenBCI now uses instead of their former OpenBCI-specific python package [pyOpenBCI](https://github.com/openbci-archive/pyOpenBCI)
  - [BrainFlow+OpenBCI](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#openbci)
  - [BrainFlow Examples](https://brainflow.readthedocs.io/en/stable/Examples.html)
* [OpenBCI+MNE](https://github.com/openbci-archive/OpenBCI_MNE)
* [Create Custom OpenBCI-GUI Widget](https://docs.openbci.com/docs/06Software/01-OpenBCISoftware/GUIWidgets#custom-widget)


Might be nice to buy in the future
* [Ultracortex "Mark IV" EEG Headset](https://shop.openbci.com/collections/frontpage/products/ultracortex-mark-iv)


-------


# OpenBCI GUI
* Download for Mac: [dmg](https://github.com/OpenBCI/OpenBCI_GUI/releases/download/v5.0.4/openbcigui_v5.0.4_2021-03-27_02-03-22_macosx.dmg) 
* Make a convenient alias that gets sourced in `.bash_profile`:
  - `alias openbci="open /Applications/OpenBCI_GUI/"`

# Ganglion Setup
* Remove Ganglion (board) from packaging
* Plug in the 4 plastic legs that are provided
* Attach the 6V battery case to the Ganglion ("outlet" located on underside)
* Place 4 AA batteries in the 6V battery case
* To see if it's working: 
  - do not yet open the OpenBCI GUI
  - click the "on" switch (located on left side of 
    Ganglion wrt to the OpenBCI logo) 
  - the blue LED should be blinking (signal indicating the Ganglion is not 
    yet wirelessly connected to your computer)

# Data Streaming (Accelerometer)
* Before opening the OpenBCI GUI, place the Ganglion Dongle into one of your 
  computer's USB ports
* Turn the Ganglion on (switch on leftside wrt Ganglion logo)
* Open the GUI (e.g., `openbci` at the command line if you've made an alias)
* At top-left corner, click on "System Control Panel"
  - then "Ganglion (live)"
  - select the Bluetooth transfer protocol
  - select the Ganglion device when it shows up in device list
  - give the streaming session a name 
    * defaults to `YYYY-MM-DD_HH-MM-SS`
    * using the default as a prefix, I added something a little more 
      descriptive ("_first-run-accel-test")
    * file save location defaults to `~/Documents/OpenBCI_GUI/Recordings/`
* Change Layout (generally optional)
  - click on "Layout" in top-right corner
  - choose from a number of presets
  - in the tutorial, we choose the 3-panel option with 1 large LHS panel
    and 2 panels stacked vertically on the RHS
    * LHS: time series plots for 4 electrodes, which I did not have connected
    * RHS-Top: FFT 4-channel electrode plot (traces overplotted)
    * RHS-Bot: Accelerometer panel
* Turn accelerometer on 
  - NOTES
    * for most EEG recordings, there will be no need to turn the Ganglion's
      accel on since the Ganglion just sits idly on a table; however, if we 
      were to do some ambulatory EEG experiments with the Ganglion housed in 
      a protective container clipped to a belt or something, then accel would 
      be awesome
    * for this tutorial, we turn the accel on as a simple first step in 
      messing around with the Ganglion and OpenBCI GUI
  - To turn on: click on "Turn Accel On" on top-right of accel's panel
    * Note that the FFT plot above the accel panel corresponds to the electrode
      time series, not the accel time series




