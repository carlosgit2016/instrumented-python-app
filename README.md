## Instrumented python app POC

Contain a sample App that can be used to generate logs for datadog sending the traces through the datadog agent

This repository contains a `python app` and a `datadog agent`

### Pre requisites
- pipenv
- python
- docker engine
- docker-compose
- Replace `DD_API_KEY` with the desired datadog api key
- Replace `DD_SERVICE` with the desired service name, must be unique

### Execute the project
```bash
docker-compose up
# Wait for python app and datadog agent
```

### Test the service
```bash
while true; do curl -Ls localhost:8181 && sleep 5; done;
```

Datadog agent will send traces to datadog

```bash
# Examples of logs being sent from dd agent
instrumented-python-app-ddagent-1     | 2022-09-29 17:28:34 UTC | TRACE | INFO | (run.go:254 in Infof) | [lang:python lang_version:3.9.2 interpreter:CPython tracer_version:1.5.0 endpoint_version:v0.4] -> traces received: 12, traces filtered: 0, traces amount: 20578 bytes, events extracted: 0, events sampled: 0
```

### Datadog APM service list

In datadog service list you must be able to see the service name that was defined in `DD_SERVICE` environment variable in `docker-compose.yml`.

### Service catalog register

In `./service_definition`

> Note `dd-service` in service_definition/definition.yml must match with the desired dd service name

Define environment variables `DD_API_KEY` `DD_HOST` `DD_APP_KEY` before applying the service catalog definition

If necessary generate a new API_KET and APP_KEY in datadog

```bash
terraform init
terraform plan
terraform apply
```

After approving you must be able to see the service definitions in datadog

### Service definition management through API

How to push a service definition
```bash
curl --request POST 'https://api.datadoghq.com/api/v2/services/definitions' \
--header 'DD-API-KEY: <API_KEY>' \
--header 'DD-APPLICATION-KEY: <APPLICATION_KEY>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "schema-version": "v2",
  "dd-service": "shopping-service"
}'
```

How to get a service definition
```bash
$DD_SERVICE="myservice"
curl --request GET "https://api.datadoghq.com/api/unstable/services/definition/$DD_SERVICE?schema_version=\"v2\"" \
--header 'DD-API-KEY: {API_KEY}' \
--header 'DD-APPLICATION-KEY: {APPLICATION_KEY}' 
```

Query all services definitions
```bash
curl --location --request GET 'https://api.datadoghq.com/api/v2/services/definitions' \
--header 'DD-API-KEY: <API_KEY>' \
--header 'DD-APPLICATION-KEY: <APPLICATION_KEY>' 
```