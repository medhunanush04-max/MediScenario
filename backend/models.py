from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='student', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }

class PatientCase(db.Model):
    __tablename__ = 'patient_cases'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    patient_history = db.Column(db.Text)
    diagnosis = db.Column(db.String(255))
    difficulty = db.Column(db.String(50), default='medium')
    category = db.Column(db.String(100))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'difficulty': self.difficulty,
            'category': self.category
        }

class Drug(db.Model):
    __tablename__ = 'drugs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    generic_name = db.Column(db.String(255))
    indication = db.Column(db.Text)
    dosage = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'generic_name': self.generic_name,
            'indication': self.indication,
            'dosage': self.dosage
        }

class DrugInteraction(db.Model):
    __tablename__ = 'drug_interactions'
    
    id = db.Column(db.Integer, primary_key=True)
    drug1_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    drug2_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    severity = db.Column(db.String(50))
    description = db.Column(db.Text)
    recommendation = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'drug1_id': self.drug1_id,
            'drug2_id': self.drug2_id,
            'severity': self.severity,
            'description': self.description,
            'recommendation': self.recommendation
        }

class UserProgress(db.Model):
    __tablename__ = 'user_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('patient_cases.id'), nullable=False)
    score = db.Column(db.Integer)
    status = db.Column(db.String(50), default='in_progress')
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'case_id': self.case_id,
            'score': self.score,
            'status': self.status,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }
