'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC80f4fcd805491f6851f7e01e98c8a290" 
AUTH_TOKEN = "b150a4aed6c4498b7c6f3f11055040e2"
BSSSPAM_APP_SID = "AP51256f61ea0279b3e7d2f5b8c12c5ca4"
BSS_SPAM_ID = "+12023041284"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
