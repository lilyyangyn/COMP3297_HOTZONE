# HotZone
A web for data managemennt, cases clustering and analysis.

Access HotZone with URL: https://dry-mesa-46974.herokuapp.com/

Superuser: adminse, Password: comp3297

### Notices
All data management pages are restricted to login-only. Therefore, unauthenticated visitors are redirected to login page before they can access their target management page.

The websie now only provide functionalities related to data management. For each kind of data, view, search, add and delete are provided. 
For location data returned by GeoData without a nameEN value, name in the search box is used. The index page of location is https://dry-mesa-46974.herokuapp.com/records/locations

### Deployment
The project is deployed using heroku, with postgresql as its database.

Dependencies are specified in Pipfile and Pipfile.lock (for pipenv) instead of requirement.txt (for pip), as unexpected errors associated with 'environs' package occur when using requirement.txt file 

### Limitation
All requirements in sprint2 are met. We also implement user-friendly data management page for patients, viruses, cases and visits. Visits are organized under each case.

Clustering will be implemented in later sprints.
