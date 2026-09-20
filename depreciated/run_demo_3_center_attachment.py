from pybricks.parameters import Color
from pybricks.tools import run_task, wait
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import Motor
from robot_config import HUB, CENTER_ATTACHMENT


#this function tests control of center attachment.
async def demo_center_attachment():
    await HUB.speaker.beep()
    #configure the attachement according to your attachment design
    CENTER_ATTACHMENT.reconfigure(Direction.CLOCKWISE, [12, 36])
    
    # for precision control, reset angle at the beginning.
    CENTER_ATTACHMENT.reset_angle(0)

    await CENTER_ATTACHMENT.run_angle(720, -90) #speed, angle
    await wait(1000)
    for i in range(2):
        await CENTER_ATTACHMENT.run_angle(720, 90) #speed, angle
        await wait(100)
        await CENTER_ATTACHMENT.run_angle(720, -90) #speed, angle
    
    await CENTER_ATTACHMENT.run_angle(720, 90) #speed, angle


 

if __name__ == "__main__":
    #CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])
    #CENTER_ATTACHMENT = Motor(Port.D, Direction.COUNTERCLOCKWISE, gears=[12,36])
    #demo_center_attachment()
    # must use run_task to run a program, otherwise it will not run.
    run_task(demo_center_attachment())