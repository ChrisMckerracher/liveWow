from dataclasses import dataclass


@dataclass
class Actor:
    id: str
    name: str
    flags: str
    raid_flags: str
