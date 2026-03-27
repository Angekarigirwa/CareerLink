# CareerLink - Job & Internship Portal

## 📌 Overview
CareerLink is a comprehensive job and internship portal connecting employers 
with students, specifically focusing on opportunities in Rwanda. The platform 
helps students find internships and entry-level jobs while enabling employers 
to post opportunities and manage applications efficiently.

## 🎯 Problem Statement
Many university students struggle to find internships and entry-level jobs due 
to:
- Lack of information about available opportunities
- Limited professional networks
- High competition in the job market
- Existing platforms requiring experience that students don't have

CareerLink bridges this gap by providing a student-focused platform that 
connects students with relevant opportunities based on their skills and 
interests.

## ✨ Features

### For Students
- Create and manage professional profiles with skills, education, and 
experience
- Browse and search for jobs and internships
- Apply to positions with resume upload
- Track application status (pending, reviewed, accepted, rejected)
- Receive personalized job recommendations based on skills
- Get email notifications for application updates

### For Employers
- Create company profiles with descriptions and websites
- Post job and internship opportunities with categories
- Review and manage applications
- Update application status with notes
- Receive notifications for new applications

### For Administrators
- Manage users (delete, promote to admin)
- Manage job categories
- View system statistics

### Additional Features
- **Mobile Responsive**: Works perfectly on all devices (phones, tablets, 
desktops)
- **Rwandan Jobs**: Dedicated page for opportunities from Rwandan companies 
(Andela, KCB, MTN, RwandAir, Zipline, etc.)
- **Job Recommendations**: Java-powered matching algorithm
- **Email Notifications**: Automated emails for verification and application 
updates
- **Resume Upload**: Support for PDF, DOC, DOCX files
- **Category Filters**: Browse by Technology, Marketing, Sales, Design, 
Finance, etc.

## 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| **Backend** | Flask (Python 3.11) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Database** | SQLite with SQLAlchemy ORM |
| **Authentication** | Flask-Login with password hashing |
| **Job Matching** | Java 8+ custom algorithm |
| **Email** | Flask-Mail |
| **Deployment** | Render.com |

## 📋 Prerequisites

- Python 3.11 or higher
- Java 8 or higher (for job recommendations)
- pip (Python package manager)
- Git

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Angekarigirwa/CareerLink.git
cd CareerLink

