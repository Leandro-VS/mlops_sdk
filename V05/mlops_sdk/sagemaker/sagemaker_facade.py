import time
from mlops_sdk.sagemaker.training.builtin_algorithm_training import BuiltinAlgorithmTraining
from mlops_sdk.sagemaker.training.framework_training import FrameworkTraining
from mlops_sdk.sagemaker.training.cidarta_training import CidartaTraining
from mlops_sdk.sagemaker.job_management.job_crud import JobCRUD
from mlops_sdk.model_registry.model_registry_manager import ModelRegistryManager

DEFAULT_ROLE = "arn:aws:iam::123456789012:role/DefaultSageMakerRole"

class SageMakerFacade:
    def __init__(self):
        self.job_crud = JobCRUD()
        self.model_registry = ModelRegistryManager()
        self.default_s3_bucket = "your-default-s3-bucket"
        self.experiment_id = None
        self.project_name = None

    def create_project(self, name, description, members):
        self.project_name = name
        project_id = self.model_registry.create_project(name, description, members)
        print(f"Projeto criado com ID {project_id}")
        return project_id

    def create_training_job(self, mode, algorithm=None, hyperparameters=None, blueprint=None, instance_type='ml.m5.large', instance_count=1, run_locally=False, **kwargs):
        if not self.project_name:
            raise ValueError("Um projeto deve ser criado antes de iniciar um treinamento. Chame o método 'create_project'.")

        self.experiment_id = self.model_registry.create_experiment()

        # Gerar nome único para o Training Job
        job_name = self.model_registry.generate_job_name(self.project_name, self.experiment_id)

        # Definir o caminho S3 com base na hierarquia
        s3_output_path = f"s3://{self.default_s3_bucket}/{self.model_registry.project_id}/{self.experiment_id}/output/"

        if mode == 'builtin':
            job = BuiltinAlgorithmTraining(
                job_name,
                algorithm,
                role=DEFAULT_ROLE,
                input_data=kwargs.get('input_data'),
                output_path=s3_output_path,
                instance_type=instance_type,
                instance_count=instance_count,
                hyperparameters=hyperparameters,
                run_locally=run_locally
            )
        elif mode == 'framework':
            job = FrameworkTraining(
                job_name,
                algorithm,
                role=DEFAULT_ROLE,
                input_data=kwargs.get('input_data'),
                output_path=s3_output_path,
                instance_type=instance_type,
                instance_count=instance_count,
                entry_point=kwargs.get('entry_point'),
                framework_version=kwargs.get('framework_version'),
                py_version=kwargs.get('py_version'),
                run_locally=run_locally
            )
        elif mode == 'cidarta':
            job = CidartaTraining(
                job_name,
                role=DEFAULT_ROLE,
                input_data=kwargs.get('input_data'),
                output_path=s3_output_path,
                instance_type=instance_type,
                instance_count=instance_count,
                run_locally=run_locally
            )
        else:
            raise ValueError(f"Modo '{mode}' não é suportado.")

        response = job.run()

        # Verificar status do treinamento e coletar metadados
        self._wait_for_completion(job_name)
        metadata = {
            "job_name": job_name,
            "mode": mode,
            "algorithm": algorithm,
            "blueprint": blueprint,
            "output_path": s3_output_path,
        }

        # Enviar metadados e artefatos para o Model Registry
        artifacts = {"model": s3_output_path}
        self.model_registry.upload_artifacts(self.experiment_id, artifacts, metadata)

        return response


    def _wait_for_completion(self, job_name):
        print(f"Aguardando a conclusão do job '{job_name}'...")
        while True:
            status = self.job_crud.get(job_name)['TrainingJobStatus']
            if status == 'Completed':
                print(f"Job '{job_name}' concluído com sucesso.")
                break
            elif status in ['Failed', 'Stopped']:
                raise Exception(f"Job '{job_name}' falhou ou foi interrompido com status '{status}'.")
            time.sleep(30)  # Aguarda 30 segundos antes de checar novamente

    def get_training_job(self, job_name):
        return self.job_crud.get(job_name)

    def list_training_jobs(self):
        return self.job_crud.list()

    def delete_training_job(self, job_name):
        return self.job_crud.delete(job_name)
