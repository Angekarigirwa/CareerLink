from app import app, db, User, Job, Profile, Category
from werkzeug.security import generate_password_hash

def add_rwandan_jobs():
    with app.app_context():
        # Create Rwandan categories if they don't exist
        categories_data = [
            ('Technology', 'Software development, IT, and tech roles in Rwanda'),
            ('Fintech', 'Financial technology and mobile money services'),
            ('Tourism & Hospitality', 'Tourism, hotels, and hospitality services'),
            ('Agriculture', 'Farming, agribusiness, and food production'),
            ('Healthcare', 'Medical services, hospitals, and healthcare'),
            ('Education', 'Teaching, training, and educational services'),
            ('Construction', 'Building, infrastructure, and real estate'),
            ('Telecommunications', 'Mobile networks, internet services'),
            ('Manufacturing', 'Production and manufacturing industries'),
            ('Logistics', 'Transportation, delivery, and supply chain')
        ]
        
        for name, desc in categories_data:
            if not Category.query.filter_by(name=name).first():
                category = Category(name=name, description=desc)
                db.session.add(category)
        db.session.commit()
        
        # Get category IDs
        tech_cat = Category.query.filter_by(name='Technology').first()
        fintech_cat = Category.query.filter_by(name='Fintech').first()
        tourism_cat = Category.query.filter_by(name='Tourism & Hospitality').first()
        agri_cat = Category.query.filter_by(name='Agriculture').first()
        healthcare_cat = Category.query.filter_by(name='Healthcare').first()
        education_cat = Category.query.filter_by(name='Education').first()
        telecom_cat = Category.query.filter_by(name='Telecommunications').first()
        
        # Create Rwandan employers
        employers_data = [
            {'username': 'andela_rwanda', 'email': 'careers@andela.com', 'company': 'Andela Rwanda'},
            {'username': 'kcb_rwanda', 'email': 'hr@kcb.rw', 'company': 'KCB Bank Rwanda'},
            {'username': 'marriott_kigali', 'email': 'careers@marriott.com', 'company': 'Marriott Hotel Kigali'},
            {'username': 'mara_phones', 'email': 'hr@maraphones.com', 'company': 'Mara Phones Rwanda'},
            {'username': 'zipline_rwanda', 'email': 'careers@zipline.com', 'company': 'Zipline Rwanda'},
            {'username': 'rwanda_energy', 'email': 'hr@reg.rw', 'company': 'Rwanda Energy Group (REG)'},
            {'username': 'mtn_rwanda', 'email': 'careers@mtn.rw', 'company': 'MTN Rwanda'},
            {'username': 'rwandair', 'email': 'careers@rwandair.com', 'company': 'RwandAir'},
            {'username': 'bank_of_kigali', 'email': 'hr@bk.rw', 'company': 'Bank of Kigali'},
            {'username': 'radisson_blu', 'email': 'careers@radisson.com', 'company': 'Radisson Blu Hotel Kigali'}
        ]
        
        rwandan_employers = []
        for emp_data in employers_data:
            employer = User.query.filter_by(username=emp_data['username']).first()
            if not employer:
                employer = User(
                    username=emp_data['username'],
                    email=emp_data['email'],
                    user_type='employer',
                    is_verified=True
                )
                employer.set_password('rwanda2026')
                db.session.add(employer)
                db.session.commit()
                
                # Create company profile
                profile = Profile.query.filter_by(user_id=employer.id).first()
                if profile:
                    profile.company_name = emp_data['company']
                    profile.location = 'Kigali, Rwanda'
                    db.session.commit()
            
            rwandan_employers.append(employer)
        
        # Create Rwandan job opportunities
        rwandan_jobs = [
            {
                'title': 'Software Engineer',
                'company': 'Andela Rwanda',
                'description': 'Join Andela\'s engineering team in Kigali to build world-class software solutions for global clients. Work with modern technologies and collaborate with international teams.',
                'location': 'Kigali, Rwanda (Hybrid)',
                'salary': 'RWF 1,500,000 - 2,500,000/month',
                'job_type': 'full-time',
                'category_id': tech_cat.id if tech_cat else None,
                'requirements': '• 3+ years of experience in software development\n• Proficiency in Python, JavaScript, or Java\n• Experience with cloud platforms (AWS, GCP)\n• Strong problem-solving skills\n• Bachelor\'s degree in Computer Science or related field',
                'employer': 'andela_rwanda'
            },
            {
                'title': 'Mobile Money Developer',
                'company': 'KCB Bank Rwanda',
                'description': 'Develop and maintain mobile banking applications and payment solutions. Work on cutting-edge fintech products serving millions of customers across East Africa.',
                'location': 'Kigali, Rwanda',
                'salary': 'RWF 1,200,000 - 2,000,000/month',
                'job_type': 'full-time',
                'category_id': fintech_cat.id if fintech_cat else None,
                'requirements': '• Experience with mobile development (Android/iOS)\n• Knowledge of payment systems and APIs\n• Understanding of financial security standards\n• 2+ years of experience in fintech',
                'employer': 'kcb_rwanda'
            },
            {
                'title': 'Frontend Developer (React)',
                'company': 'Mara Phones Rwanda',
                'description': 'Build responsive web applications for Mara Phones\' e-commerce platform and customer portals. Create beautiful user interfaces for African consumers.',
                'location': 'Kigali Special Economic Zone, Rwanda',
                'salary': 'RWF 800,000 - 1,500,000/month',
                'job_type': 'full-time',
                'category_id': tech_cat.id if tech_cat else None,
                'requirements': '• 2+ years of React.js experience\n• Strong HTML, CSS, JavaScript skills\n• Experience with REST APIs\n• Portfolio of previous work',
                'employer': 'mara_phones'
            },
            {
                'title': 'Drone Operations Intern',
                'company': 'Zipline Rwanda',
                'description': 'Join Zipline\'s drone delivery team in Muhanga. Learn about drone operations, logistics, and medical supply delivery systems.',
                'location': 'Muhanga, Rwanda',
                'salary': 'RWF 150,000 - 250,000/month',
                'job_type': 'internship',
                'category_id': tech_cat.id if tech_cat else None,
                'requirements': '• Recent graduate in Engineering, IT, or related field\n• Interest in drone technology and logistics\n• Strong analytical skills\n• Available for 6-month internship',
                'employer': 'zipline_rwanda'
            },
            {
                'title': 'Hotel Management Intern',
                'company': 'Marriott Hotel Kigali',
                'description': 'Learn hotel operations, customer service, and hospitality management at one of Kigali\'s premier hotels.',
                'location': 'Kigali, Rwanda',
                'salary': 'RWF 100,000 - 150,000/month',
                'job_type': 'internship',
                'category_id': tourism_cat.id if tourism_cat else None,
                'requirements': '• Studying Hospitality Management or related field\n• Excellent communication skills\n• Customer service oriented\n• Fluent in English and Kinyarwanda',
                'employer': 'marriott_kigali'
            },
            {
                'title': 'Agricultural Technology Specialist',
                'company': 'Rwanda Energy Group (REG)',
                'description': 'Work on agricultural technology projects combining renewable energy with modern farming techniques.',
                'location': 'Kigali & Various Districts, Rwanda',
                'salary': 'RWF 700,000 - 1,200,000/month',
                'job_type': 'full-time',
                'category_id': agri_cat.id if agri_cat else None,
                'requirements': '• Degree in Agriculture, Engineering, or related field\n• Knowledge of irrigation systems\n• Experience with renewable energy projects\n• Willing to travel to rural areas',
                'employer': 'rwanda_energy'
            },
            {
                'title': 'Network Engineer',
                'company': 'MTN Rwanda',
                'description': 'Manage and optimize MTN\'s mobile network infrastructure across Rwanda. Ensure reliable connectivity for millions of users.',
                'location': 'Kigali, Rwanda',
                'salary': 'RWF 1,200,000 - 2,000,000/month',
                'job_type': 'full-time',
                'category_id': telecom_cat.id if telecom_cat else None,
                'requirements': '• 3+ years of network engineering experience\n• CCNA/CCNP certification\n• Experience with 4G/5G technologies\n• Strong troubleshooting skills',
                'employer': 'mtn_rwanda'
            },
            {
                'title': 'Customer Service Representative',
                'company': 'RwandAir',
                'description': 'Provide exceptional customer service to RwandAir passengers. Handle bookings, inquiries, and assist with travel needs.',
                'location': 'Kigali International Airport, Rwanda',
                'salary': 'RWF 400,000 - 600,000/month',
                'job_type': 'full-time',
                'category_id': tourism_cat.id if tourism_cat else None,
                'requirements': '• Excellent communication skills\n• Fluency in English, French, and Kinyarwanda\n• Customer service experience\n• Flexible with shift work',
                'employer': 'rwandair'
            },
            {
                'title': 'Cybersecurity Analyst',
                'company': 'Bank of Kigali',
                'description': 'Protect Bank of Kigali\'s digital assets and customer data. Monitor security threats and implement security measures.',
                'location': 'Kigali, Rwanda',
                'salary': 'RWF 1,500,000 - 2,200,000/month',
                'job_type': 'full-time',
                'category_id': fintech_cat.id if fintech_cat else None,
                'requirements': '• Cybersecurity certification (CISSP, CEH, or similar)\n• 2+ years security experience\n• Knowledge of banking security standards\n• Bachelor\'s in Computer Science or related field',
                'employer': 'bank_of_kigali'
            },
            {
                'title': 'Event Management Intern',
                'company': 'Radisson Blu Hotel Kigali',
                'description': 'Assist in planning and executing corporate events, weddings, and conferences at Radisson Blu.',
                'location': 'Kigali, Rwanda',
                'salary': 'RWF 100,000 - 150,000/month',
                'job_type': 'internship',
                'category_id': tourism_cat.id if tourism_cat else None,
                'requirements': '• Studying Event Management or Hospitality\n• Strong organizational skills\n• Creative and detail-oriented\n• Available for 3-6 months',
                'employer': 'radisson_blu'
            },
            {
                'title': 'Full Stack Developer',
                'company': 'Andela Rwanda',
                'description': 'Build end-to-end web applications for Andela\'s global clients. Work with React, Node.js, and cloud technologies.',
                'location': 'Kigali, Rwanda (Remote options)',
                'salary': 'RWF 1,800,000 - 2,800,000/month',
                'job_type': 'full-time',
                'category_id': tech_cat.id if tech_cat else None,
                'requirements': '• 4+ years full-stack development\n• Expertise in React and Node.js\n• Database design skills\n• Experience with agile methodologies',
                'employer': 'andela_rwanda'
            },
            {
                'title': 'Medical Sales Representative',
                'company': 'Zipline Rwanda',
                'description': 'Promote Zipline\'s medical delivery services to hospitals and health centers across Rwanda.',
                'location': 'Kigali, Rwanda',
                'salary': 'RWF 500,000 - 800,000/month + commission',
                'job_type': 'full-time',
                'category_id': healthcare_cat.id if healthcare_cat else None,
                'requirements': '• Sales experience in healthcare sector\n• Knowledge of Rwandan healthcare system\n• Strong communication skills\n• Willing to travel',
                'employer': 'zipline_rwanda'
            }
        ]
        
        # Add jobs to database
        jobs_added = 0
        for job_data in rwandan_jobs:
            # Find employer
            employer = User.query.filter_by(username=job_data['employer']).first()
            if employer:
                # Check if job already exists
                existing = Job.query.filter_by(
                    title=job_data['title'],
                    company=job_data['company'],
                    employer_id=employer.id
                ).first()
                
                if not existing:
                    job = Job(
                        title=job_data['title'],
                        company=job_data['company'],
                        description=job_data['description'],
                        location=job_data['location'],
                        salary=job_data['salary'],
                        job_type=job_data['job_type'],
                        category_id=job_data['category_id'],
                        requirements=job_data['requirements'],
                        employer_id=employer.id,
                        is_active=True
                    )
                    db.session.add(job)
                    jobs_added += 1
        
        db.session.commit()
        
        print(f"\n✅ Added {jobs_added} Rwandan job opportunities!")
        print("\n📝 Rwandan Employers:")
        for emp in rwandan_employers:
            profile = Profile.query.filter_by(user_id=emp.id).first()
            company_name = profile.company_name if profile else emp.username
            print(f"  - {company_name}")
        
        print("\n🎯 Categories added:")
        categories = Category.query.all()
        for cat in categories:
            print(f"  - {cat.name} ({cat.description})")
        
        print("\n🔑 Login credentials for employers:")
        print("  Username: any employer username (andela_rwanda, kcb_rwanda, etc.)")
        print("  Password: rwanda2026")
        
        print("\n💼 Available jobs include:")
        print("  • Software Engineer - Andela Rwanda")
        print("  • Mobile Money Developer - KCB Bank")
        print("  • Frontend Developer - Mara Phones")
        print("  • Drone Operations Intern - Zipline")
        print("  • Hotel Management Intern - Marriott Hotel")
        print("  • Agricultural Technology Specialist - REG")
        print("  • Network Engineer - MTN Rwanda")
        print("  • Cybersecurity Analyst - Bank of Kigali")
        print("  • And many more...")
        
        print("\n🌍 Visit http://127.0.0.1:5000/jobs to see all opportunities!")

if __name__ == "__main__":
    add_rwandan_jobs()
