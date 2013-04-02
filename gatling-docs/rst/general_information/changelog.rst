#########
Changelog
#########

:milestone:`v1.4.6 <34>`
========================

.. warning::
  Be aware of the 2 breaking changes:

  * Maven plugin property `simulation` renamed into `simulationClass`
  * JsonPath not longer supports attribute axis (didn't really make sense and was equivalent to child element one).

  See :ref:`Migration guide <1.4.6>` for more information.

Fixes
-----

* :issue:`1018` and :issue:`1019` Core: Possible race condition on initialization
* :issue:`1020` HTTP: Warm up done twice, slowing down start up
* :issue:`1037` Maven: Renaming property `simulation` into `simulationClass` in order to avoid clash when passing as System property
* :issue:`1042` Recorder: Invalid generated simulation when first element is a tag
* :issue:`1044` Maven: Fails when propagating a System property with a space

Features
--------

* :issue:`1046` Core: Drop attribute axis support in JsonPath, introduce magic value `_` to target root array

:milestone:`v1.4.5 <33>`
========================

Fixes
-----

* :issue:`995` and :issue:`1013` Core: Can't use assertions with "manual scaling" procedure, see :ref:`scaling-out`
* :issue:`1003` Maven: line.separator disappears when propagation System properties
* :issue:`1009` Core: config doesn't get overridden with System properties

Features
--------

* :issue:`1017` HTTP: Upgrade to `async-http-client 1.7.12 <https://github.com/AsyncHttpClient/async-http-client/issues?milestone=2&page=1&state=closed>`_

:milestone:`v1.4.4 <32>`
========================

Fixes
-----

* :issue:`971` Maven: Plugin broken, wrong Scala version resolved
* :issue:`974` HTTP: XPath and JsonPath checks crash on empty body
* :issue:`984` and :issue:`993` Charts: stats.tsv file broken

Features
--------

.. todo:: fix cross doc links when possible

* :issue:`906`, :issue:`911` and :issue:`972` Core: add new `foreach` DSL, see [doc](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-foreach)
* :issue:`960` Core: Make user ids unique
* :issue:`977` Maven: Propagate System properties in fork mode
* :issue:`983` Charts: Make Graphite root configurable, defaulting to gatling
* :issue:`996` HTTP: Make SslContext configurable

+ tons of optimizations, see full issues list for details

:milestone:`v1.4.3 <31>`
========================

Fixes
-----

* :issue:`914`, :issue:`915`, :issue:`918`, :issue:`919` Charts: Charts not rendering when request/group name contains special characters
* :issue:`922` Core: Fix pause shift computation
* :issue:`926` HTTP: Improve domain matching in cookie handling
* :issue:`942` Recorder: Handle poorly encoded queries
* :issue:`944` Core: NPE when running a simulation with 2 scenarios with the same name
* :issue:`954` and :issue:`956` HTTP: Filtered out multiple cookies with the same name/path (support PHP bug)

Features
--------

* :issue:`913` HTTP: Upgrade Netty 3.6.2
* :issue:`934` HTTP: Upgrade async-http-client 2.10
* :issue:`941` Core: Loops clean up
* :issue:`957` HTTP: Add Connection to possible common headers

:milestone:`v1.4.2 <30>`
========================

Fixes
-----

* :issue:`881` and :issue:`910` Core: Fix Zinc incremental compiler NPE
* :issue:`898` Charts: invalid group OK/KO stats
* :issue:`899` HTTP: Cookies are not propagated from HTTP to HTTPS
* :issue:`907` JDBC: JdbcFeeder SQLException with Oracle

:milestone:`v1.4.1 <29>`
========================

Fixes
-----

* :issue:`882` Core: Possible SOE when too many requests
* :issue:`884` Recorder: Not working with HTTPS
* :issue:`886` Charts: Wrong statistics for groups
* :issue:`893` Maven: reportsOnly not work with maven plugin

Features
--------

* :issue:`889` Core: Upgrade Scala 2.9.3-RC1
* :issue:`892` Core: Upgrade Akka 2.0.5
* :issue:`894` HTTP: Upgrade Netty 3.6.1

:milestone:`v1.4.0 <22>`
========================

.. warning::
  This release introduce a breaking change in the Simulation classes format. Deprecated methods in 1.3.X have been removed.

  See :ref:`Migration guide <1.4.0>` for more information.

Fixes
-----

* :issue:`844` Charts: Handle parentheses in request names
* :issue:`846` Core: Fix possible NPE in FileDataWriter.sanitize
* :issue:`866` :issue:`867` Charts: Fix stats.tsv file header, thanks to Pete Capra

Features
--------

* :issue:`170` :issue:`322` Charts: New API for grouping requests
* :issue:`560` Core: New API for acceptance criteria
* :issue:`594` Maven: New Jenkins plugin
* :issue:`772` Charts: Reorganize description
* :issue:`782` Core: 1.3.X deprecated APIs removed
* :issue:`788` :issue:`810` Core: Jackson fully configurable through gatling.conf
* :issue:`802` HTTP: Host header doesn't have to be specified as AHC computes it
* :issue:`829` Core: Feeder is now ``Iterator[Map[String, T]]``
* :issue:`832` Charts: Upgrade jQuery 1.8.3
* :issue:`838` :issue:`840` Core: Breaking change in Simulation structure: remove apply and configure, introduce setUp
* :issue:`839` Maven: maven plugin now use src/test/scala and src/test/resources folders
* :issue:`841` Core: New `.size` EL function
* :issue:`847` Core: Make extraResponseInfoExtractor take an ExtendedResponse
* :issue:`848` :issue:`879` HTTP: Better tracing/debugging of requests and responses
* :issue:`849` HTTP: Upgrade Netty 3.6.0.Final
* :issue:`857` Core: Stop engine nicely instead of System.exit on feeder starvation
* :issue:`860` Core: Upgrade Logback 1.0.9
* :issue:`861` Core: Upgrade Jackson 2.1.2
* :issue:`864` :issue:`872` Maven: maven-gatling-plugin refactoring
* :issue:`870` HTTP: Make fileBody dynamic
* :issue:`874` Core: Fix Zinc when Gatling path contains special characters
* :issue:`876` App: Rename deb package name into gatling-tool
* :issue:`877` HTTP: Upgrade AHC 1.7.9, fix bug when no headers
* :issue:`880` Charts: Upgrade Highcharts 2.3.5 and Highstock 1.2.5

:milestone:`v1.3.5 <28>`
========================

Fixes
-----

* :issue:`799` Maven: src/test/scala directory missing in projects generated with the archetype
* :issue:`800` Core: Fix debig logger in logback.xml
* :issue:`808` HTTP: Original ContentType header shouldn't be propagated when redirecting
* :issue:`813` HTTP: followRedirect not working properly when Location contains a query
* :issue:`816` HTTP: CookieStore not accounting for port number in domain computation
* :issue:`820` Core: JsonPath not supporting wildcards

Features
--------

* :issue:`765` and :issue:`814` HTTP: Print HTTP params in debug
* :issue:`792` Core: Make request names dynamic
* :issue:`817` HTTP: Authorization header can now be declared as a common header in HttpProtocolConfiguration
* :issue:`818` HTTP: Support for non UTF-8 encoded cookies (value containing an "=" character)

:milestone:`v1.3.4 <27>`
========================

Fixes
-----

* :issue:`785` Recorder: Fix followRedirect support
* :issue:`786` Core: Fix during loop timer
* :issue:`787` Core: Fix JsonPath

:milestone:`v1.3.3 <26>`
========================

Features
--------

* :issue:`754` Core: Use Zinc incremental compiler
* :issue:`763` and :issue:`769` Charts: Redesign statistic summary table
* :issue:`775` HTTP/Recorder: DNT common header support
* :issue:`779` Core: Loop index is now directly exposed as Session attribute

Fixes
-----

* :issue:`755` Charts: Square and curly braces in request names mess up with javascript
* :issue:`756` HTTP: Fix abusing caching
* :issue:`759` Core: Fix check when forcing Simulation
* :issue:`760` Maven: add missing logback.xml file
* :issue:`762` HTTP: Support Expires headers numerical values
* :issue:`766` Metrics: Max and count should be reseted along with the buckets
* :issue:`770` Charts: Run description is not properly printed
* :issue:`777` Core: Fix unrecoverable crash on while condition evaluation
* :issue:`778` Core: Counter should be incremented before the loop content
* :issue:`780` Recorder: Fix pauses shift

:milestone:`v1.3.2 <25>`
========================

Features
--------

* :issue:`750` HTTP: better support of multivalued params and queryParams with multiValuedParam and multiValueQueryParam, see :ref:`query_params`

Fixes
-----

* :issue:`753` HTTP: regression: params were being sent as query params

:milestone:`v1.3.1 <24>`
========================

Features
--------

.. todo :: fix cross docs links when possible

* :issue:`743` Checks: Add new bodyString check, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-responseBody)
* :issue:`744` HTTP: Upgrade Netty to 3.5.8.Final, critical performance fixes
* :issue:`752` Config: Add aliases for built-ins data readers and writers: console, file and graphite

