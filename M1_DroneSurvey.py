from pybricks.tools import run_task
from library import set_drivebase
from robot_config import DRIVE_BASE

async def main():
	DRIVE_BASE.use_gyro(True)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=300,
		straight_acceleration=300,
		turn_rate=100,
		turn_acceleration=400,
	)
	print("Driving forward 100 mm")
	await DRIVE_BASE.straight(630)
	print("Drone off map (20) and Turning left 48 degrees")
	await DRIVE_BASE.turn(-50)
	await DRIVE_BASE.turn(55)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=800,
		straight_acceleration=1000,
		turn_rate=200,
		turn_acceleration=300,
	)
	print("Going to next task")
	await DRIVE_BASE.straight(-1030)

	print("Return complete")

if __name__ == "__main__":
	run_task(main())
