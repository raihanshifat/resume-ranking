import re
class MakeJobDataset:
    def __init__(self,data_dict):
        self.data_dict=data_dict
        self.degree_name=[]
        self.major_name=[]
        self.skills_name=[]
        self.experience=None
        self.description=''
    def retrieve_degree_name(self):
        self.degree_name = [i['degree_name'].lower().strip() for i in self.data_dict['degrees']]
        return self.degree_name
    def retrieve_major_name(self):
        for value in self.data_dict['degrees']:
            self.major_name.append(value['major_name'].lower().strip())
        return self.major_name
    def retrieve_experience(self):
        temp_list=self.data_dict['job_description'].split('\n')
        result=0
        for i in temp_list:
            try:
                if 'experience' in i:
                    pattern = '\d+'

                    result = re.findall(pattern, i)
                    result = "".join(result[0])
                    break
            except Exception:
                pass
        if result is None:
            result=0
        self.experience=result
        return int(self.experience)
    def retrieve_skills(self):
        self.skills_name = [i['skill_name'].lower().strip() for i in self.data_dict['skills']]
        return self.skills_name
    def retrieve_all_description(self):
        self.description=self.data_dict['nice_to_have'].lower()+' ' + self.data_dict['job_title'].lower()+' '+self.data_dict['job_responsibilities'].lower() + ' ' + self.data_dict['job_description'].lower()
        return self.description




