import mlflow
from importlib import import_module
import os
from dotenv import load_dotenv
import errno

def setup_with_dagshub(repo_owner:str,repo_name:str,experiment_name:str,runtime:str):
    '''
    Performs MLFlow setup with Dagshub as tracking server

    Arguments:
    repo_owner:str: Owner name of the dagshub repo
    repo_name:str: Dagshub repo name
    experiment_name:str: Experiment name in Dagshub tracking server
    runtime:str: Indicates currently active runtime type. Can be colab, jupyter or python-script
    '''
    
    if mlflow.is_tracking_uri_set() is True:
        print('MLFlow is already setup!!')
    else:
        if runtime=='colab':
            userdata=import_module('google.colab.userdata')
            os.environ['MLFLOW_TRACKING_USERNAME']=userdata.get('MLFLOW_TRACKING_USERNAME')
            os.environ['MLFLOW_TRACKING_PASSWORD']=userdata.get('MLFLOW_TRACKING_PASSWORD')
        elif runtime in ['jupyter','python-script']:
            if os.path.isfile(os.path.join(os.path.expanduser('~'),'.env',repo_name,'environment_variables.env')):
                load_dotenv(dotenv_path=os.path.join(os.path.expanduser('~'),'.env',repo_name,'environment_variables.env'))
            else:
                raise FileNotFoundError(errno.ENOENT,os.strerror(errno.ENOENT),'.env')
        
        mlflow.set_tracking_uri(f'https://dagshub.com/{repo_owner}/{repo_name}.mlflow')
        mlflow.set_experiment(experiment_name)

        print('MLFlow setup with Dagshub is done!!')



    

    






