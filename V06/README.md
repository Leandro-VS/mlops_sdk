# Diagrama de Sequencia

@startuml
actor Usuario as U
participant Lotus as L
participant "CidartaFacade" as CF
participant "ProjectManager" as PM
participant "Optimizer" as O
participant "SageMakerFacade" as SMF

U -> L: create_project(name, description, members)
L -> PM: create_project(name, description, members)
PM -> L: project_id
L -> U: project_id

U -> L: train_with_flavor(flavor_name, project_id, data, blueprint, run_locally)
L -> CF: optimize(data, blueprint, run_locally, project_id)
CF -> PM: create_experiment(project_id)
PM -> CF: experiment_id
CF -> O: run(data, blueprint, run_locally, experiment_id)
alt run_locally == True
    O -> CF: {"status": "success", "model": "local_model"}
else run_locally == False
    O -> SMF: create_byoc_training(...)
    SMF -> O: {"status": "success", "job_name": "byoc-training-job"}
end
O -> CF: Result of Training
CF -> L: Result
L -> U: Result
@enduml


# Diagrama UML

@startuml

class Lotus {
  +create_project(name, description, members)
  +list_flavors()
  +train_with_flavor(flavor_name, project_id, data, blueprint, run_locally)
}

class ProjectManager {
  +create_project(name, description, members)
  +create_experiment(project_id)
}

class CidartaFacade {
  +run_eda(data)
  +list_blueprints()
  +optimize(data, blueprint, run_locally, project_id)
  +explain(model)
}

class Optimizer {
  +run(data, blueprint, run_locally, experiment_id)
}

class SageMakerFacade {
  +create_builtin_training(algorithm, input_data, output_path, hyperparameters, instance_type, instance_count)
  +create_framework_training(framework, entry_point, input_data, output_path, instance_type, instance_count)
  +create_byoc_training(image_uri, input_data, output_path, instance_type, instance_count)
}

class BuiltinTraining {
  +run()
}

class FrameworkTraining {
  +run()
}

class BYOCTraining {
  +run()
}

Lotus --> ProjectManager : uses
Lotus --> CidartaFacade : uses
Lotus --> SageMakerFacade : uses
CidartaFacade --> Optimizer : uses
Optimizer --> SageMakerFacade : uses
SageMakerFacade --> BuiltinTraining : creates
SageMakerFacade --> FrameworkTraining : creates
SageMakerFacade --> BYOCTraining : creates
CidartaFacade --> ProjectManager : uses

@enduml
