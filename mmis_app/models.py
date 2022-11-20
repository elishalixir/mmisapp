from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


# # Create your models here.

class User(AbstractUser):
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    is_admin = models.BooleanField('Is Admin', default=False)
    is_cement = models.BooleanField('Cement Sector', default=False)
    is_health = models.BooleanField('Health Sector', default=False)
    is_waste = models.BooleanField('Waste Sector', default=False)
    is_asgm = models.BooleanField('ASGM Sector', default=False)
    is_map = models.BooleanField('MAP Sector', default=False)
    is_EandF = models.BooleanField('Energy & Fuel Sector', default=False)
    Fname = models.CharField(max_length=50, null=False, verbose_name="First Name", default='')
    Mname = models.CharField(max_length=50, blank=True, verbose_name="Middle Name", default='')
    Sname = models.CharField(max_length=50, null=False, verbose_name="Surname Name", default='')
    gender = models.CharField(max_length=6, null=False, choices=gender_choice, default='')
    Organization_name = models.CharField(max_length=150, null=False, verbose_name="Organization's Name", default='')
    ContactPhone = PhoneField(null=False, verbose_name='Contact phone number', default='' )
    OrganizationPhone = PhoneField(null=False, verbose_name="Organization's phone number", default='')
    Alternate_mobile = PhoneField(blank=True, help_text='Contact phone number')
    Full_address = models.TextField(max_length=250, null=False, verbose_name="Organization's Address", default='')
    email = models.EmailField(max_length=200, null=True, verbose_name="Organization's email address", default='')
    Web_page = models.CharField(max_length=50, blank=True, verbose_name="Web address", default='')

    def __str__(self):
        return f'{self.Fname} from {self.Organization_name}'


class MercuryAddedProducts(models.Model):
    mercury_compound_Choice = (

        ('Mercury Product', 'Mercury Product'),
        ('Commodity Chemical', 'Commodity Chemical'),
        ('Disposed Mercury Products', 'Disposed Mercury Products'),
        ('Thermometers', 'Thermometers'),
        ('Light Fittings', 'Light Fittings'),
        ('Cosmetics', 'Cosmetics'),
        ('Batteries', 'Batteries'),
        ('Paint', 'Paint'),
        ('Polyurethane', 'Polyurethane')
    )

    mercury_compound = models.CharField(max_length=300, null=True, choices=mercury_compound_Choice, default='')
    item = models.CharField(max_length=250)
    imported = models.CharField(max_length=200)
    consumption_or_production = models.CharField(max_length=200)
    year = models.DateField(max_length=4)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)


