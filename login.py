import requests
import time
import logging
import logging.handlers

LOG_FILENAME = "logging.out"            #creates a log file called logging.out
#setting up the logger
logger = logging.getLogger('MyLogger')  
logger.setLevel(logging.DEBUG)

def main():  
    #setup for logging
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes=50,
                                               )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  #format in which the logs are displayed
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    #define url to log into and the username and password as variables
    url = 'url'
    user = 'user'
    password = "password"
    #data that is sent to the server
    data = {
        'user': user,
        'pass': password,
    }
    #while loop to account for loss of internet, try till the system has a net connection and logs in successfully
    while(1):
        try:
            response = requests.post(url, data=data)
            #status code 200 indicates a successful login and hence we check for it
            if response.status_code == 200:
                logger.info("Successfully logged in as {username}".format(username=user))
                break
            else:
                logger.info("Login unsuccessful: HTTP/{status_code}".format(status_code=response.status_code))
                continue
        except Exception as err:
            logger.exception(err)
            time.sleep(5) 
            continue
        
if __name__ == "__main__":
   main() 
