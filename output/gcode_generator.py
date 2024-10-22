import math

def generate_helix_gcode(center_x, center_y, start_z, radius, segments_per_revolution, revolutions, pitch, filename="helix.gcode"):
    """
    Generates G-code for a helical path and writes it to a file.
    
    Parameters:
    center_x (float): The x-coordinate center of the helix.
    center_y (float): The y-coordinate center of the helix.
    start_z (float): The starting height (z-coordinate).
    radius (float): The radius of the helix.
    segments_per_revolution (int): Number of segments per revolution.
    revolutions (int): Number of revolutions.
    pitch (float): The height increment per revolution.
    filename (str): The name of the output file.
    """
    
    extrusion_per_segment = 0.1
    feedrate = 600.0
    total_segments = revolutions * segments_per_revolution

    # Step increments for each segment
    angle_increment = (2 * math.pi) / segments_per_revolution
    height_increment = pitch / segments_per_revolution

    # Initialize G-code
    gcode_lines = [
        "; Initialize settings",
        "G21             ; Set units to mm",
        "G90             ; Absolute positioning",
        "M83             ; Set relative mode for extruder",
        "M107            ; Set fan off to help first layer fasten to build plate",
        "",
        "; Start heating processes",
        "M140 S60        ; Start heating bed to 60 degrees in the background",
        "M104 S200       ; Start heating the extruder to 200 degrees in the background",
        "M190 S60        ; Wait for bed to reach 60 degrees",
        "M109 S200       ; Wait for the extruder to reach 200 degrees",
        "",
        "; Home all axes",
        "G28             ; Home all axes",
        "",
        "; Reset the extruder position",
        "G92 E0          ; Reset the extruder position (to be sure)",
        "",
        f"; Move to the starting point",
        f"G1 X{center_x + radius} Y{center_y} Z{start_z} F6000 ; Move to starting point at a safe speed",
        "",
        "; Start extrusion",
        "G1 F600        ; Set the printing speed",
    ]

    # Generate the helical motion
    current_z = start_z
    for segment in range(total_segments):
        angle = angle_increment * segment
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        current_z += height_increment
        gcode_lines.append(f"G1 X{x:.4f} Y{y:.4f} Z{current_z:.4f} E{extrusion_per_segment:.4f}")

    # End of extrusion
    gcode_lines += [
        "",
        "; Move to a safe position",
        "G1 Z10 F1200    ; Move the nozzle up to 10mm to avoid dragging across the print",
        "",
        "; End of program",
        "M104 S0         ; Turn off extruder heater",
        "M140 S0         ; Turn off bed heater",
        "M84             ; Disable motors",
        "M107            ; Turn off fan",
    ]

    # Write the G-code to a file
    with open(filename, "w") as file:
        for line in gcode_lines:
            file.write(line + "\n")

# Example usage
generate_helix_gcode(
    center_x=110,
    center_y=110,
    start_z=0.2,
    radius=10,
    segments_per_revolution=100,
    revolutions=50,
    pitch=0.4,
    filename="helix.gcode"
)