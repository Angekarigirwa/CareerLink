from app import app, db, User, Job, Profile
from werkzeug.security import generate_password_hash
from datetime import datetime

def add_sample_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create sample employers
        employers = [
            User(username="techcorp", email="hr@techcorp.com", user_type="employer"),
            User(username="webstudio", email="jobs@webstudio.com", user_type="employer"),
            User(username="datainc", email="careers@datainc.com", user_type="employer"),
        ]
        
        for employer in employers:
            employer.set_password("password123")
            db.session.add(employer)
        
        db.session.commit()
        
        # Create sample students
        students = [
            User(username="john_doe", email="john@student.com", user_type="student"),
            User(username="jane_smith", email="jane@student.com", user_type="student"),
        ]
        
        for student in students:
            student.set_password("password123")
            db.session.add(student)
        
        db.session.commit()
        
        # Create sample jobs
        jobs = [
            Job(
                title="Senior Software Engineer",
                company="TechCorp",
                description="Looking for an experienced software engineer to join our team. You'll be working on cutting-edge technology and building scalable applications.",
                location="San Francisco, CA",
                salary="$120,000 - $150,000",
                job_type="full-time",
                requirements="5+ years of experience with Python, Java, or similar. Experience with cloud platforms is a plus.",
                employer_id=employers[0].id
            ),
            Job(
                title="Frontend Developer",
                company="WebStudio",
                description="Join our creative team to build beautiful and responsive web applications. Work with React and modern frontend technologies.",
                location="New York, NY",
                salary="$90,000 - $110,000",
                job_type="full-time",
                requirements="3+ years of experience with React, HTML, CSS, JavaScript.",
                employer_id=employers[1].id
            ),
            Job(
                title="Data Scientist Intern",
                company="DataInc",
                description="Exciting internship opportunity for students passionate about data science and machine learning.",
                location="Remote",
                salary="$25/hour",
                job_type="internship",
                requirements="Currently enrolled in Computer Science or related field. Knowledge of Python and basic ML concepts.",
                employer_id=employers[2].id
            ),
            Job(
                title="Full Stack Developer",
                company="TechCorp",
                description="Build end-to-end web applications using modern frameworks. Work with both frontend and backend technologies.",
                location="Austin, TX",
                salary="$100,000 - $130,000",
                job_type="full-time",
                requirements="Experience with React, Node.js, and databases. Strong problem-solving skills.",
                employer_id=employers[0].id
            ),
            Job(
                title="Marketing Intern",
                company="WebStudio",
                description="Learn digital marketing strategies and help grow our brand presence.",
                location="New York, NY",
                salary="$20/hour",
                job_type="internship",
                requirements="Strong communication skills, familiarity with social media platforms.",
                employer_id=employers[1].id
            ),
            Job(
                title="DevOps Engineer",
                company="DataInc",
                description="Manage cloud infrastructure and CI/CD pipelines. Work with AWS and Kubernetes.",
                location="Seattle, WA",
                salary="$110,000 - $140,000",
                job_type="full-time",
                requirements="Experience with AWS, Docker, Kubernetes, and CI/CD tools.",
                employer_id=employers[2].id
            ),
        ]
        
        for job in jobs:
            db.session.add(job)
        
        db.session.commit()
        
        # Create profiles for students
        student_profiles = [
            Profile(
                user_id=students[0].id,
                full_name="John Doe",
                education="BS in Computer Science, Stanford University",
                skills="Python, Java, JavaScript, React, SQL",
                experience="Summer intern at Google, Teaching Assistant at University"
            ),
            Profile(
                user_id=students[1].id,
                full_name="Jane Smith",
                education="MS in Data Science, MIT",
                skills="Python, Machine Learning, TensorFlow, R, SQL",
                experience="Data Science intern at Amazon, Research Assistant"
            ),
        ]
        
        for profile in student_profiles:
            db.session.add(profile)
        
        db.session.commit()
        
        print("✅ Sample data added successfully!")
        print("\n📝 Test Accounts:")
        print("Employers (password: password123):")
        for employer in employers:
            print(f"  - Username: {employer.username}")
        print("\nStudents (password: password123):")
        for student in students:
            print(f"  - Username: {student.username}")
        print("\n🎯 Jobs and internships have been added!")
        print("\n🌐 Visit http://127.0.0.1:5000 to see your CareerLink website!")

if __name__ == "__main__":
    add_sample_data()