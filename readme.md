![Alt text](view.jpeg?raw=true "Title")

## Clean up
stop all containers
###### docker stop $(docker ps -a -q)
remove all containers
###### docker rm $(docker ps -a -q)
delete producer image
###### docker rmi <id>
delete web image
###### docker rmi <id>

## download code and run the containers
###### download code
###### download spark 2.4.8 from https://archive.apache.org/dist/spark/
###### update the location of spark in compose file "/Users/mubarak/Documents/Demos/spark248"
###### cd FraudAnalytics
###### docker-compose up

## run producer (on port 9000)
###### curl --header "Content-Type: application/json" --request POST --data "{\"transaction\":\"123\"}" http://localhost:9000/add

## see messages in kafka
###### docker images ps
###### docker exec -it 1c31511ce206 bash
###### /* list all topics */
###### kafka-topics.sh --bootstrap-server localhost:9092 --list
###### /* read */
###### kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic -from-beginning
###### /* if you want to write directly */
###### kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic
###### > {"transaction":"234"}
###### > {"transaction":"456"}
###### > ^c


## open zeppelin editor (on port 8080)
###### http://localhost:8080/

## configure Spark interpeter
###### org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.8 
###### mysql:mysql-connector-java:8.0.11

## in zeppelin editor install mysql connector 
###### %sh
###### pip install mysql-connector-python

## run Spark job
###### copy StreamJob.py code to the editor
###### run code

## check data in SQL
###### docker exec -it id /bin/bash
###### mysql -u[username] -p[password]
###### mysql -uroot -pabc
###### mysql> use FRAUDSDB;
###### mysql> select * from fraudtrans;


## see output in web App (on port 8000)
###### http://localhost:8000
###### configure llm key
###### run query "show all frauds"

## data
- Timestamp: This column records the date and time when the transaction occurred. It helps in understanding the temporal aspect of transactions, such as patterns over time, frequency, and clustering of activities.

- TransactionID: An identification number assigned to each transaction. It serves as a unique identifier for referencing or tracking specific transactions.

- AccountID: This field represents the unique identifier associated with the bank account involved in the transaction. It links multiple transactions to a specific account, enabling analysis on a per-account basis.

- Amount: The monetary value involved in the transaction. This column provides information about the financial magnitude of each transaction, which is crucial for anomaly detection since unusually high or low values might signify irregularities.

- Merchant: Specifies the entity or business involved in the transaction. This information helps in categorizing transactions (e.g., retail, online, restaurant) and identifying patterns related to specific merchants.

- TransactionType: Describes the nature or category of the transaction, whether it's a withdrawal, deposit, transfer, payment, etc. This column helps in understanding the purpose or direction of the transaction.

- Location: Indicates the place where the transaction occurred. It could be a physical location (e.g., city, country) or an identifier (e.g., store code, online portal), aiding in analyzing geographical spending patterns or detecting anomalies based on unusual transaction locations.

###### https://www.kaggle.com/datasets/devondev/financial-anomaly-data/data?select=financial_anomaly_data.csv

