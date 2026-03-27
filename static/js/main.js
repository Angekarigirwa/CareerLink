// Search functionality
function searchJobs() {
    const query = document.getElementById('searchInput').value;
    if (query.trim()) {
        fetch(`/api/jobs/search?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                displaySearchResults(data);
            })
            .catch(error => console.error('Error:', error));
    }
}

function displaySearchResults(jobs) {
    const resultsDiv = document.createElement('div');
    resultsDiv.className = 'search-results mt-3';
    resultsDiv.innerHTML = '<h4>Search Results:</h4>';
    
    if (jobs.length === 0) {
        resultsDiv.innerHTML += '<p>No jobs found</p>';
    } else {
        jobs.forEach(job => {
            resultsDiv.innerHTML += `
                <div class="job-card mb-2 p-3 border rounded">
                    <h6>${job.title}</h6>
                    <p class="text-muted">${job.company} - ${job.location}</p>
                    <span class="badge bg-primary">${job.job_type}</span>
                    <a href="/apply/${job.id}" class="btn btn-sm btn-outline-primary float-end">Apply</a>
                </div>
            `;
        });
    }
    
    // Remove existing results and add new ones
    const existingResults = document.querySelector('.search-results');
    if (existingResults) existingResults.remove();
    document.querySelector('.hero-section .container').appendChild(resultsDiv);
}

// Auto-save profile data
function autoSaveProfile() {
    const formData = new FormData(document.getElementById('profileForm'));
    const data = Object.fromEntries(formData);
    
    fetch('/api/update-profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        showNotification('Profile saved!', 'success');
    })
    .catch(error => console.error('Error:', error));
}

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 end-0 m-3`;
    notification.style.zIndex = '9999';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Job matching with Java backend
function getJobMatches() {
    fetch(`/api/match-jobs/${currentUserId}`)
        .then(response => response.json())
        .then(matches => {
            const matchDiv = document.getElementById('jobMatches');
            if (matchDiv) {
                matchDiv.innerHTML = '<h5>Recommended Jobs</h5>';
                matches.forEach(match => {
                    matchDiv.innerHTML += `
                        <div class="job-card mb-2 p-3 border rounded">
                            <div class="d-flex justify-content-between">
                                <h6>${match.title}</h6>
                                <span class="badge bg-success">${match.matchScore}% Match</span>
                            </div>
                            <p class="text-muted">${match.company}</p>
                            <small>Salary: $${match.salary}/year</small>
                        </div>
                    `;
                });
            }
        });
}

// Real-time form validation
document.addEventListener('DOMContentLoaded', function() {
    // Add animation to cards
    const cards = document.querySelectorAll('.job-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('animate-fade-in');
    });
    
    // Add event listeners for forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Please fill all required fields', 'danger');
            }
        });
    });
});

// Debounce function for search
function debounce(func, delay) {
    let timeout;
    return function() {
        const context = this;
        const args = arguments;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), delay);
    };
}

// Add debounced search
if (document.getElementById('searchInput')) {
    const searchInput = document.getElementById('searchInput');
    const debouncedSearch = debounce(searchJobs, 500);
    searchInput.addEventListener('input', debouncedSearch);
}
