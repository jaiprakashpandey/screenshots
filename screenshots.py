'''

screenshots as a service -- main module responsible for initiating the Tasks
(loading driver,
analysing parallel processing,
taking shots and DB communications,
responding back to front controller) respectively.

'''

import json
import logging
import multiprocessing as mp
import sys
import time
import copy

import pymongo
from drivers import ScreenWebDriver
from persistence import ScreenShotDao
from itertools import product
from configs import ScreenConfigurations

log = logging.getLogger(__name__)
cconfig = ScreenConfigurations()
screen_driver = ScreenWebDriver(cconfig)
__driver = screen_driver.get_driver()


class ScreenShooter:

    def __init__(self, config):        
        log.info('--  ScreenShooter class constructor --')
        #self.config = config
        self.dao_instance = ScreenShotDao(config)

    def prepare_shooting(self, _urls):
        log.info('--  ScreenShooter class constructor --')

        # Load driver to process with Sngle CPU processor
        #driver_instance = ScreenWebDriver(self.config)

        #__driver = driver_instance.get_driver()

        # Prepare to open browser and take screen shot
        self._initiate_taking_shots(_urls)
        

    def _initiate_taking_shots(self, urls):
        log.info('----------- Initializing to take shots for each URL -----------')
        print("_prepare_taking_shots")
        shot_lists = []

        # enable for Single processing 
        #for urlDict in urls:
            #shot_lists.append(self.__take_shots(__driver, urlDict))

        # lets use multi shooters to fasten shooting    

        available_cpus = mp.cpu_count()
        print('Number of CPU on this machine:')
        print(available_cpus)
        # can be controlled number of pool size from configuration file, setting name parallel_pool_size
        pool = mp.Pool(available_cpus)    
        #pool = mp.Pool(5)       
        
        shot_lists = pool.map(take_shots, urls)

        pool.close()
        close_driver()
        
        self.dao_instance.store_screen_shots(shot_lists)

        

def take_shots(urlDict):        
        log.info('----------- starting to take shots ------------')
        
        url = urlDict['url']
        domain = urlDict['domain']
        print('taking shots for domain:' + domain)
        __driver.get(url.strip())
        img = __driver.get_screenshot_as_base64()
                
        shot_dict = {"domain": domain, "image": img}
        
        # enable when incase if needed to save into file system for system performance & just store file paths into DB
        # __driver.save_screenshot("%s %s" % (domain, ".png"))
        # __driver.close

        
        log.info('----------- take shots ended -----------')
        return shot_dict

def close_driver():
    screen_driver.close_resources(__driver)


class ScreenFinder:

    def __init__(self, config):
        log.info('--  ScreenFinder class constructor --')
        self.config = config
        self.dao_instance = ScreenShotDao(config)

    def find_screen(self, screen_domain):    
        img = self.dao_instance.retrieve_image(screen_domain)
        return img
