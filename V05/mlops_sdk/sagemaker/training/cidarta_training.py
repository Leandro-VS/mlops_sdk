class CidartaTraining:
    def __init__(self, job_name, role, input_data, output_path, instance_type='ml.m5.large', instance_count=1):
        self.job_name = job_name
        self.client = boto3.client('sagemaker')
        self.config = self._build_config(role, input_data, output_path, instance_type, instance_count)

    def _build_config(self, role, input_data, output_path, instance_type, instance_count):
        return {
            "TrainingJobName": self.job_name,
            "AlgorithmSpecification": {
                "TrainingImage": "custom-cidarta-container:latest",  # Container customizado para o Cidarta
                "TrainingInputMode": "File"
            },
            "RoleArn": role,
            "InputDataConfig": [
                {
                    "ChannelName": "train",
                    "DataSource": {
                        "S3DataSource": {
                            "S3DataType": "S3Prefix",
                            "S3Uri": input_data,
                            "S3DataDistributionType": "FullyReplicated"
                        }
                    },
                    "ContentType": "text/csv",
                    "InputMode": "File"
                }
            ],
            "OutputDataConfig": {
                "S3OutputPath": output_path
            },
            "ResourceConfig": {
                "InstanceType": instance_type,
                "InstanceCount": instance_count,
                "VolumeSizeInGB": 50
            },
            "StoppingCondition": {
                "MaxRuntimeInSeconds": 86400
            }
        }

    def run(self):
        response = self.client.create_training_job(**self.config)
        return response
