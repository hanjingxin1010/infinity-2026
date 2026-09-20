from pybricks.tools import run_task, wait, multitask

from run_demo_3_center_attachment import demo_center_attachment 
from run_demo_1_drive_straight_turn import demo_drive_straight_turn

async def demo_multitasking():
    await multitask(
        demo_drive_straight_turn(),
        demo_center_attachment()
    )


if __name__ == "__main__":
    run_task(demo_multitasking())