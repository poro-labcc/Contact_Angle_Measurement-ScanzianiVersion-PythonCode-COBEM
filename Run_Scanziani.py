"""
Created on Tue Oct 24 15:29:55 2023

@author: Christoph Zevenbergen
"""


#Scanziani code for contact angle measurement
import Library_Scanziani as S
import numpy as np
import os


radius =   14
plane  = '101'
size   =   80
angle  =   90

directory = '/home/usuario/Documentos/teste'
output_file_name = f'Droplet_R{radius}_P{plane}'
input_file = f'/home/usuario/Documentos/Raw/P{plane}R{radius}x{size}/Droplet_{size}x{size}x{size}_R{radius}_P{plane}_Angulo{angle}.raw'  

npimg = np.fromfile(input_file, dtype=np.uint8)
npimg.astype(int)
imageSize = (size, size, size)
npimg = npimg.reshape(imageSize)

#K_sub     -> Length of the cubic sub-volume for extracking 2d image
#k_line    -> Length of the fluid-fluid interface
#k_ROI     -> Size of the region for the moving average procedure
#N         -> Number of points for the moving average procedure
#Parallel  -> Number of Cores for Parallelization of the code

theta, Radius = S.Scanziani(npimg, k_sub = size, k_line = 200, k_ROI = 15, N = 5, Parallel = 1)
if not os.path.exists(f'{directory}'):       
    os.makedirs(f'{directory}') 
np.save(f"{directory}/{output_file_name}_Results_theta", theta)
np.save(f"{directory}/{output_file_name}_Results_Radius", Radius)