
from scoring.calculating_score import CalculateScore

class ResumeRanking:
    def ranking_resume(self,job_data,resume_data):
        result=[]
        for resume in resume_data:
            score_dict={}
            score_dict['user_name']=resume['user_name']
            score_object=CalculateScore(job_data,resume)
            score = 10 * score_object.calculate_skill_score() + 8 * score_object.calculate_major_score() + 8 * score_object.calculate_degree_score() + 4 * score_object.calculate_cosine_similarity_score() + 10 * score_object.calculate_experience_score()
            score=score/40
            score_dict['score'] = score
            result.append(score_dict)
        return result