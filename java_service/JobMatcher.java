import java.util.*;

public class JobMatcher {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("[]");
            return;
        }
        
        String userSkills = args[0].toLowerCase();
        
        // Create a list of jobs
        List<Map<String, Object>> jobs = new ArrayList<>();
        
        // Job 1
        Map<String, Object> job1 = new HashMap<>();
        job1.put("jobId", 1);
        job1.put("title", "Software Engineer");
        job1.put("company", "Tech Corp");
        job1.put("salary", 80000);
        job1.put("skills", new String[]{"java", "python", "sql"});
        jobs.add(job1);
        
        // Job 2
        Map<String, Object> job2 = new HashMap<>();
        job2.put("jobId", 2);
        job2.put("title", "Web Developer");
        job2.put("company", "Web Studio");
        job2.put("salary", 65000);
        job2.put("skills", new String[]{"javascript", "html", "css"});
        jobs.add(job2);
        
        // Job 3
        Map<String, Object> job3 = new HashMap<>();
        job3.put("jobId", 3);
        job3.put("title", "Data Scientist");
        job3.put("company", "Data Inc");
        job3.put("salary", 95000);
        job3.put("skills", new String[]{"python", "ml", "statistics"});
        jobs.add(job3);
        
        // Job 4
        Map<String, Object> job4 = new HashMap<>();
        job4.put("jobId", 4);
        job4.put("title", "DevOps Engineer");
        job4.put("company", "Cloud Systems");
        job4.put("salary", 90000);
        job4.put("skills", new String[]{"docker", "kubernetes", "aws"});
        jobs.add(job4);
        
        // Job 5
        Map<String, Object> job5 = new HashMap<>();
        job5.put("jobId", 5);
        job5.put("title", "Frontend Developer");
        job5.put("company", "Creative Agency");
        job5.put("salary", 70000);
        job5.put("skills", new String[]{"react", "vue", "angular"});
        jobs.add(job5);
        
        // Job 6 - Full Stack
        Map<String, Object> job6 = new HashMap<>();
        job6.put("jobId", 6);
        job6.put("title", "Full Stack Developer");
        job6.put("company", "Startup Inc");
        job6.put("salary", 85000);
        job6.put("skills", new String[]{"java", "javascript", "react", "python", "sql"});
        jobs.add(job6);
        
        // Job 7 - Backend Developer
        Map<String, Object> job7 = new HashMap<>();
        job7.put("jobId", 7);
        job7.put("title", "Backend Developer");
        job7.put("company", "API First");
        job7.put("salary", 82000);
        job7.put("skills", new String[]{"java", "python", "sql", "aws"});
        jobs.add(job7);
        
        // Calculate matches
        List<Map<String, Object>> matches = new ArrayList<>();
        String[] userSkillArray = userSkills.split(",");
        
        for (Map<String, Object> job : jobs) {
            String[] jobSkills = (String[]) job.get("skills");
            int matchCount = 0;
            
            for (String userSkill : userSkillArray) {
                userSkill = userSkill.trim();
                for (String jobSkill : jobSkills) {
                    if (jobSkill.contains(userSkill)) {
                        matchCount++;
                        break;
                    }
                }
            }
            
            double matchScore = (matchCount * 100.0) / jobSkills.length;
            int roundedScore = (int) Math.round(matchScore);
            
            Map<String, Object> match = new HashMap<>();
            match.put("jobId", job.get("jobId"));
            match.put("title", job.get("title"));
            match.put("company", job.get("company"));
            match.put("matchScore", roundedScore);
            match.put("salary", job.get("salary"));
            
            matches.add(match);
        }
        
        // Sort by match score
        matches.sort((a, b) -> {
            int scoreA = (int) a.get("matchScore");
            int scoreB = (int) b.get("matchScore");
            return Integer.compare(scoreB, scoreA);
        });
        
        // Build JSON
        StringBuilder json = new StringBuilder("[");
        for (int i = 0; i < matches.size(); i++) {
            Map<String, Object> m = matches.get(i);
            json.append("{");
            json.append("\"jobId\":").append(m.get("jobId")).append(",");
            json.append("\"title\":\"").append(m.get("title")).append("\",");
            json.append("\"company\":\"").append(m.get("company")).append("\",");
            json.append("\"matchScore\":").append(m.get("matchScore")).append(",");
            json.append("\"salary\":").append(m.get("salary"));
            json.append("}");
            if (i < matches.size() - 1) {
                json.append(",");
            }
        }
        json.append("]");
        
        System.out.println(json.toString());
    }
}
