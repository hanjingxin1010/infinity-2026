from pybricks.parameters import Button, Stop
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT, MANUAL_MOTOR_SPEED, RIGHT_ATTACHMENT

async def push_measurements():
    await wait(0)
    # Push/turn the robot to take measurements.
    # Prints to console
    # Turns robot into a fancy tape measurer
    DRIVE_BASE.stop()
    DRIVE_BASE.reset(0, 0)
    HUB.imu.reset_heading(0)
    HUB.display.number(HUB.imu.heading())
    await wait(200)
    while True:
        await wait(0)
        if Button.CENTER in HUB.buttons.pressed():
            # When center button is pressed take a measurement
            print('Distance Pushed', DRIVE_BASE.distance(), ' mm,  ', 'Degrees Turned', HUB.imu.heading())
            DRIVE_BASE.reset(0, 0)
            HUB.imu.reset_heading(0)
            HUB.display.number(HUB.imu.heading())
            await HUB.speaker.beep(500, 200)
        elif Button.BLUETOOTH in HUB.buttons.pressed():
            # Bluetooth button exits program/returns to menu
            await HUB.speaker.beep(500, 100)
            break
        else:
            await wait(10)
            # Display the degrees turned (essentially a fancy protractor)
            HUB.display.number(HUB.imu.heading())

async def left_attach_measurements():
    await wait(0)
    # Manually move the attachment motors and take measurements
    LEFT_ATTACHMENT.reset_angle(0)
    HUB.display.number(LEFT_ATTACHMENT.angle())
    await wait(200)
    while True:
        await wait(0)
        if Button.RIGHT in HUB.buttons.pressed():
            # Right button moves the motor forward at speed from robot_config file
            LEFT_ATTACHMENT.run(MANUAL_MOTOR_SPEED)
            HUB.display.number(LEFT_ATTACHMENT.angle())
        elif Button.LEFT in HUB.buttons.pressed():
            # Left button moves the motor backwards at speed from robot_config file
            LEFT_ATTACHMENT.run(-1 * MANUAL_MOTOR_SPEED)
            HUB.display.number(LEFT_ATTACHMENT.angle())
        elif Button.CENTER in HUB.buttons.pressed():
            # Center button takes a measurement
            print('Degrees Left Attachment Moved', LEFT_ATTACHMENT.angle())
            LEFT_ATTACHMENT.reset_angle(0)
            HUB.display.number(LEFT_ATTACHMENT.angle())
            await HUB.speaker.beep(500, 200)
        elif Button.BLUETOOTH in HUB.buttons.pressed():
            # Bluetooth button exits the program
            await HUB.speaker.beep(500, 100)
            break
        else:
            # Stop motor and display the degrees moved
            LEFT_ATTACHMENT.hold()
            HUB.display.number(LEFT_ATTACHMENT.angle())
            await wait(10)

async def right_attach_measurements():
    await wait(0)
    # Manually move the attachment motors and take measurements
    RIGHT_ATTACHMENT.reset_angle(0)
    HUB.display.number(RIGHT_ATTACHMENT.angle())
    await wait(200)
    while True:
        await wait(0)
        if Button.RIGHT in HUB.buttons.pressed():
            # Right button moves the motor forward at speed from robot_config file
            RIGHT_ATTACHMENT.run(MANUAL_MOTOR_SPEED)
            HUB.display.number(RIGHT_ATTACHMENT.angle())
        elif Button.LEFT in HUB.buttons.pressed():
            # Left button moves the motor backwards at speed from robot_config file
            RIGHT_ATTACHMENT.run(-1 * MANUAL_MOTOR_SPEED)
            HUB.display.number(RIGHT_ATTACHMENT.angle())
        elif Button.CENTER in HUB.buttons.pressed():
            # Center button takes a measurement
            print('Degrees Right Attachment Moved', RIGHT_ATTACHMENT.angle())
            RIGHT_ATTACHMENT.reset_angle(0)
            HUB.display.number(RIGHT_ATTACHMENT.angle())
            await HUB.speaker.beep(500, 200)
        elif Button.BLUETOOTH in HUB.buttons.pressed():
            # Bluetooth button exits the program
            await HUB.speaker.beep(500, 100)
            break
        else:
            # Stop motor and display the degrees moved
            RIGHT_ATTACHMENT.hold()
            HUB.display.number(RIGHT_ATTACHMENT.angle())
            await wait(10)

async def main():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )


run_task(main())