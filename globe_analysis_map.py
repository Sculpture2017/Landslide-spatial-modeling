#!/usr/bin/env python

import grass.script as gscript
from math import *

## Quantile linear regression model: by Marchesini et al.(2014)
def QLR_M():
    relimap = 'relief'
    slopmap = 'slope' 
    gscript.run_command('g.region', raster = slopmap)
    outmap = 'non_QLR'
    gscript.mapcalc("$ns=if((24.5+3.2*$r)>$s,1,0)", ns=outmap, r=relimap, s=slopmap, overwrite = True)

## Quantile non-linear (exponential) model: by Marchesini et al.(2014) 
def QNL_M1():
    relimap = 'relief'
    slopmap = 'slope' 
    gscript.run_command('g.region', raster = slopmap)
    outmap = 'non_QNL'
    gscript.mapcalc("$ns=if(353.9*exp(0.0028*$r)>$s,1,0)", ns=outmap, r=relimap, s=slopmap, overwrite = True)

## Quantile non-linear (exponential) model: by Marchesini et al.(2014), with maximum slope threshold of 58 (relief >= 1000m)
def QNL_M2():
    relimap = 'relief'
    slopmap = 'slope' 
    gscript.run_command('g.region', raster = slopmap)
    outmap = 'non_58'
    gscript.mapcalc("$ns=if(((353.9*exp(0.0028*$r)<$s) | ($s>5800),0,1)", ns=outmap, r=relimap, s=slopmap, overwrite = True)

## Quantile non-linear (exponential) model: by our study with GLC datasets
def QLR_Q():
    relimap = 'relief'
    slopmap = 'slope' 
    gscript.run_command('g.region', raster = slopmap)
    outmap = 'non_GLC'
    gscript.mapcalc("$ns=if(193.8*exp(0.003*$r)>$s,1,0)", ns=outmap, r=relimap, s=slopmap, overwrite = True)


if __name__ == '__main__':
    QLR_Q()
