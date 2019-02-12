from tap_kit.streams import Stream


class JobStagesStream(Stream):

    stream = 'jobstages'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='updated_at',
        valid_replication_keys=['updated_at'],
        incremental_search_key='updated_after',
        replication_method='incremental',
        selected_by_default=False,
        api_path='job_stages',
    )
    schema = \
{
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
    "name": {
      "type": [
        "null",
        "string"
      ]
    },
    "created_at": {
      "type": [
        "null",
        "string"
      ]
    },
    "updated_at": {
      "type": [
        "null",
        "string"
      ]
    },
    "job_id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "interviews": {
      "type": [
        "null",
        "array"
      ],
      "items": {
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
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "interview_kit": {
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
              "content": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          }
        }
      }
    }
  }
}

