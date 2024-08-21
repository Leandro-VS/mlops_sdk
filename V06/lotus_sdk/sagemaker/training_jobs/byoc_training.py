class BYOCTraining:
    def __init__(self, image_uri, role, input_data, output_path, instance_type="ml.m5.large", instance_count=1):
        self.image_uri = image_uri
        self.role = role
        self.input_data = input_data
        self.output_path = output_path
        self.instance_type = instance_type
        self.instance_count = instance_count

    def run(self):
        # Lógica para criar e executar o Training Job com contêineres customizados no SageMaker
        print(f"Executando treinamento com contêiner customizado {self.image_uri}")
        return {"status": "success", "job_name": "byoc-training-job"}
