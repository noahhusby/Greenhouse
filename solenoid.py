class solenoid:
    def __init__(self, id):
        self.id = id

    try:
        from gpiozero import LED
    except RuntimeError:
        print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
    
    control=LED(4)
    
    def init():
        global control
        control=LED(self.id)

    def isEnabled():
        return false

    def enable():
        global control
        control.on()
    
    def disable():
        global control
        control.off()