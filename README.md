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
