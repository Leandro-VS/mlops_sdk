from mlops_sdk.model_registry.andromeda_sdk.py import AndromedaSDK

class ModelRegistryManager:
    def __init__(self):
        self.andromeda = AndromedaSDK()
        self.project_id = None

    def create_project(self, name, description, members):
        self.project_id = self.andromeda.create_project(name, description, members)
        return self.project_id

    def create_experiment(self, metadata=None):
        if not self.project_id:
            raise ValueError("O projeto deve ser criado antes de iniciar um experimento.")
        experiment_id = self.andromeda.create_experiment(self.project_id, metadata)
        return experiment_id

    def upload_artifacts(self, experiment_id, artifacts, metadata=None):
        # Lógica para enviar artefatos e metadados ao Andromeda
        response = self.andromeda.upload_artifacts(experiment_id, artifacts, metadata)
        print(f"Artefatos e metadados enviados para o experimento {experiment_id}")
        return response

    def generate_job_name(self, project_name, experiment_id):
        return f"{project_name}-{experiment_id}-training-job"
