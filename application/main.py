import pandas as pd;

def load_data():
    df = pd.read_csv('data/cards.csv')
    return df

def get_random_cards():
    data = load_data()
    df_load = data.sample(n=10)
    return df_load

def print_random_cards():
    random_data = get_random_cards()
    message = ""
    for index, row in random_data.iterrows():
        message += 'id :' + str(row["cid"]) + ' | ' + 'Nom : ' + str(row["cname"])+' | '+ 'Type :' +str(row["type"]) +"\n"
    print(message)
    return message
