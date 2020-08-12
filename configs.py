import yaml


class ScreenConfigurations:
    def __init__(self):
        with open("screenshot_config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

            self.welcome_msg = cfg['welcome_msg']

            self.database = cfg['database']
            self.error_msg_driver_not_loaded = cfg.get('error_msg').get('driver_not_loaded')
            self.mongo_db_url = "%s%s%s%s%s%s%s" % (self.database['dbtype'], '://', self.database['username'], ':', self.database['password'], '@', self.database['host'])
            self.screens_shots_collections = cfg.get('database').get('screen_db_collections_name')

            self.api_url_header_get_screenshots = cfg.get('api_url_header_get')
            self.api_url_header_post = cfg.get('api_url_header_post')
            self.mimetype_appl_or_json = cfg.get('mimetype_appl_or_json')

            self.status_completed = cfg.get('status').get('completed')
            self.status_failed = cfg.get('status').get('failed')
            self.status_action = cfg.get('status').get('action')

            self.mimetype_image = cfg.get('mimetype_image')

            self.driver_options_headless = cfg.get('chrome').get('driver').get('options').get('headless_chrome')
            self.driver_options_disable_gpu = cfg.get('chrome').get('driver').get('options').get('disable_gpu')
            self.driver_options_start_full_screen = cfg.get('chrome').get('driver').get('options').get('start_full_screen')
            self.driver_options_test_type = cfg.get('chrome').get('driver').get('options').get('test_type')
            self.driver_options_ignore_certificate_errors = cfg.get('chrome').get('driver').get('options').get('ignore_certificate')


#class ScreenDatabaseConfig:
 #     def __init__(self):
  #          with open("screenshot_config.yml", 'r') as ymlfile:
   #               cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)    
    #              self.database = cfg['database']
     #             self.error_msg_driver_not_loaded = cfg.get('error_msg').get('driver_not_loaded')
      #            self.mongo_db_url = "%s%s%s%s%s%s%s" % (self.database['dbtype'], '://', self.database['username'], ':', self.database['password'], '@', self.database['host'])
       #           self.screens_shots_collections = cfg.get('database').get('screen_db_collections_name')
