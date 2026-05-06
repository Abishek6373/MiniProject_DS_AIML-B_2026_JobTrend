import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os

# Paths
processed_path = '../dataset/processed_data/'
output_path = '../outputs/graphs/'
cleaned_data_file = os.path.join(processed_path, 'cleaned_job_data.csv')

def load_processed_data():
    return pd.read_csv(cleaned_data_file)

def plot_top_skills(df, top_n=15):
    """
    Identifies and plots the most frequent skills.
    """
    all_skills = []
    for skills in df['cleaned_skills'].dropna():
        all_skills.extend([s.strip() for s in skills.split(',')])
    
    skill_counts = Counter(all_skills).most_common(top_n)
    skill_df = pd.DataFrame(skill_counts, columns=['Skill', 'Count'])
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=skill_df, x='Count', y='Skill', hue='Skill', palette='viridis', legend=False)
    plt.title(f'Top {top_n} Trending Skills in 2024')
    plt.xlabel('Frequency in Job Postings')
    plt.ylabel('Skill Name')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'top_skills.png'))
    plt.close()
    print("Saved top_skills.png")

def plot_job_levels(df):
    """
    Plots the distribution of job levels.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, y='job_level', hue='job_level', order=df['job_level'].value_counts().index, palette='magma', legend=False)
    plt.title('Distribution of Job Seniority Levels')
    plt.xlabel('Number of Postings')
    plt.ylabel('Job Level')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'job_levels.png'))
    plt.close()
    print("Saved job_levels.png")

def plot_top_locations(df, top_n=10):
    """
    Plots the top hiring locations.
    """
    location_counts = df['job_location'].value_counts().head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=location_counts.values, y=location_counts.index, hue=location_counts.index, palette='rocket', legend=False)
    plt.title(f'Top {top_n} Hiring Locations')
    plt.xlabel('Number of Job Postings')
    plt.ylabel('Location')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'top_locations.png'))
    plt.close()
    print("Saved top_locations.png")

if __name__ == "__main__":
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    df = load_processed_data()
    plot_top_skills(df)
    plot_job_levels(df)
    plot_top_locations(df)
