from db import db, Expenditure, Summary


def get_form_data():
    committee_names = db.session.query(Summary.committee_name).distinct().all()
    candidate_names = db.session.query(Expenditure.candidate_name).distinct().all()

    return (
        [name[0] for name in committee_names],
        [name[0] for name in candidate_names]
    )
