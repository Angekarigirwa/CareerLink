from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
import subprocess
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///careerlink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'student' or 'employer'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100))
    salary = db.Column(db.String(50))
    job_type = db.Column(db.String(50))  # 'full-time', 'part-time', 'internship'
    requirements = db.Column(db.Text)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    resume = db.Column(db.String(200))
    cover_letter = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    full_name = db.Column(db.String(100))
    education = db.Column(db.String(200))
    skills = db.Column(db.Text)
    experience = db.Column(db.Text)
    profile_picture = db.Column(db.String(200))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    jobs = Job.query.filter_by(is_active=True, job_type='full-time').limit(6).all()
    internships = Job.query.filter_by(is_active=True, job_type='internship').limit(6).all()
    return render_template('index.html', jobs=jobs, internships=internships)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, user_type=user_type)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        # Create profile for user
        profile = Profile(user_id=user.id)
        db.session.add(profile)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.user_type == 'employer':
        jobs = Job.query.filter_by(employer_id=current_user.id).all()
        return render_template('dashboard.html', jobs=jobs)
    else:
        applications = Application.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', applications=applications)

@app.route('/jobs')
def jobs():
    job_type = request.args.get('type', 'all')
    if job_type == 'internship':
        jobs = Job.query.filter_by(is_active=True, job_type='internship').all()
    else:
        jobs = Job.query.filter_by(is_active=True).all()
    return render_template('jobs.html', jobs=jobs, job_type=job_type)

@app.route('/internships')
def internships():
    internships = Job.query.filter_by(is_active=True, job_type='internship').all()
    return render_template('internships.html', internships=internships)

@app.route('/post-job', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.user_type != 'employer':
        flash('Only employers can post jobs', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        company = request.form.get('company')
        description = request.form.get('description')
        location = request.form.get('location')
        salary = request.form.get('salary')
        job_type = request.form.get('job_type')
        requirements = request.form.get('requirements')
        
        job = Job(
            title=title,
            company=company,
            description=description,
            location=location,
            salary=salary,
            job_type=job_type,
            requirements=requirements,
            employer_id=current_user.id
        )
        
        db.session.add(job)
        db.session.commit()
        
        flash('Job posted successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('post_job.html')

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@login_required
def apply(job_id):
    if current_user.user_type != 'student':
        flash('Only students can apply for positions', 'danger')
        return redirect(url_for('jobs'))
    
    job = Job.query.get_or_404(job_id)
    
    if request.method == 'POST':
        cover_letter = request.form.get('cover_letter')
        
        # Check if already applied
        existing = Application.query.filter_by(job_id=job_id, user_id=current_user.id).first()
        if existing:
            flash('You have already applied for this position', 'warning')
            return redirect(url_for('jobs'))
        
        application = Application(
            job_id=job_id,
            user_id=current_user.id,
            cover_letter=cover_letter,
            status='pending'
        )
        
        db.session.add(application)
        db.session.commit()
        
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('apply.html', job=job)

# Java Service Integration
@app.route('/api/match-jobs/<int:user_id>')
@login_required
def match_jobs(user_id):
    """Call Java service for job matching"""
    try:
        # Get user profile
        profile = Profile.query.filter_by(user_id=user_id).first()
        if not profile or not profile.skills:
            return jsonify({'error': 'No skills found'}), 400
        
        # Call Java program
        result = subprocess.run(
            ['java', '-cp', 'java_service', 'JobMatcher', profile.skills],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            matches = json.loads(result.stdout)
            return jsonify(matches)
        else:
            return jsonify({'error': 'Java service error'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoints for dynamic features
@app.route('/api/jobs/search')
def search_jobs():
    query = request.args.get('q', '')
    jobs = Job.query.filter(
        Job.title.contains(query) | 
        Job.company.contains(query) |
        Job.description.contains(query)
    ).all()
    
    return jsonify([{
        'id': job.id,
        'title': job.title,
        'company': job.company,
        'location': job.location,
        'job_type': job.job_type
    } for job in jobs])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
