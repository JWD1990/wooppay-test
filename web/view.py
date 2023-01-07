from collections import namedtuple
from sqlalchemy.inspection import inspect
from sqlalchemy import and_

from db import db, Expenditure, Summary


def get_form_data():
    committee_names = db.session.query(Summary.committee_name).distinct().all()
    candidate_names = db.session.query(Expenditure.candidate_name).distinct().all()

    return (
        [name[0] for name in committee_names],
        [name[0] for name in candidate_names]
    )


def get_report_data(request_data):
    committees_list = request_data.getlist('committees-list')
    candidates_list = request_data.getlist('candidates-list')

    Settings = namedtuple('Settings', ['model', 'target_col', 'search_values', 'period_names_cols'])
    committees_s = Settings(*(Summary, 'committee_name', committees_list, ('start_date', 'end_date')))
    candidates_s = Settings(*(Expenditure, 'candidate_name', candidates_list, tuple(['disbursement_date'] * 2)))
    cur_s = committees_s if len(committees_list) else candidates_s

    column_names = [col.name for col in inspect(cur_s.model).c]
    qry = db.session.query(cur_s.model)\
        .filter(getattr(cur_s.model, cur_s.target_col).in_(cur_s.search_values))\
        .filter(and_(
            getattr(cur_s.model, cur_s.period_names_cols[0]) >= request_data.get('start-period'),
            getattr(cur_s.model, cur_s.period_names_cols[1]) <= request_data.get('end-period')
        ))\
        .limit(500).all()

    return column_names, qry
