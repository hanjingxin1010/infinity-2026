

from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, RIGHT_ATTACHMENT


#WHEEL_DIAMETER = 56
#ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def test_run():
	DRIVE_BASE.use_gyro(True)
	await wait(1000)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=200,
		turn_rate=600,
		turn_acceleration=600,
	)
	await multitask(
		RIGHT_ATTACHMENT.run_angle(100000000, -127),
		DRIVE_BASE.straight(20),
	)

	#print("Driving forward one wheel rotation")
	#await DRIVE_BASE.straight(ONE_WHEEL_ROTATION)
	#print("Driving backward one wheel rotation")
	#await DRIVE_BASE.straight(-ONE_WHEEL_ROTATION
	#await DRIVE_BASE.straight(300)
	#await DRIVE_BASE.straight(-300)
	#await DRIVE_BASE.turn(90)
	#await DRIVE_BASE.straight(100)

if __name__ == "__main__":
	run_task(test_run())
