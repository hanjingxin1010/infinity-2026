from pybricks.tools import multitask, run_task, wait
from robot_config import CENTER_ATTACHMENT, DRIVE_BASE, FRONT_ATTACHMENT
DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
async def subtask_test_center_attachment():
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-706.7)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-125)
    await DRIVE_BASE.turn(-20)
    await FRONT_ATTACHMENT.run_angle(9999, -1500)
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.straight(150)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(-650)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-141)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(121)
    await CENTER_ATTACHMENT.run_angle(500, 75.67416741674167416741674167416741674167416741)
    wait(500)
    await DRIVE_BASE.straight(-60)
    await CENTER_ATTACHMENT.run_angle(500, -75.67416741674167416741674167416741674167416741)
    await DRIVE_BASE.straight(200)
    await DRIVE_BASE.straight(-500)
  
async def main():
    await multitask(
        wait(0),
        subtask_test_center_attachment()
    )
run_task(main())
if "__file__" == "__main__":
    run_task(main())