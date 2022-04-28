class EntryViewData:
    def __init__(self, body):
        self.channel_id = body['channel']['id']
        self.message_ts = body['message_ts']
        self.thread_ts = body['message']['thread_ts']
        self.metadata = self.channel_id + '-' + self.message_ts + '-' + self.thread_ts
        self.solution = body['message']['text']
        self.problem = ''
