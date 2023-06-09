
Πίνακας Στοιχείων Αναφοράς ΔΧΠ που συναλλάσονται οι ΠΜ (EDR)
============================================================
Χρησιμοποιείται για την παροχή πληροφοριακών στοιχείων των διαπραγματεύσιμων χρηματοοικονομικών παραγώγων που κατέχει η ΠΜ (οι ΠΜ).


ΔΙΑΣΤΑΣΕΙΣ
----------

ID
    Ο αναγνωριστικός κωδικός :ref:`EDR <edr>` του διαπραγματεύσιμου παράγωγου.


ΜΕΤΑΒΛΗΤΕΣ
----------
BIRTHDATE (DT_BRTH)
    Ημερομηνία έκδοσης/ενεργοποίησης/αρχικοποίησης·

CLOSEDATE (DT_CLS)
    Ημερομηνία λήξης (κατά περίπτωση)·

NAME (NM)
    Ονομασία·

TICKER (TCKR)
    Το σύμβολο του παραγώγου όπως αποδίδεται από τη χρηματιστηριακή αγορά.

TYPE (TYP)
    Είδος με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/drvtv_typ`

.. _edrcurrency:

CURRENCY (CRRNCY)
    Το νόμισμα συναλλαγής με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`

MULTIPLIER (MLTPLR)
    Ο πολλαπλασιαστής·

WRITER (WRTR)
    Ο κεντρικός αντισυμβαλλόμενος του διαπραγματεύσιμου παραγώγου με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/gen_mrkt` που προκύπτει από το πρότυπο ISO-10383.

ALIAS OF (ALS_OF)
    Χρησιμοποιείται κατά περίπτωση για την συσχέτιση εσωτερικών αναγνωριστικών κωδικών :ref:`EDR <edr>` σε περίπτωση αλλαγής της ΜΠΣ ή σε περίπτωση εταιρικής πράξης της ΜΠΣ.
