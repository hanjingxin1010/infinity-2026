from pybricks.parameters import Color, Direction
from pybricks.tools import multitask, run_task, wait



from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT
DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
#this function plays the star wars opening music.

async def test():
    '''await DRIVE_BASE.straight(500)
    await DRIVE_BASE.straight(-500)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.turn(-90)'''
    await CENTER_ATTACHMENT.run_angle(150,-150)
    await CENTER_ATTACHMENT.run_angle(300,150)

#this function tests control of center attachment.
async def reset_motor():
    # Just a demo to show off the center attachment
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    CENTER_ATTACHMENT.reset_angle(0)
    """for count in range(2):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, 90) 
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, -90) """
async def straight(m):
    DRIVE_BASE.straight(m)

async def turn(degrees):
    DRIVE_BASE.turn(degrees)
# write code in "async def mission():" or line 28
async def liftup(speed,degrees):
    await CENTER_ATTACHMENT.run_angle(speed,degrees)


async def mission():
    CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE,gears=[12,20])
    
    DRIVE_BASE.use_gyro(True)
    #await liftup(200,135)
    await DRIVE_BASE.straight(440)
    


    
    await DRIVE_BASE.turn(53)
    await DRIVE_BASE.straight(135)
    #await DRIVE_BASE.turn(-30)
    #await DRIVE_BASE.turn(15)
    #await DRIVE_BASE.straight(150)
    
    await liftup(300,250)
    #await liftup(300,-50)
    DRIVE_BASE.settings(straight_speed=100, straight_acceleration=100)
    await DRIVE_BASE.straight(-400)
    #await liftup(100,-10)
    DRIVE_BASE.settings(straight_speed=300, straight_acceleration=300)
    await DRIVE_BASE.straight(25)
    await liftup(300,-100)
    

    #await wait(500)
    await DRIVE_BASE.turn(-30)
    await DRIVE_BASE.straight(-90)
    await liftup(25,15)
    await DRIVE_BASE.turn(47) #used to be 90
    await liftup(50,44)
    await wait(50)
    await liftup(75,-6.25)
    #await liftup(25,12)
    await DRIVE_BASE.straight(50)
    await DRIVE_BASE.turn(-47) #used to be -90
    DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
    await DRIVE_BASE.straight(-600)
    await liftup(300,-150)

    '''await DRIVE_BASE.straight(50)
    await DRIVE_BASE.turn(-45)
    await DRIVE_BASE.straight(350)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(125)'''
    
    #await DRIVE_BASE.straight(-10)
    #await DRIVE_BASE.turn(90)
''' await straight(300)
    await turn(-30)
    await turn(30)
    await straight(100)
    await straight(-100)'''

'''await DRIVE_BASE.straight(220)
    await DRIVE_BASE.turn(100)
    await liftup(300,-40)
    await DRIVE_BASE.straight(160)
    await liftup(300,40)
    await DRIVE_BASE.straight(-260)
    await DRIVE_BASE.turn(-30)
    await liftup(300,-50)
    await DRIVE_BASE.straight(167)
    await liftup(300,50)
    await DRIVE_BASE.straight(-100)
    await DRIVE_BASE.turn(-65)
    await DRIVE_BASE.straight(-250)
    DRIVE_BASE.use_gyro(False)'''
"""
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True)
    #await DRIVE_BASE.straight(100) #in mm
    #await liftup(300,90)
    await DRIVE_BASE.straight(667)
    await DRIVE_BASE.turn(73)
    await wait(1)
    await liftup(300,-90)
    
    await DRIVE_BASE.straight(385.67676767)
    await DRIVE_BASE.turn(78)#, then=Stop.COAST )
    #return
    await DRIVE_BASE.straight(40)
    await liftup(300,116)
    await wait(1)
    await liftup(300,-116)
    #return
    #put down. the lever
    await DRIVE_BASE.straight(-50)
    # back 
    await DRIVE_BASE.turn(-78)
    await DRIVE_BASE.straight(-350)#back to T


    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(167)
    await wait(1)
    await DRIVE_BASE.turn(-90)
    
    await DRIVE_BASE.straight(10.6767676767676767)
    await liftup(300,126)
    await wait(1)
    
    await DRIVE_BASE.straight(-85)
    await DRIVE_BASE.turn(-70)   
    await DRIVE_BASE.straight(-667.676767)
    #await DRIVE_BASE.straight(-10)
    DRIVE_BASE.use_gyro(False)
"""
async def subtask_test_center_attachment():
    # Just a demo to show off the center attachment
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    CENTER_ATTACHMENT.reset_angle(0)
    for count in range(2):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, 90) 
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, -90)

async def main():
    await wait(0)
    # Just a demo to show off the drivebase as well as music, icons,
    # and multitasking
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    await HUB.speaker.beep(500, 400)
    await reset_motor()
    #await mission()
    await mission()
    #await subtask_test_center_attachment()

    
       # subtask_test_left_attachment()
    




run_task(main())

if "__file__" == "__main__":
    run_task(main())
