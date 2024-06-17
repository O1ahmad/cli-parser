# CLI Parser

A tool to recursively parse CLI commands, subcommands and associated program options.

## Example Usage
`python cli-parser/cli_parser/parser-v3.py netstat`

## Output Schema
```
{
  "title": "CLI Command Output Schema",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the CLI command or binary."
    },
    "subcommands": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the subcommand."
          },
          "description": {
            "type": "string",
            "description": "Description of the subcommand."
          },
          "subcommands": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Name of nested subcommand."
                },
                "description": {
                  "type": "string",
                  "description": "Description of nested subcommand."
                },
                "subcommands": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {},  // Can recursively define structure here if needed
                    "additionalProperties": false
                  }
                },
                "options": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "option": {
                        "type": "string",
                        "description": "Option name prefixed with '--'."
                      },
                      "shortcut": {
                        "type": "string",
                        "description": "Option shortcut prefixed with '-'."
                      },
                      "description": {
                        "type": "string",
                        "description": "Description of the option."
                      },
                      "value": {
                        "type": ["string", "null"],
                        "description": "Optional value of the option (e.g., '<EPOCH>')."
                      },
                      "default": {
                        "type": ["string", "null"],
                        "description": "Default value of the option."
                      },
                      "section": {
                        "type": ["string", "null"],
                        "description": "Section to which the option belongs."
                      }
                    },
                    "required": ["option", "description"],
                    "additionalProperties": false
                  }
                }
              },
              "additionalProperties": false,
              "required": ["name", "description", "subcommands", "options"]
            }
          },
          "options": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "option": {
                  "type": "string",
                  "description": "Option name prefixed with '--'."
                },
                "shortcut": {
                  "type": "string",
                  "description": "Option shortcut prefixed with '-'."
                },
                "description": {
                  "type": "string",
                  "description": "Description of the option."
                },
                "value": {
                  "type": ["string", "null"],
                  "description": "Optional value of the option (e.g., '<EPOCH>')."
                },
                "default": {
                  "type": ["string", "null"],
                  "description": "Default value of the option."
                },
                "section": {
                  "type": ["string", "null"],
                  "description": "Section to which the option belongs."
                }
              },
              "required": ["option", "description"],
              "additionalProperties": false
            }
          }
        },
        "required": ["name", "description", "subcommands", "options"],
        "additionalProperties": false
      }
    },
    "options": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "option": {
            "type": "string",
            "description": "Option name prefixed with '--'."
          },
          "shortcut": {
            "type": "string",
            "description": "Option shortcut prefixed with '-'."
          },
          "description": {
            "type": "string",
            "description": "Description of the option."
          },
          "value": {
            "type": ["string", "null"],
            "description": "Optional value of the option (e.g., '<EPOCH>')."
          },
          "default": {
            "type": ["string", "null"],
            "description": "Default value of the option."
          },
          "section": {
            "type": ["string", "null"],
            "description": "Section to which the option belongs."
          }
        },
        "required": ["option", "description"],
        "additionalProperties": false
      }
    }
  },
  "required": ["name", "subcommands", "options"],
  "additionalProperties": false
}
```

## Example Output (netstat)
```
{
  "name": "netstat",
  "description": "Network statistics tool",
  "subcommands": [],
  "options": [
    {
      "option": "--all",
      "shortcut": "-a",
      "description": "display all sockets",
      "default": "connected"
    },
    {
      "option": "--cache",
      "shortcut": "-C",
      "description": "display routing cache instead of FIB"
    },
    {
      "option": "--continuous",
      "shortcut": "-c",
      "description": "continuous listing"
    },
    {
      "option": "--context",
      "shortcut": "-Z",
      "description": "display SELinux security context for sockets"
    },
    {
      "option": "--extend",
      "shortcut": "-e",
      "description": "display other/more information"
    },
    {
      "option": "--fib",
      "shortcut": "-F",
      "description": "display Forwarding Information Base",
      "default": ""
    },
    {
      "option": "--groups",
      "shortcut": "-g",
      "description": "display multicast group memberships"
    },
    {
      "option": "--interfaces",
      "shortcut": "-i",
      "description": "display interface table"
    },
    {
      "option": "--listening",
      "shortcut": "-l",
      "description": "display listening server sockets"
    },
    {
      "option": "--masquerade",
      "shortcut": "-M",
      "description": "display masqueraded connections"
    },
    {
      "option": "--numeric-hosts",
      "shortcut": "None",
      "description": "don\"t resolve host names"
    },
    {
      "option": "--numeric-ports",
      "shortcut": "None",
      "description": "don\"t resolve port names"
    },
    {
      "option": "--numeric-users",
      "shortcut": "None",
      "description": "don\"t resolve user names"
    },
    {
      "option": "--numeric",
      "shortcut": "-n",
      "description": "don\"t resolve names"
    },
    {
      "option": "--programs",
      "shortcut": "-p",
      "description": "display PID/Program name for sockets"
    },
    {
      "option": "--route",
      "shortcut": "-r",
      "description": "display routing table"
    },
    {
      "option": "--statistics",
      "shortcut": "-s",
      "description": "display networking statistics (like SNMP)"
    },
    {
      "option": "--symbolic",
      "shortcut": "-N",
      "description": "resolve hardware names"
    },
    {
      "option": "--timers",
      "shortcut": "-o",
      "description": "display timers"
    },
    {
      "option": "--verbose",
      "shortcut": "-v",
      "description": "be verbose"
    },
    {
      "option": "--version",
      "shortcut": "-V",
      "description": "show version information"
    },
    {
      "option": "--wide",
      "shortcut": "-W",
      "description": "don\"t truncate IP addresses"
    }
  ]
}
```
