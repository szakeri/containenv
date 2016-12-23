class ContainenvError(Exception):
    pass


class ProjectDirectoryDoesNotExist(ContainenvError):
    pass


class ProjectAlreadyInitialized(ContainenvError):
    pass
