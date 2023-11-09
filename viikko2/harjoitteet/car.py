class Car:
    def __init__(self, regPlate, color, speed):
        self._engineOn = False
        self._plate = regPlate
        self._color = color
        self._speed = speed
    def start(self):
        if self._engineOn is True:
            print('Car:',self._plate,'already running')
            return
        else:
            self._engineOn = True
            print('Car:',self._plate,'started')
    def stop(self):
        if self._engineOn is False:
            print('Car:',self._plate,'is already stopped.')
        else:
            self._engineOn = False
            print('Car:',self._plate,'engine stopped.')
    def honk(self):
        print(self._color,'car honked')
    def getLicensePlate(self):
        return self._plate
