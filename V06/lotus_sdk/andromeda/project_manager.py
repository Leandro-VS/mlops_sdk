class ProjectManager:

    def create_project(self, name, description, members):
        # Simulação da criação de um projeto
        project_id = '123'
        print(f"Andromeda create project: {project_id}")
        return project_id

    def create_experiment(self, project_id, metadata=None):
        # Simulação da criação de um experimento
        exp_id = '456'
        print(f'Andromeda Create Experiment {exp_id}')
        return exp_id

    def upload_artefatos(self, experiment_id):
        # Simulação do upload de artefatos para o um experimento no andromeda
        print(f'Enviando artefatos do experimento {experiment_id}')