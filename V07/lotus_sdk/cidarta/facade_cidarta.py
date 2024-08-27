class CidartaFacade:
    def __init__(self, andromeda_facade):
        self.andromeda = andromeda_facade

    def list_blueprints(self):
        blueprints = {
            "simple_clf": "Default Classifier with common preprocessing steps",
            "xgboost_clf": "XGBoost Classifier with common preprocessing steps",
            "xgboost_reg": "XGBoost Regressor with common preprocessing steps"
        }
        return blueprints


    def optimize(self, data_train, target, blueprint, run_on_training_job, project_id):
        # Cria automaticamente um experimento antes de realizar o treinamento
        experiment_id = self.andromeda.create_experiment(project_id)
        print(f"Experimento criado automaticamente com ID: {experiment_id}")
        if not run_on_training_job:
            # Lógica para executar o treinamento localmente
            model_artifact = "<class 'sklearn.pipeline.Pipeline'>"
            return {"status": "success", "model": model_artifact, "experiment_id": experiment_id}
        else:
            # Lógica para executar o treinamento no SageMaker
            return {"status": "submitted", "job_name": "sagemaker-training-job", "experiment_id": experiment_id}


    def explainer(self, model):
        return "Lotus Explain Model"