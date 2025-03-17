#Step 1: Create a dictionary
language = {'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5}
#Step 2: Print it
print("Programming language popularity")
print(language)
#Step 3: Make a bar plot from the data.
import numpy as np
import matplotlib.pyplot as plt
N = 5
scores = (62.3, 52.9, 51, 51, 38.5)
ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind, scores, width, color='skyblue')
plt.title('Programming language popularity')
plt.xticks(ind, ('JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript'))
plt.yticks(np.arange(0, 81, 10))
plt.xlabel("language")
plt.ylabel("percentage(%)")
plt.show()
#Step 4:Print the percentage of developers who use the language that si input.
#Pseudocode:
#1.Prompt user to input a language
#2.Check if the language in the dictionary
#3.If in it, print the percentage; if not, print error
#1.
language_input = input("Please input a programming language:")# get the input language
#2.3.
if language_input in language:
    percentage = language[language_input]
    print(f"the percentage of users who use {language_input} is {percentage}%")
else:
    print("error")