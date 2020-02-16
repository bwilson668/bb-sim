import random
import time
import pandas as pd
from sqlalchemy import create_engine


def random_base():
    return random.random()


def insert_transaction():
    data = {'booking': [random_base()]}
    df = pd.DataFrame(data)
    df.to_sql('transactions', con = )

def generate_data(func, t=60):
    for t in range(t):

        print(func())
        time.sleep(1)
