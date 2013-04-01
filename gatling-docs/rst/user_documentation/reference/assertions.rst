.. _assertions:

##########
Assertions
##########

Set up
======

You need the following import in your Simulation (automatically added by
the Recorder)::

  import assertions._

Concepts
========

The Assertions API is used to verify that global statistics like
response time or number of failed requests matches expectations for a
whole simulation.

Assertions are registered for a simulation using the method
``assertThat``. For example::

  assertThat(
    global.responseTime.max.lessThan(50),
    global.successfulRequest.percent.greaterThan(95)
  )

This method takes as many assertions as you like.

The API provides a dedicated DSL for chaining the following steps :

1. defining the scope of the assertion
2. selecting the statistic
3. selecting the metric
4. defining the condition

All the assertions are evaluated after running the simulation. If at
least one assertion fails, the simulation fails.

Scope
=====

An assertion can test a statistic calculated from all requests or only a
part.

.. method:: global

  Use statistics calculated from all requests.

.. method:: details(path)

 Use statistics calculated from a group or a request. The path is defined
 like a Unix filesystem path. For example, to perform an assertions on
 the request ``Index`` in the group ``Search``, use::

   details("Search" / "Index")

More information on how to use groups [here](Structure-Elements#wiki-group).

.. todo:: fix cross-doc links when possible

Statistics
==========

.. method:: responseTime

 Target the reponse time in milliseconds.

.. method:: allRequests

 Target the number of requests.

.. method:: failedRequests

 Target the number of failed requests.

.. method:: successfulRequests

 Target the number of successful requests.

.. method:: requestsPerSec

 Target the rate of requests per second.

Selecting the metric 
====================

Applicable to response time
---------------------------

.. method:: min

 Perform the assertion on the minimum of the statistic.

.. method:: max

  Perform the assertion on the maximum of the statistic.

.. method:: mean

  Perform the assertion on the mean of the statistic.

.. method:: stdDev

  Perform the assertion on the standard deviation of the statistic.

.. method:: percentile1

  Perform the assertion on the first percentile of the statistic.

.. method:: percentile2

  Perform the assertion on the second percentile of the statistic.

Applicable to number of requests (all, failed or successful)
------------------------------------------------------------

.. method:: percent

 Use the value as a percentage between 0 and 100.

.. method:: count

   Perform the assertion directly on the count of requests.

Condition
=========

Conditions can be chained to apply several conditions on the same
statistic.

.. method:: lessThan(threshold)

 Check that the value of the statistic is less than the threshold.

.. method:: greaterThan(threshold)

 Check that the value of the statistic is greater than the threshold.

.. method:: between(thresholdMin, thresholdMax)

 Check that the value of the statistic is between two thresholds.

.. method:: is(value)

 Check that the value of the statistic is equal to the given value.

.. method:: in(sequence)

 Check that the value of statistic is in a sequence.

.. method:: assert(condition, message)

 Create a custom condition on the value of the statistic.

 The first argument is a function that take an Int (the value of the
 statistics) and return a Boolean which is the result of the assertion.

 The second argument is a function that take a String (the name of the
 statistic) and a Boolean (result of the assertion) and return a message
 that describes the assertion as a String.

 For example::

    assert(value => value % 2 == 0,(name, result) => name + " is even : " + result)

 This will assert that the value is even.

Putting it all together
-----------------------

To help you understand how to use assertions, here is a list of examples:

::

  assertThat(global.responseTime.max.lessThan(100))

Assert that the max response time of all requests is less than 100 ms.

::

  assertThat(details("Search" / "Index").failedRequests.percent.is(0))

Assert that the percentage of failed requests for the request named
``Index`` in the group ``Search`` is exacly 0 %.

::

  assertThat(details("Search").requestsPerSec.greaterThan(100).lessThan(1000))

Assert that the rate of requests per seconds for the group ``Search`` is
between 100 and 1000. This is the same as::

  assertThat(details("Search").requestsPerSec.between(100, 1000))

