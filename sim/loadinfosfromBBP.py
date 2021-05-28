import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

CircuitPath = '/home/fernando/CA1_netpyne/info/data-bbp/20191017/'
BioName = CircuitPath + 'bioname/'
Atlas = CircuitPath + 'atlas/'
MorphologyPath = CircuitPath + 'morphologies/swc/'
CellLibraryFile = CircuitPath + 'sonata/nodes/nodes_hippocampus.h5'
METypePath = CircuitPath + 'emodels/20190402/hoc/'
MEComboInfoFile = CircuitPath + 'emodels/20190402/mecombo_emodel.tsv'
UserTargetFile = CircuitPath + 'user.target'
StartTargetFile = CircuitPath + 'start.target'

from bluepysnap import Circuit
from bluepysnap.bbp import Cell
circuit_path = CircuitPath + 'circuit_config.json'
circuit = Circuit(circuit_path)
cells = circuit.nodes["hippocampus_neurons"]
cells_projections = circuit.nodes["hippocampus_projections"]
nodesinfo = cells.get()
nodesinfo_projections = cells_projections.get()

hoclist = list(cells.property_values(Cell.MODEL_TEMPLATE))
Morpholist = list(cells.property_values(Cell.MORPHOLOGY))
Mtypelist = list(cells.property_values(Cell.MTYPE))

Morpholist_hoclist = []
cellNamelist = []
MENamelist = []
for gid in range(18198):    
    cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3] 
    if cellName not in cellNamelist:
        cellNamelist.append(cellName)  
        
    MEName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid]
    if MEName not in MENamelist:
        MENamelist.append(MEName)  

    MorphohocName = nodesinfo['morphology'][gid] + '__' + nodesinfo['model_template'][gid][4:]    
    if MorphohocName not in Morpholist_hoclist:
        Morpholist_hoclist.append(MorphohocName)           
         
            
MENumber = {}
for cellgid in MENamelist:    
    MENumber[cellgid] = 0     
    
cellNumber = {}
for cellgid in cellNamelist:    
    cellNumber[cellgid] = 0       
       
cellNumber_swc_hoc = {}
for cellgid in Morpholist_hoclist:    
    cellNumber_swc_hoc[cellgid] = 0

    
popNumber = {}
for popgid in Mtypelist:    
    popNumber[popgid] = 0 

for gid in range(18198):
    cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3] 
    cellNumber[cellName] += 1 
    
    MEName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid]
    MENumber[MEName] += 1 
    
    MorphohocName = nodesinfo['morphology'][gid] + '__' + nodesinfo['model_template'][gid][4:]     
    cellNumber_swc_hoc[MorphohocName] += 1 
    
    Mtype = nodesinfo['mtype'][gid]
    popNumber[Mtype] += 1 

print('\nFrom loadinfosfromBBP.py import cells info')

print('\n-> nodesinfo of 18198 cells and nodesinfo_projections of 15928 virtual cells')

hoclist = list(cells.property_values(Cell.MODEL_TEMPLATE))
print('\n hoclist size =',np.size(hoclist))

Morpholist = list(cells.property_values(Cell.MORPHOLOGY))
print('\n Morpholist size =',np.size(Morpholist))

Mtypelist = list(cells.property_values(Cell.MTYPE))
print('\n Mtype size =',np.size(Mtypelist))

print('\n celllist size =',np.size(cellNamelist))

print('\n ME size =',np.size(MENamelist))

print('\n SWC_HOC size =',np.size(Morpholist_hoclist))

# print('\n popNumbers',popNumber)

# for cellgid in cellNamelist[:1]:    
#     print(cellgid,cellNumber[cellgid])

# for cellgid in Morpholist_hoclist[:1]:    
#     print(cellgid,cellNumber_swc_hoc[cellgid])

# gid = 0
# MorphoName = nodesinfo['morphology'][gid] + '.swc'
# hocName = nodesinfo['model_template'][gid][4:]  
# mcName = nodesinfo['region'][gid][:3]  
# Mtype = nodesinfo['mtype'][gid]
# cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3]
# MEName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid]
# MorphohocName = nodesinfo['morphology'][gid] + '__' + nodesinfo['model_template'][gid][4:]    

# print('%s \n %d %s %s \n hoc = %s \n swc = %s' % (cellName,gid,mcName,Mtype,hocName,MorphoName))

popLabel = {}
cellParamLabels = []
cellName = 'first_'
def printexemples(infoexemple):
	most_central_10_SP_PC = [11617, 6393, 6789, 6243, 13513, 14311, 9397, 3699, 12245, 12001]
	most_central_10_SP_PC = most_central_10_SP_PC - np.ones_like(most_central_10_SP_PC)

	gid_2neuronsMtype_central = [18097, 18109, 18140, 18149, 18163, 18177,18189, 18191, 16950, 16963, 17199, 17202, 
						17411, 17416, 17486, 17497, 13513, 14311, 17946, 17958, 22, 25, 1, 3]
	gid_2neuronsMtype_central = gid_2neuronsMtype_central - np.ones_like(gid_2neuronsMtype_central)

	if infoexemple == '2neuronsMtype':
		for gid in gid_2neuronsMtype_central:
			MorphoName = nodesinfo['morphology'][gid] + '.swc'
			hocName = nodesinfo['model_template'][gid][4:]  
			mcName = nodesinfo['region'][gid][:3]  
			Mtype = nodesinfo['mtype'][gid]
			MEName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid]
			MorphohocName = nodesinfo['morphology'][gid] + '__' + nodesinfo['model_template'][gid][4:]    
			
			if cellName == nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3]:
				cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3] + '_2'
			else:  
				cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3]
			
			cellParamLabels.append(cellName)
			popLabel[cellName] = Mtype
			print('%s \n %d %s %s \n hoc = %s \n swc = %s' % (cellName,gid,mcName,Mtype,hocName,MorphoName))
	elif infoexemple == 'most_central_10_SP_PC':
		for gid in most_central_10_SP_PC:
			MorphoName = nodesinfo['morphology'][gid] + '.swc'
			hocName = nodesinfo['model_template'][gid][4:]  
			mcName = nodesinfo['region'][gid][:3]  
			Mtype = nodesinfo['mtype'][gid]
			MEName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid]
			MorphohocName = nodesinfo['morphology'][gid] + '__' + nodesinfo['model_template'][gid][4:]    
			
			if cellName == nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3]:
				cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3] + '_2'
			else:  
				cellName = nodesinfo['mtype'][gid] + '_' + nodesinfo['etype'][gid] + '_' + nodesinfo['region'][gid][:3]
			
			cellParamLabels.append(cellName)
			popLabel[cellName] = Mtype
			print('%s \n %d %s %s \n hoc = %s \n swc = %s' % (cellName,gid,mcName,Mtype,hocName,MorphoName))
	else:
		print('the options are the str: 2neuronsMtype or most_central_10_SP_PC')
print('\n\n-> def printexemples(infoexemple):','\n options str: 2neuronsMtype or most_central_10_SP_PC')