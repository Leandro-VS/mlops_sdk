import sagemaker
from sagemaker.sklearn import SKLearn

class SklearnTrainer:
    def __init__(self):
        self.sagemaker_session = sagemaker.Session()

    def train(self, entry_point, role, instance_type, **kwargs):
        print(f"Iniciando treinamento com sklearn no SageMaker")
        sklearn = SKLearn(
            entry_point=entry_point,
            role=role,
            instance_type=instance_type,
            sagemaker_session=self.sagemaker_session,
            **kwargs
        )
        sklearn.fit()
        return sklearn.latest_training_job.describe()
