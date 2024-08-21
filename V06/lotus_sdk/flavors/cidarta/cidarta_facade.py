# from cidarta.eda import EDA
# from cidarta.catalog import Catalog
# from cidarta.explainers import Explainers
from lotus_sdk.flavors.cidarta.new_optimizer import Optimizer
from lotus_sdk.sagemaker.cidarta_training_job import CidartaTrainingJob

class CidartaFacade:
    def __init__(self, sagemaker_facade, project_manager):
        # self.eda = EDA()
        # self.catalog = Catalog()
        self.optimizer = Optimizer(sagemaker_facade, project_manager)
        # self.explainers = Explainers()

    def run_eda(self, data):
        print(f'Run Cidarta EDA on {data}')

    def list_blueprints(self):
        print('Cidarta Blueprints List')

    def optimize(self, data, blueprint, run_locally, project_id):
        # Cria automaticamente um experimento antes de realizar o treinamento
        experiment_id = self.optimizer.project_manager.create_experiment(project_id)
        print(f"Experimento criado automaticamente com ID: {experiment_id}")
        return self.optimizer.run(data, blueprint, run_locally, experiment_id)


    def explain(self, model):
        print('Cidarta Explain Model')