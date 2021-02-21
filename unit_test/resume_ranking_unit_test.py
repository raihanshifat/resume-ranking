import unittest
from data_preprocessing.preprocessing import PreProcessing
from make_dataset.make_job_dataset import MakeJobDataset
from make_dataset.make_resume_dataset import MakeResumeDataset
from scoring.scoring_functions import degree_score,major_name_score,experience_score,cosine_similarity_score,skill_score
from scoring.calculating_score import CalculateScore
from utility.degree_rank import degree_rank
from utility.scaling import sigmoid_normalization,sigmoid_normalization_v2


class MyTestCase(unittest.TestCase):
    def test_MakeJobDataset(self):
        job = {"nice_to_have": "Age at least 24 years\nBoth males and females are allowed to apply\n\nKnowledge in PHP, AJAX, JavaScript, Jquery, JSON, AngularJS, NodeJS\nMust be able to work in a team\nSound knowledge on OOP principles, design patterns etc.\nAbility to work quickly with high-quality\nGood working knowledge with other programming knowledge is preferable\nTeam oriented attitude with strong communications skills\nFluent in English (spoken an written)\nInnovative, open minded and ready to put the necessary effort to reach the goals and deadlines.\nAble to Analyze, design and develop software in Web based using: PHP, JavaScript, MySQL, Oracle, SQL Server 2012 etc.\nExperience with an MVC framework such as Zend, CodeIgniter, Laravel is must.\nExtensive knowledge in PHP with CodeIgniter,  Laravel, Javascript & AJAX\nProfessional experience using Design Pattern\nExperience in developing web application\nKnowledge in Open source Tools\nShould have sound knowledge in Web 2.0 concept",
               "degrees": [{"major_name": "CSE", "degree_id": "e4a795df-5748-462b-81b2-8fb37c021378",
                            "degree_name": "Bachelor of Science (BSc)",
                            "major_id": "f6a94b67-9154-406e-bf0b-1d15306ee26a"}],
               "job_responsibilities": "Analysis, Coding & Leading.",
                "job_description": "3+ Years' experience with Laravel\nHands on experience with ReactJS / React Native is required\nAt least 3 year's experience of Web Application Development using Laravel, CodeIgniter.",
               "skills": [{"skill_id": "6abd1d43-c294-4c95-a3f5-c90a7ec2bcbd", "skill_name": "PHP"},
                          {"skill_id": "d500814f-fd53-469c-b197-e790f64c4509", "skill_name": " AJAX"},
                          {"skill_id": "3c9a9e41-6ab8-4aa2-99e2-0922e57574d1", "skill_name": " JavaScript"},
                          {"skill_id": "d6b13385-f9e5-403d-bc6a-0c46b89e5b6c", "skill_name": " Jquery"},
                          {"skill_id": "179a56de-1dbc-462c-b4af-9468f6b7ed2e", "skill_name": " JSON"},
                          {"skill_id": "50cbaf60-04db-4471-92c3-26540fe320fb", "skill_name": " AngularJS"},
                          {"skill_id": "56b3fd31-ec6a-460e-a9f9-a3e806096d64", "skill_name": " NodeJS"}]}
        a=MakeJobDataset(job)
        self.assertEqual(a.retrieve_skills(),['php', 'ajax', 'javascript', 'jquery', 'json', 'angularjs', 'nodejs'])
        self.assertEqual(a.retrieve_experience(),3)
        self.assertEqual(' '.join(a.retrieve_major_name()),'cse')
        self.assertTrue('bsc' in ' '.join(a.retrieve_degree_name()))
    def test_PreProcessing(self):
        a=PreProcessing('asdjgadg \n asdasd   asdasd &*%^&$')
        a.remove_new_line().remove_punctuation().remove_multiple_space()
        self.assertEqual(a.data, 'asdjgadg asdasd asdasd ')
    def test_degree_rank(self):
        a=degree_rank(['Bachelor of Scence (bsc)'])
        self.assertEqual(a,3)
    def test_degree_score(self):
        a=degree_score(['bsc'],['ssc'])
        self.assertEqual(a,-2)
    def test_skill_score(self):
        a=skill_score(['java','php'],['php'])
        self.assertEqual(a,1/2)
    def test_major_name_score(self):
        a=major_name_score(['cse'],['cse'])
        self.assertEqual(a,1)


if __name__ == '__main__':
    unittest.main()
