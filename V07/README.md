```
@startuml

class Lotus {
  +create_project(name, description, members)
  +train_model(project_id, data, blueprint, run_locally)
  +get_features_and_execute_query(feature_list)
  +aws_login(role)
}

class AndromedaFacade {
  +create_project(name, description, members)
  +create_experiment(project_id)
}

class CidartaFacade {
  +optimize(data, blueprint, run_locally, project_id)
}

class SmithFacade {
  +get_and_execute_query(feature_list)
  +get_feature_metadata(feature_list)
  +build_query(metadata)
  +execute_query(query)
}

class AWSUtils {
  +aws_login(role)
}

Lotus --> AndromedaFacade : uses
Lotus --> CidartaFacade : uses
Lotus --> SmithFacade : uses
Lotus --> AWSUtils : uses
CidartaFacade --> AndromedaFacade : uses
SmithFacade --> AWSUtils : uses

@enduml


```