class EnergyConsumptionAndFuelProduction(models.Model):
    energy_fuel_Choice = (

        ('Coal Combustion in Large Power Plants', 'Coal Combustion in Large Power Plants'),
        ('Other Coal Uses', 'Other Coal Uses'),
        ('Combustion/Use of Petroleum Coke and Heavy Oil', 'Combustion/Use of Petroleum Coke and Heavy Oil'),
        ('Use of Raw or Pre-cleaned Natural Gas', 'Use of Raw or Pre-cleaned Natural Gas'),
        ('Use of Pipeline Gas (Consumer quality)', 'Use of Pipeline Gas (Consumer quality)'),
        ('Biomass Fired Power & Heat Production', 'Biomass Fired Power & Heat Production'),
        ('Charcoal Combustion', 'Charcoal Combustion'),
        ('Oil Extraction', 'Oil Extraction'),
        ('Oil Refining', 'Oil Refining'),
        ('Extraction & Processing of Natural Gas', 'Extraction & Processing of Natural Gas'),
    )

    energy_fuel = models.CharField(max_length=300, null=True, choices=energy_fuel_Choice, default='')
    imported = models.CharField(max_length=200, default='')
    consumption_or_production = models.CharField(max_length=200, default='')
    year = models.DateField(max_length=4, default='')
    note = models.TextField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Cement(models.Model):
    yes_choices = (
        ('Select', 'Select'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    operation_cover_Choice = (

        ('Cement Production', 'Cement Production'),
        ('Cement Production/without Co-incineration of Waste', 'Cement Production/without Co-incineration of Waste'),
        ('With no filters', 'With no filters'),
        ('With filters and no filter dust recycling: Simple particle control (ESP / PS / FF)\
Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)', 'With filters an no filter dust recycling: Simple particle control (ESP / PS / FF)\
Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)'),
        ('With filters and filter dust recycling *2:\
Simple particle control (ESP / PS / FF) Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)\
', 'With filters and filter dust recycling *2:\
Simple particle control (ESP / PS / FF) Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)\
'),
        ('Production of Lime', 'Production of Lime'),
        ('Production of lime and lightweight aggregates', 'Production of lime and lightweight aggregates'),
        ('Production of light weight aggregate using kiln', 'Production of light weight aggregate using kiln'),
        ('Other minerals and materials', 'Other minerals and materials')

    )

    operation_cover = models.CharField(max_length=300, null=True, choices=operation_cover_Choice, default='')
    yes = models.CharField(max_length=6, null=True, choices=yes_choices, default='')
    consumption_or_production = models.CharField(max_length=200, default='')
    year = models.DateField(max_length=4, default='')
    note = models.TextField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class EnvironmentAndHealth(models.Model):
    option1 = (("z)", "select"), ("a)", "Domestic"), ("b)", "Hazardous/Industrial"), ("d)", "Not applicable"))
    option2 = (("z)", "select"), ("a)", "Daily (Kg)"), ("b)", "Weekly (Kg)"), ("c)", "Monthly (Kg)"), ("d)", "Yearly "
                                                                                                             "(Kg)"))
    option3 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
    option4 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"),)
    option5 = (("z)", "select"), ("a)", "Incineration"), ("b)", "Sewage Effluent treatment"), ("c)", "Dumping on "
                                                                                                     "landfill"),
               ("d)", "Controlled Dump sites"))
    option6 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))

    option8 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
    option9 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
    option10 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))

    option12 = (("a)", "Yes"), ("b)", "No"))

    submit_choice = (("Yes", "Yes"), ("Yes", "Yes"))

    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    one = models.CharField(verbose_name="1.	Types of Waste Collected: ",
                           max_length=300, default='', choices=option1, null=True)
    two = models.CharField(
        verbose_name="2. What is the volume of waste disposed in (Kg) and the frequency: ", max_length=300,
        default='', choices=option2, null=True)
    three = models.CharField(verbose_name="3.	Are the waste sorted: ",
                             max_length=300, default='', choices=option3, null=True)
    four = models.CharField(verbose_name="4.	Are there mercury products in contained in the waste e.g Electric bulbs "
                                         "florescent tubes, thermometers etc  ",
                            max_length=300, default='', choices=option4, null=True)
    five = models.CharField(verbose_name="5.	What method of disposal/recycling is carried: ",
                            max_length=300, default='', choices=option5, null=True)
    six = models.CharField(verbose_name="6.	Is there any control measures in place to mitigate against or reduce the "
                                        "environmental hazards/degradation from the mercury contained waste "
                                        "available:  ",
                           max_length=300, default='', choices=option6, null=True)
    seven = models.CharField(
        verbose_name="7.	If yes, Kindly indicate what control measure is available, if No state 'N/A'  ",
        max_length=3000, default='fill here')
    eight = models.CharField(
        verbose_name="8.	Is there any measurement of Mercury in your waste collected and in Kg? ",
        max_length=300, default='', choices=option8, null=True)
    nine = models.CharField(verbose_name="9.	Is there any emission reduction devices? ",
                            max_length=300, default='', choices=option9, null=True)
    ten = models.CharField(verbose_name="10.	Is there any form of Particulate Matter (PM) Reduction?",
                           max_length=300, default='', choices=option10, null=True)
    eleven = models.CharField(
        verbose_name="11.  If yes above, do you use acid gas control with Limestone or any similar acid "
                     "gas absorbent? ", max_length=300, default='')
    twelve = models.CharField(verbose_name="12.	Do you use mercury specific absorbent? (Kg Hg/Year) ",
                              max_length=300, default='', choices=option12, null=True)
    thirteen = models.CharField(
        verbose_name="13. Kindly state other necessary information below that can help this research work: ",
        max_length=3000, default='fill here')
    fourteen = models.CharField(verbose_name="14.	Tonnes/year of municipal waste incinerated ", max_length=3000,
                                default='fill here')
    fifteen = models.CharField(verbose_name="15.	Tonnes/year of hazardous waste incinerated", max_length=3000,
                               default='fill here')
    sixteen = models.CharField(verbose_name="16.	Tonnes/year of medical waste incinerated ", max_length=3000,
                               default='fill here')
    seventeen = models.CharField(verbose_name="17.	Tonnes/year of sewage sludge incinerated ", max_length=3000,
                                 default='fill here')
    eighteen = models.CharField(verbose_name="18.	Tonnes/year of domestic waste disposed off at dumpsite",
                                max_length=3000, default='fill here')
    nineteen = models.CharField(verbose_name="19.	Tonnes/year waste burned", max_length=3000, default='fill here')
    twenty = models.CharField(verbose_name="20.	Tonnes/year Sewage sludge incinerated ", max_length=3000,
                              default='fill here')
    twenty_one = models.CharField(
        verbose_name="21.	Tonnes/year of Open fire waste burning (on landfills and informally)", max_length=3000,
        default='fill here')
    twenty_two = models.CharField(verbose_name="22.	What other technology do you use in treating waste?",
                                  max_length=3000, default='fill here')
    twenty_three = models.CharField(verbose_name="23.	What other pollution control mechanisms do you have in place?",
                                    max_length=3000, default='fill here')
    twenty_four = models.CharField(verbose_name="24.	What are your challenges?", max_length=3000,
                                   default='fill here')
    twenty_five = models.CharField(verbose_name="25.	What are your Suggestions/Recommendation?", max_length=3000,
                                   default='fill here')
    note = models.TextField(max_length=200, default='', help_text='Max of 200 characters.', null=True)

    submitted = models.CharField(verbose_name="	Are you ready to submit? ",
                            max_length=300, default='', choices=submit_choice, null=True)

    def __str__(self):
        return self.submitted


