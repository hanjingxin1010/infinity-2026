from pybricks.tools import run_task
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def main():
	DRIVE_BASE.use_gyro(True)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=300,
		straight_acceleration=300,
		turn_rate=100,
		turn_acceleration=400,
	)
	#print("Driving forward 100 mm")
	await DRIVE_BASE.straight(50)
	await LEFT_ATTACHMENT.run_angle(200, 360)
	await RIGHT_ATTACHMENT.run_angle(200, 360)
	print("done.")

if __name__ == "__main__":
	run_task(main()) 
