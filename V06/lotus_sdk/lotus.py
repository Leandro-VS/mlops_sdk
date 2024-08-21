from lotus_sdk.andromeda.project_manager import ProjectManager
from lotus_sdk.flavors.cidarta.cidarta_facade import CidartaFacade
from lotus_sdk.flavors.other_flavor.other_flavor_facade import OtherFlavor
from lotus_sdk.sagemaker.sagemaker_facade import SageMakerFacade

class Lotus:
    def __init__(self):
        self.project_manager = ProjectManager()
        self.sagemaker_job_manager = SageMakerFacade()
        self.flavors = {
            'cidarta': CidartaFacade(self.sagemaker_job_manager, self.project_manager),
            'other_flavor': OtherFlavor()
        }

    def create_project(self, name, description, members):
        return self.project_manager.create_project(name, description, members)

    def create_experiment(self, project_id, metadata=None):
        return self.project_manager.create_experiment(project_id, metadata)

    def list_flavors(self):
        return list(self.flavors.keys())

    def train_with_flavor(self, flavor_name):
        flavor = self.flavors.get(flavor_name)
        if not flavor:
            raise ValueError(f"Flavor '{flavor_name}' não suportado.")
        return flavor
