class BuiltinTraining:
    def __init__(self, algorithm, role, input_data, output_path, hyperparameters, instance_type="ml.m5.large", instance_count=1):
        self.algorithm = algorithm
        self.role = role
        self.input_data = input_data
        self.output_path = output_path
        self.hyperparameters = hyperparameters
        self.instance_type = instance_type
        self.instance_count = instance_count

    def run(self):
        # Lógica para criar e executar o Training Job no SageMaker
        print(f"Executando treinamento builtin com algoritmo {self.algorithm}")
        return {"status": "success", "job_name": f"{self.algorithm}-training-job"}
