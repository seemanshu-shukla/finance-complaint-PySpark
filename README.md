# <p align="center"><u>Finance-Complaint</u></p>

## <u>Problem Statement</u>:
Complaints can give us insights into problems people are experiencing in the marketplace and help us to understand the reason and do necessary modifications in exisiting financial product if required.

## <u>Solution Proposed</u>: 
By understanding existing complaints registered against financial products we can create an ML model that can help us to identify newly registered complaints whether they are problematic or not and accordingly company can take quick action to resolve the issue, and satisfy the customer's need.

Therefore, the problem statement is to identify registered complaint will be disputed by customer or not.

## <u>Tech Stack Used</u>:
1. <b>Python</b>
2. <b>PySpark</b>
3. <b>PySpark ML</b>
4. <b>Airflow</b> - as a scheduler for scheduling the pipelines
5. <b>MongoDB</b> - to store the artifact info of respective components for monitoring purpose
6. <b>Terraform</b> - to automate the provisioning and deprovisioning of the required infrastructure
7. <b>circleci</b> - for CICD deployment workflow automation

## <u>Infrastructure Required</u>:
1. <b>GCP Compute Engine</b> - to deploy our AI powered application over cloud
2. <b>AWS S3 Bucket</b> - to register best performing trained model
3. <b>GCP Artifact Registry</b> - to store the docker image built during continous delivery

## <u>Dashboarding</u>:
1. <b>Node Exporter</b> - to collect or scrap the system logs like RAM, ROM utilization etc
2. <b>Prometheus</b> - to store the logs collected by Node Exporter
3. <b>Promtail</b> - to collect or scrap the application logs
4. <b>Loki</b> - to store the logs collected by Promtail
5. <b>Grafana</b> - to create dashboard using logs stored in Prometheus and Loki

## <u>Steps to run project in local system</u>:
1. Build docker image
```
docker build -t fc:lts .
```
2. Set environment variable
```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export MONGO_DB_URL=
export AWS_DEFAULT_REGION="ap-south-1"
export IMAGE_NAME=fc:lts
```
3. To start your application
```
docker-compose up
```
4. To stop your application
```
docker-compose down
``` 

## <u>How to setup airflow in local</u>:
1. Set airflow directory
```
export AIRFLOW_HOME="/home/seema/census_consumer_project/census_consumer_complaint/airflow"
```

2. To install airflow 
```
pip install apache-airflow
```

3. To configure database
```
airflow db init
```

4. To create login user for airflow
```
airflow users create  -e seemanshu.shukla11@gmail.com -f Seemanshu -l Shukla -p admin -r Admin  -u admin
```

5. To start scheduler
```
airflow scheduler
```

6. To launch airflow server
```
airflow webserver -p <port_number>
Eg; airflow webserver -p 8080
```

7. Update in airflow.cfg
```
enable_xcom_pickling = True
```
