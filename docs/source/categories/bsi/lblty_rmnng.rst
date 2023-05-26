LIAB_REM
--------
Χρησιμοποιείται για την παροχή λογιστικών στοιχείων λοιπών πληρωτέων λογαριασμών της ``ΠΜ``.

ΔΙΑΣΤΑΣΕΙΣ
~~~~~~~~~~

ID
    Ο αναγνωριστικός κωδικός :ref:`ORG <org>` της ``ΠΜ``

COUNTERGROUP (CNTRGRP)
    Ομαδοποίηση αντισυμβαλλόμενων με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/grp_cntrgrp`

.. _lremcurrency:

CURRENCY (CRRNCY)
    Ομαδοποίηση με βάση το νόμισμα με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`

DATE (DT)
    Ημερομηνία αναφοράς.  Περισσότερες πληροφορίες στην ενότητα :doc:`../../../generic`.


ΜΕΤΑΒΛΗΤΕΣ
~~~~~~~~~~

.. _lremstock:

STOCK (STCK)
    Ονομαστική αξία εκφρασμένο στο lremcurrency_·

STOCK IN EURO (EUR_STCK)
    Η lremstock_ σε Ευρώ.
