class FrameworkTraining:
    def __init__(self, framework, role, entry_point, input_data, output_path, instance_type="ml.m5.large", instance_count=1):
        self.framework = framework
        self.role = role
        self.entry_point = entry_point
        self.input_data = input_data
        self.output_path = output_path
        self.instance_type = instance_type
        self.instance_count = instance_count

    def run(self):
        # Lógica para criar e executar o Training Job com frameworks no SageMaker
        print(f"Executando treinamento com framework {self.framework}")
        return {"status": "success", "job_name": f"{self.framework}-training-job"}
