from pathlib import Path
from ml_project.config_schemas.config_schema import Config
from ml_project.utils.config_utils  import get_config
from ml_project.utils.data_utils import initialize_dvc
from ml_project.utils.utils import get_logger

@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None: 
    initialize_dvc()

    initialize_dvc_storage(config.dvc_remote_name, config.dvc_remote_url)  


if __name__ == "__main__":
    version_data() 
