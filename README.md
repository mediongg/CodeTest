## Prerequisite

1. The API server depends on python Flask. Run `pip3 install flask` to install the dependency.


## How to run the service

1. Run the following command to start flask server. It opens port at 127.0.0.1:5000

```bash
flask --app backend run
```

2. The server has two endpoints:
    1. GET / - This endpoint returns a simple webpage that allows you to call `/log` endpoint by passing 3 parameters - filename, entries and filter.
       ![output](https://github.com/user-attachments/assets/2749f9ec-b088-4b98-b30b-f9494410067e)
    2. GET /log - This endpoint allows you to view the log file under `/var/log` folder on the machine where the server is deployed.


## How to run test

```bash
python3 -m unittest tests.test_api tests.test_log_reader
```

1. test_api.py tests the error handling of the API
2. test_log_reader.py tests the funtionality of LogReader


## Caveats
Although the spec requires that the API returns the newest log entries first, however in some cases, a log entry may contain multiple lines. For example,

```
Aug 23 00:30:07 HOSTNAME syslogd[125]: Configuration Notice:
	ASL Module "com.apple.cdscheduler" claims selected messages.
	Those messages may not appear in standard system log files or in the ASL database.
```

The LogReader implementation tries to read from the last line to first line of the log by using `seek()`. It then delimits the log entries by newline character `\n`.
Therefore, the above example will become the following:

```
	Those messages may not appear in standard system log files or in the ASL database.
	ASL Module "com.apple.cdscheduler" claims selected messages.
Aug 23 00:30:07 HOSTNAME syslogd[125]: Configuration Notice:
```

### Suggestion

We could mimic the behaviour of `tail` command so we don't have the above problem.
