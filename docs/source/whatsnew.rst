:tocdepth: 2

What's new?
===========

.. contents::
   :local:
   :backlinks: none
   :depth: 1

.. Next release
.. ============

v0.9.2 (2025-06-24)
-------------------
* Examples were added and imporoved
* Corner cases were added
* Change SHR_KEY to KEY where needed
* Fix license and credits
* Other improvements in documentation

v0.9.1 (2025-01-31)
-------------------
* Rename MNGMNT tables to RA
* Replace bool to enum_bool
* Improve documentation

v0.9.0 (2024-12-21)
-------------------
* Add financial instrument treatment examples
* Allow negative values for STCK, NMNL_STCK, QNTTY for ACC.SHR and AND ACC.ASST_DBT to accomodate short positions
* Improve tables documentation

v0.8.5 (2024-11-27)
-------------------
* Fix bugs in regulation
* Fix bugs in tables
* Add IEK columns in EO sheet of IFDAT-LIST
* Fix bugs in IFDAT-LIST
* Add max length in url fields

v0.8.4 (2024-11-20)
-------------------
* Added derogation tables 
* Created IFDAT-LIST reports at the end of the main example
* Fix bugs

v0.8.3 (2024-11-11)
-------------------
* Fix bugs

v0.8.2 (2024-11-06)
-------------------

* Merge SFT tables into LON tables
* Update init and main examples based on IFDAT 30/10/2024 presentation
* Fix bugs

v0.8.1 (2024-10-29)
-------------------

* Removed IID dimension from ACC.LBLTY_DBT table
* Improve DER identifier 

v0.8.0 (2024-10-28)
-------------------

* Add ACC.FND_KEY table so that IFs explicitly provide fees per fund
* Renamed ACC.KEY to ACC.SHR_KEY
* Dropped MLTPLR from REF.DER table and renamed NM_LTN to FISN
* Imporoved examples
* Modify regulation
* Update data base checks
* Bug fixes

v0.7.6 (2024-10-24)
-------------------

* Remove ACC.RVN and ACC.EXPNS and drop check
* Modify sbscrpt, rdmptn defs
* Bug fixes


v0.7.5 (2024-10-23)
-------------------

* Fix bugs
* Reintroduce examples
* Improve data model and schema

v0.7.4 (2024-10-18)
-------------------

* Transform to Greek some enumerations
* Fix bugs

v0.7.3 (2024-10-17)
-------------------

* Introduce once again examples
* Refactor the data model

v0.7.2 (2024-10-13)
-------------------

* Minor changes in data model
* Improve documentation

v0.7.1 (2024-10-07)
-------------------

* Refactored excel data model
* New json schema for improvements in data model
* Removed temporarily acknowledgment schema
* Removed examples temporarily
* Improve documentation
* Improve regular expressions
* Added IF reporting agents report

v0.7.0 (2024-02-29)
-------------------

* Refactored excel data model
* Added acknowledgment schema
* Other syntactic changes
* Example section (not available on this version)


v0.6.1 (2023-09-15)
-------------------

* Merge ACC.CSH table into ACC.DPST
* Rename ACC.AGG to ACC.KEY, PSN to USR
* Created formats DBT, DEP, EDR, LON, ODR, ORG, SFT, SHR, USR
* Rename Κατηγορίες to Δέσμες in categories.rst 
* Improve categories documentation
* Improve and refactor codelists (dbt_prmry_clss to dbt_typ, fnd_dstrbtn_typ to fnd_dstrbtn_plcy, fnd_typ to fnd_lgl_typ, fnd_sbtyp to fnd_eqty_typ, shr_prmry_clss to shr_typ) 
* Refactor REF.DPST
* Fix bug in regex A-z to A-Z
* Add to glossary
* Improve generic.rst description
* Improve identifiers description
* Add Ελληνικη Αναπτυξιακή Τράπεζα to RAs
* Update accounting checks
* Spell check
* Note: Examples have not yet been updated to reflect the updated model


  
v0.6.0 (2023-06-11)
-------------------

* Merge ACC tables regarding non-financial assets into ASST_NN_FNNCL
* Refactor ACC tables ASST_RMNNG, LBLTY_RMNNG by adding types in the dimensions.
* Refactor all ACC tables to include FLOWS (FLS)
* Accrued interest, rent not included in STOCK
* If not explicitly stated in the variables definitions all monetary variables are expressed in Euros (and thus removed explicit variables for Euro and FSC in ACC tables)
* Refactor examples
* Merge DEBT TRANCHE and REDEMPTION tables in REF into OUTSTANDING_CHANGE
* Add validation section
* Refactor documentation to reflect the above changes
* Clean documentation
  
v0.5.4 (2023-05-30)
-------------------

* Add FSC valuation in acc tables
* Add T1 correction example file for MFMC
* Other minor changes
  
v0.5.3 (2023-05-28)
-------------------

* Refactor IFDat categories to three (REF, ACC)
* Complete t0 and t1 full examples for MFMC
* Other minor changes
  
v0.5.2 (2023-05-26)
-------------------

* Refactor IFDat categories to three (REF, BSI, INC)
* Refactor data category presentation
* Start introducing variable data types into docs
* Refactor examples
* Other minor changes
  
v0.5.1 (2023-05-24)
-------------------

* Add codelist section and links of enumerated variables and dimensions to codelists 
* Start introducing greek names for categories and variables
* Start refactoring examples
* Other minor changes
  
v0.5.0 (2023-05-16)
-------------------

* Reorganize categories
* Drop other_key category
* Introduce examples per table
* Drop not needed variables
* Drop all other static tables
  
v0.4.3 (2023-05-11)
-------------------

* Adjust SI and SK to reflect current data needs
* Drop attributes
* Added to SK TRANCHE and REDEMPTION tables
  
v0.4.2 (2023-04-18)
-------------------

* Add Reporting Agents
  
v0.4.1 (2023-04-18)
-------------------

* Introduce docx documentation
  
v0.4.0 (2023-04-18)
-------------------

* Introduce one DATA MODEL, one json schema and one template file rather than
  seperate ones for each category


v0.3.1 (2023-04-13)
-------------------

* Fix INTERNAL ID format
* Fix minor bugs
* Fix syntax

v0.3.0 (2023-04-11)
-------------------

* Refactor to IFDat-Docs

v0.2.3 (2023-04-03)
-------------------

* Fix bug in restricting Greek IF reporting population.

v0.2.1 (2023-03-29)
-------------------

* In IFDat, BSI, DEPOSIT removed arrears and write-offs
* Fix OTC_DERIVATIVE BSI stock greek definition
* Bug fixes

v0.2.0 (2023-01-16)
-------------------

* In IFDat domain new RA tables in self_info category.
* In IFDat domain introduce DEDUPLICATE OF measures in case of a change in ``RA``.
* Update documentation to accomodate above changes.
* Fix syntax and spelling bugs in documentation.

v0.1.1 (2023-01-04)
-------------------

* Introduce License
* Documentation fixes

v0.1.0 (2023-01-04)
-------------------

* Pre-release of documentation
