import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
galaxy_data = pd.read_csv('galaxy.csv')
#speed of light=c in km/s
c=299792
#radial velocities are in km/s
galaxy_data['radial_velocities']=abs(galaxy_data['Observed Wavelength of H-alpha']- 6562.8)*c/6562.8
#print(galaxy_data['radial_velocities'])

temp = galaxy_data['RA J2000.0'].str.split(' ', expand=True)
galaxy_data['RA J2000.0'] = temp[0].astype(float) + temp[1].astype(float) / 60 + temp[2].astype(float) / 3600
temp = galaxy_data['Dec J2000.0'].str.split(' ', expand=True)
galaxy_data['Dec J2000.0'] = temp[0].astype(float) + temp[1].astype(float) / 60 + temp[2].astype(float) / 3600

#we can use Hubble's law
#H=Hubble constant in km/s/Mpc
H=69.8
#distance of celetial body= radial velocity/Hubble constant
galaxy_data['distance']=galaxy_data['radial_velocities']/H
#apparent size(theta)= 1.22* lambda / distance
galaxy_data['apparent size']=1.22*galaxy_data['Observed Wavelength of H-alpha']/galaxy_data['distance']
#print(galaxy_data['apparent size'])

RA = galaxy_data['RA J2000.0']
declination = galaxy_data['Dec J2000.0']
radial_velocity = galaxy_data['radial_velocities']
plt.scatter(RA, declination, c=radial_velocity, cmap='viridis', alpha=0.7)
plt.colorbar(label='Radial Velocity')
plt.xlabel('Right Ascension (RA)')
plt.ylabel('Declination')
plt.title('Galaxy Positions and Radial Velocities')
plt.grid(True)
plt.show()
