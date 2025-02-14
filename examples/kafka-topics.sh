{
  "name": "kafka-topics",
  "version": "3.9.0",
  "usage": [
    "kafka-topics.sh [options]"
  ],
  "description": "This tool helps to create, delete, describe, or change a topic.",
  "options": [
    {
      "option": "--alter",
      "description": "Alter the number of partitions and replica assignment."
    },
    {
      "option": "--at-min-isr-partitions",
      "description": "Only show partitions whose ISR count is equal to the configured minimum."
    },
    {
      "option": "--bootstrap-server",
      "value": "<String: server to connect to>",
      "description": "REQUIRED: The Kafka server to connect to."
    },
    {
      "option": "--command-config",
      "value": "<String: command config property file>",
      "description": "Property file containing configs to be passed to Admin Client."
    },
    {
      "option": "--config",
      "value": "<String: name=value>",
      "description": "A topic configuration override for the topic being created."
    },
    {
      "option": "--create",
      "description": "Create a new topic."
    },
    {
      "option": "--delete",
      "description": "Delete a topic."
    },
    {
      "option": "--delete-config",
      "value": "<String: name>",
      "description": "A topic configuration override to be removed for an existing topic."
    },
    {
      "option": "--describe",
      "description": "List details for the given topics."
    },
    {
      "option": "--exclude-internal",
      "description": "Exclude internal topics when running list or describe command."
    },
    {
      "option": "--help",
      "description": "Print usage information."
    },
    {
      "option": "--if-exists",
      "description": "Execute action only if the topic exists when altering, deleting, or describing."
    },
    {
      "option": "--if-not-exists",
      "description": "Execute action only if the topic does not already exist when creating."
    },
    {
      "option": "--list",
      "description": "List all available topics."
    },
    {
      "option": "--partition-size-limit-per-response",
      "value": "<Integer: maximum number of partitions in one response>",
      "description": "The maximum partition size to be included in one DescribeTopicPartitions response."
    },
    {
      "option": "--partitions",
      "value": "<Integer: # of partitions>",
      "description": "The number of partitions for the topic being created or altered."
    },
    {
      "option": "--replica-assignment",
      "value": "<String: broker_id_for_part1_replica1 : broker_id_for_part1_replica2, ...>",
      "description": "A list of manual partition-to-broker assignments for the topic being created or altered."
    },
    {
      "option": "--replication-factor",
      "value": "<Integer: replication factor>",
      "description": "The replication factor for each partition in the topic being created."
    },
    {
      "option": "--topic",
      "value": "<String: topic>",
      "description": "The topic to create, alter, describe, or delete."
    },
    {
      "option": "--topic-id",
      "value": "<String: topic-id>",
      "description": "The topic ID to describe."
    },
    {
      "option": "--topics-with-overrides",
      "description": "Only show topics that have overridden configs when describing topics."
    },
    {
      "option": "--unavailable-partitions",
      "description": "Only show partitions whose leader is not available when describing topics."
    },
    {
      "option": "--under-min-isr-partitions",
      "description": "Only show partitions whose ISR count is less than the configured minimum."
    },
    {
      "option": "--under-replicated-partitions",
      "description": "Only show under-replicated partitions when describing topics."
    },
    {
      "option": "--version",
      "description": "Display Kafka version."
    }
  ]
}
