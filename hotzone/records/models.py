from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Patients diagnosed with the disease
class Patient(models.Model):
	name = models.CharField(max_length=128)				# name
	identity = models.CharField(max_length=32)			# identity document number
	birth = models.DateField()							# date of birth
	
	def __str__(self):
		return self.name

# Infecting viruses
class Virus(models.Model):
 	name = models.CharField(max_length=128)				# name
 	commonName = models.CharField(max_length=64)		# common name (of associated disease)
 	maxPeriod = models.DecimalField(
 		max_digits=2,
 		decimal_places=0,
 		validators=[MinValueValidator(Decimal('0'))]
 	)													# max. infectious period (before a case confirmed as infected and isolated)
 	
 	def __str__(self):
 		return self.commonName

# Locations visited by the patient during the Infectious Period.
class Location(models.Model):
	name = models.CharField(max_length=128)				# name
	address = models.TextField(blank=True, null=True)	# address, only when listed in Geodata dataset
	XCoord = models.DecimalField(
		max_digits=8,
		decimal_places=2
	)													# HK1980 Grid X Coordinate
	YCoord = models.DecimalField(
		max_digits=8,
		decimal_places=2
	)													# HK1980 Grid Y Coordinate
	
	def __str__(self):
		return self.name

# Confirmed case of a viral infection
class Case(models.Model):
	caseNumber = models.CharField(max_length=32)		# case number, unique for a particular Infecting Virus
	patient = models.ForeignKey(
		Patient, 
		on_delete=models.CASCADE
	)													# patient
	virus = models.ForeignKey(
		Virus, 
		on_delete=models.CASCADE
	)													# infecting virus
	date = models.DateField()

	LOCAL = 'Local'
	IMPORTED = 'Imported'
	CASE_ORIGIN_CHOICE = (
		(LOCAL, 'Local'),
		(IMPORTED, 'Imported'),
	)
	origin = models.CharField(
		max_length=8, 
		choices=CASE_ORIGIN_CHOICE
	)													# origin: Local / Imported

	def __str__(self):
		return self.patient.name + '_' + self.caseNumber

# visit of of locations visited by the patient during the infectious period.
class Visit(models.Model):
	case = models.ForeignKey(
		Case,
		on_delete=models.CASCADE
	)													# case that visits the location during the infectious period
	location = models.ForeignKey(
		Location,
		on_delete=models.CASCADE
	)													# location visited during the infectious period
	dateFrom = models.DateField()						# dates from which the patient was present at the location
	dateTo = models.DateField()							# dates to which the patient was present at the location

	RESIDENCE = 'Residence'
	WORKPLACE = 'Workplace'
	VISIT = 'Visit'
	VISIT_CATEGORY_CHOICE = (
		(RESIDENCE, 'Residence'),
		(WORKPLACE, 'Workplace'),
		(VISIT, 'Visit'),
	)
	category = models.CharField(
		max_length=10,
		choices=VISIT_CATEGORY_CHOICE
	)													# category: Residence, Workplace, Visit

	def __str__(self):
		return self.location.name + '_' + self.case.caseNumber
