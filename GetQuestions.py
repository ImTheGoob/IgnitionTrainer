from html.parser import HTMLParser
from Content import HTMLKey, DataTracking
import itertools

#Strips HTML tags
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(str(html))
    return s.get_data()


class GetQuestions():


    def CreateTable(Questions, Answers, Corrects):

        Data = {}
        Result = {}

        i = 0
        for (Question, Answer, Correct) in zip(Questions, Answers, Corrects):

            Data["Question"+str(i)] = {"Question": Question, "Answers": Answer, "Correct": Correct}
            i += 1

            for key,value in Data.items():
                if value not in Result.values():
                    Result[key] = value

        print(Result)
            

        return Result

    #Was for Testing
    def CountElements(HTML):
        i = 0
        for tag in HTML:
            i =+ 1
        return i


    def GetAnswers(soup):

        #Class Objects
        DataClass = DataTracking
        HTMLKeyFinder = HTMLKey

        #Global Lists
        QuestionList = DataClass.Question
        QuestionCorrect = DataClass.Correct
        AnswersList = DataTracking.Answers

        #Html Keys
        TrueFalseKey = HTMLKeyFinder.SelectTrueFalseAnswerTag
        TrueFalseClass = HTMLKeyFinder.SelectTrueFalseAnswerClass
        QuestionKey = HTMLKeyFinder.QuestionTag
        CorrectQuestionClass = HTMLKeyFinder.CorrectQuestionClass
        QuestionTextKey = HTMLKeyFinder.QuestionTextTag
        QuestionTextClass = HTMLKeyFinder.QuestionTextClass
        MultipleAnswerKey = HTMLKeyFinder.SelectMultipleAnswerTag
        MultipleAnswerClass = HTMLKeyFinder.SelectMultipleAnswerClass
        IncorrectQuestionClass = HTMLKey.IncorrectQuestionClass


        #Looping Through all Correct Questions
        for correctQuestion in soup.find_all(QuestionKey, class_=CorrectQuestionClass):

            #Getting Current Question and Appending to Dataset
            Questions = strip_tags(correctQuestion.find_all(QuestionTextKey, QuestionTextClass))
            QuestionList.append(Questions)

            #Adding True to Dataset
            QuestionCorrect.append("True")

            selectedValue = ""
            Answer = ""

            #Gets Selected Answer
            if(len(correctQuestion.find_all(TrueFalseKey, TrueFalseClass)) > 0):
                selectedValue = correctQuestion.find_all(TrueFalseKey, TrueFalseClass)
            else:
                selectedValue = correctQuestion.find_all(MultipleAnswerKey, MultipleAnswerClass)
                print("Multiple Choice or Selection")
                print(selectedValue)

            #Need to loop through to get Answer
            if(len(correctQuestion.find_all('p')) == 1):
                for Text in selectedValue:
                    print("---Multiple Choice Question---")
                    Answer = strip_tags(Text.find_all('p'))

            elif(len(correctQuestion.find_all('p')) > 1):
                print("---Multiple Select Question---")

                MultipleAnswersList = []

                for value in selectedValue:

                    value.find_all(MultipleAnswerKey, MultipleAnswerClass)
                    AllAnswers = strip_tags(value.find_all('p'))
                    MultipleAnswersList.append(AllAnswers)

                    print(MultipleAnswersList)

                    Answer = MultipleAnswersList

            elif(len(correctQuestion.find_all('p')) == 0):
                print("---True or False Question---")
                for value in selectedValue:
                    Answer = str(strip_tags(value)).replace(" ", "")
                
            AnswersList.append(Answer)

        for incorrectQuestion in soup.find_all(QuestionKey, IncorrectQuestionClass):
            
            #Getting Current Question and Appending to Dataset
            Questions = strip_tags(incorrectQuestion.find_all(QuestionTextKey, QuestionTextClass))
            QuestionList.append(Questions)

            #Adding True to Dataset
            QuestionCorrect.append("False")

            selectedValue = ""
            Answer = ""

            #Gets Selected Answer
            if(len(incorrectQuestion.find_all(TrueFalseKey, TrueFalseClass)) > 0):
                selectedValue = incorrectQuestion.find_all(TrueFalseKey, TrueFalseClass)
            else:
                selectedValue = incorrectQuestion.find_all(MultipleAnswerKey, MultipleAnswerClass)
                print(selectedValue)

            #Need to loop through to get Answer
            if(len(incorrectQuestion.find_all('p')) == 1):
                for Text in selectedValue:
                    print("---Multiple Choice Question---")
                    Answer = strip_tags(Text.find_all('p'))

            elif(len(incorrectQuestion.find_all('p')) > 1):
                print("---Multiple Select Question---")

                MultipleAnswersList = []

                for value in selectedValue:

                    value.find_all(MultipleAnswerKey, MultipleAnswerClass)
                    AllAnswers = strip_tags(value.find_all('p'))
                    MultipleAnswersList.append(AllAnswers)

                    print(MultipleAnswersList)

                    Answer = MultipleAnswersList

            elif(len(incorrectQuestion.find_all('p')) == 0):
                print("---True or False Question---")
                for value in selectedValue:
                    Answer = str(strip_tags(value)).replace(" ", "")

                
            AnswersList.append(Answer)
            print("Selected Answers: "+str(Answer))

        ##
        Table = GetQuestions.CreateTable(DataTracking.Question, DataTracking.Answers, DataTracking.Correct)

        return Table

            