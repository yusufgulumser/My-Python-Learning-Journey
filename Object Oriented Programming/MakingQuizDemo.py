# MAKE A QUIZ

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionindex=0
    
    def getQuestion(self):
       return self.questions[self.questionindex]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Question{self.questionindex+1}: {question.text}')
        for q in question.choices:
            print('-' + q)
        answer=input('answer: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question=self.getQuestion()
    
        if question.checkAnswer(answer):
            self.score+=1
        self.questionindex +=1

    
    def loadQuestion(self):
        if(len(self.questions))==self.questionindex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionindex+1

        if questionNumber> totalQuestion:
            print('Quiz is over')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))



q1=Question('what is the best software language?',['javascript','java','c','python'],'python')
q2=Question('what is the most profitable software language?',['python','java','c','javascript'],'python')
q3=Question('what is the most popular software language?',['c','python','javascript','java'],'python')
questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.loadQuestion()