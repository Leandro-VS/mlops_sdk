from mlops_sdk.sagemaker.training.estimator_factory import EstimatorFactory

class BuiltinAlgorithmTraining:
    def __init__(self, job_name, algorithm, role, input_data, output_path, instance_type='ml.m5.large', instance_count=1, hyperparameters=None, run_locally=False):
        self.job_name = job_name
        self.run_locally = run_locally
        self.estimator = Estimator(
            image_uri=f"1.dkr.ecr.us-west-2.amazonaws.com/{algorithm}:latest",
            role=role,
            instance_type=instance_type,
            instance_count=instance_count,
            output_path=output_path
        )
        if hyperparameters:
            self.estimator.set_hyperparameters(**hyperparameters)

    def run(self):
        if self.run_locally:
            print(f"Rodando o job '{self.job_name}' localmente...")
            self.estimator.fit(inputs=self.input_data, wait=True, logs=True, job_name=self.job_name, run_locally=True)
        else:
            print(f"Rodando o job '{self.job_name}' no SageMaker...")
            self.estimator.fit(inputs=self.input_data, wait=True, logs=True, job_name=self.job_name)
