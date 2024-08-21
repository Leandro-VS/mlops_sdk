# from cidarta import optimizer

class Optimizer:
    def __init__(self, sagemaker_facade, project_manager):
        self.sagemaker_facade = sagemaker_facade
        self.project_manager = project_manager

    def run(self, data, blueprint, run_locally, experiment_id):
        if run_locally:
            print(f"Executando o treinamento com o blueprint {blueprint} localmente.")
            self.project_manager.upload_artefatos(experiment_id)
            return {"status": "success", "model": "local_model", "experiment_id": experiment_id}
        else:
            print(f"Executando o treinamento com o blueprint {blueprint} no SageMaker.")
            training_result = self.sagemaker_facade.create_byoc_training(
                image_uri="your-account-id.dkr.ecr.your-region.amazonaws.com/cidarta:latest",
                input_data=data,
                output_path=f"s3://{self.sagemaker_facade.default_bucket}/output/",
                instance_type="ml.m5.large",
                instance_count=1
            )
            self.project_manager.upload_artefatos(experiment_id)
            return {"status": training_result["status"], "job_name": training_result["job_name"], "experiment_id": experiment_id}
