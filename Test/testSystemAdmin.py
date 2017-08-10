import os
import sys
sys.path.append('..')

from SystemAdmin import ToggleHyperthreading


if not ToggleHyperthreading.checkUser(os.geteuid()):
    print("Root priviliges required to toggle hyperthreading, try again.")
    sys.exit(1)
if ToggleHyperthreading.HyperthreadingEnabled():
    print("Toggling hyperthreading off and back on")
    ToggleHyperthreading.toggleOff()
    ToggleHyperthreading.toggleOn()
else:
    print("Toggling hyperthreading on and back off")
    ToggleHyperthreading.toggleOn()
    ToggleHyperthreading.toggleOff()

