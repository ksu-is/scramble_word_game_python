import random

class Quiz():
    def __init__(self):
        self.word =['lion', 'eagle', 'piano', 'cheese', 'machine learning']
        self.clue = ['king of the jungle', 'popular bird', 'music that is black and white', 'mouse\'s food', 'machine that learning by itself']

        random_number = random.randint(0, len(self.word)-1)
        self.question_word = self.word[random_number]
        self.question_clue = self.clue[random_number]

    def question(self):

        question = ''
        
        random_number1  = random.randint(0,len(self.question_word)-1) # -1 because it start from 0
        random_number2  = random.randint(0,len(self.question_word)-1)
        # print(word[random_number])
        while random_number1 == random_number2:
            random_number1 = random.randint(0,len(self.question_word)-1)

        for i in range(len(self.question_word)):
            
            if self.question_word[i] == " ":
                question += " "
            elif random_number1 != i and random_number2 != i: 
                question += '_'
            elif random_number1 == i and random_number2 != i:
                question += self.question_word[random_number1]
            
            else:
                question += self.question_word[random_number2]
        
        return question, self.question_word, self.question_clue
    
    def play(self, user_answer):
        if user_answer == self.question_word:
            return 'Answer is correct'
        else:
            return 'Answer is wrong'
        
    def update_question(self, new_word, new_clue):
        self.word.append(new_word)
        self.clue.append(new_clue)
        print(self.word)

        return 'question added successfully, thank you for participating'
        
    def show_option(self):
        print("============= OPTIONS =============")
        print("1. play")
        print("2. update questions and clue")
        print("3. exit")

        option = int(input("select option: "))
        if option == 1:
            quest, word, clue = self.question()
            print(quest)
            print(clue)

            answer = input('write your answer: ')

            print(self.play(answer))

        elif option == 2:
            new_word = input('write your new word question: ')
            new_clue = input('write your new word clue: ')

            print(self.update_question(new_word, new_clue))

        else :
            print('Thank you for playing')
            exit()





