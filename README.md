# Python3-dummy

Flask app that returns a json with the aws identity caller.

## Prerequisites

- Python (version 3.6 or higher) installed
- AWS credentials properly configured if using the `/` endpoint

## Endpoints

The application provides the following endpoints:

- `/`: Returns the AWS caller identity information in JSON format.
- `/counter`: Returns the current count of requests made to the server.
- `/ping`: Returns "pong" as a response.
- `/switch`: Toggles the switch status between true and false, returning the updated status as a JSON response.
- `/liveness`: Returns a response indicating the liveness probe status (200 OK if the switch is true, otherwise 503 Service Unavailable).
- `/readiness`: Returns a response indicating the readiness probe status (200 OK if the switch is true, otherwise 503 Service Unavailable).

### Example response

- `/`
```=json
{
  "Account": "340604397924",
  "Arn": "arn:aws:iam::340604397924:user/agustin.lare",
  "UserId": "AIDAU6TM2VFSMWUNJZN5W"
}
```

## Configuration

No additional configuration is required to run the application. However, if you want to use the / endpoint to retrieve AWS caller identity information, ensure that your AWS credentials are properly configured.