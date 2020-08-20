def config():
    return {
        "test_name": "test_sync",
        "tap_name": "tap-ms-teams",
        "type": "platform.ms_teams",
        "properties": {
            "start_date": "TAP_MS_TEAMS_START_DATE",
            "tenant_id": "TAP_MS_TEAMS_TENANT_ID",
            "client_id": "TAP_MS_TEAMS_CLIENT_ID",
        },
        "credentials": {
            "client_secret": "TAP_MS_TEAMS_CLIENT_SECRET"
        },
        "bookmark": {
            "bookmark_key": "team_drives",
            "bookmark_timestamp": "2020-08-17T19:04:22.000000Z"
        },
        "streams": {
            "users": {"id"},
            "groups": {"id"},
            "group_members": {"id"},
            "group_owners": {"id"},
            "team_drives": {"id"},
            "channels": {"id"},
            "channel_members": {"id"},
            "channel_tabs": {"id"},
            "channel_messages": {"id"},
            "channel_message_replies": {"id"},
            "conversations": {"id"},
            "conversation_threads": {"id"},
            "conversation_posts": {"id", "change_key"},
            "team_device_usage_report": {"user_principal_name", "report_refresh_date"}
        },
        "exclude_streams": [
            "team_device_usage_report"
        ]
    }
