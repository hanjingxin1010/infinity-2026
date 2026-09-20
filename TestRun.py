from math import pi

from pybricks.tools import run_task

from library import set_drivebase
from robot_config import DRIVE_BASE


WHEEL_DIAMETER = 56
ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def test_run():
	await set_drivebase()
	print("Driving forward one wheel rotation")
	await DRIVE_BASE.straight(ONE_WHEEL_ROTATION)
	print("Driving backward one wheel rotation")
	await DRIVE_BASE.straight(-ONE_WHEEL_ROTATION)


if __name__ == "__main__":
	run_task(test_run())
