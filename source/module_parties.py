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

  ("temp_party_autobattle_player","{!}temp_party_autobattle",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("temp_party_autobattle_ally","{!}temp_party_autobattle",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("temp_party_autobattle_enemy","{!}temp_party_autobattle",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
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

  ("town_1", "Winterhold", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-180.94, -234.86),[]),
  ("town_2", "Icehaven", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-40.65, -260.21),[]),
  ("town_3", "Helgard", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-27.42, -142.47),[]),
  ("town_4", "Northwatch", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(50.85, -219.17),[]),
  ("town_5", "Frostpeak", icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-139.93, -183.45),[]),
  
  #Ost-Gart Syndicate towns
  ("town_6", "Merchant's_Bay", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-179.58, -15.28),[]),
  ("town_7", "Goldbee", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-22.65, -65.35),[]),
  ("town_8", "Caravanserai", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-145.78, -85.33),[]),
  ("town_9", "Welsburg", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-116.81, 12.45),[]),
  ("town_10", "Coinstead", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-75.98, -30.21),[]),

  #Kara-Thar towns 
  ("town_11", "Obsidian_Citadel", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-145.24, 63.06),[]),
  ("town_12", "Shadow_Cage", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-131.63, 113.60),[]),
  ("town_13", "Voidspire", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-80.35, 38.79),[]),                        

  #Ashkar towns
  ("town_14", "Jafar-Abad", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(51.61, 233.15),[]),
  ("town_15", "Mirage", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(26.35, 132.47),[]),
  ("town_16", "Whispersands", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-63.54, 139.75),[]),
  ("town_17", "Sahar-Dun", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-100.84, 235.61),[]),
  ("town_18", "Ashkai", icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(8.63, 215.74),[]),

  #Solmark Inquisition towns
  ("town_19", "Sanctum", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(154.93, 144.66),[]),
  ("town_20", "Oldtown", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(148.07, 81.02),[]),
  ("town_21", "Moonport", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(204.50, 134.09),[]),
  ("town_22", "Bronzegate", icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(51.05, 90.34),[]),

  #Union of Eirven towns
  ("town_23", "Eir-Glen", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(126.58, -146.87),[]),
  ("town_24", "Mosscliff", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(168.48, -73.38),[]),                           
  ("town_25", "Eldergrove", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(60.49, -114.79),[]),
  ("town_26", "Highmist", icon_town|pf_town, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(179.73, -174.13),[]),

  #Kingdom of Vallor towns
  ("town_27", "Asteria", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(12.54, 23.29),[]),
  ("town_28", "Sunreach", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(168.28, -15.09),[]),
  ("town_29", "Silverpeak", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(49.94, -25.54),[]),
  ("town_30", "Argenthold", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(8.60, 80.09),[]),                          
  ("town_31", "Saltcliffe", icon_town|pf_town, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(80.09, 43.41),[]),

  #----------------------------------
  #North Castles
  ("castle_1", "The_Twins", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-125.67, -202.46),[]),
  ("castle_2", "Torrhen's_Square", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-131.42, -225.19),[]),
  ("castle_3", "Last_Hearth", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-116.82, -256.34),[]),
  ("castle_4", "Deepwood_Motte", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-58.11, -197.08),[]),
  ("castle_5", "Dreadfort", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(79.60, -255.66),[]),
  ("castle_6", "Moat_Cailin", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-29.95, -283.05),[]),
  ("castle_7", "Hammerhorn", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-65.06, -245.47),[]),
  ("castle_51", "Blackstone_Keep", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(-87.71, -200.57),[]),


  #Ost-Gart castles
  ("castle_8", "Starfall", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-154.12, 15.85),[]),
  ("castle_9", "Casterly_Rock", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-133.32, -39.09),[]),
  ("castle_10", "Riverrun", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-99.19, -56.06),[]),                      #[swycartographr] prev. coords: (-114.72, 19.85)
  ("castle_11", "Brightwater_Keep", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-48.57, 23.88),[]),
  ("castle_12", "Pinkmaiden", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-43.94, -84.72),[]),
  ("castle_13", "Atranta", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-41.21, -39.23),[]),
  ("castle_14", "Godsgrace", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-162.17, -49.08),[]),                   

  #Kara-Thar castles
  ("castle_15", "Pyke", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-162.82, 103.67),[]),
  ("castle_16", "Sandstone", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-103.07, 121.06),[]),                       
  ("castle_17", "Cider_Hall", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-70.82, 99.20),[]),
  ("castle_18", "Claw_Isle", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-86.00, 72.37),[]),
  ("castle_19", "Runestone", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-50.64, 54.90),[]),
  ("castle_20", "Evenfall_Hall", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-42.69, 74.61),[]),
  ("castle_21", "Deep_Den", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-122.75, 48.86),[]),
  ("castle_53", "Ironhold", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(-97.81, 96.54),[]),


  #Ashkar castles
  ("castle_22", "Coldwater_Burn", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(45.64, 180.65),[]),
  ("castle_23", "Crakehell", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-22.03, 126.05),[]),
  ("castle_24", "Tarth_Keep", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-34.86, 186.40),[]),
  ("castle_25", "Driftmark", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-9.19, 175.76),[]),
  ("castle_26", "Harrenhal", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-123.48, 242.93),[]),
  ("castle_27", "Antlers", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-84.04, 160.94),[]),
  ("castle_28", "Kayce_Keep", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(92.11, 220.43),[]),
  ("castle_52", "Ravenwatch", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(-70.50, 260.81),[]),


  #Solmark castles
  ("castle_29", "Yronwood", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(110.63, 139.80),[]),
  ("castle_30", "Strongsong", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(104.88, 91.92),[]),                     #[swycartographr] prev. coords: (48.36, -46.99)
  ("castle_31", "Rain_House", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(124.07, 65.94),[]),
  ("castle_32", "Hornvale", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(66.57, 58.48),[]),
  ("castle_33", "Sea_Dragon_Cove", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(67.11, 117.81),[]),
  ("castle_34", "Dragonstone", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(100.16, 75.10),[]),
  ("castle_35", "Stonehelm", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(120.70, 38.65),[]),

  #Eirven castles
  ("castle_36", "Trident_Ford", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(149.36, -170.34),[]),
  ("castle_37", "Stormlands_Watch", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(125.26, -183.93),[]),
  ("castle_38", "Harlaw_Hall", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(171.40, -141.10),[]),
  ("castle_39", "Karhold", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(107.86, -129.75),[]),
  ("castle_40", "The_Eyrie", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(91.30, -151.63),[]),                      #[swycartographr] prev. coords: (77.98, -13.36)
  ("castle_41", "Grey_Garden", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(136.64, -118.49),[]),
  ("castle_42", "Ironoaks", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(84.26, -113.48),[]),                       #[swycartographr] prev. coords: (65.75, -43.36)

  #Vallor castles
  ("castle_43", "Longbow_Hall", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(-25.91, 100.07),[]),                    #[swycartographr] prev. coords: (40.2, 8.02)
  ("castle_44", "Redfort", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(52.15, 24.65),[]),
  ("castle_45", "Long_Lake_Fort", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(108.41, -37.93),[]),
  ("castle_46", "Ninestars", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(119.08, -8.74),[]),                        #[swycartographr] prev. coords: (46.7, -10.72)
  ("castle_47", "Sharp_Point", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(139.64, -46.61),[]),
  ("castle_48", "Hornwood", icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(25.11, 53.56),[]),
  ("castle_49", "Bear_Island_Keep", icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(90.26, 2.67),[]),
  ("castle_50", "Rook's_Rest", icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(76.81, -54.61),[]),



