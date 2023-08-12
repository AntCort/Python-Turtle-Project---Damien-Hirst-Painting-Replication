import colorgram

class ColorExtractor:
    def __init__(self):
        self.image_path = '537b6eca8c43b46982da4c2af786fb1124592d0a-1200x995.webp'

    def extract_colors(self):
        # Extract colors from the image
        colors = colorgram.extract(self.image_path, 80)
        # Creating the list that will contain all colors
        color_from_picture = []
        # Convert RGB to hexadecimal color code and
        # appending them to the list
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            color_code = "#{:02X}{:02X}{:02X}".format(r, g, b)
            color_from_picture.append(color_code)
        return color_from_picture
