from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *


####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_northern_phalanx,1,0), (trp_swadian_peasant,10,0), (trp_northern_marksman,1,0), (trp_northern_guard, 1, 0), (trp_northern_footman, 1, 0), (trp_northern_spearman,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

#North towns
("town_1", "Winterhold", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-67.68, 88.43),[]),
("town_2", "Icehaven", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-14.71, 78.63),[]),
("town_3", "Helgard", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-37.86, 113.8),[]),
("town_4", "Northwatch", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(53.32, 110.38),[]),
("town_5", "Frostpeak", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(2.21, -2.46),[]),

#Ost-Gart Syndicate towns
("town_6", "Merchant's_Bay", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(138.55, 34.17),[]),
("town_7", "Goldbee", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(138.86, -36.34),[]),
("town_8", "Caravanserai", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-89.16, 56.72),[]),
("town_9", "Welsburg", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(37.85, -76.46),[]),
("town_10", "Coinstead", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-76.93, -2.33),[]),

#Kara-Thar towns 
("town_11", "Obsidian_Citadel", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(81.76, 43.82),[]),
("town_12", "Shadow_Cage", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(9.27, -106.06),[]),
("town_13", "Voidspire", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-49.11, 14.48),[]),                        

#Ashkar towns
("town_14", "Jafar-Abad", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(13.35, 107.38),[]),
("town_15", "Mirage", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-20.14, 34.51),[]),
("town_16", "Whispersands", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(115.50, 13.56),[]),
("town_17", "Sahar-Dun", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(43.24, -27.55),[]),
("town_18", "Ashkai", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(128.23, -76.09),[]),

#Solmark Inquisition towns
("town_19", "Sanctum", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-62.50, -65.18),[]),
("town_20", "Oldtown", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-29.53, -32.38),[]),
("town_21", "Moonport", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(88.72, 12.73),[]),
("town_22", "Bronzegate", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-117.31, -108.74),[]),

#Union of Eirven towns
("town_23", "Eir-Glen", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(167.81, -96.32),[]),
("town_24", "Mosscliff", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(-78.54, -85.42),[]),                           
("town_25", "Eldergrove", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(-132.56, 7.10),[]),
("town_26", "Highmist", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(33.36, -109.21),[]),

#Kingdom of Vallor towns
("town_27", "Asteria", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(-92.58, -60.81),[]),
("town_28", "Sunreach", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(100.67, -119.18),[]),
("town_29", "Silverpeak", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(112.57, 105.10),[]),
("town_30", "Argenthold", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(-104.68, 75.99),[]),                          
("town_31", "Saltcliffe", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(89.70, -92.93),[]),

#----------------------------------
#North Castles
("castle_1", "The_Twins", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.59, 42.52),[]),
("castle_2", "Torrhen's_Square", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131.03, 84.03),[]),
("castle_3", "Last_Hearth", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.07, 104.21),[]),
("castle_4", "Deepwood_Motte", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.63, 85.30),[]),
("castle_5", "Dreadfort", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.46, 109.37),[]),
("castle_6", "Moat_Cailin", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.34, 57.05),[]),
("castle_7", "Hammerhorn", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.80, -105.25),[]),

#Ost-Gart castles
("castle_8", "Starfall", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.55, -81.26),[]),
("castle_9", "Casterly_Rock", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160.16, 25.27),[]),
("castle_10", "Riverrun", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.95, 23.55),[]),                      #[swycartographr] prev. coords: (-114.72, 19.85)
("castle_11", "Brightwater_Keep", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.50, -46.76),[]),
("castle_12", "Pinkmaiden", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.11, -60.25),[]),
("castle_13", "Atranta", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130.16, 36.54),[]),
("castle_14", "Godsgrace", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.31, -72.18),[]),                   

#Kara-Thar castles
("castle_15", "Pyke", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.86, 22.17),[]),
("castle_16", "Sandstone", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.80, -88.43),[]),                       
("castle_17", "Cider_Hall", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.56, -56.74),[]),
("castle_18", "Claw_Isle", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.51, 70.20),[]),
("castle_19", "Runestone", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.74, -26.27),[]),
("castle_20", "Evenfall_Hall", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.28, 23.68),[]),
("castle_21", "Deep_Den", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.33, -6.18),[]),

