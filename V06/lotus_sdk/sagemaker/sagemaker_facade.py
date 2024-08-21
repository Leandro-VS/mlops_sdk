from lotus_sdk.sagemaker.training_jobs.builtin_training import BuiltinTraining
from lotus_sdk.sagemaker.training_jobs.framework_training import FrameworkTraining
from lotus_sdk.sagemaker.training_jobs.byoc_training import BYOCTraining

class SageMakerFacade:
    def __init__(self):
        self.default_role = "arn:aws:iam::123456789012:role/SageMakerRole"
        self.default_bucket = "sagemaker-bucket"

    def create_builtin_training(self, algorithm, input_data, output_path, hyperparameters, instance_type="ml.m5.large", instance_count=1):
        training_job = BuiltinTraining(
            algorithm=algorithm,
            role=self.default_role,
            input_data=input_data,
            output_path=output_path,
            hyperparameters=hyperparameters,
            instance_type=instance_type,
            instance_count=instance_count
        )
        return training_job.run()

    def create_framework_training(self, framework, entry_point, input_data, output_path, instance_type="ml.m5.large", instance_count=1):
        training_job = FrameworkTraining(
            framework=framework,
            role=self.default_role,
            entry_point=entry_point,
            input_data=input_data,
            output_path=output_path,
            instance_type=instance_type,
            instance_count=instance_count
        )
        return training_job.run()

    def create_byoc_training(self, image_uri, input_data, output_path, instance_type="ml.m5.large", instance_count=1):
        training_job = BYOCTraining(
            image_uri=image_uri,
            role=self.default_role,
            input_data=input_data,
            output_path=output_path,
            instance_type=instance_type,
            instance_count=instance_count
        )
        return training_job.run()
