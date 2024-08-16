from mlops_sdk.sagemaker.training.estimator_factory import EstimatorFactory

class FrameworkTraining:
    def __init__(self, job_name, framework, role, input_data, output_path, instance_type='ml.m5.large', instance_count=1, **kwargs):
        self.job_name = job_name
        self.estimator = EstimatorFactory.create_estimator(
            mode='framework',
            algorithm=framework,
            role=role,
            instance_type=instance_type,
            instance_count=instance_count,
            output_path=output_path,
            **kwargs
        )
        self.input_data = input_data

    def run(self):
        self.estimator.fit(self.input_data)
        return self.estimator.latest_training_job.describe()
