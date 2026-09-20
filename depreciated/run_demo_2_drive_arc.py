from pybricks.tools import run_task, wait

from robot_config import DRIVE_BASE, HUB


async def demo_drive_arc():
    await HUB.speaker.beep()
    await DRIVE_BASE.arc(radius=100, angle=45) #forward right turn 45 degree
    await wait(1000)
    await DRIVE_BASE.arc(radius=100, angle=-45)#backward right turn 45 degree
    await wait(1000)
    await DRIVE_BASE.arc(radius=-100, angle=45) #forward left turn 45 degree
    await wait(1000)
    await DRIVE_BASE.arc(radius=-100, angle=-45) #backward left turn 45 degree
    await wait(1000)

if __name__ == "__main__":
    run_task(demo_drive_arc())