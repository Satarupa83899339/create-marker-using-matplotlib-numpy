# code 3:  marker and line color change
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

''' Line Reference:
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
Color Reference:
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White '''
