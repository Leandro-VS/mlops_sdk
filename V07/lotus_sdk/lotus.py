from lotus_sdk.andromeda.facade_andromeda import AndromedaFacade
from lotus_sdk.cidarta.facade_cidarta import CidartaFacade
from lotus_sdk.smith.facade_smith import SmithFacade
from lotus_sdk.aws.aws_utils import AWSUtils

class Lotus:
    def __init__(self):
        self.andromeda = AndromedaFacade()
        self.cidarta = CidartaFacade(self.andromeda)
        self.smith = SmithFacade()
        self.aws_utils = AWSUtils()

    def create_project(self, name, description, members):
        return self.andromeda.create_project(name, description, members)

    def list_blueprints_pipelines(self):
        return self.cidarta.list_blueprints()

    def train_model(self, project_id, data_train, target, blueprint, run_on_training_job=False):
        return self.cidarta.optimize(data_train, target, blueprint, run_on_training_job, project_id)

    def explainer_model(self, model_artifact):
        return self.cidarta.explainer(model_artifact)

    def get_features(self, feature_list):
        return self.smith.get_and_execute_query(feature_list)

    def aws_login(self):
        return self.aws_utils.aws_login()
