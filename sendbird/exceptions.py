class SendbirdException(Exception):
    status_code = 502
    default_detail = "External API unavailable, try again later"
    default_code = "sendbird_unavailable"

    def __init__(self, error_response):
        super().__init__(detail=error_response["message"], code=error_response["code"])


# Sendbird Error Codes
# docs: https://sendbird.com/docs/chat/v3/platform-api/guides/error-codes
UNEXPECTED_PARAMETER_TYPE = 400100
RESOURCE_ALREADY_EXISTS = 400202
