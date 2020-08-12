'''

screenshots as a service -- Driver class responsible for installing and making available of the webdriver
This class has function to first check if the driver there in cache else installs first time

'''

import logging
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

log = logging.getLogger(__name__)


class ScreenWebDriver:

    def __init__(self, config):        
        log.info('--  ScreenWebDriver class constructor --')
        self.config = config

    def get_driver(self):        
        options = self.__config_options()        
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        except Exception as exc:            
            log.info(self.config.error_msg_driver_not_loaded)
            log.error(sys.exc_info()[0], exc_info=True)
            raise RuntimeError(self.config.error_msg_driver_not_loaded, sys.exc_info()[0])
        else:
            return driver

    def __config_options(self):
        options = Options()
        options.add_argument(self.config.driver_options_ignore_certificate_errors)
        options.add_argument(self.config.driver_options_headless)
        options.add_argument(self.config.driver_options_disable_gpu)
        options.add_argument(self.config.driver_options_start_full_screen)
        options.add_argument(self.config.driver_options_test_type)
        return options

    def close_resources(self, driver):
        driver.close()
        log.info('----------- resource closed -----------')       


# will be used in case auto install doesnt works -- Deprecated function kind of
def get_driver_manually(self):
    log.info('----------- Starting to load driver -----------')
    options = self.__config_options()
    try:
        options.binary_location = "./test/chromedriver.exe"
        # options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
        # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=options)
        driver = webdriver.Chrome(options=options)
        log.info('----------- Driver Loaded -----------')

    except Exception:
        log.info('Unable to load Driver, please check if its installed correctly')
        log.info(sys.exc_info()[0])
    else:
        return driver
