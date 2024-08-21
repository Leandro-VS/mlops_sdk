from mlops_sdk.sagemaker import SageMakerFacade


########### Builtin
### Cidarta
facade = SageMakerFacade()
project_id = facade.create_project(
    name="ML Project Cidarta",
    description="Projeto para treinamento com Cidarta",
    members=["user1"]
)

response = facade.create_training_job(
    mode="cidarta",
    input_data="s3://my-bucket/data",
    instance_type="ml.m5.large",
    instance_count=1,
    run_locally=False  # Pode ser alterado para True para rodar localmente
)

