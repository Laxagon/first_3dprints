; Initialize settings
G21             ; Set units to mm
G90             ; Absolute positioning
M83             ; Set relative mode for extruder
M107            ; Set fan off to help first layer fasten to build plate

; Start heating processes
M140 S60        ; Start heating bed to 60 degrees in the background
M104 S200       ; Start heating the extruder to 200 degrees in the background
M190 S60        ; Wait for bed to reach 60 degrees
M109 S200       ; Wait for the extruder to reach 200 degrees

; Home all axes
G28             ; Home all axes

; Reset the extruder position
G92 E0          ; Reset the extruder position (to be sure)

; Move to the starting point
G1 X1 Y40 Z0.2 F6000 ; Move to starting point at a safe speed

; Start extrusion of line
G1 F600         ; Set the printing speed
G1 X192 E19     ; Move to X=192, Y=40 while extruding 19mm of filament

; Start extrusion of helix



; End of extrusion

; Optional: Move to a safe position
G1 Z10 F1200    ; Move the nozzle up to 10mm to avoid dragging across the print

; End of program
M104 S0         ; Turn off extruder heater
M140 S0         ; Turn off bed heater
M84             ; Disable motors
M107            ; Turn off fan