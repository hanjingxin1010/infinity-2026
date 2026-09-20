from pybricks.parameters import Color
from pybricks.tools import run_task, wait
from pybricks.parameters import Axis, Direction, Port
from robot_config import HUB, CENTER_ATTACHMENT

from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Direction, Port
# set up the attachments, if needed
#CENTER_ATTACHMENT = Motor(Port.D, Direction.COUNTERCLOCKWISE, gears=[20,40])


#this function tests control of center attachment.
async def demo_center_attachment():
    await HUB.speaker.beep()
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [8, 36])
    CENTER_ATTACHMENT.reset_angle(0)

    #need to reset initial position
    CENTER_ATTACHMENT.run_until_stalled(-100,duty_limit=20)


    await CENTER_ATTACHMENT.run_angle(90, 90) #speed, angle
    await wait(500)
    await CENTER_ATTACHMENT.run_angle(60, 180) #speed, angle
    return 
    await CENTER_ATTACHMENT.run_angle(180, -360) 

    #repeat small movements
    for i in range(5):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(180, 90) 
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(180, -90)
 

if __name__ == "__main__":
    run_task(demo_center_attachment())