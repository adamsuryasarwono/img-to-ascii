import cv2
import numpy as np
import sys
import time

IMG_PATH = "squidward.jpg"  
TERMINAL_WIDTH = 100    
PRINT_DURATION = 5.0    

ASCII_CHARS = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqgdpbkhagW#M%&B@$"

img = cv2.imread(IMG_PATH)
if img is None:
    print(f"Error: tidak dapat memuat gambar: {IMG_PATH}")
    sys.exit(1)

h, w, _ = img.shape
aspect_ratio = h / w
new_height = int(aspect_ratio * TERMINAL_WIDTH * 0.55) 
img = cv2.resize(img, (TERMINAL_WIDTH, new_height))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.convertScaleAbs(gray, alpha=1.2, beta=0)

output_lines = []
for y in range(new_height):
    line = []
    for x in range(TERMINAL_WIDTH):
        brightness = gray[y, x]
        r, g, b = img_rgb[y, x]

        char_index = int(brightness / 255 * (len(ASCII_CHARS) - 1))
        char = ASCII_CHARS[char_index]
        
        line.append(f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m")
    output_lines.append("".join(line))

total_lines = len(output_lines)
delay_per_line = PRINT_DURATION / total_lines 

for line in output_lines:
    print(line)
    time.sleep(delay_per_line)