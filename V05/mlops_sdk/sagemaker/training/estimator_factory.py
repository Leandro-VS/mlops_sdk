from sagemaker.estimator import Estimator
from sagemaker.sklearn import SKLearn
from sagemaker.pytorch import PyTorch

class EstimatorFactory:
    @staticmethod
    def create_estimator(mode, algorithm=None, role=None, instance_type='ml.m5.large', instance_count=1, hyperparameters=None, **kwargs):
        if mode == 'builtin':
            return EstimatorFactory._create_builtin_estimator(algorithm, role, instance_type, instance_count, hyperparameters, **kwargs)
        elif mode == 'framework':
            return EstimatorFactory._create_framework_estimator(algorithm, role, instance_type, instance_count, **kwargs)
        else:
            raise ValueError(f"Modo '{mode}' não é suportado.")

    @staticmethod
    def _create_builtin_estimator(algorithm, role, instance_type, instance_count, hyperparameters=None, **kwargs):
        estimator = Estimator(
            image_uri=f"1.dkr.ecr.us-west-2.amazonaws.com/{algorithm}:latest",
            role=role,
            instance_type=instance_type,
            instance_count=instance_count,
            **kwargs
        )
        if hyperparameters:
            estimator.set_hyperparameters(**hyperparameters)
        return estimator

    @staticmethod
    def _create_framework_estimator(algorithm, role, instance_type, instance_count, **kwargs):
        if algorithm == 'sklearn':
            return SKLearn(
                entry_point=kwargs.get('entry_point'),
                role=role,
                instance_type=instance_type,
                instance_count=instance_count,
                **kwargs
            )
        elif algorithm == 'pytorch':
            return PyTorch(
                entry_point=kwargs.get('entry_point'),
                role=role,
                instance_type=instance_type,
                instance_count=instance_count,
                framework_version=kwargs.get('framework_version', '1.5.0'),
                py_version=kwargs.get('py_version', 'py3'),
                **kwargs
            )
        else:
            raise ValueError(f"Framework '{algorithm}' não é suportado.")
