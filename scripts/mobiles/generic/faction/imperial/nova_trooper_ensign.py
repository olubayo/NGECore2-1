import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from resources.datatables import FactionStatus
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('stormtrooper_novatrooper_ensign')
	mobileTemplate.setLevel(81)
	mobileTemplate.setDifficulty(Difficulty.ELITE)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("imperial")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(False)
	mobileTemplate.setFaction("imperial")
	mobileTemplate.setFactionStatus(FactionStatus.Combatant)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_stormtrooper_black_black.iff')
	templates.add('object/mobile/shared_dressed_stormtrooper_black_blue.iff')
	templates.add('object/mobile/shared_dressed_stormtrooper_black_gold.iff')
	templates.add('object/mobile/shared_dressed_stormtrooper_black_green.iff')
	templates.add('object/mobile/shared_dressed_stormtrooper_black_grey.iff')
	templates.add('object/mobile/shared_dressed_stormtrooper_black_red.iff')	
	templates.add('object/mobile/shared_dressed_stormtrooper_black_white.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/carbine/shared_carbine_e11.iff', WeaponType.CARBINE, 1.0, 15, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('novatrooper_ensign', mobileTemplate)
	return