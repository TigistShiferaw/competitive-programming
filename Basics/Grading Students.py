
def gradingStudents(grades):
    for i in range(len(grades)):
       
        
            if grades[i]  < 38:
                grades[i]=grades[i]
        
            elif 5*(math.floor(grades[i]/5)+1)-grades[i] <3:
                grades[i]=5*(math.floor(grades[i]/5)+1)
                
            else:
                grades[i]=grades[i]
            
    return grades