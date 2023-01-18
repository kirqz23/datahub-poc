# How to use
Make sure you have docker installed.

### Install datahub
```
python3 -m pip install --upgrade acryl-datahub
```

### Start datahub instance
```
datahub docker quickstart [--version TEXT (e.g. "v0.9.2")]
```

### Load sample data
```
datahub docker ingest-sample-data
```

### Start local airflow
Go to local_airflow directory and run
```
 docker-compose -f docker-compose.yml up -d
```

### Start local kafka (optional) if you want to test kafka ingestion to DataHub
Go to local_kafka directory and run
```
 docker-compose -f docker-compose.yml up -d
```

### Ingest local kafka (optional) if you want to test kafka ingestion to DataHub
Go to local_datahub/recipes
```
datahub ingest -c kafka_test_recipe.dhub.yaml
```

### Sending ethereum transactions to local kafka (optional) if you want to test kafka ingestion to DataHub
Go to scripts and run
```
python3 eth_tx.py
```

# Useful scripts
### List kafka topics
```
docker exec kafka_test_broker \
kafka-topics --bootstrap-server kafka_test_broker:49816 \
                       --list
```

### Read messages from a topic
``` 
docker exec --interactive --tty kafka_test_broker \
kafka-console-consumer --bootstrap-server kafka_test_broker:49816 \
                       --topic transaction \
                       --from-beginning
```
