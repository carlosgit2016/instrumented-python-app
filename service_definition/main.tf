resource "datadog_service_definition_yaml" "service_definition" {
  service_definition = file("${path.module}/definition.yml")
}