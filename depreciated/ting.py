from pybricks.parameters import Color, Direction
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT,FRONT_ATTACHMENT

DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)

#use this function as a template to define how to drive the base
#drive_base_to_heavy_lifting
async def run1():
    await set_drivebase()
    CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,
                                  gears=[12,36])
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True) 
    await DRIVE_BASE.straight(660)
    #return
    await DRIVE_BASE.turn(44)
    #return
    #slow down for more precision
    #approach for heavy lifting 
    await DRIVE_BASE.straight(135)
    #return
    #await DRIVE_BASE.turn(-16)
    #await DRIVE_BASE.straight(125)
    #return
    #await DRIVE_BASE.turn(-35)
    #await DRIVE_BASE.straight(31)
    #return
    
    await wait(100)
    #await BACK_ATTACHMENT.run_angle(799,160)
    await wait(100)
    #return
    #perform heavy lifting
    #await CENTER_ATTACHMENT.run_angle(100, 110)
    await wait(255)
    await multitask(FRONT_ATTACHMENT.run_angle(799,160), CENTER_ATTACHMENT.run_angle(100, 110))
    #return
    await CENTER_ATTACHMENT.run_angle(70,-120)
    #return 
    #await BACK_ATTACHMENT.run_angle(799,160)
    await DRIVE_BASE.straight(-120)
    await FRONT_ATTACHMENT.run_angle(500,100)
    #await multitask(BACK_ATTACHMENT.run_angle(799,160), CENTER_ATTACHMENT.run_angle(100, 110))
    await DRIVE_BASE.turn(-40)
    await DRIVE_BASE.straiht(140)
    await DRIVE_BASE.turn(-10)
    await FRONT_ATTACHMENT.run_angle(200,-90)
    await DRIVE_BASE.straight(-799)
    
    

if __name__ == "__main__":
    run_task(run1())