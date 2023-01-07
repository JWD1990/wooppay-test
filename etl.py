from sqlalchemy import create_engine
import pandas as pd
import config.base as conf

db = create_engine(conf.db_dsn)

# загрузка expenditures данных в базу
df = pd.read_csv('etl/expenditures.csv')
df = df.drop(df.columns[0], axis=1)
df['disbursement_date'] = pd.to_datetime(df['disbursement_date'])
df.to_sql(name='expenditure', con=db, if_exists="append", index=False)

# загрузка summary данных в базу
cols = [
    'committee_id',
    'committee_name',
    'committee_street1',
    'committee_city',
    'candidate_id',
    'candidate_name',
    'report_type',
    'start_date',
    'end_date',
    'cashonhand_start',
    'total_receipts',
    'subtotal',
    'total_disbursements',
    'cashonhand_end'
]

df = pd.read_csv('etl/summary.csv', usecols=cols)
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])
df.to_sql(name='summary', con=db, if_exists="append", index=False)
