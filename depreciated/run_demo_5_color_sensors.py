from pybricks.parameters import Color
from pybricks.tools import run_task, wait
from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT

LEFT_COLOR_SENSOR = ColorSensor(Port.A)
RIGHT_COLOR_SENSOR = ColorSensor(Port.E)

# This is a function that waits for a desired color.
async def wait_for_color(desired_color):
    # While the color is not the desired color, we keep waiting.
    print("waiting for color.")
    while await LEFT_COLOR_SENSOR.color() != desired_color:
        print("color is ", await LEFT_COLOR_SENSOR.color())
        await wait(1000)
    print("color ", desired_color, " is detected!")
    await HUB.speaker.beep(500, 400)
    return True

async def wait_for_white_color():
    detected = await wait_for_color(Color.WHITE)

    return detected

if __name__ == "__main__":
    print("program has started!")
    run_task(wait_for_white_color())