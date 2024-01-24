from esdbclient import EventStoreDBClient, NewEvent, StreamState
from uuid import uuid4


class DataLayer:

    def __init__(self, uri):
        self.uri = uri
    
    def connect(self):
        self.client = EventStoreDBClient(
            uri=f"{self.uri}"
        )

    def create_shout(self, shout):
        new_event = NewEvent(
            id=uuid4(),
            type="Shout",
            data=shout.encode('utf-8'),
        )
    
        self.client.append_to_stream(
            "platform-events",
            events=[new_event],
            current_version=StreamState.ANY,
        )

    def list_shouts(self, limit=100):
        events = self.client.get_stream("platform-events", limit=limit, backwards=True)
        return [event.data.decode('utf-8') for event in events if event.type == "Shout"]
