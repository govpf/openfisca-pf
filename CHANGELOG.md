# Changelog

## 0.2.2

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `all.
* Details:
  - Changed float32 to float34 in openfisca-core (sed in Dockerfile)

## 0.2.1

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp` and `entreprise`
* Details:
  - `IT` tax calculation : added rounds (no impact in float32)
  - `CST-NS` tax calculation : added rounds (no impact in float32)
  - `CST-S` tax calculation : added rounds for personal CST-S
  - `CST-S` : added tests cases

## 0.2.0

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp` and `entreprise`
* Details:
  - `IT` tax calculation refactor and corrections
  - `CST-NS` tax calculation
  - Removed all examples from template

## 0.1.0

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp` and `entreprise`
* Details:
  - `entreprise` entity created
  - `CA` and `Charges` variables created
  - `IT` tax calculation
  - `CST-S` tax calculation
