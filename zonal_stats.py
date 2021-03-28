#!/usr/bin/env python3

import grass.script as gscript
import os

def importdata():
    path = 'D:/non-sus/thesis/zones/'
    os.chdir(path)
    gscript.run_command('r.in.gdal', input='climate.vrt',output='climate')
    gscript.run_command('r.in.gdal', input='plain.vrt',output='plain')
    gscript.run_command('r.in.gdal', input='susce.vrt',output='susce')
    gscript.run_command('r.in.gdal', input='pop.vrt',output='pop')
    gscript.run_command('r.in.gdal', input='built.vrt',output='built')
    gscript.run_command('v.in.ogr', input='continent.shp',output='continent')
    gscript.run_command('v.to.rast', input='continent',output='continent',use='attr',attribute_column='region')

## 1.continents
# 1-NA, 2-SA, 3-AF, 4-EU, 5-AS, 6-OC
def stats_con():
    path = 'D:/non-sus/thesis/data/'
    os.chdir(path)
    gscript.run_command('g.region', raster='non58')
    gscript.run_command('r.stats', flags='a',input='non58,continent',output='continent58.csv',separator='comma',overwrite=True)

    gscript.run_command('g.region', raster='non_GLC')
    gscript.run_command('r.stats', flags='a',input='non_GLC,continent',output='continentG.csv',separator='comma',overwrite=True)

## 2. climate zones: data from Beck et al., 2018
def stats_clim():
    path = 'D:/non-sus/thesis/data/'
    os.chdir(path)
    gscript.run_command('g.region', raster='non58')
    gscript.run_command('r.stats', flags='a',input='non58,climate',output='climate58.csv',separator='comma',overwrite=True)

    gscript.run_command('g.region', raster='non_GLC')
    gscript.run_command('r.stats', flags='a',input='non_GLC,climate',output='climateG.csv',separator='comma',overwrite=True)

## 3. plain areas: data from Nardi et al., 2019
def stats_plain():
    path = 'D:/non-sus/thesis/data/'
    os.chdir(path)
    gscript.run_command('g.region', raster='non58')
    gscript.run_command('r.stats', flags='a',input='non58,plain',output='plain58.csv',separator='comma',overwrite=True)

    gscript.run_command('g.region', raster='non_GLC')
    gscript.run_command('r.stats', flags='a',input='non_GLC,plain',output='plainG.csv',separator='comma',overwrite=True)

## 4. susceptibility proposed by Stanley and Kirschbaum 2017
def stats_susce():
    path = 'D:/non-sus/thesis/data/'
    os.chdir(path)
    gscript.run_command('g.region', raster='non58')
    gscript.run_command('r.stats', flags='a',input='non58,susce',output='susce58.csv',separator='comma',overwrite=True)

    gscript.run_command('g.region', raster='non_GLC')
    gscript.run_command('r.stats', flags='a',input='non_GLC,susce',output='susceG.csv',separator='comma',overwrite=True)

## 5. population and built data: by Florczyk et al., 2019
def stats_exp():
    path = 'D:/non-sus/thesis/data/'
    os.chdir(path)
    gscript.run_command('g.region', raster='non58')
    gscript.run_command('r.stats', flags='a',input='non_58,pop', output='pop58.csv', separator='comma',overwrite=True)
    gscript.run_command('r.stats', flags='a',input='non_58,built', output='built58.csv', separator='comma',overwrite=True)

    gscript.run_command('g.region', raster='non_GLC')
    gscript.run_command('r.stats', flags='a',input='non_GLC,pop',output='popG.csv',separator='comma',overwrite=True)
    gscript.run_command('r.stats', flags='a',input='non_GLC,built',output='builtG.csv',separator='comma',overwrite=True)

if __name__ == '__main__':
    stats_susce()
