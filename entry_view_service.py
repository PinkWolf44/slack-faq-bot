from entry_view_data import EntryViewData

class EntryViewService:
    def __init__(self, body, client):
        self.body = body
        self.client = client

    def get_entry_view_data(self):
        data = EntryViewData(self.body)
        data.problem = self.get_problem(data.channel_id, data.thread_ts)
        return data

    def get_problem(self, channel_id, message_id):
        result = self.client.conversations_history(
            channel = channel_id,
            inclusive = True,
            oldest = message_id,
            limit = 1
        )

        messages = result['messages'][0]
        
        text = messages.get('text','')
        if text:
            return text

        attachements = messages.get('attachments',[])
        if attachements:
            attachement = attachements[0]
            return attachement['pretext'] + ' ' + attachement['title'] + ' ' + attachement['title_link'] 

        return text
