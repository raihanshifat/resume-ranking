class MakeResumeDataset:
    def __init__(self,data_dict):
        self.data_dict = data_dict
        self.degree_name = ''
        self.major_name = []
        self.skills_name = []
        self.experience = 0
        self.description = ''

    def retrieve_degree_name(self):
        self.degree_name=[self.data_dict['degree_name'].lower().strip()]
        return self.degree_name
    def retrieve_major_name(self):
        for i in self.data_dict['education']:
            try:
                self.major_name.append(i['major_name'].lower().strip())
            except Exception:
                pass
        return self.major_name
    def retrieve_experience(self):
        self.experience=self.data_dict['year_of_exp']
        return self.experience
    def retrieve_skills(self):
        self.skills_name = [i['skill_name'].lower().strip() for i in self.data_dict['skill']]
        return self.skills_name
    def retrieve_all_description(self):
        try:
            self.description= ' '.join([i['experience_description'].lower().strip() for i in self.data_dict['experience']])
        except Exception:
            self.description=''
        return self.description