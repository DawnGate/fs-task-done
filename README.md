# Full-stack Software Engineering at Konigle 
We are thrilled you are interviewing with us!  The goal of this task is to give you a feel of the kind of work that you will be doing at Konigle.  We strive to build meaningful tools to scale an online store. The tools help the online seller save time, reduce cost of running the store and increase sales.

We believe in technologies that help us to provide customer value in the shortest time possible and architect our product around this. We invest in technologies that we know the best and try to build things around that.

Konigle is a web first product and each seller tool inside Konigle is a Django application with it's own UI and data models. As a full stack engineer, we expect you to take the end-to-end responsibilities of building, maintaining, scaling the seller tool and deliver the value to our customers. In order to give you the feel of the actual work that you will be doing, this task in itself is a seller tool that should take you not more than 4 hours to prototype.

## Customer Acquisition Tool
It is important to have a loyal customer base for any business. The first step in building this customer base is acquiring them. 
The Customer Acquisition Tool is a seller tool that helps the online seller to acquire and manage customers. 
It is a combination of a widget that will be installed on the seller's online store and a Django application which will provide the ability to manage these new customers.

![Seller Tool](cac-widget.png)

Here is the brief functionality of the seller tool
- A widget pops up on the online store and prompts the store visitor to signup using email address
- The signup data will be sent to an API provided by the Django app (seller tool)
- The app stores the data in its own model
- The app exposes a view which 
	1.  lists down the signups in the reverse chronological order of their signup timestamp
	2. Shows the number of new signups in the current calendar month
- The app sends an email to the seller every Monday and Wednesday including the statistics around the new customer acquisition

## Task
Build a Django application with following functionalities
1. Exposes an API to store the customers. Feel free to use Django REST Framework
2. A view to list down the signups in the reverse chronological order and show the number of new signups this calendar month
3. Bonus - setup a celery task that runs every Monday and Wednesday 8AM UTC and prints the number of new signups occurred in the current calendar month to the console.

You don't have to build the javascript widget as part of this task. We have created one for you!

 _NOTES_
 - This seller tool must serve more than one store
 - The widget itself sits on seller's online store (3rd party site) and sends data to your app (Konigle). The API is public but we don't want anyone to misuse it.

## Steps
1. Download the attached zip file which is a git repo. The repo already contains the following
    - `widgets` - a Javascript project for creating the widget. This includes the webpack based toolchain to generate the widget's JS file. If you are not comfortable with all these, don't worry about it.
    - `static/js/e-widgets.v1.min.js` - The widget's javascript file to be included in the seller's online store. You need to configure your Django project to serve this static file to any online store.
    - `widgets/test/store.html` - A test HTML file which includes the widget. You need replace your Django server's address to load the widget on this sample page.
2. Create a Django project inside the repo
3. Create Django app with a meaningful name for the seller tool
4. Create a data model to store the customers
5. Expose an REST API to be used by the widget to submit the signup data.
	- The API endpoint must be copied at `widgets/src/widgets.js:5` in order to make the submission work
6. Create a Django view for listing the customers. Below is a sample Figma design for your reference
7. Bonus - Create a celery periodic task that does what is specified above

## Submission
Zip the working repo and email us

**OR**

Push it to your own git repo and share us the link. This way you have a useful, working project against your profile!





