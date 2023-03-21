from src.domain.event.event import Event


class SwingDamageEvent(Event):
    def __init__(self, timestamp, sub_event, hide_caster, source_guid,
                 source_name, source_flags, source_raid_flags, dest_guid, dest_name, dest_flags,
                 dest_raid_flags, amount, overkill, school, resisted, blocked, absorbed, critical,
                 glancing, crushing, is_off_hand):
        self.timestamp = timestamp
        self.sub_event = sub_event
        self.hide_caster = hide_caster
        self.source_guid = source_guid
        self.source_name = source_name
        self.source_flags = source_flags
        self.source_raid_flags = source_raid_flags
        self.dest_guid = dest_guid
        self.dest_name = dest_name
        self.dest_flags = dest_flags
        self.dest_raid_flags = dest_raid_flags
        self.amount = amount
        self.overkill = overkill
        self.school = school
        self.resisted = resisted
        self.blocked = blocked
        self.absorbed = absorbed
        self.critical = critical
        self.glancing = glancing
        self.crushing = crushing
        self.is_off_hand = is_off_hand
