from entry_data import EntryData

class EntryService:
    def __init__(self, body, client):
        self.body = body
        self.client = client

    def get_entry_data(self):
        data = EntryData(self.body)
        data.message_link = self.get_message_link(data.channel, data.message_ts)
        data.thread_link = self.get_message_link(data.channel, data.thread_ts)
        return data

    def get_message_link(self, channel, message_id):
        response = self.client.chat_getPermalink(
            channel=channel,
            message_ts=message_id
        )
        return response.data['permalink']
    