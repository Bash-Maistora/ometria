#  Batch Import System

Given the high performance and scalability demands of the system, it would need to be asynchronous and distributed. In order to schedule and communicate between services a message broker would be necessary, two good choices are RabbitMQ and Apache Kafka. MQs can be used to backup the data during processing to improve data retention and avoid accidental loss. The batch import can be executed asyncronously from a task queue with priority support such as Celery. Decoupling logging database from the regular database if a must and a good choice that can support the heavy load is NoSQL Db such as Cassandra.

To speed up database actions several strategies could be implemented together:
1. Validation in application layer not in database
2. Drop indices before load and recreate later
3. Parallel bulk load if possible

I do not have experience setting up ETL systems on AWS. While researching potential products, I came across AWS Glue, which is a fully managed etl service that automates a large part of import process. The generated Python code is customizable, which would allow project optimizations and reusability. AWS Glue come with a scheduler that handles dependecy resolution, job monitoring, alerts and retries. This would allow instant notifications upon failures and help prevent out of date data. 

### Getting Started

1. Setup virtualenv with Python 3
2. Install dependencies from requirements.txt
3. Run from CLI with python app.py command
