from .builtin_algorithm_trainer import BuiltinAlgorithmTrainer
from .sklearn_trainer import SklearnTrainer
from .pytorch_trainer import PytorchTrainer

class SageMakerTrainer:
    def __init__(self, mode='builtin'):
        if mode == 'builtin':
            self.trainer = BuiltinAlgorithmTrainer()
        elif mode == 'sklearn':
            self.trainer = SklearnTrainer()
        elif mode == 'pytorch':
            self.trainer = PytorchTrainer()
        else:
            raise ValueError(f"Modo '{mode}' não é suportado para SageMaker")

    def train(self, project_id, **kwargs):
        if not project_id:
            raise ValueError("O project_id é necessário para executar o treinamento.")
        return self.trainer.train(project_id=project_id, **kwargs)
