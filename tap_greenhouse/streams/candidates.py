from ..tap_kit.streams import Stream


class CandidatesStream(Stream):

    stream = 'candidates'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='updated_at',
        valid_replication_keys=['updated_at', 'created_at'],
        incremental_search_key='updated_after',
        replication_method='incremental',
        selected_by_default=False
    )
    schema = \
{
    "properties": {
        "id": {
            "type": "integer"
        },
        "first_name": {
            "type": ["null", "string"]
        },
        "last_name": {
            "type": ["null", "string"]
        },
        "company": {
            "type": ["null", "string"]
        },
        "title": {
            "type": ["null", "string"]
        },
        "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
        },
        "updated_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time"
        },
        "last_activity_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time"
        },
        "is_private": {
            "type": ["null", "boolean"]
        },
        "photo_url": {
            "type": ["null", "string"]
        },
        "attachments": {
            "type": ["null", "array"]
        },
        "application_ids": {
            "type": ["null", "array"]
        },
        "phone_numbers": {
            "type": ["null", "array"]
        },
        "addresses": {
            "type": ["null", "array"]
        },
        "email_addresses": {
            "type": ["null", "array"]
        },
        "website_addresses": {
            "type": ["null", "array"]
        },
        "social_media_addresses": {
            "type": ["null", "array"]
        },
        "recruiter": {
            "properties": {
            }
        },
        "applications": {
            "type": ["null", "array"]
        },
        "tags": {
            "type": ["null", "array"]
        },
        "educations": {
            "type": ["null", "array"]
        },
        "employments": {
            "type": ["null", "array"]
        },
        "custom_fields": {
            "properties": {
            }
        },
        "keyed_custom_fields": {
            "properties": {
            }
        }
    }
}
