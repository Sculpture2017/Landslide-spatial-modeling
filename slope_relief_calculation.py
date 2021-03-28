#!/usr/bin/env python

import grass.script as gscript

def reliefG():
    gscript.run_command('g.region', raster='srtm')
    gscript.run_command('r.neighbors',input='srtm',output='relief',method='range',size=15)

def slopeG():
    # setting calculation region
    gscript.run_command('g.region', raster='srtm')
    region = grasscore.region()
    res=region['res']
    
    # parameters
    pi = 3.14159265359
    a = 6378137.0
    b = 6356752.3142
    f = 1/298.257223563
    e2 = (a^2-b^2)/a^2
    dx = 2*pi*a*res/360
    dy = a*(1-e2)*res
    
    # slope calculation
    exp1 = '(($z[1,1]+2*$z[1,0]+$z[1,-1]-$z[-1,1]-2*$z[-1,0]-$z[-1,-1])/(8*$p*cos(y())))^2'
    exp2 = '(($z[1,1]+2*$z[0,1]+$z[-1,1]-$z[1,-1]-2*$z[0,-1]-$z[-1,-1])/(8*$q*(1-0.$r*(sin(y()))^2)^1.5))^2'
    exp = '$s=atan(('+exp1+'+'+exp2+')^0.5)'
    gscript.mapcalc(exp, s='slope', z='strm', overwrite = True, quiet = True)

if __name__ == '__main__':
    main()
