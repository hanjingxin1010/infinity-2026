from pybricks.parameters import Color, Direction
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase



from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT

#use this function as a template to define how to drive the base
async def drive_base_to_heavy_lifting():
    await set_drivebase()
    CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,
                                  gears=[12,36])
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True) 
    await wait(1000) #wait for 1000 ms
    await DRIVE_BASE.straight(735)
    await DRIVE_BASE.turn(44)
    await DRIVE_BASE.straight(110)

    #perform heavy lifting
    await CENTER_ATTACHMENT.run_angle(45, 90)
    await wait(200)
    await CENTER_ATTACHMENT.run_angle(45,-90)

    #swipe lever for rocks
    await DRIVE_BASE.straight(-10)
    #need to adjust turn rate to be higher to swipe lever faster 
    #so that the rocks will roll further away
    DRIVE_BASE.settings(turn_rate=90,turn_acceleration=90)
    await DRIVE_BASE.turn(-80)
    await DRIVE_BASE.straight(45)

    #push lever
    DRIVE_BASE.settings(turn_rate=40,turn_acceleration=40)
    await DRIVE_BASE.arc(radius=-20, angle=145)
    
    await DRIVE_BASE.straight(70)
    
    DRIVE_BASE.settings(turn_rate=90,turn_acceleration=90)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(-380)
    await DRIVE_BASE.arc(radius=70, angle=-90) #forward left turn 45 degree

    return
    await wait(2000)
    await DRIVE_BASE.straight(500)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(735)
    
    await DRIVE_BASE.straight(740)
    #await DRIVE_BASE.straight(20)
   
if __name__ == "__main__":
    run_task(drive_base_to_heavy_lifting())
