
ΣΜΕ
===

Στην περίοδο Τ0 ο ΕΟ έχει 1000 ευρώ σε καταθέσεις:

===========  ========================
Τ0 ACC.DPSTS 
-------------------------------------
Μεταβλητή    Τιμή   
===========  ========================
STCK          1000        
FLS           0       
===========  ========================
 
===========  ========================
Τ0 ACC.KEY 
-------------------------------------
Μεταβλητή    Τιμή   
===========  ========================
BK_PRC        1000        
INCM          0       
===========  ========================


Στα τέλος της περιόδου Τ1 ο ΕΟ πραγματοποιεί αγοϱά 2 τυποποιημένων ΣΜΕ
με τιμή του δείκτη αναφοράς τις 1000 μονάδες με κατάθεση περιθωρίου:

================  ===================
Τ1: ACC.DER
-------------------------------------
Μεταβλητή         Τιμή
================  ===================
STCK              0
FLS               0
QNTTY             2
================  ===================

Στο τέλος της περιόδου Τ2 η τιμή του δείκτη αναφοράς αυξάνεται στις 1100 μονάδες:

================  ===================
Τ2: ACC.DER
-------------------------------------
Μεταβλητή         Τιμή
================  ===================
STCK              0
FLS               -1000
QNTTY             2
================  ===================

===========  ========================
Τ2: ACC.DPSTS 
-------------------------------------
Μεταβλητή    Τιμή   
===========  ========================
STCK          2000        
FLS           1000       
===========  ========================

===========  ========================
Τ2 ACC.KEY 
-------------------------------------
Μεταβλητή    Τιμή   
===========  ========================
BK_PRC        2000        
INCM          0       
===========  ========================

Στο τέλος της περιόδου Τ3 η τιμή του δείκτη αναφοράς μειώνεται στις 1050
μονάδες και πωλούνται τα ΣΜΕ.

================  ===================
Τ3: ACC.DER
-------------------------------------
Μεταβλητή         Τιμή
================  ===================
STCK              0
FLS               500
QNTTY             0 
================  ===================

===========  ========================
Τ3: ACC.DPSTS 
-------------------------------------
Μεταβλητή    Τιμή   
===========  ========================
STCK          1500        
FLS           -500       
===========  ========================

===========  ========================
Τ3: ACC.KEY 
-------------------------------------
Μεταβλητή    Τιμή   
===========  ========================
BK_PRC        1500        
INCM          0       
===========  ========================
