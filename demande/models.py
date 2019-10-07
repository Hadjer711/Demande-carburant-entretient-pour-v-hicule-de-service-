from django.db import models


# Create your models here.
class Carburant(models.Model):
    compteAnalytiqueChoice=[
        ('200000', 'DIRECTION GENERALE'),
        ('200001', 'MINISTERE ENERGIE'),
        ('200008', 'PROJET PHOSPHATES'),
        ('201000', 'DIRECTION CENTRALE AUDIT GROUP & CONFORMITE  (ADG) '),
        ('203000', "SURETE INTERNE DE L'ETABLISSEMENT"),
        ('204000', 'SYNDICAT NATIONAL SONATRACH'),
        ('206000', 'SONATRACH MANAGEMENT ACADEMY (SMA)'),
        ('210000', 'DCP RESSOURCES HUMAINES (RHU)'),
        ('220000', 'DCP STRATEGIE, PLANIFICATION & ECONOMIE (SPE)'),
        ('220001', 'Projet SH 2030'),
        ('220002', 'Projet logicielle de Tableaux de Bord et de Business Intelligence'),
        ('220003', 'Projet SAP '),
        ('220004', "Projet Transformation Digitale & Centre d'Innovation Conjoint"),
        ('230000', 'DCP FINANCES (FIN)'),
        ('240000', 'DIRECTION CENTRALE ACTIVITES CENTRALES SIEGE (ACT)'),
        ('241000', 'DIRECTION DEVELOPPEMENT DES INFRASTRUCTURES (DDI)'),
        ('242000', 'DIRECTION FINANCES SIEGE (DFS)'),
        ('243000', 'DIRECTION GESTION SIEGE & ANNEXES (DGSA)'),
        ('245000', 'DIRECTION HYGIENE & SECURITE (DHS-ACT)'),
        ('246000', "DIRECTION PROJET NOUVEAUX CENTRES DE FORMATION (NCF-ACT)"),
        ('247000', 'CORDONNATEUR SIE/ACT'),
        ('248000', 'DIRECTION APPROVISIONNEMENT & CONTRATS (DAC) '),
        ('249000', " DIRECTION PROJET DELOCALISATION DES ACTIVITES DE SONATRACH A LA NOUVELLE VILLE   DE HASSI MESSAOUD (DHM)"),
        ('250000', 'DIRECTION CENTRALE JURIDIQUE (JUR)'),
        ('260000', "DIR. CENTRALE  INFORMATIQUE & SYSTÈME D'INFORMATION (ISI)"),
        ('300000', 'DIRECTION CENTRALE DES MARCHES & LOGISTIQUE  (MLG)'),
        ('320000', 'SANTE SECURITE ENVIRONNEMENT (HSE)'),
        ('330000', 'DIRECTION CORPORATE BUSINESS DEVELOPPENT ET MARKETING (BDM)'),
        ('340000', 'RECHERCHE & DEVELOPPEMENT (RDT)'),
        ('Autre', "Autre"),

    ]
    alimentationChoice=[('TPE','TPE'), ('Carnet', 'Carnet')]
    typeCarburantChoice=[('Diesel','Diesel'), ('Essence','Essence'), ('Super','Super')]
    nomPrenom = models.CharField(max_length=100, verbose_name='Nom Prénom')
    structure = models.CharField(max_length=100, verbose_name='Structure')
    compteAnalytique = models.CharField(max_length=10, choices=compteAnalytiqueChoice, verbose_name='Compte Analytique')
    telephonePv = models.CharField(max_length=100, verbose_name='Téléphone privé')
    telephoneBr = models.CharField(max_length=100, verbose_name='Téléphone de bureau')
    typeCarburant = models.CharField(max_length=30, choices=typeCarburantChoice, verbose_name='Type Carburant')
    alimentation = models.CharField(max_length=20, choices=alimentationChoice, verbose_name='Alimentation')



class Entretient(models.Model):
    nomPrenom= models.CharField(max_length=120)
    service= models.CharField(max_length=120)
    immatriculation = models.CharField(max_length=200)
    kilometrage= models.CharField(max_length=10)
    marque = models.CharField(max_length=5)
    type = models.CharField(max_length=100)
    contactName = models.CharField(max_length=100)
    telephonePv = models.CharField(max_length=100)
    telephoneBr = models.CharField(max_length=100)
    description=models.TextField(blank=True)
    urgence=models.CharField(max_length=100)


