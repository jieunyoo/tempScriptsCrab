import CRABClient
from CRABClient.UserUtilities import config 

config = config()
config.General.requestName = 'HWW_boosted200GeV_GEN'
config.General.workArea = 'HZJ_LHE'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '/afs/cern.ch/user/j/jiyoo/HZJ_LHE/HWW_boosted200GeV_GEN_1_cfg.py'

config.Data.outputPrimaryDataset = 'HWW_boosted200GeV_GEN'
config.Data.splitting = 'EventBased'
#config.Data.unitsPerJob = 1000 not sure what i should do
config.Data.unitsPerJob = 10
#NJOBS = 25  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
NJOBS = 5  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputLFNDirBase = '/store/user/jiyoo'
config.Data.outputDatasetTag = 'HWW_boosted200GeV_GEN'

config.Site.storageSite = 'T3_US_FNALLPC'


#config.Data.ignoreLocality = True