Fixes
-----

* :issue:`732` HTTP: responseChunksDiscardingEnabled was not working properly
* :issue:`734` HTTP: Host header was being ignored, fixed thanks to @dustinbarnes
* :issue:`735` Core: NPE when using chain
* :issue:`736` Charts: Drop Scalding/Cascading, considerably reduce memory footprint, introduce accuracy config parameter defaulting to 10ms
* :issue:`745` Recorder: Tags were not dumped in the generated Simulation
* :issue:`747` Charts: Some charts disappear. This is due to a Highstock bug that has been fixed yet, so a workaround was introduced
* :issue:`751` Feeders and Charts: File streams were not properly closed

>_Note_: Due to the new accuracy parameter, you will experience less precise values in the charts. You can get the old behavior by setting a 1 ms value, at the cost of a higher memory usage.

:milestone:`v1.3.0 <20>`
========================

.. warning::
  Migration required, see :ref:`Migration guide <1.3.0>` for more information.

API changes
-----------

* :issue:`669` Core: Config file format change
* :issue:`698` Core: Durations expressed as (value, unit) are deprecated
* :issue:`699` Core: Loops refactoring, old ones are deprecated
* :issue:`705` Core: insertChain deprecated, use exec
* :issue:`711` Core: Feeders are now Iterators
* :issue:`730` Core: doIf refactoring

