from django.db import models
from openpyxl import Workbook, load_workbook
import datetime

structureChoice = [
        ('DIRECTION GENERALE', 'DIRECTION GENERALE'),
        ('MINISTERE ENERGIE', 'MINISTERE ENERGIE'),
        ('PROJET PHOSPHATES', 'PROJET PHOSPHATES'),
        ('DIRECTION CENTRALE AUDIT GROUP & CONFORMITE  (ADG) ', 'DIRECTION CENTRALE AUDIT GROUP & CONFORMITE  (ADG) '),
        ("SURETE INTERNE DE L'ETABLISSEMENT", "SURETE INTERNE DE L'ETABLISSEMENT"),
        ('SYNDICAT NATIONAL SONATRACH', 'SYNDICAT NATIONAL SONATRACH'),
        ('SONATRACH MANAGEMENT ACADEMY (SMA)', 'SONATRACH MANAGEMENT ACADEMY (SMA)'),
        ('DCP RESSOURCES HUMAINES (RHU)', 'DCP RESSOURCES HUMAINES (RHU)'),
        ('DCP STRATEGIE, PLANIFICATION & ECONOMIE (SPE)', 'DCP STRATEGIE, PLANIFICATION & ECONOMIE (SPE)'),
        ('Projet SH 2030', 'Projet SH 2030'),
        ('Projet logicielle de Tableaux de Bord et de Business Intelligence', 'Projet logicielle de Tableaux de Bord et de Business Intelligence'),
        ('Projet SAP ', 'Projet SAP '),
        ("Projet Transformation Digitale & Centre d'Innovation Conjoint", "Projet Transformation Digitale & Centre d'Innovation Conjoint"),
        ('DCP FINANCES (FIN)', 'DCP FINANCES (FIN)'),
        ('DIRECTION CENTRALE ACTIVITES CENTRALES SIEGE (ACT)', 'DIRECTION CENTRALE ACTIVITES CENTRALES SIEGE (ACT)'),
        ('DIRECTION DEVELOPPEMENT DES INFRASTRUCTURES (DDI)', 'DIRECTION DEVELOPPEMENT DES INFRASTRUCTURES (DDI)'),
        ('DIRECTION FINANCES SIEGE (DFS)', 'DIRECTION FINANCES SIEGE (DFS)'),
        ('DIRECTION GESTION SIEGE & ANNEXES (DGSA)', 'DIRECTION GESTION SIEGE & ANNEXES (DGSA)'),
        ('DIRECTION HYGIENE & SECURITE (DHS-ACT)', 'DIRECTION HYGIENE & SECURITE (DHS-ACT)'),
        ('DIRECTION PROJET NOUVEAUX CENTRES DE FORMATION (NCF-ACT)', "DIRECTION PROJET NOUVEAUX CENTRES DE FORMATION (NCF-ACT)"),
        ('CORDONNATEUR SIE/ACT', 'CORDONNATEUR SIE/ACT'),
        ('DIRECTION APPROVISIONNEMENT & CONTRATS (DAC) ', 'DIRECTION APPROVISIONNEMENT & CONTRATS (DAC) '),
        (" DIRECTION PROJET DELOCALISATION DES ACTIVITES DE SONATRACH A LA NOUVELLE VILLE   DE HASSI MESSAOUD (DHM)",
         " DIRECTION PROJET DELOCALISATION DES ACTIVITES DE SONATRACH A LA NOUVELLE VILLE   DE HASSI MESSAOUD (DHM)"),
        ('DIRECTION CENTRALE JURIDIQUE (JUR)', 'DIRECTION CENTRALE JURIDIQUE (JUR)'),
        ("DIR. CENTRALE  INFORMATIQUE & SYSTÈME D'INFORMATION (ISI)", "DIR. CENTRALE  INFORMATIQUE & SYSTÈME D'INFORMATION (ISI)"),
        ('DIRECTION CENTRALE DES MARCHES & LOGISTIQUE  (MLG)', 'DIRECTION CENTRALE DES MARCHES & LOGISTIQUE  (MLG)'),
        ('SANTE SECURITE ENVIRONNEMENT (HSE)', 'SANTE SECURITE ENVIRONNEMENT (HSE)'),
        ('DIRECTION CORPORATE BUSINESS DEVELOPPENT ET MARKETING (BDM)', 'DIRECTION CORPORATE BUSINESS DEVELOPPENT ET MARKETING (BDM)'),
        ('RECHERCHE & DEVELOPPEMENT (RDT)', 'RECHERCHE & DEVELOPPEMENT (RDT)'),
        ('Autre', "Autre"),

    ]


