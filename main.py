from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder 
import random
import time
from coders import generate

class Start(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        

    def first(self):
        global q,a,i,ques
        ques = self.ids.ques_id.text
        level = self.ids.level_id.text
        self.ids.generate.disabled = False
        self.ids.generate.text = "Next"
        self.ids.random_question.text=""
        print(ques,level)
        q,a = generate(int(ques),int(level))
        i = -1
        self.generate_question()

    def generate_question(self):
        global i,opts,q,a,ques,start_time,end_time
        if i==-1:
            start_time = time.time()
        i+=1
        if i >= int(ques) - 1:
            self.ids.generate.text = "End"
            end_time = time.time() - start_time
            self.ids.generate.background_color = (0,0,0)
            self.ids.random_question.text = f"Time : {round(end_time,2)} seconds"
            self.ids.generate.disabled = True
            self.ids.option_a.text ="" 
            self.ids.option_b.text =""
            self.ids.option_c.text =""
            return
        
        self.ids.random_question.text = q[i]
        opts = [a[i],a[i] - 1,a[i] + 1]
        opts = sorted(opts, key=lambda x: random.random())
        self.ids.option_a.text = str(opts[0])
        self.ids.option_a.background_color = (0,0,0)
        self.ids.option_b.text = str(opts[1])
        self.ids.option_b.background_color = (0,0,0)
        self.ids.option_c.text = str(opts[2])
        self.ids.option_c.background_color = (0,0,0)

    def check_answer(self,ans):
        global i,opts,q,a
        ans=int(ans)
        print("options are : ",opts)
        print(f"correct is {a[i]}")
        print(ans)
        if opts[0] == ans:
            if ans==a[i]:
                self.ids.option_a.background_color = (0,255,0)
            else:
                self.ids.option_a.background_color = (255,0,0)
        elif opts[1] == ans:
            if ans==a[i]:
                self.ids.option_b.background_color = (0,255,0)
            else:
                self.ids.option_b.background_color = (255,0,0)
        elif opts[2] == ans:
            if ans==a[i]:
                self.ids.option_c.background_color = (0,255,0)
            else:
                self.ids.option_c.background_color = (255,0,0)
        else:
            pass
        

#q,a =generate()
#print(q,a)
i=-1

class MainApp(MDApp):
    def build(self):
        return Start()

MainApp().run()