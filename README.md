# Hoosh Pardaz Parstech Interview Project

## 💡 Overview
In this project, a shipment tracking API has been developed by which the user can get the list of all the shipment and check the status of a single article as well. Users can access the list of shipments by a GET request to the `/shipment/` endpoint and also by sending a POST request containing two parameters, `tracking_number` and `carrier`, in the body of the request to this endpoint.


## ⚙️ Project Structure
As this application has very brief functionalities, it includes few amount of services. Python is the main programming language used for developing the services. Let's discuss more about the technical details.

### web Framework
The API service employs Django web framework and PostgresSQL as the primary database of the backend service. Django models defines the structure of the tables in our database. One of the main advantages of Django framework is that it handles the process of accessing the database and the queries by its own. This feature helps developer to not pay attention to the details of accessing the database and the connectors, and moreover developers do not need to write SQL code for their queries, since django provide built-in methods to query on the dataset using only python code, even for the very complex queries.

### Backend Database
The databases used in this project are the PostgresSQL as the primary database in the production stage and Sqlite for debugging purposes. Our django code checks if we are in the debugging stage, uses the Sqlite instead of heavy-weighted database like Potgres. However, in the deployment stage, we have used the Potgres database because of the security, usage convinience and its speed. In addition, Potgres brings extenssions to suport more data types, which makes it one of the best relational databases.

### Job Distributer
One of the challenges of this project was to efficiently handle the request to the external sources. The API for the list of shipments must provide the current weather condition of the location of the shipment. Therefore, we needed to use some third-party APIs for the weather condition ([WeatherAPI](https://www.weatherapi.com/) is the service used in this project). This job could be carried out using serveral ways. 
1. Develop a separate standalone service to request to the Weather API endpoint and update a table of the backend database with the fetched information.
2. 🌟 Use a job distributer and implement make a function in our Django app to send the task (Updating weather information) to it. This is the procedure I chose to have in this application. [`Celery`](https://docs.celeryq.dev/en/stable/getting-started/introduction.html), which is an asynchronous task queue and commenly used for handling background tasks, is the job distirbuter used for this purpose in our project. Django transmits the updating weather tasks to Celery using a message broker like RabbitMQ or Redis. The celery then distribute the tasks acroos the one or more worker processes. The Celery worker is the process that runs in the background and executes the tasks that are sent to it. 


<div style="border: 1px solid #999; padding: 10px;">

**Then why not to request to the API endpoint in our web server?** \
In order to make sure that the web application runs smoothly and without any delays, developers must offload any time/resource-intensive task, which runs independently from the web application service. In particular, when the web server receives lots of requests from the users. 
</div>

<br>

### Message Broker
As mentioned earlier, django sends the tasks to the celery using a message broker. For this project, I chose to use Redis as the message broker over the RabbitMQ. **Then why?** Because Redis is actully a Key-Value NoSQL database. In addition, Redis is known as an in-memory database, which makes it so fast to retrieve data from it. These two features bring so many functionalities to Redis. Such as storing stream data, time series data, and also being used as a message broker. Having the capability of working as a database, is main reason to chose Redis over the other available tools for our project. 

After completing the given tasks, the celery worker must store the result somewhere. So, an other database is needed here to fullfill this need. This is the place that Redis comes handy and helps us store the results in itself as well as facilitating the process of the transmitting the tasks.

⚠️ It is worth mentioning that in the larger systems, it may be necessary to employ a different database as the number of requests and users grow, since the storing data in the memory requires more amount of memory in the server. Thus separating the message queue and the results' database become a must!

### Task Scheduler
One of the required parts of the project is to limit the number of request to the third-party weather API. **Why?** Because open APIs allow users to use the service for a limited amount requests. This is for preventing the problem of over-usage or security problems like DDos attacks. Therefore, it is necessary to send requests to that service periodically. To tackle this problem, the Django app, create the updating weather tasks every 2 hours to satisfy this requirement. The component responsible for scheduling these tasks is `Celery Beat`. Celery Beat schedules tasks by sending messages to the message broker at predefined intervals. These messages are then consumed by Celery workers, which execute the scheduled tasks.

The picture below, illustrates the architecture of this application. Notice that there is only one Redis server in our project.

<div >
<img src="images/architecture.jpg">
</div>

<br>

## **How to run?**
For running this project, you can clone this repo into your local machine and then just run:

```shell
docker compose up -d --build
```

And the you can find the application in ```http://localhost```.