# Create your models here.
class Carburant(models.Model):
    need=[
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
    compteAnalytiqueChoice=[
        ('200000', '200000'),
        ('200001', '200001'),
        ('200008', '200008'),
        ('201000', '201000'),
        ('203000', "203000"),
        ('204000', '204000'),
        ('206000', '206000'),
        ('210000', '210000'),
        ('220000', '220000'),
        ('220001', '220001'),
        ('220002', '220002'),
        ('220003', '220003'),
        ('220004', "220004"),
        ('230000', '230000'),
        ('240000', '240000'),
        ('241000', '241000'),
        ('242000', '242000'),
        ('243000', '243000'),
        ('245000', '245000'),
        ('246000', "246000"),
        ('247000', '247000'),
        ('248000', '248000'),
        ('249000', "249000"),
        ('250000', '250000'),
        ('260000', "260000"),
        ('300000', '300000'),
        ('320000', '320000'),
        ('330000', '330000'),
        ('340000', '340000'),
        ('Autre', "Autre"),

    ]

    alimentationChoice=[('TPE','TPE'), ('Carnet', 'Carnet')]
    typeCarburantChoice=[('Diesel','Diesel'), ('Essence','Essence'), ('Super','Super')]
    nomPrenom = models.CharField(max_length=100, verbose_name='Nom & Prénom')
    structure = models.CharField(max_length=100, choices=structureChoice, verbose_name='Structure')
    compteAnalytique = models.CharField(max_length=10, choices=compteAnalytiqueChoice, verbose_name='Compte Analytique')
    telephonePv = models.CharField(max_length=100, verbose_name='Téléphone privé')
    telephoneBr = models.CharField(max_length=100, verbose_name='Téléphone de bureau')
    typeCarburant = models.CharField(max_length=30, choices=typeCarburantChoice, verbose_name='Type Carburant')
    alimentation = models.CharField(max_length=20, choices=alimentationChoice, verbose_name='Alimentation', default='TPE')
    traite=models.BooleanField(default=False)

    def get_detail_url (self):
        return f"traitement/{self.id}"




class Entretient(models.Model):
    urgenceChoice=[
        ('A Exécuter Immediatement','A Exécuter Immediatement'),
        ('A Exécuter Dans Les Plus Brefs Délais', 'A Exécuter Dans Les Plus Brefs Délais'),
        ('Peut Etre Reporté', 'Peut Etre Reporté'),
    ]
    marqueChoice=[
        ('AUDI', 'AUDI'),
        ('CHEVEROLET', 'CHEVEROLET' )
    ]
    nomPrenom= models.CharField(max_length=120, verbose_name='Nom & Prénom')
    service= models.CharField(max_length=120, choices=structureChoice, verbose_name='Service')
    immatriculation = models.CharField(max_length=200, verbose_name='Immatriculation')
    kilometrage= models.FloatField(verbose_name='Kilometrage')
    marque = models.CharField(max_length=5, verbose_name='Marque')
    type = models.CharField(max_length=100, verbose_name='Type')
    contactName = models.CharField(max_length=100, verbose_name='Nom & Prénom')
    telephonePv = models.CharField(max_length=100, verbose_name='Téléphone privé')
    telephoneBr = models.CharField(max_length=100, verbose_name='Téléphone de bureau')
    description=models.TextField(blank=True, verbose_name='Description')
    urgence=models.CharField(max_length=100, verbose_name='Urgence', choices=urgenceChoice)
    traite = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)
    def traitement(self):
        wb = load_workbook("Copie de Demande d'entretien véhicule.xlsx")
        template = wb.active
        template['B7']=self.nomPrenom
        template['C7']=self.service
        template['G8'] = self.marque
        template['G9'] = self.type
        template['G10'] = self.kilometrage
        template['B14'] = self.description
        template['E12'] = self.telephonePv
        template['G12'] = self.telephoneBr
        template['B9'] = datetime.datetime.now()
        wb.save("Demande d'entretien véhicule2.xlsx")





class TraitementCarburant(models.Model):
    kilometrageInitial=models.FloatField(verbose_name="Kilométrage Initial")
    kilometrageActuel = models.FloatField(verbose_name="Kilometrage Actuel")

    kilometrageParcouru = models.FloatField( verbose_name="Kilometrage Parcouru")
    quantiteConsommee = models.FloatField(verbose_name="Quantité Consommée")
    tauxConsomation = models.FloatField( verbose_name="Taux De Consomation")
    montantAlimentation = models.FloatField(max_length=100, verbose_name="Montant Alimentation")
    dateAlimentation = models.DateField( verbose_name="Date Alimentation")
    nouveauKilometrage = models.FloatField(max_length=100, verbose_name="Nouveaux Kilométrage")








