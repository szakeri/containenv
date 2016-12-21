class ContainenvError(Exception):
    pass


class ContainEnvDockerfileDoesNotExist(ContainenvError):
    pass


class ContainEnvDockerfileAlreadyExists(ContainenvError):
    pass
