import random

class Quiz():
    def __init__(self):
        word = []
        clue = []

        with open('word.txt','r') as w:
            for line in w.readlines():
                line = line.rstrip()
                word.append(line)
            w.close()
        
        with open('clue.txt','r') as c:
            for line in c.readlines():
                line = line.rstrip()
                clue.append(line)
            c.close()

        self.word = word
        self.clue = clue

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
        with open('word.txt', 'a') as w:
            w.write('\n'+new_word)

        with open('clue.txt', 'a') as c:
            c.write('\n'+new_clue)

        w.close()
        c.close()
        # self.word.append(new_word)
        # self.clue.append(new_clue)
        # print(self.word)

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