#Ashkar castles
("castle_22", "Coldwater_Burn", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.82, -32.17),[]),
("castle_23", "Crakehell", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(174.31, -18.66),[]),
("castle_24", "Tarth_Keep", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.23, 59.17),[]),
("castle_25", "Driftmark", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.30, 109.66),[]),
("castle_26", "Harrenhal", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.12, 118.99),[]),
("castle_27", "Antlers", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.40, 40.37),[]),
("castle_28", "Kayce_Keep", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.94, -42.28),[]),

#Solmark castles
("castle_29", "Yronwood", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.47, -57.90),[]),
("castle_30", "Strongsong", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.35, -46.43),[]),                     #[swycartographr] prev. coords: (48.36, -46.99)
("castle_31", "Rain_House", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.58, 55.26),[]),
("castle_32", "Hornvale", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.15, -3.70),[]),
("castle_33", "Sea_Dragon_Cove", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.07, 16.25),[]),
("castle_34", "Dragonstone", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.81, 121.54),[]),
("castle_35", "Stonehelm", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.78, -3.18),[]),

#Eirven castles
("castle_36", "Trident_Ford", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.14, -47.43),[]),
("castle_37", "Stormlands_Watch", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.12, 44.98),[]),
("castle_38", "Harlaw_Hall", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.19, -106.03),[]),
("castle_39", "Karhold", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.12, 74.30),[]),
("castle_40", "The_Eyrie", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.7, -22.12),[]),                      #[swycartographr] prev. coords: (77.98, -13.36)
("castle_41", "Grey_Garden", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.28, -68.73),[]),
("castle_42", "Ironoaks", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.77, -48.99),[]),                       #[swycartographr] prev. coords: (65.75, -43.36)

#Vallor castles
("castle_43", "Longbow_Hall", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.20, -9.11),[]),                    #[swycartographr] prev. coords: (40.2, 8.02)
("castle_44", "Redfort", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.11, -8.93),[]),
("castle_45", "Long_Lake_Fort", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.18, -0.44),[]),
("castle_46", "Ninestars", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.70, 6.75),[]),                        #[swycartographr] prev. coords: (46.7, -10.72)
("castle_47", "Sharp_Point", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.24, 84.02),[]),
("castle_48", "Hornwood", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.81, 83.92),[]),
("castle_49", "Bear_Island_Keep", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.22, 90.73),[]),
("castle_50", "Rook's_Rest", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.17, 93.74),[]),