class ASGMining(models.Model):
    submit_choice = (("Yes", "Yes"), ("Yes", "Yes"))


    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    one = models.CharField(verbose_name="1. How many people are engaged in ASGM mining IN Nigeria?", max_length=3000,
                           null=False)
    two = models.CharField(
        verbose_name="2. Are women and children involved in the ASGM activities? What is their population ("
                     "Men, Women and Children)", help_text="Write the number of Men=..., women=..., "
                                                           "children=...", max_length=3000, null=False)
    three = models.CharField(verbose_name="3. How much gold do ASG miners produce annually? in g, Kg or tonnes",
                             max_length=3000, null=False)
    four = models.CharField(verbose_name="4. What is the range of the karat of gold produced?", max_length=3000,
                            null=False)
    five = models.CharField(verbose_name="5. Do the miners use mercury for mining? Where do they get Mercury from? ",
                            max_length=3000, null=False)
    six = models.CharField(
        verbose_name="6. Is mercury added to the whole ore (before or during crushing) or to concentrates?",
        max_length=3000, null=False)
    seven = models.CharField(verbose_name="7. Is there open burning of mercury to amalgamate sponge gold? ",
                             max_length=3000, null=False)
    eight = models.CharField(
        verbose_name="8. Are there issues of cross-borders trade or activities involved in ASGM activities?"
                     " ( If yes please list types of activities, countries... etc) ", max_length=3000, null=False)
    nine = models.CharField(
        verbose_name="9. Are the miners organized in cooperatives? How many cooperatives are registered?",
        max_length=3000, null=False)
    ten = models.CharField(
        verbose_name="10. Are there Small scale gold mining in Nigeria? Do they use mercury? How many companies?",
        max_length=3000, null=False)
    eleven = models.CharField(
        verbose_name="11.  Are there large scale gold mining in Nigeria? Do they use mercury? How many companies?",
        max_length=3000, null=False)
    twelve = models.CharField(
        verbose_name="12. Are any of these companies currently working with ASG miners? Are any in direct conflict "
                     "with ASG miners? ",
        max_length=3000, null=False)
    thirteen = models.CharField(
        verbose_name="13. What is the scale of the impacts the MINING is having on the landscape and other "
                     "environmental media?   ",
        max_length=10, null=False)
    fourteen = models.CharField(
        verbose_name="14. Is there intensive deforestation, conflict with protected areas, land use conflicts with "
                     "farmers, rising unemployment etc.?",
        max_length=100, null=False)
    fifteen = models.CharField(verbose_name="15. Do Miners throw away “dirty” Hg? ", max_length=100, null=False)
    sixteen = models.CharField(verbose_name="16. Is all Hg used released to the environment? ", max_length=100,
                               null=False)
    seventeen = models.CharField(verbose_name="17. What is the available capacity for environmental monitoring? ",
                                 max_length=100, null=False)
    eighteen = models.CharField(
        verbose_name="18. What is the available capacity for human bio-monitoring of mercury exposure? ",
        max_length=100, null=False)
    nineteen = models.CharField(
        verbose_name="19. Do you know current level of environmental contamination (or) exposure? ", max_length=100,
        null=False)
    twenty = models.CharField(
        verbose_name="20. How many environmental media (air, land and water) have been impacted?  ", max_length=100,
        null=False)
    twentyone = models.CharField(
        verbose_name="21. Are there water bodies near mining Sites? Is it used for domestic use e.g drinking? ",
        max_length=100, null=False)
    twentyTwo = models.CharField(
        verbose_name="22. Is it polluted by mining activities?",
        max_length=100, null=False)
    twentyThree = models.CharField(
        verbose_name="23.  Do the communities at the Site engage in high fish consumption levels? ",
        max_length=100, null=False)
    twentyFour = models.CharField(
        verbose_name="24. Are there any communities or areas NEAR MINING SITE or BENEFICIATING SITE considered to be "
                     "particularly impacted or vulnerable to health effects of ASGM?  ",
        max_length=100, null=False)
    twentyFive = models.CharField(
        verbose_name="25. Is any burning of the amalgam in residential areas or burning the amalgam in open areas "
                     "–within 500metres?",
        max_length=10, null=False)
    twentySix = models.CharField(
        verbose_name="26. If yes, are women and children around the open burning?  ",
        max_length=100, null=False)
    twentySeven = models.CharField(
        verbose_name="27. Are there any studies or data on environmental contamination or health impacts from ASGM in "
                     "Nigeria? ",
        max_length=100, null=False)
    twentyEight = models.CharField(verbose_name="28. Do you have an estimate for mercury emissions or releases?  ",
                                   max_length=100, null=False)
    twentyNine = models.CharField(verbose_name="29. What are the estimates (if any)  ", max_length=100, null=False)
    thirty = models.CharField(
        verbose_name="30. Are the miners aware of the health and environmental effects of mercury?  ",
        max_length=100, null=False)
    thirtyOne = models.CharField(
        verbose_name="31. Are miners sensitive to price of mercury OR ARE THEY WORRIED ABOUT THE PRICE OF MERCURY?  ",
        max_length=100, null=False)
    thirtyTwo = models.CharField(verbose_name="32. Does the price of Mercury affect their activities at anytime?  ",
                                 max_length=100, null=False)
    thirtyThree = models.CharField(
        verbose_name="33. Does their mining assist in reducing poverty in the family? ",
        max_length=100, null=False)
    thirtyFour = models.CharField(
        verbose_name="34. Has there been any miner environmental awareness raising campaigns and/or worker health and "
                     "safety campaigns?",
        null=False, max_length=100)
    thirtyFive = models.CharField(
        verbose_name="35. Are there any existing health care or social service programs geared towards the miners "
                     "and/or gold "
                     "processing communities (such as AIDs awareness, health promotion, water sanitation and/or "
                     "worker health and safety programs)? ",
        null=False, max_length=100)
    thirtySix = models.CharField(
        verbose_name="36. Do the miners / mining communities at the Site have adequate access to health care?",
        max_length=100, null=False)

    submitted = models.CharField(verbose_name="submitted",
                            max_length=300, default='', choices=submit_choice, null=True)

    def __str__(self):
        return self.submitted



class Waste(models.Model):
    pass
