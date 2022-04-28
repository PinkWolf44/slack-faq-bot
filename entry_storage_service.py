import pandas as pd

def store_entry(data):
    df = pd.read_csv('data.csv', sep='|')
    row = pd.DataFrame(data.get_entry_record())
    df = pd.concat([df, row])
    df.to_csv('data.csv', encoding='utf-8', sep='|', index=False)
