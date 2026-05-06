import pandas as pd
import os
import re

# Paths
raw_path = '../dataset/raw_data/'
processed_path = '../dataset/processed_data/'
metadata_file = os.path.join(raw_path, 'linkedin_job_postings.csv')
skills_file = os.path.join(raw_path, 'job_skills.csv')

def clean_skill_string(skill_str):
    """
    Cleans and standardizes skill strings.
    """
    if pd.isna(skill_str):
        return ""
    # Remove special characters except commas for splitting
    clean = re.sub(r'[^\w\s,]', '', str(skill_str))
    # Standardize to lowercase and strip whitespace
    return ", ".join(sorted(list(set([s.strip().lower() for s in clean.split(',') if s.strip()]))))

def preprocess_data(sample_size=100000):
    """
    Main preprocessing pipeline.
    """
    print(f"Loading {sample_size} rows for preprocessing...")
    
    # Load metadata and skills
    df_meta = pd.read_csv(metadata_file, nrows=sample_size)
    df_skills = pd.read_csv(skills_file, nrows=sample_size)
    
    # 1. Merge datasets on job_link
    print("Merging datasets...")
    df = pd.merge(df_meta, df_skills, on='job_link', how='inner')
    
    # 2. Basic Cleaning
    print("Handling missing values and duplicates...")
    df.drop_duplicates(subset=['job_link'], inplace=True)
    df.dropna(subset=['job_title', 'job_skills'], inplace=True)
    
    # 3. Filter for Tech/Data roles (Optional but recommended for 'JobTrend')
    tech_keywords = ['data', 'engineer', 'developer', 'scientist', 'analyst', 'ai', 'machine learning', 'python', 'sql']
    pattern = '|'.join(tech_keywords)
    df_tech = df[df['job_title'].str.contains(pattern, case=False, na=False)].copy()
    print(f"Filtered to {len(df_tech)} tech-related roles.")
    
    # 4. Clean Skills
    print("Cleaning skills strings...")
    df_tech['cleaned_skills'] = df_tech['job_skills'].apply(clean_skill_string)
    
    # 5. Save processed data
    output_file = os.path.join(processed_path, 'cleaned_job_data.csv')
    df_tech.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to: {output_file}")
    
    return df_tech

if __name__ == "__main__":
    if not os.path.exists(processed_path):
        os.makedirs(processed_path)
    preprocess_data()
