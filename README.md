# CLI Parser

A tool to recursively parse CLI commands, subcommands and associated program options from unstructured help text and extract them into a structured JSON object.

<p><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXc3Nmk0YWN1MDlqZzA2aG05Ym5idGlqdWI3MmxpcmN5MHVzMDAxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/w9Sb2fZrLPxHUFxLV2/giphy.webp" alt="ansible logo" title="ansible" align="center" height="200" /></p>

## Example Usage
`OPENAI_API_KEY=xxxxxxxxxxxxxx python src/parser.py netstat`

## Output Schema
```
{
  "title": "CLI Command Output Schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "description": "The name of the CLI command or binary." },
    "version": { "type": "string", "description": "The version of the CLI command or binary." },
    "usage": {
      "type": "array",
      "description": "Usage strings for the CLI command or binary.",
      "items": { "type": "string" }
    },
    "subcommands": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string", "description": "Name of the subcommand." },
          "description": { "type": "string", "description": "Description of the subcommand." },
          "subcommands": { "$ref": "#/properties/subcommands" },  // Recursively defined structure
          "options": {
            "type": "array",
            "items": { "$ref": "#/properties/options/items" }  // Reuse option structure
          }
        },
        "required": ["name", "description"],
        "additionalProperties": false
      }
    },
    "options": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "option": { "type": "string", "description": "Option name prefixed with '--'." },
          "shortcut": { "type": "string", "description": "Option shortcut prefixed with '-'." },
          "description": { "type": "string", "description": "Description of the option." },
          "value": { "type": ["string", "null"], "description": "Optional value of the option (e.g., '<EPOCH>')." },
          "default": { "type": ["string", "null"], "description": "Default value of the option." },
          "section": { "type": ["string", "null"], "description": "Section to which the option belongs." }
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
  "description": "A command-line tool for displaying network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.",
  "usage": [
    "netstat [-vWeenNcCF] [<Af>] -r",
    "netstat {-V|--version|-h|--help}",
    "netstat [-vWnNcaeol] [<Socket> ...]",
    "netstat { [-vWeenNac] -i | [-cnNe] -M | -s [-6tuw] }"
  ],
  "options": [
    {
      "option": "--all",
      "shortcut": "-a",
      "description": "display all sockets (default: connected)"
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
      "description": "display Forwarding Information Base (default)"
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
      "option": "--numeric",
      "shortcut": "-n",
      "description": "don't resolve names"
    },
    {
      "option": "--numeric-hosts",
      "description": "don't resolve host names"
    },
    {
      "option": "--numeric-ports",
      "description": "don't resolve port names"
    },
    {
      "option": "--numeric-users",
      "description": "don't resolve user names"
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
      "description": "display version information"
    },
    {
      "option": "--wide",
      "shortcut": "-W",
      "description": "don't truncate IP addresses"
    },
    {
      "option": "--help",
      "shortcut": "-h",
      "description": "display this help and exit"
    }
  ],
  "subcommands": [],
  "version": "2.10-alpha"
}
```

See [Here](./examples/) for more program parsing examples.
