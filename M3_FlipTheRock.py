from pybricks.tools import multitask, run_task
from library import set_drivebase
from robot_config import DRIVE_BASE, RIGHT_ATTACHMENT

async def M3():
    DRIVE_BASE.use_gyro(True)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=300,
        turn_rate=100,
        turn_acceleration=400,
    )
    print("going to flip the rock")
    await RIGHT_ATTACHMENT.run_angle(180, -100)
    await DRIVE_BASE.straight(500),
    await DRIVE_BASE.straight(-200)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=800,
        straight_acceleration=1000,
        turn_rate=300,
        turn_acceleration=600,
    )
    await DRIVE_BASE.turn(45)
    await DRIVE_BASE.straight(400)
    await DRIVE_BASE.turn(-85)
    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=100,
        turn_rate=300,
        turn_acceleration=600,
    )
    await RIGHT_ATTACHMENT.run_angle(180, 160)
    await DRIVE_BASE.straight(310)
    await RIGHT_ATTACHMENT.run_angle(180, -100)
    DRIVE_BASE.settings(
        straight_speed=800,
        straight_acceleration=1000,
        turn_rate=300,
        turn_acceleration=600,
    )
    await DRIVE_BASE.straight(-440)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(400)
if __name__ == "__main__":
    run_task(M3())
