from tkinter import *

question = {
     "What is the capital of France?": ["London", "Berlin", "Paris", "Madrid"],
            "Who wrote 'Romeo and Juliet'?": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
            "What is the chemical symbol for water?": ["O2", "CO2", "H2O", "NaCl"],
            "What year did the Titanic sink?": ["1910", "1912", "1914", "1916"],
            "What is the tallest mammal?": ["Elephant", "Giraffe", "Rhino", "Hippo"]
        }
	
ans = ['Paris','William Shakespeare','H2O','1912','Giraffe']

current_question = 0


def start_quiz():
	start_button.forget()
	next_button.pack()
	next_question()


def next_question():
	global current_question
	if current_question < len(question):
		
		check_ans()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		clear_frame()
		Label(f1, text=f"Question : {c_question}", padx=10,
			font="calibre 12 normal").pack(anchor=NW)
		for option in question[c_question]:
			Radiobutton(f1, text=option, variable=user_ans,
						value=option, padx=20).pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"Your Score is {user_score.get()} out of {len(question)}"
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text="Thanks for Participating In The Quiz",
			font="calibre 18 bold").pack()


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


if __name__ == "__main__":
	root = Tk()

	root.title("quiz by sarita")
	root.geometry("350x300")
	root.minsize(800, 400)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="Quizerr", 
		font="calibre 40 bold",
		relief=SUNKEN, background="cyan", 
		padx=10, pady=9).pack()
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, 
						text="Start",
						command=start_quiz, 
						font="calibre 17 bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Question",
						command=next_question, 
						font="calibre 17 bold")

	root.mainloop()
