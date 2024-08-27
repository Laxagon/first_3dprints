# Assignment 1 - IN5590

- https://www.uio.no/tjenester/it/ki/gpt-uio
- https://claude.ai

### Intro
In this project, we will look at the low levels of 3D printing and make and test our own G-code on the Ender 3. We will also design a simple cube in SolidWorks with overhang, and experience the need for support in certain situations.

Make sure to follow our [guides](https://www.uio.no/studier/emner/matnat/ifi/IN5590/h24/guides/) on [*General requirements for assignments in IN5590*](https://www.uio.no/studier/emner/matnat/ifi/IN5590/h24/guides/general_requirements.html) and [*GitHub guide for assignments*](https://www.uio.no/studier/emner/matnat/ifi/IN5590/h24/guides/github_guide.html).

### Requirements
- All custom G-code to be printed must first be loaded into Cura to make sure the printer head is not commanded to move outside its physical limits (crash)
- When you power on your printer the first time in your session - always first run "Prepare - Auto home" from the printer display, otherwise the printer may crash.
- When you leave the printer - TURN IT OFF, as we typically let the heater elements be on during experiments to save time
- Before any extrusion commands (Ex) the code must include a blocking command (M109 S200) to make sure the nozzle is hot enough to extrude, otherwise, parts of the filament will be destroyed
- All point that are numbered in this text must be done to pass this assignment

### Tips
- It is possible to print over USB, but we do not recommend it
- It may be a good idea to take out your printer from the rack and locate it close to your PC on a table during these experiments
- It is not necessary to run printer calibration during this project. "Prepare - Auto home" will be enough
  - When starting a new print job (with or without filemant extrusion) make sure the calibration option is off
- To save time, it is not necessary to run G28 (home axis) when you have run "Prepare - Auto home" once
- You will typically need to plug in/out your SD card many times during this exercise. You will save time not ejecting it before removal (there may be a small risk of losing data)
 
### For all examples under, finalize your code with 
  - M84; Disable all stepper motors to reduce heat
  - It will save you time to not shut off the heating elements between each run from your G-code, but remember to shut off the printer power when you leave the printer 

### Running the stepper motors with no extrusion

1) Run "Prepare - Auto home" from the printer display (if not done yet after power up)
2) Move nozzle to position x = 10mm, y = 40mm, z = 20mm via a single G1 command. Speed = 10000 mm/min
3) Move nozzle to position x = 110mm with a speed of 11000 mm/min
4) Move nozzle to position x = 10mm with a speed of 12000 mm/min
5) Repeat point 3/4 with an increasing speed until the nozzle do not move faster (listen to the motor sound). What is the maximum speed? 

#### Making a circular motion with no extrusion

6) We want to run the nozzle in a helical motion with the center in x = 110mm, y = 110mm, starting from z = 0.2mm, 5 revolutions, and a pitch (height increment per revolution) of 0.4mm, and a radius of 10mm. We want to make the helix by many short G1 line commands (100 lines per revolution). Ask GPT4 or Claude to make a Python function that can take in the center point, start height, radius, number of segments per revolution, number of revolutions, and pitch. Then run this helix on the printer with a speed of 3000mm/min with no filament extrusion

### Extruding PLA

- NB:
  - The temperature on the nozzle must be 200 degrees before any extrusion (Ex) motion is done (M109 S200), otherwise the nozzle will be blocked and the extruder gear will "eat up" the PLA filament
  - The extrusion length (volume) of the filament must match the length of the XYZ line the nozzle/head moves. If to too much filament is extruded per mm nozzle motion - the extrusion will be blocked and the extruder will "eat up" the PLA filament. Then the filament must be manually pushed into the extruder to continue
  - A thick printed single wall line in the X direction with a layer height of 0.4mm can be made by an extrusion length/nozzle motion length ratio (E/X) of: E = X/10   
  - A safe printing speed can be 600mm/min 

#### Header for all extrusion examples
- M83 ; Set relative modus for extruder, makes our examples easier to implement
- M107 ; Set fan off to help first layer fasten to build plate
- M140 S60 ; Start heating bed to 60 degrees in the background
- M104 S200 ; Start heating the extruder to 200 degrees in the background
- M190 S60 ; Wait for bed to reach 60 degrees
- M109 S200 ; Wait for the extruder to reach 200 degrees
- G92 E0 ; Reset the extruder position (to be sure)

7) We want to extrude a 191mm long line at a height of 0.2mm in the X direction from the starting point X = 1mm, Y = 40mm. An ok extrusion length of E19 is fine to make a very thick line. A safe printing speed of 600mm/min is ok. Notice that it takes some time for the filament to appear at the nozzle, thus the choice of the long line

8) After the line in 7) is printed, print the helix with a layer height of 0.4mm. All G1 segment lengths should be equal to make it simple. If you use the same helix parameters as before, and 50 revolutions, a proper E value is 0.1. Use F600.0. Take a picture of the result similar to `./output/ob1.png` below including that includes the name of the printer. 

<img src="./output/ob1.png" alt="Alt text" width="300" height="200">

9) Make a 15mm x 30mm x 15mm cube in SolidWorks with one wall increasing in steepness from 90 degrees to 0 degrees as shown in the picture. Use Cura with no support, and print it out on the Ender to get an idea on how the printer handles steep overhangs. Make a 0.4mm debossed number on top representing your group number. Take a screenshot similar to the one below and save it as `./output/cube.png`. Additionally, save the SolidWorks file as `./output/cube.sldprt`

<img src="./output/cube.png" alt="Alt text" width="300" height="200">

### FUN 
You can make music on 3D printers
- https://www.youtube.com/watch?v=LOWB9ZnZVhY
- https://www.youtube.com/watch?v=8jDROj236R4



### Deliverables

- Picture of the printed part in the tray stored as `./output/ob1.png` \*
- Screenshot from SolidWorks of the cube stored as `./output/cube.png` \*
- SolidWorks file stored as `./output/cube.sldprt`

\* Replace the existing files in this repo with your own.


-) Szczepan Praetextatus
