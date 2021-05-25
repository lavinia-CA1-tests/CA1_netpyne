from neuron import h

def loadCell(cellName, MorphoName):

    h.load_file('import3d.hoc')
    h.load_file('stdrun.hoc')
    MorphologyPath = '/home/fernando/CA1_netpyne/info/data-bbp/20191017/morphologies/swc/'
    gid = 1
    h.load_file('cells/hoc/' + cellName + '.hoc')

    cell = getattr(h, cellName)(gid,MorphologyPath,MorphoName)

    return cell
