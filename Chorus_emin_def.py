    

# import some general useful stuff
from __future__ import division
import plasmaconst as pc
import itertools
import numpy as np
#from scipy.stats import nanmedian
import math


#Here we are calling up the plasma constants that we will need
#Here we run the plasma constants to get out the SI and CGS values
const =pc.plasmaSI()
constcgs = pc.plasmaCGS()

#This just stores then the info about who wrote this code and what version it is in
 
__version__ = 0.01
__author__ = 'A.J. Halford'

#The magnetic field B is given in Tesla
#Density is given in #/cm^3 and the center frequency is given in 
#normalized angular frequency to the electron cyclotron frequency
#for example
#B = 167.*10**(-9.)
#den = 12.
#w_center = (2.*np.pi*2600.)/(const['e']*abs(B)/const['m_e']) normalized center frequency

def chorus_emin(B, den, w_center):
    #### only want alpha = 0 I think as this should produce the minimum energy the wave is resonant with. 
    #Here we are getting the needed constants and hard coding in the local magnetic field (B), density (den) 
    #and center freqnecy of the wave (w_center)
    q = const['e'] #A coulomb = Ampere x Second
    c = const['c'] # meters per second
    me = const['m_e'] # Kg 

    #These are the relevent electron cyclotron and plasma frequencies
    omega_e =q*B/(const['m_e']) # Hz remember f = omega_p/(2pi)
    omega_p = den*q**2./(const['ep_0']*me) #Hz remember f = omega_p/(2pi)

    #Now we start calculating the minimum resonant energy following the equations from Summers et al 2007
    k2 = (w_center**2./c**2.) - ((omega_p**2/c**2.)/(1-(omega_e/w_center)))
    k = np.sqrt(k2)

    a = k2 + ((den**2.*omega_e**2.)/(c**2.))
    b = 2.*k*w_center
    d = w_center**2.-(den**2.*omega_e)

    vpos = (b+np.sqrt(b**2. -4.*a*d))/(2.*a)
    vneg = (b-np.sqrt(b**2. -4.*a*d))/(2.*a)
    Epos = 1.5*me*vpos**2.
    Eneg = 1.5*me*vneg**2.

    print 'Epos = ', Epos*6.242*10**18
    print 'Eneg = ', Eneg*6.242*10**18



    print 'Emin = ',  np.nanmin([Epos*6.242*10**18,  Eneg*6.242*10**18])
    return np.nanmin([Epos*6.242*10**18,  Eneg*6.242*10**18])
