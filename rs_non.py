#!/usr/bin/env python

import grass.script as gscript
from math import *

def main():
    relimap = 'relief'
    slopmap = 'slope' 
    gscript.run_command('g.region', raster = slopmap)
    outmap = 'non_QLR'
    gscript.mapcalc("$ns=if((24.5+3.2*$r)>$s,1,0)", ns=outmap, r=relimap, s=slopmap, overwrite = True)

if __name__ == '__main__':
    main()
