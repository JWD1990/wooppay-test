from flask_sqlalchemy import SQLAlchemy

__all__ = (
    "Expenditure",
    "Summary",
    "db"
)


db = SQLAlchemy()


class Report(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    committee_id = db.Column(db.String(9))
    candidate_id = db.Column(db.String(9))
    candidate_name = db.Column(db.String(255))


class Expenditure(Report):
    recipient_name = db.Column(db.String(255))
    disbursement_amount = db.Column(db.DECIMAL)
    disbursement_date = db.Column(db.TIMESTAMP)
    recipient_city = db.Column(db.String(255))
    recipient_state = db.Column(db.String(255))
    recipient_zipcode = db.Column(db.String(255))
    disbursement_desc = db.Column(db.String(255))
    memo_code = db.Column(db.String(255))
    memo_text = db.Column(db.String(255))
    form_type = db.Column(db.String(255))
    file_number = db.Column(db.Integer)
    transaction_id = db.Column(db.String(255))
    election_type = db.Column(db.String(255))


class Summary(Report):
    committee_name = db.Column(db.String(255))
    committee_street1 = db.Column(db.String(255))
    committee_city = db.Column(db.String(255))
    report_type = db.Column(db.String(255))
    start_date = db.Column(db.TIMESTAMP)
    end_date = db.Column(db.TIMESTAMP)
    cashonhand_start = db.Column(db.DECIMAL)
    total_receipts = db.Column(db.DECIMAL)
    subtotal = db.Column(db.DECIMAL)
    total_disbursements = db.Column(db.DECIMAL)
    cashonhand_end = db.Column(db.DECIMAL)
