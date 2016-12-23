class ContainenvError(Exception):
    pass


class ProjectDirectoryDoesNotExist(ContainenvError):
    pass


class ProjectAlreadyInitialized(ContainenvError):
    pass


class ProjectContainsNoRegisteredNodes(ContainenvError):
    pass
