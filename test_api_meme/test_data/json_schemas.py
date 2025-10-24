json_schema_get_memes = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "text": {"type": "string"},
        "url": {"type": "string", "format": "uri"},
        "tags": {
            "type": "array",
            "items": {"type": "string"}
        },
        "info": {"type": "object"}
    },
    "required": ["id", "text", "url", "tags", "info"],
    "additionalProperties": True
}

json_schema_get_meme_id = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "text": {
            "type": "string"
        },
        "url": {
            "type": "string"
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "info": {
            "type": "object"
        }
    },
    "required": ["text", "url", "tags", "info"],
    "additionalProperties": True
}

json_schema_post_meme = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "text": {
            "type": "string"
        },
        "url": {
            "type": "string"
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "info": {
            "type": "object"
        }
    },
    "required": ["id", "text", "url", "tags", "info"],
    "additionalProperties": True
}

json_schema_put_meme = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "text": {
            "type": "string"
        },
        "url": {
            "type": "string"
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "info": {
            "type": "object"
        }
    },
    "required": ["id", "text", "url", "tags", "info"],
    "additionalProperties": True
}
