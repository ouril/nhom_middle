from rest_framework.exceptions import APIException


class BadSendPaymentRequest(APIException):
    status_code = 400
    default_detail = 'bad params in json'
