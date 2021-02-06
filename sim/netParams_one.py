
"""
netParams.py

High-level specifications for M1 network model using NetPyNE

Contributors: salvadordura@gmail.com
"""

from netpyne import specs
import pickle, json
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import os

netParams = specs.NetParams()   # object of class NetParams to store the network parameters


try:
    from __main__ import cfg  # import SimConfig object with params from parent module
except:
    from cfg import cfg
    
#------------------------------------------------------------------------------
# General connectivity parameters
#------------------------------------------------------------------------------
netParams.defaultThreshold = -10.0 # spike threshold, 10 mV is NetCon default, lower it for all cells
netParams.defaultDelay = 2.0 # default conn delay (ms)
netParams.propVelocity = 500.0 # propagation velocity (um/ms)

#------------------------------------------------------------------------------
# loadTemplateName
#------------------------------------------------------------------------------
rootFolder = '/home/fernando/S1detailed/'
os.chdir(rootFolder)
folder = os.listdir('cell_data/')
folder = sorted(folder)

def loadTemplateName(cellnumber):     
    outFolder = rootFolder+'cell_data/'+folder[cellnumber]
    f = open(outFolder+'/template.hoc', 'r')
    for line in f.readlines():
        if 'begintemplate' in line:
            templatename = str(line)     
    templatename=templatename[:-1]        
    templatename=templatename[14:]
    return templatename


#------------------------------------------------------------------------------
# Cell parameters
#------------------------------------------------------------------------------
cellnumber=0
cellName = folder[cellnumber]
cellTemplateName = loadTemplateName(cellnumber)
cellRule = netParams.importCellParams(label=cellName + '_rule', somaAtOrigin=False,
    conds={'cellType': cellName, 'cellModel': 'HH_full'},
    fileName='cellwrapper.py',
    cellName='loadCell',
    cellInstance = True,
    cellArgs={'cellName': cellName, 'cellTemplateName': cellTemplateName})

os.chdir(rootFolder)

cellnumber=0
cellName1 = folder[cellnumber]
cellTemplateName1 = loadTemplateName(cellnumber)

cellRule = netParams.importCellParams(label=cellName1 + '_rule', somaAtOrigin=False,
    conds={'cellType': cellName1, 'cellModel': 'HH_full'},
    fileName='cellwrapper.py',
    cellName='loadCell',
    cellInstance = True,
    cellArgs={'cellName': cellName1, 'cellTemplateName': cellTemplateName1})

os.chdir(rootFolder)
#------------------------------------------------------------------------------
# Population parameters
#------------------------------------------------------------------------------

netParams.popParams['L1_1'] = {'cellType': cellName, 'cellModel': 'HH_full', 'numCells': 1} 
netParams.popParams['L1_2'] = {'cellType': cellName, 'cellModel': 'HH_full', 'numCells': 1} 
netParams.popParams['L1_3'] = {'cellType': cellName, 'cellModel': 'HH_full', 'numCells': 1} 
netParams.popParams['L1_4'] = {'cellType': cellName, 'cellModel': 'HH_full', 'numCells': 1} 

#------------------------------------------------------------------------------
# Current inputs (IClamp)
#------------------------------------------------------------------------------
if cfg.addIClamp:
     for key in [k for k in dir(cfg) if k.startswith('IClamp')]:
        params = getattr(cfg, key, None)
        [pop,sec,loc,start,dur,amp] = [params[s] for s in ['pop','sec','loc','start','dur','amp']]

        #cfg.analysis['plotTraces']['include'].append((pop,0))  # record that pop

        # add stim source
        netParams.stimSourceParams[key] = {'type': 'IClamp', 'delay': start, 'dur': dur, 'amp': amp}
        
        # connect stim source to target
        netParams.stimTargetParams[key+'_'+pop] =  {
            'source': key, 
            'conds': {'pop': pop},
            'sec': sec, 
            'loc': loc}


