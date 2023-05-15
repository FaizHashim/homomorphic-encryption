# Modified Cloud Server

In this assignment, a model of the system is created, in which the Query User (QU), the Data Owner (DO)
and the Cloud Server (CS) are present. The communication between them is simulated with the help
of socket programming. This assignment is a basic introduction to socket programming in Python.

This is a modification of the first assignment. The `factor()` function from the SageMath library is used instead of manually calculating the divisors of the number received by the cloud server.

In order to simulate the system, simply run each of the files in separate terminals.

The command to run the Cloud server is:
```
python ./cloud_server/cs.py
```

The command to run the Data Owner server is:
```
python ./data_owner/do.py
```

The command to simulate the Query User is:
```
python ./query_user/qu.py
```