from src.domain.event.event import Event


#Representing a change in movement, health, mana, etc. IE: a delta on a value of an actor

class ActorEvent(Event):
    event_types = ["location.update",
                   "health.update",
                   "mana.update",
                   #ToDo: should death be a health change event?
                   "Death"
                   #ToDo: cooldown change is an aggregate change, that is a cooldown to what? vs mana is just a value change
                   "cooldown.update"]
    #ToDo: If cooldown change is valid, we need to track what resource is being cooled down
    resource = None
    old_value = None
    new_value = None
    pass