Features
--------

.. todo:: fix cross doc links when possible (x9)

* :issue:`592` Charts: Display mean number of requests/sec in global chart page
* :issue:`593` Charts: Generate a csv file with global stats
* :issue:`604` and :issue:`672` Charts: Response time and latency charts now display (min, max) ranges instead of a max values line
* :issue:`606` HTTP: New byteArrayBody(Session => Array[Byte]), see :ref:`documentation <byteArrayBody>`
* :issue:`607` HTTP: New baseUrls for round-robin, thanks to @israel, see :ref:`documentation <base-url>`
* :issue:`607` and :issue:`683` Charts: New summary table on global page
* :issue:`621` Checks: Css checks underlying parser now supports browser conditional tests
* :issue:`623` HTTP: New caching support, see :ref:`documentation <caching>`
* :issue:`624` Core: New console dashboard
* :issue:`627` Checks: New currentLocation check, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-location)
* :issue:`628` Core: New pauseCustom(() => Long), see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-pause)
* :issue:`641` and :issue:`658` HTTP: Log requests and responses on failure
* :issue:`644` HTTP: paramKey and fileName upload parameters are now dynamic
* :issue:`646` HTTP: Multi file upload support, thanks to @codemnky
* :issue:`647` and :issue:`690` Core: New randomSwitch, see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-randomSwitch)
* :issue:`652` HTTP: New disableResponseChunksDiscarding, see :ref:`documentation <custom-dump>`
* :issue:`652` Checks: Css checks now support attribute node selection, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-css)
* :issue:`674` and :issue:`675` Graphite: Gatling can now report to Graphite, see wiki
* :issue:`685` Project: Continuous Integration now on Cloudbees
* :issue:`688` Charts: New polar chart with request counts
* :issue:`701` Core: New exitBlockOnFail and exitHereIfFailed, see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-exitBlockOnFail)
* :issue:`702` Core: New tryMax, see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-tryMax)
* :issue:`703` Core: Remove bootstrapping from chain, see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-bootstrap)
* :issue:`706` Core: new randomRoundRobin, see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-roundRobinSwitch)
* :issue:`712` Core: Let exec take a chain vararg, see [wiki](https://github.com/excilys/gatling/wiki/Structure-Elements#wiki-exec)
* :issue:`714` Core: Better simulations compilation warnings

Fixes
-----

* :issue:`571` HTTP: Better cookies support
* :issue:`609` HTTP: NPE when Location header missing
* :issue:`615` HTTP: Url is encoded twice on redirect
* :issue:`630` Charts: Fix percentiles
* :issue:`639` and :issue:`687` Recorder: should ask before overwriting
* :issue:`651` Check: responseTime and latency checks mustn't cause body to be stored
* :issue:`653` HTTP: Duration computation problems
* :issue:`664` Core: Don't display Abstract simulations
* :issue:`665` Core: LinkageError when using inheritance
* :issue:`709` Recorder: support empty valued parameters
* :issue:`713` and :issue:`715` Charts: support quotes in request names


:milestone:`v1.2.5 <21>`
========================

Features
--------

* :issue:`596` Better live informations

Fixes
-----

* :issue:`597` Fix cookie handling regression
* :issue:`599` Time measurement is intrinsically imprecise, ensure that it can't cause negative response times
* :issue:`600` Fix response time distribution chart, max value wasn't properly displayed
* :issue:`601` Fix gatling-maven-plugin JVM arguments

:milestone:`v1.2.4 <16>`
========================

Features
--------

.. todo:: fix cross docs links when possible (x4)

* :issue:`446` Add the ability to dump custom data in the logs, thanks to Stephen Kuenzli, see :ref:`documentation <custom-dump>`
* :issue:`569` New reponseTimeInMillis and latencyInMillis checks, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-response-time)
* :issue:`576` new headerRegex check, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-header-regex)
* :issue:`591` Location header is now automatically decoded when checked, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-header)
* :issue:`595` New simple feeder, see [wiki](https://github.com/excilys/gatling/wiki/Feeders#wiki-simple)

Fixes
-----

* :issue:`572` Fix a bug where cookies with the same name could be sent both under certain conditions
* :issue:`573` Fix script variables scope under Windows, thanks to Henri Tremblay
* :issue:`574` Fix logger in logback.conf, thanks to Henri Tremblay
* :issue:`583` Fix engine encoding handling
* :issue:`586` Fix recorder class name and package generation
* :issue:`587` Fix recorder encoding handling

:milestone:`v1.2.3 <15>`
========================

Fixes
-----

* :issue:`566` Fix body checks regression in 1.2.2

:milestone:`v1.2.2 <14>`
========================

.. warning::
  due to :issue:`566`, 1.2.2 users are recommended to upgrade to 1.2.3

Features
--------

.. todo:: fix cross doc links when possible (x2)

* :issue:`543` Make charts generation consume multiple simulation(.*).log files, ease multiple instances testing, see :ref:`documentation <scaling-out>`
* :issue:`548` New `Redis <http://redis.io>`_ Feeder, thanks to @krishnenc (Krishnen Chedambarum), see [wiki](https://github.com/excilys/gatling/wiki/Feeders#wiki-redis)
* :issue:`548` New byteArrayBody, thanks to @krishnenc (Krishnen Chedambarum), see :ref:`documentation <request-body>`
* :issue:`552` Gatling modules can now be built independantly, thanks to @nire (Nicolas Rémond)
* :issue:`553` New checksum checks, see [wiki](https://github.com/excilys/gatling/wiki/Checks#wiki-checksum)
* :issue:`555` Run name can now be set on gatling-maven-plugin, see :ref:`documentation <advanced>`
* :issue:`557` Gatling now ships `Grizzly <http://grizzly.java.net>`_ to ease switching NIO provider (Gatling still uses Netty by default)

Fixes
-----

* :issue:`562` Fix gatling-maven-plugin crash when setting no-reports or run-name options, thanks to @skuenzli (Stephen Kuenzli)
* :issue:`558` Ensure IfAction and WhileAction don't lose messages on crash

:milestone:`v1.2.1 <13>`
========================

.. warning::
  Due to :issue:`545`, 1.2.0 users are highly recommended to upgrade!

Features
--------

* :issue:`539` much better reports generation memory footprint

Fixes
-----

* :issue:`536` HttpProtocolConfiguration DSL wouldn't compile when proxy was defined in the middle of the chain
* :issue:`537` Warm up request would break the run when target url cannot be reached
* :issue:`538` Fix scatter plot chart
* :issue:`540` Fix percentile ordinal suffix, thanks to Nicolas Rémond
* :issue:`544` Fix times computation at very high throughput
* :issue:`545` Fix pause duration
* :issue:`546` Fix launch script when path contains special characters, thanks to Jean-François Bilger

:milestone:`v1.2.0 <6>`
=======================

.. warning::
  Migration required, see :ref:`Migration guide <1.2.0>` for more information.

Features
--------

* :issue:`376` loop times condition can now be dynamic
* :issue:`432` & :issue:`523` Referer header can now be automatically computed
* :issue:`435` & :issue:`518` CSS Selector extractors are now supported, thanks to Nicolas Rémond (@nire)
* :issue:`493` & :issue:`531` HEAD HTTP word is now supported, thanks to Nicolas Rémond (@nire)
* :issue:`501` Reports global page has been refactored
* :issue:`509` Recorder has been migrated to Scala
* :issue:`514` Common HTTP Headers can be configured on ProtocolConfiguration
* :issue:`522` Outgoing proxy credentials can now be configured in the Recorder
* :issue:`527` Percentiles have been reworked to make more sense
* :issue:`530` New exponentially distributed pauses, thanks to Stephen Kuenzli (@skuenzli)
* :issue:`532` Add automatic request to compensate for engine warm up
* :issue:`535` Calling check() several times will now append them instead of overriding them

Fixes
-----

* :issue:`512` & :issue:`528` Fix class name resolution in gatling-maven-plugin, thanks to Cyril Couturi (@ccouturi) and Stephen Kuenzli (@skuenzli)
* :issue:`520` Add protection from SimpleAction crashes
* :issue:`534` Handle empty lines in CSV files

:milestone:`v1.1.6 <12>`
========================

Fixes
-----

* :issue:`498` Recorder: fix NPE on request body
* :issue:`507` gatling-maven-plugin: fix simulation package on Windows
* :issue:`508` Charts: fix encoding
* :issue:`510` Recorder: fix request bodies folder name

:milestone:`v1.1.5 <11>`
========================

Fixes
-----

* :issue:`489` Make recorder use relative URIs once connection established
* :issue:`490` Handle 303 redirect status code
* :issue:`491` Fix status code check when using non default one
* :issue:`497` Fix reports when request name contains "'"
* :issue:`498` Fix NPE in recorder when dumping request bodies
* :issue:`499` Fix latency chart

Features
--------

* :issue:`484` - Remove check logic from the AHC handler in order to reduce pressure on IO threads
* :issue:`486` - Charts: all session series is computed once for all
* :issue:`492` - Add a "maybe" check strategy when one want to capture an optional value
* :issue:`500` - Document transactions/sec chart
* :issue:`502` - Expose AHC configuration in Gatling conf

:milestone:`v1.1.4 <10>`
========================

Fixes
-----

* :issue:`481` Fix http client start up
* :issue:`483` Fix multiple simulations launching

Features
--------

* :issue:`485` - Charts: add new response time distribution
* :issue:`487` - EL: let occurrence be dynamic

:milestone:`v1.1.3 <9>`
=======================

Fixes
-----

* :issue:`459` - Upgrade Netty 3.4.0.Final that fixes a compression bug.
* :issue:`460` - Fix recorder SSL certificate.
* :issue:`466` - Support relative Location headers
* :issue:`469` - Regression: the recorder shouldn't record Cookie and Content-Length headers
* :issue:`470` - Fix statistics displayed in the CLI while running

Features
--------

* :issue:`465` - Charts: display percentiles

:milestone:`v1.1.2 <8>`
=======================

Fixes
-----

* :issue:`450` - Properly fixes cookie expiration
* :issue:`453` - Make XPathExtractor threadsafe
* :issue:`455` - Fix global statistics

Features
--------

* :issue:`327` - Akka 2 migration, wouhou!!!

:milestone:`v1.1.1 <7>`
=======================

Fixes
-----

* :issue:`442` - Fixes fileBody templating
* :issue:`444` - Fixes cookie deletion

Features
--------

* :issue:`447` - Log at debug level the response on failed check

:milestone:`v1.1.0 <2>`
=======================

.. warning::
  Migration required, see :ref:`Migration guide <1.1.0>` for more information.

Features
--------

* Engine

  * configurable run id and run description, see :issue:`416`
  * periodic statistic display while running, see :issue:`384`
  * link to generated reports, see :issue:`383`

* Check API

  * Check API is now type safe
  * optional transform step on extraction result
  * new JSONPath, see :issue:`433`
  * xpath namespaces support, see :issue:`434`

* Feeder API

  * new JDBC feeders for retrieving data from a RDBMS, see :issue:`37`
  * escape character support on CSV based feeders, see :issue:`105`
  * circular feeders, see :issue:`321`

* HTTP API

  * follow redirect support, see :issue:`105`
  * clean cookie handling, see :issue:`396`

* Charts API

  * configurable time window, see :issue:`323`
  * new active transactions/sec over time chart
  * new response latency over time chart

* Recorder

  * no longer an ubber jar, now to be launched from a script
  * follow redirect support
  * configurable generated Simulation package and class name, see :issue:`438`
  * configurable encoding, see :issue:`386`

* Extensions

  * new gatling-maven-plugin, contributed by @nhuray
  * new gatling debian package, contributed by @nhuray

And tons of bug fixes and performance enhancements!

:milestone:`v1.0.3 <5>`
=======================

Fixes
-----

* Fix a bug  in the recorder introduced in 1.0.2 that prevent from recording scenarios with less than 100 requests

:milestone:`v1.0.2 <4>`
=======================

Features
--------

* :issue:`345`, :issue:`348` & :issue:`330` - Better support for long scenarios (via :ref:`manual splitting <long-scenarios>`)
* :issue:`347` - Recorder splits long scenarios so they can be run with no extra configuration.

:milestone:`v1.0.1 <3>`
=======================

Fixes
-----

* :issue:`334` - Fixes reports template resolution under Windows
* :issue:`320` - Stops scenario if queue feeder not big enough
* Fixes a bug with empty lines at end of feeders

Features
--------
* Better CLI feedback

:milestone:`v1.0.0 <1>`
=======================

Initial Release