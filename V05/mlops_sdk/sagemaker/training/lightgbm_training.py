import boto3
import sagemaker
from sagemaker import hyperparameters
from sagemaker import image_uris, model_uris, script_uris


class LightGBMTraining:

    # Constantes
    train_model_id = "lightgbm-classification-model"
    train_model_version = "*"
    train_scope = "training"
    training_instance_type = "ml.m5.xlarge"

    def __init__(self, job_name, role, input_data, output_path, instance_type='ml.m5.large', instance_count=1):
        self.job_name = job_name
        self.client = boto3.client('sagemaker')
        self.train_image = self._retrieve_ligthgbm_image()
        self.train_script = self._retrieve_training_script()
        self.pretraining_model = self._retrieve_pretraining_model()
        self.config = self._build_config(role, input_data, output_path, instance_type, instance_count)


    def _retrieve_ligthgbm_image(self):
        # Retrieve the docker image
        train_image_uri = image_uris.retrieve(
            region=None,
            framework=None,
            model_id=train_model_id,
            model_version=train_model_version,
            image_scope=train_scope,
            instance_type=training_instance_type,
        )
        return train_image_uri

    def _retrieve_training_script(self):
        # Retrieve the training script
        train_source_uri = script_uris.retrieve(
            model_id=train_model_id, model_version=train_model_version, script_scope=train_scope
        )
        return train_source_uri


    def _retrieve_pretraining_model(self):
        # Retrieve the pre-trained model tarball to further fine-tune
        train_model_uri = model_uris.retrieve(
            model_id=train_model_id, model_version=train_model_version, model_scope=train_scope
        )
        return train_model_uri


    def _build_config(self, role, input_data, output_path, instance_type, instance_count):
        return {
            "TrainingJobName": self.job_name,
            "AlgorithmSpecification": {
                "TrainingImage": "1.dkr.ecr.us-west-2.amazonaws.com/lightgbm:latest",
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
