import numpy as np
scores = np.array([
    #Ma  Ph   Ch
    [80, 75, 90],   #Ab
    [65, 70, 60],   #sa
    [95, 88, 92],   #Jh
    [72, 78, 85]    #he
])

# print(scores[1,1])
# print(scores[0:,0])
# print(scores[0:,2])
# print(scores[2,0:])
# print(scores[0:2,0:])
# print(scores[0:,1:])

#Exersice 2

#1 higest score per subject

#math
# print(np.max(scores[0:,0]))

# #phy
# print(np.max(scores[0:,1]))

# #che
# print(np.max(scores[0:,2]))

#2 average score per subject

# #math
# print("Maths average score : ",np.average(scores[0:,0]))

# #Phy
# print("Phy average score : ",np.average(scores[0:,1]))

# #Che
# print("Che average score : ",np.average(scores[0:,2]))

# #3 average result pf students

# #Abel
# print("Abel's average score : ",np.average(scores[0,0:]))

# #Sara
# print("Sara's average score : ",np.average(scores[1,0:]))

# #John
# print("John's average score : ",np.average(scores[2:,0:]))

#  #helen
# print("Helen's average score : ",np.average(scores[3,0:]))


subject = ["Maths","Physics","Chem"]
students = ["Abel", "Sara", "John", "Helen"]

student_average = np.mean(scores,axis=1)
subject_average = np.mean(scores,axis=0)

for i,av in enumerate(student_average):
    print(students[i],"Average: ",av)
print("")
for i , av in enumerate(subject_average):
    print(subject[i] ,"Average: " ,av)

print("")
print("1st Ranked student is: ", students[np.argmax(student_average)])