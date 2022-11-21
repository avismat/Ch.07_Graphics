#Sign your name: Matthew A

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
clr = arcade.color

arcade.open_window(500,400)
window = arcade.get_window()

arcade.set_background_color(clr.ALMOND)
arcade.start_render()

for i in range(25):  # Grid loop
    arcade.draw_line(i*window.width/25,0,i*window.width/25,window.height,clr.BLACK)
    arcade.draw_line(0,i*window.width/25,window.width,i*window.width/25, clr.BLACK)

arcade.draw_lrtb_rectangle_filled(20,80,380,360,clr.PHLOX)  # Pink rectangle thing

arcade.draw_rectangle_filled(200,260,40,20,clr.BLUSH,-45)  # Tilted rectangle

arcade.draw_circle_filled(250,200,40,clr.WISTERIA)  # Middle circle

arcade.draw_text("I love you. I know.",20,160,clr.BRICK_RED,20)  # Text

arcade.draw_ellipse_filled(100,100,120,40,clr.AMBER)  # Ellipse

arcade.draw_line(80,20,120,60,clr.BLUE)  # Line

arcade.draw_arc_filled(400,320,120,120,clr.YELLOW,30,330)  # Pac Man

arcade.draw_point(460,10,clr.RED,5)  # Red dot

arcade.finish_render()
arcade.run()