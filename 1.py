#!/usr/bin/env python
# coding: utf-8

# In[7]:


#ตรวจสอบตัวเลข
def check_num():
    global score
    while True:
        try:
            score = float(input('กรุณาใส่คะแนน : '))
            if 0<=score<=100:
                break
            else:
                print('กรุณาใส่คะแนนเป็นตัวเลข 0-100')
        except ValueError:
            print('กรุณาใส่คะแนนเป็นตัวเลข 0-100')
    return score

#ให้เกรด
def check_grade(score):
    grade_base = [('A',80), ('B',70), ('C',60), ('D',50), ('F',0)]
    
    for grade, min_score in grade_base:
        if score >= min_score:
            print (f'เกรดที่ได้ คือ : {grade}')
            break
    
        
check_num()
check_grade(score)
    
    
    


# In[ ]:





# In[ ]:




