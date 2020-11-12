import os,sys
import logging.config
import yaml

class SandboxLogger:
    logger=None
    def __init__(self,name,konfigFileName):
        self.logger = logging.getLogger(name)
        configPath = os.environ["PYTHONCONFIGPATH"]
        if configPath is None:
            print("Fatal error: env variable PYTHONCONFIGPATH not set ...exiting")
            sys.exit(0)

        configFileName = configPath + "/" + konfigFileName
        if os.path.exists(configFileName) == False:
            print("Fatal error: File " + configFileName + " does not exist...exiting")
            sys.exit(0)

        if os.path.exists(configFileName):
            with open(configFileName) as f:
                config = yaml.load(f.read())
            logging.config.dictConfig(config)

    def warning(self,message):
        self.logger.warning(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
            self.logger.debug(message)