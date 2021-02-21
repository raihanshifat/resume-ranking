from make_dataset.make_job_dataset import MakeJobDataset
from make_dataset.make_resume_dataset import MakeResumeDataset
from utility.scaling import sigmoid_normalization,sigmoid_normalization_v2
from data_preprocessing.preprocessing import PreProcessing
from scoring.scoring_functions import degree_score,skill_score,major_name_score,experience_score,cosine_similarity_score
class CalculateScore:
    def __init__(self,job_data,resume_data):
        self.score=0
        self.job_data=job_data
        self.resume_data=resume_data
        self.job_dataset_object=MakeJobDataset(self.job_data)
        self.resume_dataset_object=MakeResumeDataset(self.resume_data)
    def calculate_degree_score(self):
        job_degree_data=self.job_dataset_object.retrieve_degree_name()
        resume_degree_data=self.resume_dataset_object.retrieve_degree_name()
        initial_score=degree_score(job_degree_data,resume_degree_data)
        normalized_score=sigmoid_normalization_v2(initial_score)
        return normalized_score
    def calculate_major_score(self):
        job_major_data=self.job_dataset_object.retrieve_major_name()
        resume_major_data=self.resume_dataset_object.retrieve_major_name()
        score=major_name_score(job_major_data,resume_major_data)
        return score
    def calculate_skill_score(self):
        job_skill_data=self.job_dataset_object.retrieve_skills()
        resume_skill_data=self.resume_dataset_object.retrieve_skills()
        score=skill_score(job_skill_data,resume_skill_data)
        return score
    def calculate_experience_score(self):
        job_experience_data=self.job_dataset_object.retrieve_experience()
        applicant_experience_data=self.resume_dataset_object.retrieve_experience()
        initial_score=experience_score(job_experience_data,applicant_experience_data)
        normalized_score=sigmoid_normalization(initial_score)
        return normalized_score
    def calculate_cosine_similarity_score(self):
        job_description_data=self.job_dataset_object.retrieve_all_description()
        resume_description_data=self.resume_dataset_object.retrieve_all_description()
        job_data_preprocessing_object=PreProcessing(job_description_data)
        resume_data_preprocessing_object=PreProcessing(resume_description_data)
        job_description_data=job_data_preprocessing_object.remove_new_line().remove_punctuation().remove_punctuation().data
        resume_description_data=resume_data_preprocessing_object.remove_new_line().remove_punctuation().remove_punctuation().data
        score=cosine_similarity_score(job_description_data,resume_description_data)
        return score