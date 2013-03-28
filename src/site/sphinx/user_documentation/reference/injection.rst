.. _injection:

#########
Injection
#########



* Ramping some users::

   scn.inject(ramp(100 users).over(1 minute))

* All at once::

   scn.inject(atOnce(100 users))

* Following a Dirac delta function::

   scn.inject(dirac(100 users).over(5 seconds))

* TODO

   scn.inject(nothingFor(10 seconds))
   scn.inject(constantRate(2 usersPerSec))
   scn.inject(rampRate(2 usersPerSec).to(4 usersPerSec))
   scn.inject(split(1000 users).into(ramp(100 users).over(30 seconds)
                               .separatedBy(10 seconds))
   scn.inject(split(1000 users).into(ramp(100 users).over(30 seconds)
                               .separatedBy(dirac(100 users).over(3 seconds)))

   scn.inject(constantRate(2 usersPerSec),
              nothingFor(10 seconds),
              dirac(50 users).over(1 minute))


