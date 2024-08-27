from .sagemaker.sagemaker_trainer import SageMakerTrainer
from .cidarta_trainer import CidartaTrainer

class TrainingModule:
    def __init__(self, framework='sagemaker', mode='builtin'):
        if framework == 'sagemaker':
            self.trainer = SageMakerTrainer(mode=mode)
        elif framework == 'cidarta':
            self.trainer = CidartaTrainer()
        else:
            raise ValueError(f"Framework '{framework}' não é suportado")

    def run(self, project_id, **kwargs):
        if not project_id:
            raise ValueError("O project_id é necessário para executar o treinamento.")
        return self.trainer.train(project_id=project_id, **kwargs)
