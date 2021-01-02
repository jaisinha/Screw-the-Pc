import rotatescreen
import time
screen=rotatescreen.get_primary_display()
#screen.rotate_to(0)
#print(31 % 3)
for i in range(13):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)
