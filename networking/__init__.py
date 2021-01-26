import importlib

_protocols = {}


class UnsupportedVersion(Exception):
    """Raised when the server does not support the requested protocol version."""


def get_protocol_library(version: int):
    """
    Returns the entire module object associated with the given protocol version.
    
    :param version: The version number to get.
    :raises UnsupportedVersion: The provided protocol version isn't supported.
    :return: The module with that protocol version's packets and information.
    """
    if _protocols.get(version, None) is not None:
        return _protocols[version]
    name = f"protocol_{version}"
    try:
        module = importlib.import_module(name)
    except Exception as e:
        if isinstance(e, ModuleNotFoundError):
            # todo: log_info("unsupported client tried connecting")
            # We couldn't find that module. No need to show the cause exception
            raise UnsupportedVersion(f"No protocol library for version {version}") from None
        else:
            # todo: log_error(e) ...
            # If we couldn't import the module for another reason (bad code?) then indicate that.
            raise UnsupportedVersion(f"Exception loading protocol library for version {version}") from e
    _protocols[version] = module
    return module


if __name__ == '__main__':
    get_protocol_library(578)
    breakpoint()
