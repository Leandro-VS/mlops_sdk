from mlops_sdk.data_prep.data_prep_module import DataPrepModule
from mlops_sdk.training.training_module import TrainingModule
from mlops_sdk.model_registry.andromeda_registry import AndromedaRegistry

class MlOpsFacade:
    def __init__(self):
        self.project_id = None
        self.andromeda_registry = AndromedaRegistry()

    def start_project(self, project_name, **kwargs):
        project_details = self.andromeda_registry.create_project(project_name, **kwargs)
        self.project_id = project_details["project_id"]
        print(f"Projeto {project_name} iniciado com ID {self.project_id}")
        return project_details

    def run_data_prep(self, **kwargs):
        if not self.project_id:
            raise ValueError("O projeto deve ser iniciado antes de executar essa etapa.")
        data_prep = DataPrepModule()
        return data_prep.run(project_id=self.project_id, **kwargs)

    def train_model(self, framework='sagemaker', mode='builtin', **kwargs):
        if not self.project_id:
            raise ValueError("O projeto deve ser iniciado antes de executar essa etapa.")
        training = TrainingModule(framework=framework, mode=mode)
        return training.run(project_id=self.project_id, **kwargs)

    def register_model(self, model_name, **kwargs):
        if not self.project_id:
            raise ValueError("O projeto deve ser iniciado antes de executar essa etapa.")
        return self.andromeda_registry.register_model(self.project_id, model_name, **kwargs)
