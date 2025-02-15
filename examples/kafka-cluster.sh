{
    "name": "/home/ahmad/Downloads/kafka_2.13-3.9.0/bin/kafka-cluster.sh",
    "description": "The Kafka cluster tool.",
    "usage": "usage: kafka-cluster [-h] {cluster-id,unregister} ...",
    "subcommands": [
        {
            "name": "/home/ahmad/Downloads/kafka_2.13-3.9.0/bin/kafka-cluster.sh cluster-id",
            "description": "CLI tool for managing Kafka clusters.",
            "usage": "kafka-cluster cluster-id [-h] [--config CONFIG] (--bootstrap-server BOOTSTRAP_SERVER | --bootstrap-controller BOOTSTRAP_CONTROLLER)",
            "options": [
                {
                    "option": "--bootstrap-controller",
                    "shortcut": "-C",
                    "description": "A list of host/port pairs to use for establishing the connection to the KRaft controllers.",
                    "value": "BOOTSTRAP_CONTROLLER"
                },
                {
                    "option": "--bootstrap-server",
                    "shortcut": "-b",
                    "description": "A list of host/port pairs to use for establishing the connection to the Kafka cluster.",
                    "value": "BOOTSTRAP_SERVER"
                },
                {
                    "option": "--config",
                    "shortcut": "-c",
                    "description": "A property file containing configurations for the Admin client.",
                    "value": "CONFIG"
                },
                {
                    "option": "--help",
                    "shortcut": "-h",
                    "description": "show this help message and exit"
                }
            ],
            "subcommands": []
        },
        {
            "name": "/home/ahmad/Downloads/kafka_2.13-3.9.0/bin/kafka-cluster.sh unregister",
            "description": "Unregister a broker from the Kafka cluster.",
            "usage": "kafka-cluster unregister [-h] [--config CONFIG] --id ID (--bootstrap-server BOOTSTRAP_SERVER | --bootstrap-controller BOOTSTRAP_CONTROLLER)",
            "options": [
                {
                    "option": "--bootstrap-controller",
                    "shortcut": "-C",
                    "description": "A list of host/port pairs to use for establishing the connection to the KRaft controllers.",
                    "value": "BOOTSTRAP_CONTROLLER"
                },
                {
                    "option": "--bootstrap-server",
                    "shortcut": "-b",
                    "description": "A list of host/port pairs to use for establishing the connection to the Kafka cluster.",
                    "value": "BOOTSTRAP_SERVER"
                },
                {
                    "option": "--config",
                    "shortcut": "-c",
                    "description": "A property file containing configurations for the Admin client.",
                    "value": "CONFIG"
                },
                {
                    "option": "--help",
                    "shortcut": "-h",
                    "description": "Show this help message and exit."
                },
                {
                    "option": "--id",
                    "shortcut": "-i",
                    "description": "The ID of the broker to unregister.",
                    "value": "ID"
                }
            ],
            "subcommands": []
        }
    ],
    "options": [
        {
            "option": "--help",
            "shortcut": "-h",
            "description": "show this help message and exit"
        }
    ],
    "version": "3.9.0"
}
