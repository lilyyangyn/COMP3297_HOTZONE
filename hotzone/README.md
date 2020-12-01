# HotZone
A web for data managemennt, cases clustering and analysis.

Access HotZone Release 2 with URL: https://fast-crag-09011.herokuapp.com/
Access HotZone Release 1 with URL: https://dry-mesa-46974.herokuapp.com/

Superuser: adminse, Password: comp3297

### Notices
All data management pages are restricted to login-only. Therefore, unauthenticated visitors are redirected to login page before they can access their target management page.

Clusterinng are also restricted to login-only. Unauthenticated visitors are redirected to login page before the real access

Different to the ordinary staff, admin can find a special entry called "Console" on the navigation bar that enable them to access the django-admin page.

### Deployment
The project is deployed using heroku, with postgresql as its database.

Dependencies are specified in Pipfile and Pipfile.lock (for pipenv) instead of requirement.txt (for pip), as unexpected errors associated with 'environs' package occur when using requirement.txt file 

### Limitation
All requirements in sprint3 are met. 

### Other Implementations
We also implement user-friendly data management page for patients, viruses, cases and visits. Visits are organized under each case.