from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Color, Stop
from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from robot_config_mini import DRIVE_BASE, HUB, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, TELEOP_ACCEL, TELEOP_ATTACH_SPEED, TELEOP_SPEED, TELEOP_TURN, TELEOP_TURN_ACCEL

# Set up all devices.
XBOX = XboxController()

# Initialize variables.
RIGHT_STICK_X_AXIS = 0
LEFT_STICK_Y_AXIS = 0
RIGHT_TRIGGER = 0
LEFT_TRIGGER = 0

async def teleop():
    global LEFT_STICK_Y_AXIS, LEFT_TRIGGER, RIGHT_STICK_X_AXIS, RIGHT_TRIGGER
    await wait(0)
    # Zero out the odometry and attachment motors so we can
    # take measurements
    DRIVE_BASE.reset()
    LEFT_ATTACHMENT.reset_angle(0)
    RIGHT_ATTACHMENT.reset_angle(0)
    DRIVE_BASE.use_gyro(True)
    HUB.light.on(Color.ORANGE)
    await set_teleop_drivebase()
    # Loop starts here
    while True:
        await wait(0)
        # Get stick/trigger inputs
        LEFT_STICK_Y_AXIS = await dead_zone(XBOX.joystick_left()[1])
        LEFT_TRIGGER = await dead_zone(XBOX.triggers()[0])
        RIGHT_STICK_X_AXIS = await dead_zone(XBOX.joystick_right()[0])
        RIGHT_TRIGGER = await dead_zone(XBOX.triggers()[1])
        if Button.A in XBOX.buttons.pressed():
            # If the A button is pressed print off to the console:
            # how far the robot drove, etc.
            print(DRIVE_BASE.distance(), ' mm driven,   ', DRIVE_BASE.angle(), 'degrees turned')
            print(LEFT_ATTACHMENT.angle(), ' degrees left attachment,   ', RIGHT_ATTACHMENT.angle(), ' degrees right attachment')
            LEFT_ATTACHMENT.reset_angle(0)
            RIGHT_ATTACHMENT.reset_angle(0)
            DRIVE_BASE.reset()
            # Beep the robot and rumble the xbox controller
            #  to let it known that a measurement was taken
            await multitask(
                HUB.speaker.beep(500, 400),
                XBOX.rumble(50, 400),
            )
        elif Button.X in XBOX.buttons.pressed():
            # X exits RC mode and allows a new program to be selected
            DRIVE_BASE.use_gyro(False)
            # Beep the robot and rumble the xbox controller
            #  to let it known that the program is exited
            await multitask(
                HUB.speaker.beep(700, 400),
                XBOX.rumble(50, 400),
            )
            await set_drivebase()
            break
        else:
            # Check to see if there are any inputs
            if LEFT_STICK_Y_AXIS != 0 or RIGHT_STICK_X_AXIS != 0:
                # Foward/reverse: Left stick up/down
                # Turning: Right stick left/right
                DRIVE_BASE.drive(LEFT_STICK_Y_AXIS * TELEOP_SPEED, RIGHT_STICK_X_AXIS * TELEOP_TURN)
            else:
                # Brake if no inputs
                DRIVE_BASE.brake()
            # Check to see if there are any inputs
            if LEFT_TRIGGER != 0:
                # Control the Left attachment motor
                # Left trigger = left motor forward
                # Left trigger + left bumper  = left motor backwards
                if Button.LB in XBOX.buttons.pressed():
                    LEFT_ATTACHMENT.run(LEFT_TRIGGER * (TELEOP_ATTACH_SPEED * -1))
                else:
                    LEFT_ATTACHMENT.run(LEFT_TRIGGER * TELEOP_ATTACH_SPEED)
            else:
                # Brake if no inputs
                LEFT_ATTACHMENT.brake()
            # Check to see if there are any inputs
            if RIGHT_TRIGGER != 0:
                # Control the Right attachment motor
                # Right trigger = right motor forward
                # Right trigger + right bumper  = right motor backwards
                if Button.RB in XBOX.buttons.pressed():
                    RIGHT_ATTACHMENT.run(RIGHT_TRIGGER * (TELEOP_ATTACH_SPEED * -1))
                else:
                    RIGHT_ATTACHMENT.run(RIGHT_TRIGGER * TELEOP_ATTACH_SPEED)
            else:
                # Brake if no inputs
                RIGHT_ATTACHMENT.brake()
        await wait(10)

async def dead_zone(stick):
    await wait(0)
    # Convert the input from the xbox controller
    # from -100 to 100 to -1 to 1. Also change small
    # values to 0 to eliminate stick drift. Rescales the
    # inputs appropriately
    if -7 <= stick <= 7:
        # Return 0 to eliminate  stick drift
        return 0
    elif 7 > stick:
        # Rescale positive (right turning input) given that 0  to  7 = 0
        return (stick - 7) / 93
    else:
        # Rescale negative (left turning input) given that 0 to -7 = 0
        return (stick + 7) / 93

async def set_teleop_drivebase():
    await wait(0)
    # Sets the telop drivebase settings as you want higher accelleration
    # and lower speeds to make the robot easier to control
    DRIVE_BASE.settings(straight_speed=TELEOP_SPEED)
    DRIVE_BASE.settings(straight_acceleration=TELEOP_ACCEL)
    DRIVE_BASE.settings(turn_rate=TELEOP_TURN)
    DRIVE_BASE.settings(turn_acceleration=TELEOP_TURN_ACCEL)

async def main():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )


run_task(main())