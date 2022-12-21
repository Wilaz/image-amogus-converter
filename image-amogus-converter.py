# Imports Pillow
from PIL import Image
import time
from tqdm import tqdm

start_time = time.time()

# Gets file locations
Input_img_path = input("Enter the path to the image you wish to amogify: ")
Output_img_path = input("Enter a path to output to: ")
Generation_type = int(input("What generation type would you like to use? (1. Scaled, 2. Compressed): "))
print("\nGenerating...")

# Opens first input
Input = Image.open(Input_img_path).convert('RGBA')

# Creates second input
Output = Image.new('RGBA', tuple(5 * i for i in Input.size))

# Converts a pixel into a 5x5 sussy amogus dud
def render_amogus(Pixel, X, Y):
    # These arrays represent the coordinates for each part of an amogus
    eye = [[2, 1], [3, 1]]
    background = [[0, 0], [4, 0], [4, 1], [4, 2], [4, 3], [0, 4], [2, 4], [4, 4]]
    
    for Y2 in range(5):
        for X2 in range(5):
            new_pixel_location = (X * (abs(Generation_type-2)*4+1) + X2, Y * (abs(Generation_type-2)*4+1) + Y2)

            if [X2, Y2] in eye: 
                Output.putpixel(new_pixel_location, tuple(sorted((0, round(elem * 1.2), 255))[1] for elem in Pixel))
            elif [X2, Y2] in background: 
                Output.putpixel(new_pixel_location, tuple(sorted((0, round(elem * 1.4), 255))[1] for elem in Pixel))
            else: Output.putpixel(new_pixel_location, Pixel)

# # Converts image
# for Y in range(Input.size[1]):
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = [executor.submit(render_amogus, Input.getpixel((X, Y)), X, Y) for X in range(Input.size[0])]

for Y in tqdm(range(0, Input.size[1], (Generation_type-1)*4+1)):
    for X in tqdm(range(0, Input.size[0], (Generation_type-1)*4+1), leave=False):
        render_amogus(Input.getpixel((X,Y)), X, Y)

if (Generation_type == 2):
    Output = Output.crop((0, 0, Input.size[0], Input.size[1]))

# Saves output
Output.save(Output_img_path)

# Tells user that conversion is done
print("\n--- %s seconds ---" % (time.time() - start_time))
print("Done converting: " + Input_img_path)
print("Output can be found at: " + Output_img_path + "\n")
