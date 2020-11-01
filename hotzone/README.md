# HotZone
A web for data managemennt, cases clustering and analysis

### Notices
The project currently does not provide user-authentication pages. User can use django-admin to login.

All data management pages are restricted to login-only. Therefore, unauthenticated visitors are redirected to admin login page before they can access their target management page.

The websie now only provide functionalities related to location management, including view, add and delete.

### Deployment
The project is deployed using heroku, with postgresql as its database.

Dependencies are specified in Pipfile and Pipfile.lock (for pipenv) instead of requirement.txt (for pip), as unexpected errors associated with 'environs' package occur when using requirement.txt file 

### Limitation
All requirements in iteration1 are met. 

Further location management, such as multi-data selection, duplicated data filtering will be added in iteration2.
