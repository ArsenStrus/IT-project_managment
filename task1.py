class Testpaper:
    def __init__(self,subject,markscheme,pass_mark):
        self.subject=subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark
    
class Student:
    def __init__(self):
        self.tests_taken="No tests taken"
    def take_test(self,paper,list_of_answers):
        if len(list_of_answers)!=len(paper.markscheme):
            return print("Give all answers!")
        differences=0
        for i in range(len(list_of_answers)):
            if list_of_answers[i]!=paper.markscheme[i]:
                differences+=1
        result=round((len(list_of_answers)-differences)/len(list_of_answers)*100)
        passing_score_int=int(paper.pass_mark[:-1])
        
        if isinstance(self.tests_taken, str):
            self.tests_taken=dict()
        self.tests_taken[paper.subject] = f"Passed! ({result}%)" if result >= passing_score_int else f"Failed! ({result}%)"

print("Hello World")