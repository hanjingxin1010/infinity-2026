from pybricks.tools import run_task, wait
from robot_config import DRIVE_BASE, HUB
from library import set_drivebase

#use this function as a template to define how to drive the base
async def demo_drive_straight_turn():
    await HUB.speaker.beep(500, 1000) #frequency & duration
    await set_drivebase()
    # Turn on Gyro
    DRIVE_BASE.use_gyro(True) 
    await wait(1000) #wait for 1000 ms
    await DRIVE_BASE.straight(50) #go straight forward 50 mm
    await DRIVE_BASE.turn(90) #turn in place (aka tank turn) right 90 degree
    await DRIVE_BASE.turn(-90) #turn in place (aka tank turn) left 90 degree
    await DRIVE_BASE.straight(-50) #go straight forward 50 mm
    DRIVE_BASE.use_gyro(False)


if __name__ == "__main__":
    run_task(demo_drive_straight_turn())