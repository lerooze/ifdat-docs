ASSET_REM
---------
Χρησιμοποιείται για την παροχή λογιστικών στοιχείων λοιπών εισπρακτέων λογαριασμών της ``ΠΜ``.

ΔΙΑΣΤΑΣΕΙΣ
~~~~~~~~~~

ID
    Ο αναγνωριστικός κωδικός :ref:`ORG <org>` της ``ΠΜ``

COUNTERGROUP (CNTRGRP)
    Ομαδοποίηση αντισυμβαλλόμενων με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/grp_cntrgrp`

.. _aremcurrency:

CURRENCY (CRRNCY)
    Ομαδοποίηση με βάση το νόμισμα με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`

DATE (DT)
    Ημερομηνία αναφοράς.  Περισσότερες πληροφορίες στην ενότητα :doc:`../../generic`.

ΜΕΤΑΒΛΗΤΕΣ
~~~~~~~~~~

.. _aremstock:

STOCK (STCK)
    Ονομαστική αξία εκφρασμένο στο aremcurrency_·

STOCK IN EURO (EUR_STCK)
    Η aremstock_ σε Ευρώ.
