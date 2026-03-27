from app import app, db, Job, User

with app.app_context():
    # Check if database has data
    users = User.query.all()
    jobs = Job.query.all()
    
    print(f"Number of users in database: {len(users)}")
    print(f"Number of jobs in database: {len(jobs)}")
    
    if users:
        print("\nUsers:")
        for user in users:
            print(f"  - {user.username} ({user.user_type})")
    
    if jobs:
        print("\nJobs:")
        for job in jobs:
            print(f"  - {job.title} at {job.company} ({job.job_type})")
    else:
        print("\n⚠️ No jobs found! Run add_sample_data.py first.")