# Changelog

## 0.5.0

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - Final TVA calculation
  - Added units on TVA and CST-S variables

## 0.4.0

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - Added TVA calculation (only basics)
  - Fixed an technical error on rates

## 0.3.6

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - Merged Entreprise and Personne
  - Fixed an technical error on rates

## 0.3.5

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - refactoring
  - adding 12 scales on it and CST NS for simulation purpose
  - addind statistics on country

## 0.3.4

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - refactoring
  - Corrections to IT ported to CST NS

## 0.3.3

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - some statistics ont companies

## 0.3.2

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - TVA thresholds are now parameters

## 0.3.1

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - Adding evaluation of which tax the company is due, and it's available options

## 0.3.0

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: all.
* Details:
  - new entity pays that is holding the "taux" and "seuils"
  - Pays also have calculation about all "entreprises"

## 0.2.12

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - corrected 2 point in IT calculation that were wrong

## 0.2.11

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - mode doc
  - More intermediate variables in IT to allow simulations from Web API

## 0.2.10

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: DICP.
* Details:
  - tuning to rounds
  - raw It  is now based on tranche calculatiion so that the "avis" is coherent

## 0.2.9

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: all.
* Details:
  - Round rules are aligned with CDI

## 0.2.8

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: all.
* Details:
  - moving from bool to enum to ensure it is well set

## 0.2.7

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp`.
* Details:
  - CST-S renaming var

## 0.2.6

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp`.
* Details:
  - IT Adding penalites

## 0.2.5

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp`.
* Details:
  - IT Adding deductions

## 0.2.4

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp`.
* Details:
  - IT Adding all intermediate calculation for avis edition

## 0.2.3

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `dicp`.
* Details:
  - CST-S ignore negative values

## 0.2.2

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: `all`.
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
