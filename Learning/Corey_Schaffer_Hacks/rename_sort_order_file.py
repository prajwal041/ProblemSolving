import os

path = '/home/prajshet/projects/Demo'
os.chdir(path)

for f in os.listdir(path):
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_titles = f_title.strip()
    f_courses = f_course.strip()
    f_nums = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_nums,f_titles,f_ext)
    os.rename(f,new_name)


"""
Input Format:
ABC - Solar System - #2.mp4
BJK - Solar System - #5.mp4
BKJ - Solar System - #1.mp4
PWF - Solar System - #9.mp4
POK - Solar System - #10.mp4

Output:
01 - BKJ.mp4
02 - ABC.mp4
05 - BJK.mp4
09 - PWF.mp4
10 - POK.mp4
"""