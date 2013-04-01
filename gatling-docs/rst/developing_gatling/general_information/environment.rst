.. _dev-environment:

#######################
Development Environment
#######################

As we chose to push Gatling on Github, it is likely that other people will want to see how we did it, and hopefully help us; the aim of this page is to ease the "get-into-developing-gatling" process.
To know how you can contribute to Gatling, visit :ref:`contributing`.

Software Requirements
=====================

* Java Development Kit 7.
* Git 1.7 or later.
* Eclipse 3.7 (Indigo) or 4.2 (Juno).
* `Scala IDE plugin <http://scala-ide.org>`_ You'll have to grab the nightly builds in running on Juno.
* Maven Integration for Eclipse Plugin : Juno Update Site > Collaboration > m2e
* Maven Integration for Scala Plugin. Update Site: http://alchim31.free.fr/m2e-scala/update-site

Importing Project into Eclipse
==============================

Once every software is installed, you can import Gatling project into Eclipse. Doing so is really easy:

1. Open Eclipse
2. Click on File > Import... > Maven > Existing Maven Project
3. Select gatling folder
4. Finish the import
5. Repeat the process for `gatling-highcharts <https://github.com/excilys/gatling-highcharts>`_
6. All Done !

Getting Gatling to run in Eclipse
=================================

Gatling is made to run as a standalone program, thus most users will want to download a tarball containing all the binaries required to execute Gatling.

As a developer, you'll want to run Gatling from Eclipse, sparing the long process of tarball creation. These are the steps required:

1. Build Gatling once via command line: ``mvn clean install``
2. Build Gatling-highcharts via command line: ``mvn clean install``
3. In Eclipse, create a new Maven project, from the archetype named ``gatling-highcharts-maven-archetype``
4. The created project should have all the gatling modules as dependencies.

  * If not, enable workspace resolution in the project's Maven configuration.

5. Now you can run Gatling via two files:

  * Engine.scala
  * Recorder.scala

6. Your project should now have the following structure :

.. image:: img/eclipse_archetype.png
  :alt: Archetype structure

Going further
=============

Another set of tools can be appreciated if you want to test things and, for example, package Gatling as an archive.

* `Scala <http://www.scala-lang.org/downloads>`_. Installing Scala on your computer will allow you to use the REPL. This is the Scala interpreter, you can use it to `test pieces <http://www.scala-lang.org/node/166>`_ of code and so on.
* `Maven <http://maven.apache.org/>`_. Having the maven integration plugin in Eclipse is enough to import the project and manage dependencies; but if you want to package Gatling or test that the *mvn clean install* process actually works, you'll need it installed on your computer as well.
* **Git tools**. To help you working with Git, you can use different software:

 * `EGit <http://eclipse.org/egit/>`_ is an integration of Git in Eclipse, it is included in Eclipse Juno's Update Site.
 * There are also tools from Github for `Windows <http://windows.github.com>`_ and `Mac OS X <http://mac.github.com>`_.