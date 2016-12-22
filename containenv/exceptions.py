class ContainenvError(Exception):
    pass


class ProjectDirectoryDoesNotExist(ContainenvError):
    pass


class ProjectAlreadyInitialized(ContainenvError):
    pass


class ContainEnvDockerfileDoesNotExist(ContainenvError):
    pass


class ContainEnvDockerfileAlreadyExists(ContainenvError):
    pass
