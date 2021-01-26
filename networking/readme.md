### Adding new protocol versions

The networking submodule is designed such that different protocol versions may be added in their own folders named for 
their protocol number. Each folder should have a few things:
 
 - `packets.py` defining all of the packets for that protocol version.
 - `ids.py` defining the clientbound packet IDs of all packets, as both a dict and Enum.
 - `lookup.py` defining the serverbound packet ID lookups of all packets, which reference the corresponding packet
  object in `packets.py`.
 - `__init__.py` defining the numeric protocol number, game version as a string, and `__all__` with the files in
  the folder.

Splitting the information out into several files is required in order to prevent circular dependencies (`lookup.py` 
requires `packets.py` and `packets.py` requires `ids.py`, and all of these is required by `__init__.py`).

The new protocol module will be lazy-loaded by the server at runtime: the library will not be executed until the
protocol library is explicitly loaded by the server (eg. by a client of that version connecting). This also means
that compile-time errors will not be discovered until such time as well (though any such compile-time errors will be
logged). In testing, it is recommended to put `get_protocol_library(n)` in a `main` statement and run it. 

`networking.connection.Connection` should check for what clientbound packets/operations are available before sending
out a new packet to the client. If the connected client's version is lower than the version the packet was added, then 
the packet should be ignored, and optionally logged (only one time) to either the server log or to the client's chat, 
or both.
