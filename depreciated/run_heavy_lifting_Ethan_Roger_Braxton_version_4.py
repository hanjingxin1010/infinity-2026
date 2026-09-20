from pybricks.parameters import Color, Direction
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT,BACK_ATTACHMENT

DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)


#use this function as a template to define how to drive the base
async def drive_base_to_heavy_lifting():
    await set_drivebase()
    CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,
                                  gears=[12,36])
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True) 
    await wait(100) #wait for 1000 ms
    await DRIVE_BASE.straight(719)
    await DRIVE_BASE.turn(43)

    #slow down for more precision
    #approach for heavy lifting
    await DRIVE_BASE.straight(80)
    #return
    #perform heavy lifting
    await CENTER_ATTACHMENT.run_angle(100, 95)
    await wait(100)
    await CENTER_ATTACHMENT.run_angle(80,-100)
    
    #swipe lever for rocks
    #await DRIVE_BASE.straight(-10)
    #need to adjust turn rate to be higher to swipe lever faster 
    #so that the rocks will roll further away
    DRIVE_BASE.settings(turn_rate=90,turn_acceleration=90)
    await DRIVE_BASE.turn(-75)
    await DRIVE_BASE.straight(60)

    #push lever
    DRIVE_BASE.settings(turn_rate=40,turn_acceleration=40)
    await DRIVE_BASE.arc(radius=-60, angle=30)
    
    await DRIVE_BASE.straight(-30)
    await DRIVE_BASE.turn(-25)                                             
    
    #go to next mission
    #await DRIVE_BASE.straight(550)
    await DRIVE_BASE.straight(10)
    await multitask(DRIVE_BASE.straight(520),BACK_ATTACHMENT.run_angle(100,93))
    await DRIVE_BASE.turn(45)
    
    #await BACK_ATTACHMENT.run_angle(100,93)
    #await DRIVE_BASE.straight(-300)
    await DRIVE_BASE.straight(-355)
    await wait(800)
    await DRIVE_BASE.straight(90)
    await DRIVE_BASE.turn(-50)
    #await multitask(DRIVE_BASE.straight(100),BACK_ATTACHMENT.run_angle(100,-48))
    #await BACK_ATTACHMENT.run_angle(100,-48)
    
    
    #go back
    #await DRIVE_BASE.straight(20)
    #await DRIVE_BASE.turn(10)
    await DRIVE_BASE.straight(-340)
    #smack
    #await DRIVE_BASE.turn(-10)
    await multitask(DRIVE_BASE.turn(-15),BACK_ATTACHMENT.run_angle(45,-95))
    await CENTER_ATTACHMENT.run_angle(45,90)
    await CENTER_ATTACHMENT.run_angle(45,-90)
    #await BACK_ATTACHMENT.run_angle(45,-45)
    #returning
    await DRIVE_BASE.turn(13)
    await DRIVE_BASE.straight(-470)
        #await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.arc(radius=-70, angle=-90)
   
   
if __name__ == "__main__":
    run_task(drive_base_to_heavy_lifting())