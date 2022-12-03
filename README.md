## Cretue
Third party tool for Academic Affairs Management System of OUC (Ocean University of China 教务管理系统) before 2020.
Basically, this is a Django project. It's build using pure css framework Bulma so there's a lot redundant css codes.

### how to run
python manage.py runserver

### Functionality
search for selected courses by semester (of anyone with a student id which is 学号), including details about how many coins he/she has committed to it.

search for grades by semester or from the beginning of your uni (of anyone also).

search for a certain course to see the grade how everyone ended up with to get a better perspective of whether it is a High-Score course for you to dive in for your GPA. (using a course number and a semeseter).

serach for students by its student id or name, by name you'll get multiple results. This part is implemented by scraping through jwgl.ouc.edu.cn's database using a BFS algorithm included in the project, which unfortunately I've lost the database backup of it, and since the backend of the system has changed since 2020 there's no way around to fetch it again.

feel free to work on this project and bring it back to life again!

### platform
supports both mobile and pc. use Chrome for best experience.
![alt text](/cretue-mobile.jpg?raw=true)

### differences between v2 & v3 : new login method (added verification code):
1. retspan/middleware/sys.py || added /ems/code for new login method.
2. static/loginbuild.js & request.js || for new login method.
3. static/y.png || to store code temporaryly.
4. user/template/log.html & ret.html || .
5. user/isvalid.py || added def getCode(ss):.
6. user/urls.py & views.py || added getVCode & getSS.

