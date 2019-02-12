from tap_kit.streams import Stream


class ApplicationsStream(Stream):

    stream = 'applications'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='last_activity_at',
        valid_replication_keys=['last_activity_at'],
        incremental_search_key='last_activity_after',
        replication_method='incremental',
        selected_by_default=False
    )
    schema = \
{
    "properties": {
        "id": {
            "type": "integer"
        },
        "candidate_id": {
            "type": ["null", "integer"]
        },
        "prospect": {
            "type": ["null", "integer"]
        },
        "applied_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
        },
        "rejected_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time",
        },
        "last_activity_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time",
        },
        "location": {
            "properties": {
            }
        },
        "source": {
            "properties": {
            }
        },
        "credited_to": {
            "properties": {
            }
        },
        "rejection_reason": {
            "properties": {
            }
        },
        "rejection_details": {
            "properties": {
            }
        },
        "jobs": {
            "type": ["null", "array"]
        },
        "status": {
            "type": ["null", "sting"]
        },
        "current_stage": {
            "properties": {}
        },
        "answers": {
            "type": ["null", "array"]
        },
        "prospect_detail": {
            "properties": {}
        },
        "custom_fields": {
            "properties": {}
        },
        "keyed_custom_fields": {
            "properties": {}
        }
    }
}
