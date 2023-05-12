# Python3-dummy

Flask app that returns a json with the aws identity caller.

## Example response

- `/`
```=json
{
  "identity_caller": {
    "Account": "111111111",
    "Arn": "arn:aws:iam::111111111:user/foo.var",
    "ResponseMetadata": {
      "HTTPHeaders": {
        "content-length": "409",
        "content-type": "text/xml",
        "date": "Fri, 12 May 2023 22:22:26 GMT",
        "x-amzn-requestid": "234v23sdfg-1d14-442b-95e5-adec67742dab"
      },
      "HTTPStatusCode": 200,
      "RequestId": "234v23sdfg-1d14-442b-95e5-adec67742dab",
      "RetryAttempts": 0
    },
    "UserId": "C4NTH1SB3AR34LUS3R1D"
  }
}
```