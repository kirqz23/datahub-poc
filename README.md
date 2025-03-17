# DataHub PoC
This repository contains a Proof of Concept (PoC) for setting up and using DataHub, an open-source metadata platform for data discovery, management, and governance. The PoC demonstrates how to install and configure DataHub using Docker, load sample data, and optionally integrate with local Kafka and Airflow instances for data ingestion and processing.

## How to use
Before you start, ensure that your Docker daemon is running. You can verify this by running:

```sh
docker --version
```

If Docker is not installed, follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install it for your operating system.

Once Docker is installed and running, you can proceed with the steps below to set up and use DataHub.

### Requirements
- Docker
- Python 3

### Install
To install the required packages, run:
```sh
python3 -m pip install --upgrade -r requirements.txt
```

### Start DataHub instance
```sh
datahub docker quickstart [--version TEXT (e.g. "v0.9.2")]
```

### Load sample data
```sh
datahub docker ingest-sample-data
```

### Start local Airflow
Go to the `local_airflow` directory and run:
```sh
docker-compose -f docker-compose.yml up -d
```

### Start local Kafka (optional)
If you want to test Kafka ingestion to DataHub, go to the `local_kafka` directory and run:
```sh
docker-compose -f docker-compose.yml up -d
```

### Ingest local Kafka (optional)
If you want to test Kafka ingestion to DataHub, go to the `local_datahub/recipes` directory and run:
```sh
datahub ingest -c kafka_test_recipe.dhub.yaml
```

### Send Ethereum transactions to local Kafka (optional)
If you want to test Kafka ingestion to DataHub, go to the `scripts` directory and run:
```sh
python3 eth_tx.py
```

## Useful scripts

### List Kafka topics
```sh
docker exec kafka_test_broker \
kafka-topics --bootstrap-server kafka_test_broker:49816 \
             --list
```

### Read messages from a topic
```sh
docker exec --interactive --tty kafka_test_broker \
kafka-console-consumer --bootstrap-server kafka_test_broker:49816 \
                       --topic transaction \
                       --from-beginning
```
