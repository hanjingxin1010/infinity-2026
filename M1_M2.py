from pybricks.tools import multitask, run_task, wait
from pybricks.parameters import Stop
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT

async def M1_M2():
	DRIVE_BASE.use_gyro(True)
	await wait(1000)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=400,
		straight_acceleration=200,
		turn_rate=600,
		turn_acceleration=600,
	)
	print("Driving forward 680 mm while moving the attachment")
	await multitask(
		LEFT_ATTACHMENT.run_angle(180, 127),
		DRIVE_BASE.straight(685),
	)

	await DRIVE_BASE.straight(-10)
	"""
	print("Turning -20 degrees")
	await DRIVE_BASE.turn(-20) 
	print("Turn complete")
			
	await wait(1000)
	print("Driving forward 100 mm")
	await DRIVE_BASE.straight(40)

	print("Driving forward 100 mm completed")
	await wait(1000)
	print("Turning -25 degrees")
	"""
	await DRIVE_BASE.turn(-25)
	await wait(1000)
	await DRIVE_BASE.straight(12)
	await wait(1000)
	await DRIVE_BASE.turn(-28)
		
	print("Turning 55 degrees")
	await wait(1000)
	await DRIVE_BASE.turn(55)

	set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=600,
		turn_rate=200,
		turn_acceleration=300,
	)
	print("Driving backward 514 mm toward the next task")
	await DRIVE_BASE.straight(-532)
	 
	#await DRIVE_BASE.turn(-50.5)
	await DRIVE_BASE.turn(-49.5)
	await LEFT_ATTACHMENT.run_angle(-180, 120)
	DRIVE_BASE.settings(
		straight_speed=300,
		straight_acceleration=600,
		turn_rate=200,
		turn_acceleration=200,
	)
	await DRIVE_BASE.straight(210)
	await multitask(
		LEFT_ATTACHMENT.run_angle(90, 16),
		DRIVE_BASE.straight(80),
	)
	await wait(500)
	DRIVE_BASE.settings(
		straight_speed=200,
		straight_acceleration=200,
		turn_rate=200,
		turn_acceleration=200,
	)
	await multitask(
		LEFT_ATTACHMENT.run_angle(180, 60),
		DRIVE_BASE.straight(-400),
	)

	await DRIVE_BASE.curve(100,-180)
	await DRIVE_BASE.straight(100)
	print("Return complete")
	
	

if __name__ == "__main__":
	run_task(M1_M2())