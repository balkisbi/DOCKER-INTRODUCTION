import os
import pandas as pd
from sqlalchemy import create_engine

# Konfigurasi koneksi database
source_db_config = {
    'host': 'source_host',
    'port': 'source_port',
    'database': 'source_db',
    'user': 'source_user',
    'password': 'source_password'
}

destination_db_config = {
    'host': 'destination_host',
    'port': 'destination_port',
    'database': 'destination_db',
    'user': 'destination_user',
    'password': 'destination_password'
}


def etl():
    data = pd.read_csv('test.csv')
    
    source_engine = create_engine(f"postgresql://{source_db_config['user']}:{source_db_config['password']}@{source_db_config['host']}:{source_db_config['port']}/{source_db_config['database']}")
    destination_engine = create_engine(f"postgresql://{destination_db_config['user']}:{destination_db_config['password']}@{destination_db_config['host']}:{destination_db_config['port']}/{destination_db_config['database']}")


    data.to_sql('titanic', destination_engine, index=False, if_exists='replace')

if __name__ == "__main__":
    etl()
