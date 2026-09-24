from pybricks.tools import run_task
from library import set_drivebase
from robot_config import DRIVE_BASE

async def main():
    DRIVE_BASE.use_gyro(True)
    
if __name__ == "__main__":
    run_task(main())
