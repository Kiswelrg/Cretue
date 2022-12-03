## Cretue
Third party tool for Academic Affairs Management System of OUC (Ocean University of China 教务管理系统) before 2020.
Basically, this is a Django project. It's build using pure css framework Bulma so there's a lot redundant css codes.

### how to run
python manage.py runserver

### Functionality
search for anyone's selected courses by semester (with a student id (学号)), including details about how many coins he/she has inserted.

search for grades(成绩) by semester or from the beginning of your uni (or of anyone else).

search for a certain course to see the grade how everyone ended up with to get a better perspective of whether it is a High-Score course for you to dive in for better GPA or it's one u should avoid taking. (using a course number(选课号) and a semeseter id(学期号)).

serach for students by its student id(学号) or name(姓名), by name you'll get multiple results. This part is implemented by scraping through jwgl.ouc.edu.cn's database using a BFS algorithm included in the project, which unfortunately I've lost the database backup of the result, and since the backend of the jwgl.ouc.edu.cn system has changed since 2020 there's no way around to fetch it again.

feel free to work on this project and bring it back to life again!

### platform
supports both mobile and pc. use Chrome for best experience.   
<img src="/cretue-mobile.jpg" width="300" />

### differences between v2 & v3 : new login method (added verification code):
1. retspan/middleware/sys.py || added /ems/code for new login method.
2. static/loginbuild.js & request.js || for new login method.
3. static/y.png || to store code temporaryly.
4. user/template/log.html & ret.html || .
5. user/isvalid.py || added def getCode(ss):.
6. user/urls.py & views.py || added getVCode & getSS.

