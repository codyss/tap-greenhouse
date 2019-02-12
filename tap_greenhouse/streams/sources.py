from tap_kit.streams import Stream


class SourcesStream(Stream):

    stream = 'sources'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='full',
        selected_by_default=False
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
    "type": {
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
        }
      }
    }
  }
}

