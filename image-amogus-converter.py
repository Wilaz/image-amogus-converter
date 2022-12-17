# Imports Pillow
from PIL import Image


# Gets file locations
Input_img_path = input("Enter the path to the image you wish to amogify: ")
Output_img_path = input("Enter a path to output to: ")

# Opens first input
Input = Image.open(Input_img_path).convert('RGBA')

# Creates second input
Output = Image.new('RGBA', tuple(5 * elem for elem in Input.size))

# Converts image
for Y in range(Input.size[1]):
    for X in range(Input.size[0]):
        Pixel = Input.getpixel((X, Y))

        for Y2 in range(5):
            for X2 in range(5):
                Location = str(X2) + str(Y2)
                
                if Location == "21" or Location == "31":
                    Output.putpixel((X * 5 + X2, Y * 5 + Y2), tuple(sorted((0, round(elem * 1.2), 255))[1] for elem in Pixel))

                elif Location == "00" or Location == "40" or Location == "41" or Location == "42"or Location == "43" or Location == "04" or Location == "24" or Location == "44":
                    Output.putpixel((X * 5 + X2, Y * 5 + Y2), tuple(sorted((0, round(elem * 1.1), 255))[1] for elem in Pixel))
                
                else:
                    Output.putpixel((X * 5 + X2, Y * 5 + Y2), Pixel)

# Saves output
Output.save(Output_img_path)

# Tells user that conversion is done
print("Done converting: " + Input_img_path)
print("Output can be found at: " + Output_img_path)
