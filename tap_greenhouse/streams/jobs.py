from tap_kit.streams import Stream


class JobsStream(Stream):

    stream = 'jobs'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='created_at',
        valid_replication_keys=['created_at'],
        incremental_search_key='updated_after',
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
    "requisition_id": {
      "type": [
        "null",
        "string"
      ]
    },
    "notes": {
      "type": [
        "null"
      ]
    },
    "confidential": {
      "type": [
        "null",
        "boolean"
      ]
    },
    "status": {
      "type": [
        "null",
        "string"
      ]
    },
    "created_at": {
        "type": [
            "null",
            "string"
        ],
        "format": "date-time",
    },
    "opened_at": {
        "type": [
            "null",
            "string"
        ],
        "format": "date-time",
    },
    "closed_at": {
      "type": [
          "null",
          "string"
      ],
      "format": "date-time",
    },
    "departments": {
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
          "parent_id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "external_id": {
            "type": [
              "null",
              "integer"
            ]
          }
        }
      }
    },
    "offices": {
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
          "location": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "primary_contact_user_id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "parent_id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "external_id": {
            "type": [
              "null",
              "integer"
            ]
          }
        }
      }
    },
    "custom_fields": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "job_type": {
          "type": [
            "null",
            "string"
          ]
        },
        "salary": {
          "type": [
            "null",
            "string",
          ]
        },
        "bonus": {
          "type": [
            "null",
            "string",
          ]
        },
        "options": {
          "type": [
            "null"
          ]
        }
      }
    },
    "keyed_custom_fields": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "employment_type": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "name": {
              "type": [
                "null",
                "string"
              ]
            },
            "type": {
              "type": [
                "null",
                "string"
              ]
            },
            "value": {
              "type": [
                "null",
                "string"
              ]
            }
          }
        },
        "salary": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "name": {
              "type": [
                "null",
                "string"
              ]
            },
            "type": {
              "type": [
                "null",
                "string"
              ]
            },
            "value": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
              }
            }
          }
        },
        "bonus": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "name": {
              "type": [
                "null",
                "string"
              ]
            },
            "type": {
              "type": [
                "null",
                "string"
              ]
            },
            "value": {
              "type": [
                "null"
              ]
            }
          }
        },
        "options": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "name": {
              "type": [
                "null",
                "string"
              ]
            },
            "type": {
              "type": [
                "null",
                "string"
              ]
            },
            "value": {
              "type": [
                "null",
                "integer",
              ]
            }
          }
        }
      }
    },
    "openings": {
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
          "opening_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "status": {
            "type": [
              "null",
              "string"
            ]
          },
          "opened_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time",
        },
          "closed_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time",
        },
          "application_id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "close_reason": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
            }
          }
        }
      }
    }
  }
}


