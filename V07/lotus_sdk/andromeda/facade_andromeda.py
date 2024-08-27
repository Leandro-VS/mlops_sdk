class AndromedaFacade:
    def create_project(self, name, description, members):
        # Implementa a lógica para criar o projeto no Andromeda
        project_id = '0123456'
        print(f'Projeto Criado no Andromeda')
        return project_id

    def create_experiment(self, project_id):
        # Implementa a lógica para criar um experimento no Andromeda
        exp_id = '789456'
        print(f"Experimento com id {exp_id}, criado no projeto {project_id}")
        return exp_id

