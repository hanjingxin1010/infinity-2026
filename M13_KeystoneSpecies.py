
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, DRIVE_LEFT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M13():
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=400,
        turn_rate=600,
        turn_acceleration=600,
    )
    DRIVE_BASE.use_gyro(True)
    
    await DRIVE_BASE.straight(700)
    await DRIVE_BASE.turn(43)
    await DRIVE_BASE.straight(130)
    await DRIVE_BASE.straight(-75)
    await DRIVE_BASE.turn(23)
    
    await RIGHT_ATTACHMENT.run_angle(100,-40)
    await RIGHT_ATTACHMENT.run_angle(900,40)
     
    #await DRIVE_RIGHT.run_angle(300,-200
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=900,
        straight_acceleration=900,
        turn_rate=900,
        turn_acceleration=900,
    )
    await DRIVE_LEFT.run_angle(500,-500)
    await DRIVE_BASE.straight(-800)
    #await DRIVE_BASE.turn(-60)
"""
    await multitask(
        LEFT_ATTACHMENT.run_target(360, 50),
        RIGHT_ATTACHMENT.run_target(360, 40),
        DRIVE_BASE.straight(-800),
    )
   """ 
if __name__ == "__main__":
    run_task(M13())