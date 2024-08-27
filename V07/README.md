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
  +upload_artefacts()
}

class CidartaFacade {
  +optimize(data, blueprint, run_locally, project_id)
  +explain(model)
}

class SmithFacade {
  +get_features(feature_list)
  +execute_query(query, account_credentials)
  +get_and_execute_query(feature_list)
}

class SQLGenerator {
  +generate_query(features, metadata)
}

class AWSUtils {
  +aws_login(role)
  +get_role_credentials()
  +get_account_credentials()
  +run_on_sagemaker_studio()
  +run_on_aws()
}

class Interface {
  +NewGetMetadata()
  +ReturnDF()
}

class Back_DataGov {
  +NewGetMetadata()
}

class API_DATAGOV {
  +NewGetMetadata()
}

Lotus --> AndromedaFacade : uses
Lotus --> CidartaFacade : uses
Lotus --> SmithFacade : uses
Lotus --> AWSUtils : uses
CidartaFacade --> AndromedaFacade : uses
SmithFacade --> SQLGenerator : uses
SmithFacade --> AWSUtils : uses
SQLGenerator --> Interface : uses
Interface --> Back_DataGov : uses
Interface --> API_DATAGOV : uses

@enduml



```