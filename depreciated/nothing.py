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
    await DRIVE_BASE.straight(630)
    
    await DRIVE_BASE.turn(36)
    await DRIVE_BASE.straight(9)
    #slow down for more precision
    #approach for heavy lifting
    await DRIVE_BASE.straight(75)

    await BACK_ATTACHMENT.run_angle(90,130)
    return
    #perform heavy lifting
    await CENTER_ATTACHMENT.run_angle(100, 100)
    await wait(100)
    await CENTER_ATTACHMENT.run_angle(80,-95)
    await DRIVE_BASE.straight(-120)
    await DRIVE_BASE.turn(-40)
    await DRIVE_BASE.straight(150)
    await BACK_ATTACHMENT.run_angle(123,-200)
    
    

if __name__ == "__main__":
    run_task(drive_base_to_heavy_lifting())