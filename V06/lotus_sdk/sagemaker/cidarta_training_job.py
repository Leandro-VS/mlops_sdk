from lotus_sdk.sagemaker.training_jobs.byoc_training import BYOCTraining

class CidartaTrainingJob(BYOCTraining):
    def __init__(self, role, input_data, output_path, instance_type="ml.m5.large", instance_count=1):
        image_uri = "your-account-id.dkr.ecr.your-region.amazonaws.com/cidarta:latest"  # URI do contêiner customizado
        super().__init__(image_uri, role, input_data, output_path, instance_type, instance_count)

    def run(self):
        print("Executando treinamento com Cidarta no SageMaker usando contêiner customizado.")
        return super().run()
