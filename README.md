# mlops_sdk
sdk de mlops para aws integrando ferramentas caseiras


+-----------------------------------+
|          Início do Fluxo          |
+-----------------------------------+
                |
                v
+-----------------------------------+
| 1. Criação de Projeto             |
| - Nome, Descrição, Membros        |
| - Chama `create_project()`        |
+-----------------------------------+
                |
                v
+-----------------------------------+
| 2. Escolha do Tipo de Treinamento |
| - Builtin, Framework, ou Cidarta  |
+-----------------------------------+
                |
                v
+---------------------------------------------------------+
| 3. Criação do Training Job                              |
| - Chama `create_training_job()`                         |
| - Configurações: algoritmo, hyperparams, instance_type  |
| - Verifica se o treinamento deve ser local (run_locally)|
+---------------------------------------------------------+
                |
                v
+-----------------------------------+
| 4. Execução do Treinamento        |
| - No SageMaker ou Localmente      |
+-----------------------------------+
                |
                v
+-----------------------------------+
| 5. Aguardar Conclusão do Job      |
| - Verifica Status até Completar   |
+-----------------------------------+
                |
                v
+-----------------------------------+
| 6. Coleta de Resultados e Metadados|
| - Artefatos, hiperparams, outputs  |
+-----------------------------------+
                |
                v
+-----------------------------------+
| 7. Envio para o Model Registry    |
| - Upload de Artefatos e Metadados |
+-----------------------------------+
                |
                v
+-----------------------------------+
|          Fim do Fluxo             |
+-----------------------------------+

@startuml

class SageMakerFacade {
    -job_crud: JobCRUD
    -model_registry: ModelRegistryManager
    -default_s3_bucket: str
    -experiment_id: str
    -project_name: str
    +create_project(name: str, description: str, members: list[str]): str
    +create_training_job(mode: str, algorithm: str, hyperparameters: dict, blueprint: str, instance_type: str, instance_count: int, run_locally: bool, **kwargs): dict
    -_wait_for_completion(job_name: str)
}

class BuiltinAlgorithmTraining {
    -job_name: str
    -estimator: Estimator
    +__init__(job_name: str, algorithm: str, role: str, input_data: str, output_path: str, instance_type: str, instance_count: int, hyperparameters: dict, run_locally: bool)
    +run(): dict
}

class FrameworkTraining {
    -job_name: str
    -estimator: Estimator
    +__init__(job_name: str, algorithm: str, role: str, input_data: str, output_path: str, instance_type: str, instance_count: int, entry_point: str, framework_version: str, py_version: str, run_locally: bool)
    +run(): dict
}

class CidartaTraining {
    -job_name: str
    -config: dict
    +__init__(job_name: str, role: str, input_data: str, output_path: str, instance_type: str, instance_count: int, run_locally: bool)
    +run(): dict
}

class ModelRegistryManager {
    -andromeda: AndromedaSDK
    -project_id: str
    +create_project(name: str, description: str, members: list[str]): str
    +create_experiment(metadata: dict): str
    +upload_artifacts(experiment_id: str, artifacts: dict, metadata: dict)
    +generate_job_name(project_name: str, experiment_id: str): str
}

class JobCRUD {
    +get(job_name: str): dict
    +list(): list[dict]
    +delete(job_name: str): dict
}

SageMakerFacade --> BuiltinAlgorithmTraining : creates
SageMakerFacade --> FrameworkTraining : creates
SageMakerFacade --> CidartaTraining : creates
SageMakerFacade --> ModelRegistryManager : manages
SageMakerFacade --> JobCRUD : manages
ModelRegistryManager --> AndromedaSDK : uses

@enduml
