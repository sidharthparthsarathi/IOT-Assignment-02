result={"Student_{}".format(i+1):[int(input("Enter marks of student_{} for subject_{}: ".format(i+1, j+1)))for j in range(5)] for i in range(10)}
[print("Total marks of Student_{} is {}".format(i+1, total)) for i,total in enumerate([sum(result[student]) for student in result])]
