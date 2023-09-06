from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
import sys
import numpy as np
import pandas as pd
import time

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ScoredQs.ui', self)
        self.setWindowIcon(QtGui.QIcon('logo-color.png'))

        self.show()

        self.TotalQ.setText("-")
        self.CurrentQ.setText("-")

        global question_bank
        question_bank = 0
        global sheet_name
        
        # def open_question_bank():
        #     global question_bank
        #     # filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter = "*.xls")
        #     question_bank = pd.read_excel('*.xls', header = None, sheet_name = 'game 1')

        #     question_bank = pd.read_excel(filename, header = None)
        #     question_bank = question_bank.fillna("IDIOT")
        #     print(question_bank)
        #     self.TotalQ.setText(str(len(question_bank)))
        #     self.CurrentQ.setText("0")

        # self.OpenButton.clicked.connect(open_question_bank)
        question_bank = pd.read_excel('*.xls', header = None, sheet_name = sheet_name)
        question_bank = question_bank.fillna("IDIOT")
        print(question_bank)
        self.TotalQ.setText(str(len(question_bank)))
        self.CurrentQ.setText("0")
        def questionR():
            if type(question_bank) == int:
                print('Open question bank first!')
            else:
                if int(self.CurrentQ.text()) < len(question_bank):
                    question_display = question_bank.loc[int(self.CurrentQ.text())][0]
                    self.QuestionBox.setText(question_display)
                    self.CurrentQ.setText(str(int(self.CurrentQ.text())+1))
                    # print(self.CurrentQ.text())
                else:
                    self.CurrentQ.setText("0") 

        self.QuestionButton_right.clicked.connect(questionR)

        def questionL():
            if type(question_bank) == int:
                print('Open question bank first!')
            else:
                if int(self.CurrentQ.text()) > 1:
                    self.CurrentQ.setText(str(int(self.CurrentQ.text())))
                    question_display = question_bank.loc[int(self.CurrentQ.text())-2][0]
                    self.QuestionBox.setText(question_display)
                    self.CurrentQ.setText(str(int(self.CurrentQ.text())-1))
                    # print(self.CurrentQ.text())
                else:
                    self.CurrentQ.setText("1") 

        self.QuestionButton_left.clicked.connect(questionL)

        def answer():
            if type(question_bank) == int:
                print('Open question bank first!')
            else:
                self.CurrentQ.setText(str(int(self.CurrentQ.text())))
                answer_display = question_bank.loc[int(self.CurrentQ.text())-1][1]
                self.AnswerBox.setText(str(answer_display))
                # print(self.CurrentQ.text())

        self.AnswerButton.clicked.connect(answer)

        def start_timer():
            timer = 480
            while timer > -1:
                self.progressBar.setValue(timer)
                time.sleep(0.1)
                timer -= 0.1
                QApplication.processEvents()
  
        self.StartTimeButton.clicked.connect(start_timer)

        self.TeamAScore.setText("0")
        self.TeamBScore.setText("0")
        self.Correct_Num_A.setText("0")
        self.Correct_Num_B.setText("0")
        self.Wrong_Num_A.setText("0")
        self.Wrong_Num_B.setText("0")
        self.Total_A.setText("0")
        self.Total_B.setText("0")
       
        def win_A(): # increments Correct_Num_A and TeamAScore
            correct_answers_A = int(self.Correct_Num_A.text())
            correct_answers_A += 1
            self.Correct_Num_A.setText(str(correct_answers_A))
            
            score_A = int(self.TeamAScore.text())
            score_A += 10
            self.TeamAScore.setText(str(score_A))

            self.Total_A.setText(str(int(self.Total_A.text()) + 1))

        def loss_A(): # increments Wrong_Num_A and TeamAScore
            wrong_answers_A = int(self.Wrong_Num_A.text())
            wrong_answers_A += 1
            self.Wrong_Num_A.setText(str(wrong_answers_A))
            
            score_A = int(self.TeamAScore.text())
            score_A -= 5
            self.TeamAScore.setText(str(score_A))
            
            self.Total_A.setText(str(int(self.Total_A.text()) + 1))

        self.Add10_A.clicked.connect(win_A)
        self.Min5_A.clicked.connect(loss_A)

        def win_B(): # increments Correct_Num_B and TeamBScore
            correct_answers_B = int(self.Correct_Num_B.text())
            correct_answers_B += 1
            self.Correct_Num_B.setText(str(correct_answers_B))
            
            score_B = int(self.TeamBScore.text())
            score_B += 10
            self.TeamBScore.setText(str(score_B))

            self.Total_B.setText(str(int(self.Total_B.text()) + 1))

        def loss_B(): # increments Wrong_Num_B and TeamBScore
            wrong_answers_B = int(self.Wrong_Num_B.text())
            wrong_answers_B += 1
            self.Wrong_Num_B.setText(str(wrong_answers_B))
            
            score_B = int(self.TeamBScore.text())
            score_B -= 5
            self.TeamBScore.setText(str(score_B))

            self.Total_B.setText(str(int(self.Total_B.text()) + 1))

        self.Add10_B.clicked.connect(win_B)
        self.Min5_B.clicked.connect(loss_B)

        def reset(): # reset all text fields to 0
            self.TeamAScore.setText("0")
            self.TeamBScore.setText("0")
            self.Correct_Num_A.setText("0")
            self.Correct_Num_B.setText("0")
            self.Wrong_Num_A.setText("0")
            self.Wrong_Num_B.setText("0")
            self.Total_A.setText("0")
            self.Total_B.setText("0")

        self.ResetScoreButton.clicked.connect(reset)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()