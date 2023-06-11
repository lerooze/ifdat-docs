
ASSET_NON_FINANCIAL
===================
Χρησιμοποιείται για την παροχή μη χρηματοοικονομικών περιουσιακών στοιχείων της ΠΜ.

ΔΙΑΣΤΑΣΕΙΣ
~~~~~~~~~~

TYPE (TYP)
    Είδος μη χρηματοοικονομικού περιουσιακού στοιχείου με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/asst_nn_fnncl`

COUNTRY (CNTRY)
    Χώρα τοποθεσίας του περιουσιακού στοιχείου με επιλογή από τη λίστα τιμών :doc:`../../types/codelists/gen_cntry`

ID
    Ο αναγνωριστικός κωδικός :ref:`ORG <org>` της ΠΜ.

DATE (DT)
    Ημερομηνία που ισχύουν οι τιμές των μεταβλητών STCK και ACCRLS.  Περισσότερες πληροφορίες στην ενότητα :doc:`../../../generic`.

FREQUENCY (FRQNCY)
    Σε συνδυασμό με τη διάσταση DT ορίζει τη χρονική περίοδο που ισχύει η τιμή της μεταβλητής FLS.  Περισσότερες πληροφορίες στις :doc:`../../../generic`.

ΜΕΤΑΒΛΗΤΕΣ
~~~~~~~~~~

STOCK (STCK)
    Αξία σύμφωνα με τους κανόνες αποτίμησης που περιγράφονται στο κεφάλαιο 7 του **ESA2010**.  

FLOWS (FLS)
    Αξία συναλλαγών (αγοροπωλησίες, ανακαινίσεις, βελτιώσεις) μικτές από
    προμήθειες/φόρους των συναλλαγών κατά τη διάρκεια της περιόδου αναφοράς.

ACCRUALS (ACCRLS)
    Δεδουλευμένα μισθώματα.