from pybricks.parameters import Color
from pybricks.tools import run_task, wait
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import Motor
from robot_config import HUB, CENTER_ATTACHMENT


#this function tests control of center attachment.
async def demo_center_attachment_2():
    await HUB.speaker.beep()
    #change rotation direction and the gear configuration to make the code more intuitive
    CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    CENTER_ATTACHMENT.reset_angle(0)

    await CENTER_ATTACHMENT.run_angle(45, 45) #speed, angle
    await wait(1000)
    await CENTER_ATTACHMENT.run_angle(45, -45) #speed, angle

 

if __name__ == "__main__":
    run_task(demo_center_attachment_2())