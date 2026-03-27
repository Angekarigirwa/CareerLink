import java.util.*;
import java.io.*;

public class JobMatcher {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Please provide user skills");
            System.exit(1);
        }
        
        String userSkills = args[0];
        
        // Sample job database with required skills
        List<Job> jobs = new ArrayList<>();
        jobs.add(new Job(1, "Software Engineer", "Tech Corp", 
            Arrays.asList("Java", "Python", "SQL"), 80000));
        jobs.add(new Job(2, "Web Developer", "Web Solutions", 
            Arrays.asList("JavaScript", "HTML", "CSS"), 65000));
        jobs.add(new Job(3, "Data Scientist", "Data Analytics Inc", 
            Arrays.asList("Python", "Machine Learning", "Statistics"), 95000));
        jobs.add(new Job(4, "DevOps Engineer", "Cloud Systems", 
            Arrays.asList("Docker", "Kubernetes", "AWS"), 90000));
        jobs.add(new Job(5, "Frontend Developer", "Creative Agency", 
            Arrays.asList("React", "Vue.js", "Angular"), 70000));
        
        // Calculate match scores
        List<Map<String, Object>> matches = new ArrayList<>();
        String[] userSkillArray = userSkills.toLowerCase().split(",");
        
        for (Job job : jobs) {
            int matchCount = 0;
            for (String skill : job.requiredSkills) {
                for (String userSkill : userSkillArray) {
                    if (skill.toLowerCase().contains(userSkill.trim())) {
                        matchCount++;
                        break;
                    }
                }
            }
            
            double matchScore = (double) matchCount / job.requiredSkills.size() * 100;
            
            Map<String, Object> match = new HashMap<>();
            match.put("jobId", job.id);
            match.put("title", job.title);
            match.put("company", job.company);
            match.put("matchScore", Math.round(matchScore));
            match.put("salary", job.salary);
            
            matches.add(match);
        }
        
        // Sort by match score
        matches.sort((a, b) -> Double.compare(
            (Double) b.get("matchScore"), 
            (Double) a.get("matchScore")
        ));
        
        // Output JSON
        String jsonOutput = "[";
        for (int i = 0; i < Math.min(5, matches.size()); i++) {
            Map<String, Object> match = matches.get(i);
            jsonOutput += "{";
            jsonOutput += "\"jobId\":" + match.get("jobId") + ",";
            jsonOutput += "\"title\":\"" + match.get("title") + "\",";
            jsonOutput += "\"company\":\"" + match.get("company") + "\",";
            jsonOutput += "\"matchScore\":" + match.get("matchScore") + ",";
            jsonOutput += "\"salary\":" + match.get("salary");
            jsonOutput += "}";
            if (i < matches.size() - 1) jsonOutput += ",";
        }
        jsonOutput += "]";
        
        System.out.println(jsonOutput);
    }
    
    static class Job {
        int id;
        String title;
        String company;
        List<String> requiredSkills;
        int salary;
        
        Job(int id, String title, String company, List<String> requiredSkills, int salary) {
            this.id = id;
            this.title = title;
            this.company = company;
            this.requiredSkills = requiredSkills;
            this.salary = salary;
        }
    }
}
