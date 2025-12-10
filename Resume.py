class Resume:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.skills = []
        self.experience = []
        
    def add_skill(self,skill):
        self.skills.append(skill)
        print('Skill add')
        
    def add_experience(self, job):
        self.experience.append(job)
        print('Exp added')
        
    def show_resume(self):
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print('Skills: ')
        for i in self.skills:
            print(f'- {i}')
        print('Exp: ')
        for i in self.experience:
            print(f'- {i}')
            
            
my_resume = Resume('Ehsan','ehsan@mail.com')

my_resume.add_skill('Python')
my_resume.add_skill('Data Analysis')

my_resume.add_experience('Intern at ABC Company')
my_resume.add_experience('Project on Machine Learning')

my_resume.show_resume()