from tap_kit.streams import Stream


class EEOCStream(Stream):

    stream = 'eeoc'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='submitted_at',
        valid_replication_keys=['submitted_at'],
        incremental_search_key='submitted_after',
        replication_method='incremental',
        selected_by_default=False
    )
    schema = \
{
  "type": [
    "null",
    "object"
  ],
  "properties": {
    "application_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "candidate_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "race": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "id": {
          "type": [
            "null",
            "integer"
          ]
        },
        "description": {
          "type": [
            "null",
            "string"
          ]
        }
      }
    },
    "gender": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "id": {
          "type": [
            "null",
            "integer"
          ]
        },
        "description": {
          "type": [
            "null",
            "string"
          ]
        }
      }
    },
    "veteran_status": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "id": {
          "type": [
            "null",
            "integer"
          ]
        },
        "description": {
          "type": [
            "null",
            "string"
          ]
        }
      }
    },
    "disability_status": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "id": {
          "type": [
            "null",
            "integer"
          ]
        },
        "description": {
          "type": [
            "null",
            "string"
          ]
        }
      }
    },
    "submitted_at": {
      "type": [
        "null",
        "string"
      ]
    }
  }
}


