from py4j.java_gateway import (JavaGateway, GatewayParameters)


import os
folder_dir = 'C:\\Users\huan289\\git\\deepgrid\\DeepGrid'
os.chdir(folder_dir)

print(os.getcwd())

java_port = 25333
gateway = JavaGateway(
    gateway_parameters=GatewayParameters(port = java_port, auto_convert=True)
    )

ipss_app = gateway.entry_point




# case_files = ['testData\\Kundur-2area\\kunder_2area_ver30.raw','testData\\Kundur-2area\\kunder_2area.dyr']
# Need to use the following way to define a String array in Python for Py4J

                
case_files_array = gateway.new_array(gateway.jvm.String, 2)
case_files_array[0] = folder_dir+'\\'+'testData\\IEEE39\\IEEE39bus_multiloads_xfmr4_smallX_v30.raw'
case_files_array[1] = folder_dir+'\\'+'testData\\IEEE39\\IEEE39bus_4motorw_4AC.dyr'

dyn_config_file = folder_dir+'\\'+'testData\\IEEE39\\json\\IEEE39_dyn_config.json'

# rl_config_file = 'testData\\Kundur-2area\\json\\kundur2area_RL_config.json'
#rl_config_file = folder_dir+'\\'+'testData\\IEEE39\\json\\IEEE39_RL_loadShedding_config.json'
rl_config_file = folder_dir+'\\'+'testData\\IEEE39\\json\\IEEE39_RL_loadShedding_addLoadStatus2Observations_config.json'
#ob_act_dim_ary = ipss_app.initStudyCase(case_files_array , dyn_config_file, rl_config_file)

#for x in ob_act_dim_ary:
#    print(x)

from PowerDynSimEnvDef import PowerDynSimEnv
env = PowerDynSimEnv(case_files_array,dyn_config_file,rl_config_file)

import numpy as np
env.reset()
for i in range(9):
    #action = np.random.randint(0,4096)
    #action = 475
    action = 1755
    print('i, action = ', i, action)
    results = env.step(action)
    print('states =',results[0])
    print('step reward =', results[1])
    

print('test completed')

			 