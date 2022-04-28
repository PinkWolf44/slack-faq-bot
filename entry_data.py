class EntryData:
    def __init__(self, body):
        self.metadata = body['view']['private_metadata'].split('-')
        self.selected_options = body['view']['state']['values']['product']['selected_product']['selected_options']
        self.selected_products = ','.join(list(map(lambda x: x['value'], self.selected_options)))
        self.problem_question = body['view']['state']['values']['problem']['problem_question']['value']
        self.solution_response = body['view']['state']['values']['solution']['solution_response']['value']
        self.channel = self.metadata[0]
        self.message_ts = self.metadata[1]
        self.thread_ts = self.metadata[2]
        self.message_link = ''
        self.thread_link = ''
    
    def get_entry_record(self):
        return [{
            'Channel': self.channel,
            'Message Id': self.message_ts,
            'Thread Id': self.thread_ts,
            'Product': self.selected_products,
            'Problem/Question': self.problem_question.replace('\n', ''),
            'Solution/Response': self.solution_response.replace('\n', ''),
            'Message Link': self.message_link,
            'Thread Link': self.thread_link
        }]