("village_1", "Tumbleton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.29, -49.94),[]),
("village_2", "Brindlewood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.34, 68.26),[]),
("village_3", "Nightfort_Ruins", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.02, 49.13),[]),
("village_4", "Pebble_Shore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166.74, -73.45),[]),
("village_5", "Hornwood_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.22, 98.51),[]),
("village_6", "Sow's_Horn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.84, 81.23),[]),
("village_7", "Westerridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.90, -24.04),[]),
("village_8", "Wickenden", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.63, 1.25),[]),
("village_9", "Blackhaven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.82, -111.84),[]),                
("village_10", "Highpath", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.53, -51.93),[]),
("village_11", "Harlaw_Port", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.07, -124.30),[]),
("village_12", "Felwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.32, 32.15),[]),
("village_13", "Windridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.36, 103.29),[]),
("village_14", "Bloodorange_Grove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.77, 83.54),[]),
("village_15", "Castamere_Ruins", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.05, 18.26),[]),
("village_16", "Blackwood_Grove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.92, -3.66),[]),
("village_17", "Plowman's_Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.58, 65.25),[]),
("village_18", "Drake's_Landing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.25, 91.06),[]),
("village_19", "Tarbeck", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156.38, 12.84),[]),
("village_20", "Skyreach", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.3, -46.59),[]),                     #[swycartographr] prev. coords: (56.49, -51.77)
("village_21", "Bitterbridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.13, -40.43),[]),
("village_22", "Reedmarsh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.00, 67.44),[]),
("village_23", "Brackenford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.88, 6.48),[]),                  #[swycartographr] prev. coords: (-83.73, 7.08)
("village_24", "Rainwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.82, 17.4),[]),                   
("village_25", "Saltstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.94, -110.04),[]),
("village_26", "Parchfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.42, 36.82),[]),
("village_27", "Blue_Fork", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.48, 12.48),[]),
("village_28", "Moon's_Brook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.38, -49.75),[]),
("village_29", "Darry", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.10, 51.55),[]),
("village_30", "Great_Wyk_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.27, -79.53),[]),
("village_31", "Squiddly", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.08, -117.28),[]),
("village_32", "Cracklaw_Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.03, 60.57),[]),
("village_33", "Saltpans", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.23, 2.85),[]),
("village_34", "Paynesford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(163.48, 19.63),[]),
("village_35", "Clawford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.35, 120.69),[]),
("village_36", "Ramsgate", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.40, 100.70),[]),
("village_37", "Rossfoss", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.23, -60.55),[]),
("village_38", "Greenfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125.73, 13.43),[]),
("village_39", "Acorn_Hall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.37, 10.85),[]),
("village_40", "Lion's_Roost", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(147.38, -15.46),[]),
("village_41", "Silverstream", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.72, -31.26),[]),
("village_42", "Greywater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.03, -27.13),[]),
("village_43", "Redbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.05, 29.44),[]),
("village_44", "Lann's_Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.04, 29.57),[]),
("village_45", "Darryford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.91, 23.41),[]),
("village_46", "Brightwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125.16, 1.50),[]),
("village_47", "Lannett", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.67, -38.57),[]),
("village_48", "Bloody_Gate", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.54, 13.09),[]),
("village_49", "Falcon's_Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.49, 3.71),[]),
("village_50", "Flint's_Finger", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(111.41, 96.44),[]),
("village_51", "Ice_River", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128.40, 75.10),[]),
("village_52", "White_Knife", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.75, 108.61),[]),
("village_53", "Blackpool", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.07, 98.75),[]),
("village_54", "Orkmont", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(161.23, -88.59),[]),
("village_55", "Sealskin", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.43, -111.68),[]),
("village_56", "Longboat_Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.80, -126.38),[]),
("village_57", "Driftwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.68, -75.53),[]),
("village_58", "Old_Wyk", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.20, -69.05),[]),
("village_59", "Wreckage_Bay", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.79, -103.93),[]),
("village_60", "Wavebreaker", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.82, -106.76),[]),
("village_61", "Thresher's_Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.97, -106.07),[]),
("village_62", "Queenscrown", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.64, 48.79),[]),
("village_63", "Mole's_Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.92, 61.11),[]),
("village_64", "Castle_Cerwyn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.10, 70.82),[]),
("village_65", "Greenstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.99, 18.06),[]),                  
("village_66", "Red_Watch", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.06, 6.86),[]),                    
("village_67", "Ironshore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.63, -122.50),[]),
("village_68", "Baratheon's_Ford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.99, -6.32),[]),            
("village_69", "Three_Towers", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.49, -40.32),[]),
("village_70", "Fossoway_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.78, -62.30),[]),
("village_71", "Honeyholt", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.13, -22.99),[]),
("village_72", "Stone_Door", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.31, 13.40),[]),
("village_73", "Arryn_Vale", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.28, -36.75),[]),
("village_74", "Longvalley", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.53, -59.53),[]),
("village_75", "Horn_Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.95, -61.33),[]),
("village_76", "Mallister's_Landing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.35, 6.08),[]),
("village_77", "Harren's_Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.82, 6.73),[]),
("village_78", "Trident_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.97, 15.73),[]),
("village_79", "Green_Fork", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.66, 33.3),[]),                  #[swycartographr] prev. coords: (-125.88, 19.93)
("village_80", "Falcon's_Brook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.15, 32.1),[]),              #[swycartographr] prev. coords: (-136.03, 31.49)
("village_81", "Oldstones", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.89, 40.13),[]),
("village_82", "Stone_Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.96, 54.84),[]),
("village_83", "Frey's_Crossing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.02, 47.66),[]),
("village_84", "Blackwater_Rush", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.58, 109.46),[]),
("village_85", "Targaryen's_Ford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.58, 114.76),[]),
("village_86", "Summerhall_Ashes", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.07, 112.72),[]),
("village_87", "Bywater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.28, 112.62),[]),
("village_88", "Frosthollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.69, 111.56),[]),
("village_89", "Summerhall_Ruins", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.17, 109.38),[]),
("village_90", "Lemonwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.76, -107.43),[]),
("village_91", "Dornish_March", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.90, -74.30),[]),               
("village_92", "Skyfall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.06, -67.21),[]),
("village_93", "Vaith", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.61, -90.32),[]),                     
("village_94", "Red_Dunes", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.7, -67.30),[]),                   
("village_95", "Water_Gardens", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.61, -60.06),[]),
("village_96", "Kingswood_Edge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.97, -80.85),[]),            
("village_97", "Lightning's_Reach", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.66, -21.26),[]),          
("village_98", "Connington", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.34, 43.47),[]),
("village_99", "Stormwatch", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.17, 38.50),[]),
("village_100", "Cape_Wrath", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.02, -90.77),[]),                  
("village_101", "Gods_Eye_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.24, 20.50),[]),            #[swycartographr] prev. coords: (-82.76, 20.5)
("village_102", "Sarsfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.39, -102.69),[]),                
("village_103", "Red_Fork_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.45, -72.9),[]),         
("village_104", "Raventree", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.22, 5.60),[]),
("village_105", "Flea_Bottom", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.03, 81.01),[]),
("village_106", "Wendwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.58, 61.42),[]),
("village_107", "High_Hollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.37, -27.89),[]),
("village_108", "Pendric", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.58, 4.97),[]),
("village_109", "Tully's_Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.84, 13.26),[]),               #[swycartographr] prev. coords: (-102.66, 28.62)
("village_110", "Weeping_Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.29, 45.02),[]),
("village_111", "Massey's_Hook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.71, 70.61),[]),
("village_112", "Mallery", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.78, 83.04),[]),
("village_113", "Grandview", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.22, 66.69),[]),
("village_114", "Timberton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.06, -125.26),[]),
("village_115", "Goldenfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.68, -3.28),[]),
("village_116", "Crannog_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.17, 80.34),[]),
("village_117", "Bolton's_Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.53, 76.42),[]),
("village_118", "Glover's_Grove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.71, 67.48),[]),
("village_119", "Umberford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.68, 80.08),[]),
("village_120", "Stony_Shore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.32, 97.10),[]),
("village_121", "Sea_Dragon_Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.85, 88.94),[]),
("village_122", "Rillwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.57, 83.11),[]),
("village_123", "Gates_of_the_Moon", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.28, -11.59),[]),
("village_124", "Salt_Shore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.40, -97.96),[]),
("village_125", "Stonecrag", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.65, -7.77),[]),
("village_126", "SixSeven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.47, 85.97),[]),                 
("village_127", "Buhalovo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.72, 75.34),[]),                  
("village_128", "Mertyns", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.81, 49.20),[]),
("village_129", "Nightsong", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.86, 15.00),[]),
("village_130", "Whispering_Wood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.27, 30.49),[]),
("village_131", "Wolfswood_Edge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.22, 114.84),[]),
("village_132", "Wintertown", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.49, 123.23),[]),
("village_133", "Parchments", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.6, -1.50),[]),                   #[swycartographr] prev. coords: (94.74, -1.5)
("village_134", "Oakenshield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.37, 31.82),[]),
("village_135", "Drowned_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.17, -97.98),[]),
("village_136", "Kraken'_Teeth", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.36, -56.86),[]),
("village_137", "Nagga's_Crag", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.42, -78.03),[]),
("village_138", "Grey_King's_Landing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.91, -124.93),[]),
("village_139", "Black_Tide", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.21, -107.19),[]),
("village_140", "Stonehouse", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.00, -79.06),[]),
("village_141", "Norton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.85, -77.05),[]),
("village_142", "Roycebridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.53, -0.09),[]),
("village_143", "Iron_Holt", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(173.94, -90.50),[]),
("village_144", "Swyft_Hollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168.80, -10.28),[]),
("village_145", "Long_Lake", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.41, 93.18),[]),
("village_146", "Longtable", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.89, -55.17),[]),
("village_147", "Brimstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.67, -86.49),[]),


  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.4, 102.8),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.8, 33),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.5, 72.0),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.5, -75.2),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.8, 12.5),[], 100),


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.37, 65.10),[], -44.8),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.44, 77.88),[], 4.28),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.87, 87.95),[], 64.5),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.71, 62.13),[], -2.13),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.02, 72.61),[], 21.5),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.83, 52.24),[], -73.5),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.79, 76.84),[], -64),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.05, -6),[], 1.72),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.95, -9.60),[], -33.76),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.32, -75.27),[], -44.07),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.39, 67.82),[], 81.3),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.33, -1.94),[], -35.5),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.02, -7),[], -17.7),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.36, 75.8),[], 66.6),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-90, -26.8),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.5, 110),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the desert",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(110, -100),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
