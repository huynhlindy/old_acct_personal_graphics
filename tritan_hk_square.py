import arcade
import random
palette = ["dd4444", "f48080", "2d676f", "194b4f"]  # put colors that you want to use here (hex strings only)
highlight = "ffdcdc"  # color for corner squaree

size = int(input("How many pixels would you like it to be?"))
arcade.open_window(size, size, "Hollow Knight")
arcade.set_background_color(arcade.color_from_hex_string(highlight))
counter = 0
# PARAMETRICS
# circle size - between (height and width / 20) and (height and width / 35)
minsize = round(size/40)
maxsize = round(size/25)
# square size - height and width / 10
square_size = round(size/10)
# corner square size - height and width / 25
corner = round(size/25)
# PIXEL ART PARAMETRICS
x_pos = round(size/3.5)  # these are complete eyeball estimates so they may need adjustment in the future
y_pos = round(size/1.25)  # these are complete eyeball estimates so they may need adjustment in the future
p_size = round(size/85)
loops = round(size*size/50)

arcade.start_render()
for x in range(loops): # background
    cs = random.randint(minsize, maxsize)
    mixer = random.randint(1, size)
    mixer2 = random.randint(1, size)
    arcade.draw_circle_filled(mixer, mixer2, cs, arcade.color_from_hex_string(random.choice(palette)))
    counter += 1
    if counter % 20 == 0:
        smixer = random.randint(1, size)
        smixer2 = random.randint(1, size)
        color = random.choice(palette)
        arcade.draw_rectangle_outline(smixer, smixer2, square_size, square_size, arcade.color_from_hex_string(color), square_size/6.75)
        # crosses in boxes to make them look like crates
        left = smixer - (square_size/2); right = smixer + (square_size/2)  # left and right coords for lines
        top = smixer2 + (square_size/2); bot = smixer2 - (square_size/2)  # top and bottom coords for lines

        arcade.draw_line(left, top, right, bot, arcade.color_from_hex_string(color), square_size/6.75)
        arcade.draw_line(right, top, left, bot, arcade.color_from_hex_string(color), square_size/6.75)
arcade.draw_rectangle_filled(corner, corner, corner, corner, arcade.color_from_hex_string(highlight))
arcade.draw_rectangle_filled((size-corner), (size-corner), corner, corner, arcade.color_from_hex_string(highlight))  # corner squares

# actual drawing now

# colors
# #d9d9d9 - base = 2
# #1f1f1f - outline/shadow = 1
# #4a4a4a - cloak = 3
# #757575 - nail = 4
# empty = 0

row1 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
row2 = [0, 0, 0, 0, 1, 1, 2, 2, 2, 1]
row3 = [0, 0, 0, 1, 2, 2, 2, 2, 2, 1]
row4 = [0, 0, 0, 1, 2, 2, 2, 2, 1]
row5 = [0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
row6 = [0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1]
row7 = [0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1]
row8 = [0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1]
row9 = [0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1]
row10 = [0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1]
row11 = [0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 1]
row12 = [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1]
row13 = [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1]
row14 = [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]
row15 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row16 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row17 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row18 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
row19 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1]
row20 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row21 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row22 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row23 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row24 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1]
row25 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1]
row26 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row27 = [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row28 = [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row29 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1]
row31 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1]
row32 = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1]
row33 = [0, 1, 3, 3, 3, 3, 1, 1, 1, 0, 0, 1, 1, 3, 3, 1, 3, 3, 1, 3, 3, 3, 1]
row34 = [0, 0, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 3, 3, 3, 1]
row35 = [0, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1]
row36 = [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 1, 3, 1, 1, 1, 3, 1, 3, 1]
row37 = [0, 0, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 3, 3, 1, 1, 1, 3, 3, 1, 1]
row38 = [0, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 3, 1]
row39 = [0, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1]
row40 = [0, 0, 1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
row41 = [0, 0, 0, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1]
row42 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1]
row43 = [0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1]
row44 = [0, 0, 0, 0, 0, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1]
row45 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1]
row46 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 4, 1, 1, 4, 4, 1, 1]
row47 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 1,
         1]
row48 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4,
         4, 1, 1]
row49 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
         1, 4, 4, 1, 1]
row50 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 1, 1, 1]
row51 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11,
        row12, row13, row14, row15, row16, row17, row18, row19, row20, row21,
        row22, row23, row24, row25, row26, row27, row28, row29, row30, row31,
        row32, row33, row34, row35, row36, row37, row38, row39, row40, row41,
        row42, row43, row44, row45, row46, row47, row48, row49, row50, row51]

x_offset = 0
y_offset = 0

for row in rows:
    x_offset = 0
    for pixel in row:
        if pixel == 0:
            x_offset += p_size
        if pixel == 1:
            arcade.draw_rectangle_filled(x_pos + x_offset, y_pos - y_offset, p_size, p_size,
                                         arcade.color_from_hex_string("1f1f1f"))
            x_offset += p_size
        if pixel == 2:
            arcade.draw_rectangle_filled(x_pos + x_offset, y_pos - y_offset, p_size, p_size,
                                         arcade.color_from_hex_string("d9d9d9"))
            x_offset += p_size
        if pixel == 3:
            arcade.draw_rectangle_filled(x_pos + x_offset, y_pos - y_offset, p_size, p_size,
                                         arcade.color_from_hex_string("4a4a4a"))
            x_offset += p_size
        if pixel == 4:
            arcade.draw_rectangle_filled(x_pos + x_offset, y_pos - y_offset, p_size, p_size,
                                         arcade.color_from_hex_string("757575"))
            x_offset += p_size
    y_offset += p_size
# for row in list "rows"; for each number in the row, fills in a pixel which then increases offsets to move next pixel
arcade.finish_render()

arcade.run()