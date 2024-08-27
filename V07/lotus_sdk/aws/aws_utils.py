import os

class AWSUtils:
    def __init__(self):
        self.run_on_sagemaker_studio = os.getenv('SAGEMAKER_STUDIO')

    def aws_login(self):
        # Lógica para login na AWS e resgate das credenciais
        if self.run_on_sagemaker_studio is not None:
            return {"role_credentials": "role_based_credentials"}
        else:
            return {"account_credentials": "account_based_credentials"}
