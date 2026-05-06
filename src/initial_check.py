import pandas as pd

# Load a sample of the metadata to explore
metadata_path = '/home/abishek/Documents/DS/MiniProject_DS_AIML-B_2026_JobTrend/dataset/raw_data/linkedin_job_postings.csv'
skills_path = '/home/abishek/Documents/DS/MiniProject_DS_AIML-B_2026_JobTrend/dataset/raw_data/job_skills.csv'

print("Loading metadata sample...")
df_meta = pd.read_csv(metadata_path, nrows=10000)

print("Job Levels Distribution:")
print(df_meta['job_level'].value_counts())

print("\nJob Types Distribution:")
print(df_meta['job_type'].value_counts())

# Check for Data Science / Tech roles
tech_keywords = ['Data Scientist', 'Data Analyst', 'Machine Learning', 'AI', 'Software Engineer', 'Developer', 'Python']
tech_jobs = df_meta[df_meta['job_title'].str.contains('|'.join(tech_keywords), case=False, na=False)]

print(f"\nFound {len(tech_jobs)} tech-related jobs in the first 10,000 rows.")
print("Sample tech job titles:")
print(tech_jobs['job_title'].head(10).tolist())
