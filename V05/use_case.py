from mlops_sdk.sagemaker import SageMakerFacade


########### Builtin
facade = SageMakerFacade()
project_id = facade.create_project(
    name="ML Project Builtin",
    description="Projeto para treinamento com algoritmo builtin (LightGBM)",
    members=["user1"]
)

response = facade.create_training_job(
    mode="builtin",
    algorithm="lightgbm",
    input_data="s3://my-bucket/data",
    hyperparameters={
        "learning_rate": 0.05,
        "num_leaves": 31,
        "objective": "binary"
    },
    instance_type="ml.c5.xlarge",
    instance_count=2,
    run_locally=False  # Pode ser alterado para True para rodar localmente
)

########### Framework
facade = SageMakerFacade()
project_id = facade.create_project(
    name="ML Project Sklearn",
    description="Projeto para treinamento com framework Sklearn",
    members=["user1"]
)

response = facade.create_training_job(
    mode="framework",
    algorithm="sklearn",
    input_data="s3://my-bucket/data",
    instance_type="ml.m5.large",
    instance_count=1,
    entry_point="train.py",  # O script de treinamento a ser executado
    framework_version="0.23-1",
    py_version="py3",
    run_locally=False  # Pode ser alterado para True para rodar localmente
)


########### Cidarta
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

