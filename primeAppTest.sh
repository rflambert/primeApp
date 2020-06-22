#!bin/bash
#Run this after starting the server at 0.1, 0.3, and 0.05 CPUs (web service) to produce logs for each

../jmeter/bin/jmeter -n -t Scenario1-300.jmx -l Log-Scenario1-300.jtl
../jmeter/bin/jmeter -n -t Scenario1-1000.jmx -l Log-Scenario1-1000.jtl
../jmeter/bin/jmeter -n -t Scenario1-5000.jmx -l Log-Scenario1-5000.jtl
../jmeter/bin/jmeter -n -t Scenario2-300.jmx -l Log-Scenario2-300.jtl
../jmeter/bin/jmeter -n -t Scenario2-1000.jmx -l Log-Scenario2-1000.jtl
../jmeter/bin/jmeter -n -t Scenario2-5000.jmx -l Log-Scenario2-5000.jtl
