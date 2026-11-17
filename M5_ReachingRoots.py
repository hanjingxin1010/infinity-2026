from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M5():
    DRIVE_BASE.use_gyro(True)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=950,
        straight_acceleration=900,
        turn_rate=500,
        turn_acceleration=400,
    )
    
    await DRIVE_BASE.straight(790)
    await RIGHT_ATTACHMENT.run_angle(1000, 110)
    await wait(500)
    await DRIVE_BASE.straight(100)
    await wait(500)
    #await RIGHT_ATTACHMENT.run_angle(1000, -50)
    await DRIVE_BASE.straight(-100)
    #await DRIVE_BASE.straight(-100)
if __name__ == "__main__":
    run_task(M5())