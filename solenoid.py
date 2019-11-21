class solenoid:
    def __init__(self,id):
        self.id = id

    try:
        import RPi.GPIO as GPIO
    except RuntimeError:
        print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.id, GPIO.OUT, initial=GPIO.LOW)

    def isEnabled():
        return GPIO.input(self.id)

    def enable():
        GPIO.output(self.id, GPIO.HIGH)
    
    def disable():
        GPIO.output(self.id, GPIO.LOW)