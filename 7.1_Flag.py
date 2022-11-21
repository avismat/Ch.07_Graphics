'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
width,height = 494, 260
arcade.open_window(width, height, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(0,7):
    arcade.draw_rectangle_filled(width/2,height-i*(height/(13/2))-height*(1/13/2),width,height*(1/13),(0xBF,0x0A,0x30))
arcade.draw_lrtb_rectangle_filled(0, height * 0.76, height, height - height * (7 / 13), (0x00, 0x28, 0x68))  # Blue corner
for j in range(0,3):
    for i in range(0,7):
        arcade.draw_text("*",(height*(0.105*i))+(height*0.063)-6,0+(height-(height*0.054*2))-(j*38),arcade.color.WHITE,24)
    for i in range(0,6):
        arcade.draw_text("*",(height*(0.105*i))+(height*0.063)*1.75-5,0+(height-(height*0.054*2)-19)-(j*38),arcade.color.WHITE,24)
for i in range(0,7):
    arcade.draw_text("*",(height*(0.105*i))+(height*0.063)-6,0+(height-(height*0.054*2))-(3*38),arcade.color.WHITE,24)
arcade.finish_render()
arcade.run()