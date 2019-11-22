class solenoid:
    from gpiozero import LED
    global LED
    def __init__(self, id):
        self.id = id
	global control
	control = LED(id)

    def isEnabled(self):
        return false

    def enable(self):
        global control
        control.on()
	print("enabling")
    
    def disable(self):
        global control
        control.off()
