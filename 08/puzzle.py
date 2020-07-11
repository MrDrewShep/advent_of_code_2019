# PART ONE
# The image you received is 25 pixels wide and 6 pixels tall. 
# To make sure the image wasn't corrupted during transmission, 
# the Elves would like you to find the layer that contains the 
# fewest 0 digits. On that layer, what is the number of 1 digits 
# multiplied by the number of 2 digits?

from pprint import pprint

def get_image():
    with open("data.txt", "r") as f:
        image = f.read()
        image = [int(i) for i in image]
    return image


class Layer():

    def __init__(self, raw_data, image):
        self.parent_image = image
        self.raw_data = raw_data
        self.rows = []
        self.create_rows()

    def __repr__(self):
        return f'{self.rows}'

    def create_rows(self):
        i = 0
        while i < self.parent_image.layer_size:
            row = [dig for dig in self.raw_data[i:i + self.parent_image.img_width]]
            self.rows.append(row)
            i += self.parent_image.img_width


class Image():

    def __init__(self, raw_data, img_width, img_height):
        self.raw_data = raw_data
        self.img_width = img_width
        self.img_height = img_height
        self.layer_size = img_width * img_height
        self.layers = []
        self.create_layers()

    def create_layers(self):
        if len(self.raw_data) % self.layer_size != 0:
            print(f'Image input is an unexpected size based upon ' \
                f'layer dimensions width {self.img_width} height ' \
                    f'{self.img_height}')
            return
        
        i = 0
        while i < len(self.raw_data):
            layer = Layer(self.raw_data[i:i + self.layer_size], self)
            self.layers.append(layer)
            i += self.layer_size

    def check_sum(self):
        fewest_0s = 99999999
        product = 0
        for layer in self.layers:
            count_0s = 0
            count_1s = 0
            count_2s = 0
            for row in layer.rows:
                for digit in row:
                    if digit == 0:
                        count_0s += 1
                    elif digit == 1:
                        count_1s += 1
                    elif digit == 2:
                        count_2s += 1
            if count_0s < fewest_0s:
                fewest_0s = count_0s
                product = count_1s * count_2s
        
        return product

    def decode(self):
        decoded_layer = []
        for _ in range(self.img_height):
            row = []
            for _ in range(self.img_width):
                row.append(2)
            decoded_layer.append(row)

        for layer in self.layers:
            row_index = 0
            for row in layer.rows:
                col_index = 0
                for digit in row:
                    if decoded_layer[row_index][col_index] != 2:
                        col_index += 1
                        continue
                    else:
                        decoded_layer[row_index][col_index] = digit
                    col_index += 1
                row_index += 1

        print_string = "\n"

        for row in decoded_layer:
            for col in row:
                if col == 0:
                    print_string += " "
                elif col == 1:
                    print_string  += "#"
            print_string += "\n"

        return print_string

image = Image(get_image(), 25, 6)
print(image.check_sum())

# PART TWO
# What message is produced after decoding your image?

print(image.decode())