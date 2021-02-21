from utility.degree_rank import degree_rank
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def degree_score(required_degree,applicant_degree):
    required_degree_rank=degree_rank(required_degree)
    applicant_degree_rank=degree_rank(applicant_degree)
    result=applicant_degree_rank-required_degree_rank
    return result
def skill_score(required_skill,applicant_skill):
    intersect_list=list(set(required_skill).intersection(applicant_skill))
    result=len(intersect_list)/len(required_skill)
    return result
def experience_score(required_experience,applicant_experience):
    result=int(applicant_experience)-int(required_experience)
    return result
def major_name_score(required_major,applicant_major):
    intersect_list=list(set(applicant_major).intersection(required_major))
    result=0
    if len(intersect_list)>0:
        result=1
        return result
def cosine_similarity_score(job_description,resume_description):
    count_vectorizer = CountVectorizer(stop_words='english')
    sparse_matrix = count_vectorizer.fit_transform([job_description, resume_description])
    result=cosine_similarity(sparse_matrix)
    return result[0][1]
