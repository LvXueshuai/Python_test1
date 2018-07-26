import configparser

comfig = configparser.ConfigParser()    #实例化对象    config={}

comfig["DEFAULT"] = {
                        'SDF':14,
                        'SDGWS':545,
                        'SDGEWS':5,
                        'WQN':99
                    }

with open('sddvc.ini','w') as f:
    comfig.write(f)