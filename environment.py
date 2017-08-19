import os

CONTRACT_BASE_URL = os.environ['CONTRACT_BASE_URL']
CLAIM_BASE_URL = os.environ['CLAIM_BASE_URL']
LOCAL_ENVS = ['dev', 'qa', 'test', 'uat']
ALL_ENVS = ['dev', 'qa', 'test', 'uat', 'e2e', 'sit']

SIT_URL = os.environ['SIT_ENV_URL']
E2E_URL = os.environ['E2E_ENV_URL']
