from sqlalchemy import create_engine
from config.db_config import DB_CONFIG
from urllib.parse import quote_plus

def load_data(df):

    password = quote_plus(DB_CONFIG['password'])
    connection_string = f"mysql+pymysql://{DB_CONFIG['user']}:{password}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    engine = create_engine(connection_string)
    df.to_sql("hr_analytics", con=engine, if_exists="replace", index=False)
    print("Data loaded successfully!")