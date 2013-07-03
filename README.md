Compi
=====

A Flask-based API and client solution for centralised monitoring of Linux servers

Requirements
------------

- [Flask](http://flask.pocoo.org/ "Flask")

Components
----------

The compi monitoring system consists of two components:
- **The server** runs on the monitoring server, and provides the RESTful API used by the monitored machines. It also generates and serves the MRTG graphs for each monitored machine.
- **The client(s)** run on the machines to be monitored, and update the server metrics at regular intervals.