#Villages for castles
  #North villages
  ("village_1", "Tumbleton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.84, -229.24),[]),
  ("village_2", "Brindlewood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.46, -235.04),[]),
  ("village_3", "Nightfort_Ruins", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.48, -263.54),[]),
  ("village_4", "Pebble_Shore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.44, -253.73),[]),
  ("village_5", "Hornwood_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.47, -204.87),[]),
  ("village_6", "Sow's_Horn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.33, -190.03),[]),
  ("village_7", "Westerridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.30, -208.96),[]),
  
  ("village_51", "Ice_River", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.29, -196.76),[]),
  ("village_52", "White_Knife", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.66, -239.22),[]),
  ("village_53", "Blackpool", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.03, -246.37),[]),
  ("village_54", "Orkmont", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.74, -289.89),[]),
  ("village_55", "Sealskin", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.70, -284.15),[]),
  ("village_56", "Longboat_Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.97, -187.82),[]),
  ("village_57", "Driftwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.58, -191.67),[]),
  ("village_58", "Old_Wyk", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.13, -156.47),[]),

  
  #Ost-Gart villages
  ("village_8", "Wickenden", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.52, -49.40),[]),
  ("village_9", "Blackhaven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.09, 12.66),[]),                
  ("village_10", "Highpath", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.31, -56.44),[]),
  ("village_11", "Harlaw_Port", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.74, -63.32),[]),
  ("village_12", "Felwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.74, -62.23),[]),
  ("village_13", "Windridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.87, 6.07),[]),
  ("village_14", "Bloodorange_Grove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.38, -61.11),[]),
  
  ("village_59", "Wreckage_Bay", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.87, -29.41),[]),
  ("village_60", "Wavebreaker", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.20, -44.43),[]),
  ("village_61", "Thresher's_Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.69, 25.85),[]),
  ("village_62", "Queenscrown", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.46, 13.42),[]),
  ("village_63", "Mole's_Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.51, -91.34),[]),
  ("village_64", "Castle_Cerwyn", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.77, -87.35),[]),
  ("village_65", "Greenstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.34, -30.21),[]),                  

  
  #Kara-Thar villages
  ("village_15", "Castamere_Ruins", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.63, 58.18),[]),
  ("village_16", "Blackwood_Grove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.81, 50.38),[]),
  ("village_17", "Plowman's_Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.65, 97.68),[]),
  ("village_18", "Drake's_Landing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.67, 104.52),[]),
  ("village_19", "Tarbeck", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.79, 79.94),[]),
  ("village_20", "Skyreach", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.90, 63.78),[]),                     #[swycartographr] prev. coords: (56.49, -51.77)
  ("village_21", "Bitterbridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.90, 63.78),[]),
  
  ("village_66", "Red_Watch", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.80, 96.73),[]),                    
  ("village_67", "Ironshore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.10, 113.97),[]),
  ("village_68", "Baratheon's_Ford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.70, 114.94),[]),            
  ("village_69", "Three_Towers", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.81, 121.36),[]),
  ("village_70", "Fossoway_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.54, 47.91),[]),
  ("village_71", "Honeyholt", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.08, 65.74),[]),
  ("village_72", "Stone_Door", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.30, 65.68),[]),
  ("village_73", "Arryn_Vale", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.06, 101.08),[]),
 
  
  #Ashkar villages
  ("village_22", "Reedmarsh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.31, 162.86),[]),
  ("village_23", "Brackenford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.62, 178.58),[]),                  #[swycartographr] prev. coords: (-83.73, 7.08)
  ("village_24", "Rainwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.89, 210.83),[]),                   
  ("village_25", "Saltstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.43, 201.83),[]),
  ("village_26", "Parchfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.72, 252.50),[]),
  ("village_27", "Blue_Fork", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.59, 259.36),[]),
  ("village_28", "Moon's_Brook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.40, 220.75),[]),
  
  ("village_74", "Longvalley", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-152.56, 240.70),[]),
  ("village_75", "Horn_Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.40, 173.29),[]),
  ("village_76", "Mallister's_Landing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.49, 174.91),[]),
  ("village_77", "Harren's_Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.05, 141.90),[]),
  ("village_78", "Trident_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.16, 126.30),[]),
  ("village_79", "Green_Fork", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.66, 183.35),[]),                  #[swycartographr] prev. coords: (-125.88, 19.93)
  ("village_80", "Falcon's_Brook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.24, 170.00),[]),              #[swycartographr] prev. coords: (-136.03, 31.49)
  ("village_81", "Oldstones", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(203.95, 142.65),[]),

  
  #Solmark villages
  ("village_29", "Darry", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.05, 112.83),[]),
  ("village_30", "Great_Wyk_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.42, 117.85),[]),
  ("village_31", "Squiddly", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.66, 98.31),[]),
  ("village_32", "Cracklaw_Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.19, 102.58),[]),
  ("village_33", "Saltpans", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.50, 146.15),[]),
  ("village_34", "Paynesford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.65, 136.84),[]),
  ("village_35", "Clawford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.61, 117.31),[]),
  
  ("village_82", "Stone_Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.62, 142.44),[]),
  ("village_83", "Frey's_Crossing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.95, 64.41),[]),
  ("village_84", "Blackwater_Rush", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.40, 58.23),[]),
  ("village_85", "Targaryen's_Ford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.29, 71.70),[]),
  ("village_86", "Summerhall_Ashes", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.34, 80.93),[]),
  ("village_87", "Bywater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.04, 28.29),[]),
  ("village_88", "Frosthollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.26, 30.90),[]),

  
  #Eirven villages
  ("village_36", "Ramsgate", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131.01, -193.98),[]),
  ("village_37", "Rossfoss", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(119.75, -170.20),[]),
  ("village_38", "Greenfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(179.12, -129.76),[]),
  ("village_39", "Acorn_Hall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(182.34, -142.52),[]),
  ("village_40", "Lion's_Roost", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.74, -106.04),[]),
  ("village_41", "Silverstream", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.18, -105.25),[]),
  ("village_42", "Greywater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.02, -150.81),[]),
  
  ("village_89", "Summerhall_Ruins", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.71, -141.78),[]),
  ("village_90", "Lemonwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.06, -129.91),[]),
  ("village_91", "Dornish_March", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.17, -146.26),[]),               
  ("village_92", "Skyfall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.50, -176.00),[]),
  
  #Vallor villages
  ("village_43", "Redbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.45, 89.12),[]),
  ("village_44", "Lann's_Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.35, 101.28),[]),
  ("village_45", "Darryford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.64, 45.33),[]),
  ("village_46", "Brightwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.44, 55.65),[]),
  ("village_47", "Lannett", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.44, 35.98),[]),
  ("village_48", "Bloody_Gate", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.61, 24.21),[]),
  ("village_49", "Falcon's_Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.26, -6.25),[]),
  ("village_50", "Flint's_Finger", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.86, 13.92),[]),
  

  ("village_93", "Vaith", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.82, -9.18),[]),                     
  ("village_94", "Red_Dunes", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.28, -19.94),[]),                   
  ("village_95", "Water_Gardens", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.54, -40.54),[]),
 
  
 
  #Villages for castles
       
  #Villages for towns
  #5 vil on town
  #Coinstead
  ("village_96", "Kingswood_Edge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.53, -43.03),[]),            
  ("village_97", "Lightning's_Reach", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.19, -39.08),[]),          
  ("village_98", "Connington", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.42, -14.60),[]),
  ("village_99", "Stormwatch", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.90, -14.66),[]),
  ("village_100", "Cape_Wrath", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.46, -0.62),[]),       
  
  #4 vil on town   
  #Welsburg        
  ("village_101", "Gods_Eye_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.34, 2.94),[]),            #[swycartographr] prev. coords: (-82.76, 20.5)
  ("village_102", "Sarsfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.59, -6.06),[]),                
  ("village_103", "Red_Fork_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.73, 5.65),[]),         
  ("village_104", "Raventree", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.96, 15.83),[]),
  #Obsidian_Citadel
  ("village_105", "Flea_Bottom", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.27, 78.78),[]),
  ("village_106", "Wendwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.54, 55.60),[]),
  ("village_107", "High_Hollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.36, 71.94),[]),
  ("village_108", "Pendric", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.37, 83.75),[]),
  #Jafar-Abad
  ("village_109", "Tully's_Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.96, 225.68),[]),               #[swycartographr] prev. coords: (-102.66, 28.62)
  ("village_110", "Weeping_Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.76, 202.52),[]),
  ("village_111", "Massey's_Hook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.31, 200.37),[]),
  ("village_112", "Mallery", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.08, 221.83),[]),
  #Asteria
  ("village_113", "Grandview", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.18, 29.80),[]),
  ("village_114", "Timberton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.55, 23.07),[]),
  ("village_115", "Goldenfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.88, 39.17),[]),
  ("village_116", "Crannog_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.83, 45.49),[]),
  #Sanctum
  ("village_117", "Bolton's_Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(158.76, 155.72),[]),
  ("village_118", "Glover's_Grove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.62, 157.67),[]),
  ("village_119", "Umberford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.81, 136.08),[]),
  ("village_120", "Stony_Shore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(169.65, 132.68),[]),
  
  #2 vil on town
  #Northwatch
  ("village_121", "Sea_Dragon_Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.52, -232.12),[]),
  ("village_122", "Rillwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.42, -212.29),[]),
  #Sahar-Dun
  ("village_123", "Gates_of_the_Moon", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.58, 222.83),[]),
  ("village_124", "Salt_Shore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.01, 259.62),[]),
  
  #3 vil on town
  #North
  ("village_125", "Stonecrag", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.80, -253.98),[]),
  ("village_126", "SixSeven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.97, -263.26),[]),                 
  ("village_127", "Buhalovo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.62, -246.92),[]),                  
  ("village_128", "Mertyns", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.30, -136.67),[]),
  ("village_129", "Nightsong", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.84, -134.87),[]),
  ("village_130", "Whispering_Wood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.31, -163.33),[]),
  ("village_131", "Wolfswood_Edge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.44, -185.20),[]),
  ("village_132", "Wintertown", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.65, -168.16),[]),
  ("village_133", "Parchments", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.16, -157.37),[]),                   #[swycartographr] prev. coords: (94.74, -1.5)
  ("village_134", "Oakenshield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.66, -214.12),[]),
  ("village_135", "Drowned_Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.08, -229.32),[]),
  ("village_136", "Kraken'_Teeth", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.85, -208.17),[]),
  #Ost-Gart
  ("village_137", "Nagga's_Crag", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.82, -86.77),[]),
  ("village_138", "Grey_King's_Landing", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.80, -75.12),[]),
  ("village_139", "Black_Tide", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.16, -50.56),[]),
  ("village_140", "Stonehouse", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.18, -77.93),[]),
  ("village_141", "Norton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.93, -95.77),[]),
  ("village_142", "Roycebridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.09, -69.25),[]),
  ("village_143", "Iron_Holt", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.08, -7.27),[]),
  ("village_144", "Swyft_Hollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.69, -15.71),[]),
  ("village_145", "Long_Lake", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.32, -12.06),[]),
  ("village_146", "Longtable", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.48, -74.02),[]),
  #Kara-Thar
  ("village_147", "Brimstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-134.94, 101.34),[]),
  ("village_148", "Stonehaven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.29, 100.59),[]),
  ("village_149", "Oakridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.34, 117.64),[]),
  ("village_150", "Ashford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.66, 38.90),[]),
  ("village_151", "Ravenmoor", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.25, 47.90),[]),
  ("village_152", "Ironhill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.01, 37.95),[]),
  #Ashkar
  ("village_153", "Goldbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.64, 145.09),[]),
  ("village_154", "Westvale", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.31, 160.25),[]),
  ("village_155", "Eastmere", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.77, 146.23),[]),
  ("village_156", "Pinewatch", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.17, 140.01),[]),
  ("village_157", "Deepwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.43, 123.82),[]),
  ("village_158", "Brightwater", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.10, 194.93),[]),
  ("village_159", "Mistfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.35, 210.40),[]),
  ("village_160", "Wolfden", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.90, 185.40),[]),
  ("village_161", "Redcliff", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.52, 146.40),[]),
  #Solmark
  ("village_162", "Highrock", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.55, 100.31),[]),
  ("village_163", "Greenhollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168.62, 98.24),[]),
  ("village_164", "Blackford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.48, 67.35),[]),
  ("village_165", "Silverbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.99, 45.86),[]),
  ("village_166", "Thornfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.46, 58.92),[]),
  ("village_167", "Fairmeadow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.21, 53.57),[]),
  ("village_168", "Frostholm", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.21, 94.72),[]),
  ("village_169", "Stormridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.38, 80.20),[]),
  ("village_170", "Kingswell", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.21, 97.33),[]),
  #Eirven
  ("village_171", "Cedarcross", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(175.76, -82.48),[]),
  ("village_172", "Rivergate", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(176.34, -93.43),[]),
  ("village_173", "Ashbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.31, -95.07),[]),
  ("village_174", "Oakridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(178.46, -163.58),[]),
  ("village_175", "Stoneford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.69, -159.43),[]),
  ("village_176", "Wolfden", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(177.48, -189.61),[]),
  ("village_177", "Blackmere", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.36, -155.62),[]),
  ("village_178", "Greyhill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.01, -138.94),[]),
  ("village_179", "Ravenmoor", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.11, -141.32),[]),
  ("village_180", "Thornfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.84, -153.25),[]),
  ("village_181", "Redbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.58, -109.96),[]),
  ("village_182", "Greenhollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.66, -128.84),[]),
  #Vallor
  ("village_183", "Elmwatch", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(179.71, -29.06),[]),
  ("village_184", "Ironwell", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(161.05, -28.00),[]),
  ("village_185", "Mistwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(148.62, -10.98),[]),
  ("village_186", "Highmead", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.52, -13.81),[]),
  ("village_187", "Deepford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.07, -27.88),[]),
  ("village_188", "Kingsbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.41, -11.92),[]),
  ("village_189", "Falconrest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.50, -51.13),[]),
  ("village_190", "Birchvale", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.33, 75.07),[]),
  ("village_191", "Silverbrook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.49, 103.13),[]),
  ("village_192", "Westmere", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.65, 92.77),[]),
  ("village_193", "Coldharbor", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(144.96, -42.20),[]),
  ("village_194", "Quill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.73, -43.79),[]),
  

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
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.56, -11.90),[], 100),


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.37, 65.10),[], -44.8),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.00, -50.58),[], 259),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.67, -37.33),[], 36),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.64, 29.64),[], 48),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.60, -5.40),[], 21.5),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.89, 24.79),[], 346),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.80, -37.66),[], 324),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.53, -51.63),[], 15),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.95, -9.60),[], -33.76),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.32, -75.27),[], -44.07),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.18, 130.94),[], 22),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.27, -26.36),[], 78),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.02, -7),[], -17.7),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.64, 114.32),[], 346),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-26.53, -17.86),[(trp_looter,15,0)]),
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
