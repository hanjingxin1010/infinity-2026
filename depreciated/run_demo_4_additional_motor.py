from pybricks.tools import run_task, wait
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor

from robot_config import CENTER_ATTACHMENT, GearSwapMotor
EXTRA_ATTACHMENT = GearSwapMotor(Port.C, Direction.CLOCKWISE)

#this function tests control of center attachment.
async def demo_extra_attachment():
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    EXTRA_ATTACHMENT.reset_angle(0)
    await wait(500)
    await EXTRA_ATTACHMENT.run_angle(300, 360) #speed, angle
    await wait(500)
    await EXTRA_ATTACHMENT.run_angle(300, -360) 
    for i in range(5):
        await wait(500)
        await EXTRA_ATTACHMENT.run_angle(180, 90) 
        await wait(500)
        await EXTRA_ATTACHMENT.run_angle(180, -90)
 

if __name__ == "__main__":
    run_task(demo_extra_attachment())