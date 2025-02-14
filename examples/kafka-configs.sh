{
  "name": "kafka-configs",
  "version": "unknown",
  "usage": [
    "kafka-configs.sh [options]"
  ],
  "description": "This tool helps to manipulate and describe entity config for a topic, client, user, broker, IP, or client-metrics.",
  "options": [
    {
      "option": "--add-config",
      "value": "<String>",
      "description": "Key-value pairs of configs to add. Use square brackets to group values containing commas."
    },
    {
      "option": "--add-config-file",
      "value": "<String>",
      "description": "Path to a properties file with configs to add."
    },
    {
      "option": "--all",
      "description": "List all configs for the given topic, broker, or broker-logger entity."
    },
    {
      "option": "--alter",
      "description": "Alter the configuration for the entity."
    },
    {
      "option": "--bootstrap-controller",
      "value": "<String>",
      "description": "The Kafka controllers to connect to."
    },
    {
      "option": "--bootstrap-server",
      "value": "<String>",
      "description": "The Kafka servers to connect to."
    },
    {
      "option": "--broker",
      "value": "<String>",
      "description": "The broker's ID."
    },
    {
      "option": "--broker-defaults",
      "description": "The config defaults for all brokers."
    },
    {
      "option": "--broker-logger",
      "value": "<String>",
      "description": "The broker's ID for its logger config."
    },
    {
      "option": "--client",
      "value": "<String>",
      "description": "The client's ID."
    },
    {
      "option": "--client-defaults",
      "description": "The config defaults for all clients."
    },
    {
      "option": "--command-config",
      "value": "<String>",
      "description": "Property file containing configs to be passed to Admin Client."
    },
    {
      "option": "--delete-config",
      "value": "<String>",
      "description": "Config keys to remove in the format 'k1,k2'."
    },
    {
      "option": "--describe",
      "description": "List configs for the given entity."
    },
    {
      "option": "--entity-default",
      "description": "Default entity name for clients/users/brokers/ips."
    },
    {
      "option": "--entity-name",
      "value": "<String>",
      "description": "Name of the entity (topic name, client ID, user principal name, broker ID, IP, client metrics)."
    },
    {
      "option": "--entity-type",
      "value": "<String>",
      "description": "Type of entity (topics, clients, users, brokers, broker-loggers, ips, client-metrics)."
    },
    {
      "option": "--force",
      "description": "Suppress console prompts."
    },
    {
      "option": "--help",
      "description": "Print usage information."
    },
    {
      "option": "--ip",
      "value": "<String>",
      "description": "The IP address."
    },
    {
      "option": "--ip-defaults",
      "description": "The config defaults for all IPs."
    },
    {
      "option": "--topic",
      "value": "<String>",
      "description": "The topic's name."
    },
    {
      "option": "--user",
      "value": "<String>",
      "description": "The user's principal name."
    },
    {
      "option": "--user-defaults",
      "description": "The config defaults for all users."
    },
    {
      "option": "--version",
      "description": "Display Kafka version."
    },
    {
      "option": "--zk-tls-config-file",
      "value": "<String>",
      "description": "Identifies the file where ZooKeeper client TLS connectivity properties are defined."
    },
    {
      "option": "--zookeeper",
      "value": "<String>",
      "description": "DEPRECATED. The connection string for the zookeeper connection in the form host:port."
    }
  ]
}
