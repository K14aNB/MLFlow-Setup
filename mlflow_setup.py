import mlflow
from importlib import import_module
import os
from dotenv import load_dotenv

def setup_with_dagshub(repo_owner:str,repo_name:str,experiment_name:str,runtime:str,dotenv_path=None):
    '''
    Performs MLFlow setup with Dagshub as tracking server

    Arguments:
    repo_owner:str: Owner name of the dagshub repo
    repo_name:str: Dagshub repo name
    experiment_name:str: Experiment name in Dagshub tracking server
    runtime:str: Indicates currently active runtime type. Can be colab, jupyter or python-script
    dotenv_path:str: Optional argument which is required if using local runtime (jupyter or python-script)
                     default is None
    '''
    if runtime=='colab':
        userdata=import_module('google.colab.userdata')
        os.environ['MLFLOW_TRACKING_USERNAME']=userdata.get('MLFLOW_TRACKING_USERNAME')
    elif runtime in ['jupyter','python-script']:
        if dotenv_path is not None :
            if '~' in dotenv_path:
                dotenv_path=dotenv_path.split('~/')[1]
                dotenv_path=os.path.join(os.path.expanduser('~'),dotenv_path)
            load_dotenv(dotenv_path=dotenv_path)
        else:
            raise FileNotFoundError(errno.ENOENT,os.strerror(errno.ENOENT),'.env')
    
    mlflow.set_tracking_uri(f'https://dagshub.com/{repo_owner}/{repo_name}.mlflow')
    mlflow.set_experiment(experiment_name)

    print('MLFlow setup with Dagshub is done!!')



    

    






