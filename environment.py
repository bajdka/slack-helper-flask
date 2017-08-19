import os

CONTRACT_BASE_URL = os.environ['CONTRACT_BASE_URL']
CLAIM_BASE_URL = os.environ['CLAIM_BASE_URL']
LOCAL_ENVS = ['dev', 'qa', 'test', 'uat']
ALL_ENVS = ['dev', 'qa', 'test', 'uat', 'e2e', 'sit']
CLAIM_MODULE = 'claims'
CONTRACT_MODULE = 'contract'

SIT_URL = os.environ['SIT_ENV_URL']
E2E_URL = os.environ['E2E_ENV_URL']

def get_url(module, env):
    if env in LOCAL_ENVS:
        return get_local_env_url(module, env)
    elif env == 'sit':
        return SIT_URL % module
    elif env == 'e2e':
        return E2E_URL % module

def get_local_env_url(module, env): 
    if module == CLAIM_MODULE:
        return CLAIM_BASE_URL % env
    elif module == CONTRACT_MODULE:
        return CONTRACT_BASE_URL % env
