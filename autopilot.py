#This script is a loose representation of an autopilot system. Functions exist as hard push-buttons for each mode type
#The pilot can activate these modes as necessary depending on the mode of flight

#KAP140 Autopilot Implementation
class KAP140():
    def __init__(self):
        self.APMaster = False
        self.trackCourse = 0
        self.heading = 0
        self.APMode = 'Off'

    def displayAPMasterStatus(self):
        if self.APMaster == True:
            print('AP On')
        elif self.APMaster == False:
            print('AP Off')
        else:
            print('AP Master Switch information not received.')

    def displayAPMode(self):
        print('AP Display: '+format(self.APMode))

    def toggleAPMaster(self):
        if self.APMaster == True:
            self.APMaster = False
            self.APMode = 'Off'
        elif self.APMaster == False:
            self.APMaster = True
            self.APMode = 'ROL'
        
    def toggleHDG(self,headingFromDG):
        self.heading = headingFromDG
        if self.APMaster == True:
            if self.APMode == 'ROL':
                self.APMode = 'HDG'
            elif self.APMode == 'HDG':
                self.APMode = 'ROL'
        elif self.APMaster == False:
            if self.APMode == 'Off':
                self.APMode = 'HDG Arm'
            elif self.APMode == 'HDG Arm':
                self.APMode = 'Off'

    def toggleNav(self,trackCourse):
        self.trackCourse = trackCourse
        print('NAV')
        print('Holding Course of ' + format())

    def ApprMode(self):
        print('APPR')

    def RevMode(self):
        print('REV')

    def AltMode(self):
        print('ALT')

    def VSModeUp(self):
        print('UP')

    def VSModeDn(self):
        print('DN')

#Directional Gyro implementation (supports HDG mode of KAP140)
class DirectionalGyro():
    def __init__(self):
        self.caged = True
        self.heading = 0
    
    def displayCurrentHeading(self):
        print('Current DG Heading: ' + format(self.heading))

    def setHeading(self,heading):
        self.heading = heading
        return self.heading

#Omni Bearing Selector (OBS) implementation (supports NAV, APR modes of KAP140)
class OBS():
    def __init__(self):
        self.course = 0

    def setCourse(self,selectedCourse):
        self.course = selectedCourse
        return self.course

    def displayCurrentCourse(self):
        print('Current OBS Course: ' + format(self.course))

#Heading/GPS selector (for approaches)
class ModeSelector():
    def __init__(self):
        self.HDG = False
        self.GPS = True

    def displayMode(self):
        if self.HDG == True and self.GPS == False:
            print('Mode Selector: HDG')
        elif self.GPS == True and self.HDG == False:
            print('Mode Selector: GPS')
        else:
            print('Mode selector information not received.')

    def setHDGMode(self):
        self.HDG = True
        self.GPS = False
    
    def setGPSMode(self):
        self.HDG = False
        self.GPS = True

#Vertical Speed Indicator (for VS selection on KAP140)
class VSI():
    def __init__(self):
        self.vertSpeed = 0
    
    def displayVS(self):
        print('VSI: '+ format(self.vertSpeed) + ' fpm')

    def setVS(self,commandedVS):
        self.vertSpeed = commandedVS

#Initialize instruments
autpilot = KAP140()
dg = DirectionalGyro()
obs = OBS()
modeSelector = ModeSelector()
vsi = VSI()

#Set parameters for each supporting instrument
print('Instruments initialized, setting parameters...')
currentHeading = dg.setHeading(360)
currentOBSCourse = obs.setCourse(290)
print('\n')

#Display status of supporting instruments before Autopilot operation
print('Instrument parameters set, displaying current status before KAP140 autopilot is turned on...')
dg.displayCurrentHeading()
currentMode = modeSelector.displayMode()
obs.displayCurrentCourse()

APDisplay = autpilot.APMode
print('AP Display: ' + APDisplay)
print('\n')

""" KAP 140 Autpilot Operations """
print('KAP 140 Autopilot operation:')
#Turn on Autopilot
print('AP button pushed...')
autpilot.toggleAPMaster()
autpilot.displayAPMode()
print('\n')

#Heading mode operation
print('Heading button pushed...')
autpilot.toggleHDG(currentHeading)
autpilot.displayAPMode()
dg.displayCurrentHeading()
print('\n')

print('DG moved to 260 degrees...')
dg.setHeading(260)
dg.displayCurrentHeading()
print('\n')

print('Heading button pushed again...')
autpilot.toggleHDG(currentHeading)
autpilot.displayAPMode()
print('\n')

#Nav mode operation



