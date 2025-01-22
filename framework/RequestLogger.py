import logging
from logging import Formatter 

class ServerLog:

    _instance = None
    



    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ServerLog, cls).__new__(cls)
            cls._instance.initialize_logger()
        return cls._instance

    def initialize_logger(self):
        self.log_file = 'app.log'
        self.apache_format = self.apache_format = '%(clientip)s - - [%(asctime)s +0000] "%(method)s %(url)s HTTP/1.1" %(status)s %(size)s'
        self.logger = logging.getLogger("server")
        self.logger.setLevel(logging.INFO)
        self.file_handler = logging.FileHandler(self.log_file)
        self.formatter = Formatter(self.apache_format, "%d/%b/%Y:%H:%M:%S")
        self.file_handler.setFormatter(self.formatter)
        
        if not self.logger.hasHandlers():
            self.logger.addHandler(self.file_handler)
        

    def log(self, client_ip, method, url, status, size, level=logging.INFO):

        extra = {
            'clientip': client_ip,
            'method': method,
            'url': url,
            'status': str(status),
            'size': str(size)
        }

        self.logger.log(level, "", extra=extra)


# server_log = ServerLog()

# # Test data simulating server request
# client_address = '127.0.0.1'
# http_response_method = 'GET'
# http_response_endpoint = '/index.html'
# http_response_status = 200
# http_response_size = 1024

# server_log.log(client_address, http_response_method, http_response_endpoint, http_response_status, http_response_size)