import bpy
import xml.etree.ElementTree as ET
import os

class MyObjectPG(bpy.types.PropertyGroup):
    col: bpy.props.PointerProperty(type=bpy.types.Collection)

class obj_properties():
    def register():
        obj_list=[]
        num=0
        db_directory = os.path.join(os.path.dirname(__file__), 'SU/')
        # print(os.path.abspath(db_directory), db_directory, os.path.realpath(__file__))
        # print(os.path.join(os.path.dirname(__file__), "SU/"))
        # print()
        for path, folders, files in os.walk(db_directory):
            for file in range(len(files)):
                tree = ET.parse(os.path.join(path, files[file]))
                # print(path, files[file])
                root = tree.getroot()
                for i in range(len(root)):
                    obj_list.append([])
                    obj_list[num].append(root[i].tag)
                    obj_list[num].append([])
                    obj_list[num][1].append(root[i].attrib)
                    obj_list[num][1].append(os.path.join(path, files[file]))
                    num += 1
        for i in range(len(obj_list)):
            temp_name = ""
            original_name = ""
            for j in obj_list[i][0]:
                if j == "-":
                    temp_name = temp_name + ""
                if j == ".":
                    # print(j, obj_list[i][0])
                    temp_name = temp_name + ""
                if j == "_":
                    temp_name = temp_name + ""
                if j != "-" and j != "_" and j != ".":
                    temp_name = temp_name + j
                original_name = original_name + j
            obj_list[i][0] = temp_name
            obj_list[i][1].append(original_name)
            # print(obj_list[i][0], obj_list[i][1])
        for i in obj_list:
            i[0] = f'{i[1][0].get("type")}_{i[0]}'
        f_obj_list = dict(obj_list)
        # print(f_obj_list)
        obj_list = []
        i = 0
        for key, value in f_obj_list.items():
            obj_list.append([])
            obj_list[i].append(key)
            obj_list[i].append(value)
            i += 1
        i = 0
        #print(obj_list)
        for i in obj_list:
            if i[1][0].get('type') == "float":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.FloatProperty(name="{i[1][2]}", default={float(i[1][0].get("default"))}, description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == "integer":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.IntProperty(name="{i[1][2]}", default={int(i[1][0].get("default"))}, description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == "uint16":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.IntProperty(name="{i[1][2]}", default={int(i[1][0].get("default"))}, description="{i[1][0].get("description")}", min=0, max=65535) # {i[1][1]}\n')
            if i[1][0].get('type') == "uint32":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.IntProperty(name="{i[1][2]}", default={int(i[1][0].get("default"))}, description="{i[1][0].get("description")}", min=0) # {i[1][1]}\n')
            if i[1][0].get('type') == "bool":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.BoolProperty(name="{i[1][2]}", default={str.capitalize(i[1][0].get("default"))}, description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == "vector":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.FloatVectorProperty(name="{i[1][2]}", default=(0.0, 0.0, 0.0), description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == 'string':
                exec(f'bpy.types.Object.{i[0]} = bpy.props.StringProperty(name="{i[1][2]}", default="{i[1][0].get("default")}", description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == 'id_list':
                exec(f'bpy.types.Object.{i[0]} = bpy.props.PointerProperty(type=bpy.types.Collection, name="{i[1][2]}", description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == "id":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.PointerProperty(type=bpy.types.Object, name="{i[1][2]}", description="{i[1][0].get("description")}") # {i[1][1]}\n')
            if i[1][0].get('type') == "target":
                exec(f'bpy.types.Object.{i[0]} = bpy.props.PointerProperty(type=bpy.types.Object, name="{i[1][2]}", description="{i[1][0].get("description")}") # {i[1][1]}\n')
    def unregister():
        obj_list=[]
        num=0
        db_directory = os.path.join(os.path.dirname(__file__), 'SU/')
        # print(os.path.abspath(db_directory), db_directory, os.path.realpath(__file__))
        # print(os.path.join(os.path.dirname(__file__), "SU/"))
        # print()
        for path, folders, files in os.walk(db_directory):
            for file in range(len(files)):
                tree = ET.parse(os.path.join(path, files[file]))
                # print(path, files[file])
                root = tree.getroot()
                for i in range(len(root)):
                    obj_list.append([])
                    obj_list[num].append(root[i].tag)
                    obj_list[num].append([])
                    obj_list[num][1].append(root[i].attrib)
                    obj_list[num][1].append(os.path.join(path, files[file]))
                    num += 1
        for i in range(len(obj_list)):
            temp_name = ""
            original_name = ""
            for j in obj_list[i][0]:
                if j == "-":
                    temp_name = temp_name + ""
                if j == ".":
                    # print(j, obj_list[i][0])
                    temp_name = temp_name + ""
                if j == "_":
                    temp_name = temp_name + ""
                if j != "-" and j != "_" and j != ".":
                    temp_name = temp_name + j
                original_name = original_name + j
            obj_list[i][0] = temp_name
            obj_list[i][1].append(original_name)
        for i in obj_list:
            i[0] = f'{i[1][0].get("type")}_{i[0]}'
        f_obj_list = dict(obj_list)
        # print(f_obj_list)

        obj_list = []
        i = 0
        for key, value in f_obj_list.items():
            obj_list.append([])
            obj_list[i].append(key)
            obj_list[i].append(value)
            i += 1
        i = 0
        for i in obj_list:
            exec(f'del bpy.types.Object.{i[0]}')
    register()

class old_obj_properties():
    bpy.types.Object.float_Amplitude = bpy.props.FloatProperty(name="Amplitude", default=1.0,
                                                               description="How far the platform moves")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_Cycle = bpy.props.FloatProperty(name="Cycle", default=1.0,
                                                           description="Movement speed of the platform")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_DialDirection = bpy.props.FloatProperty(name="DialDirection", default=0.0,
                                                                   description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.float_FitDirection = bpy.props.FloatProperty(name="FitDirection", default=0.0,
                                                                  description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.float_Gravity = bpy.props.FloatProperty(name="Gravity", default=45.0,
                                                             description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_GroundOffset = bpy.props.FloatProperty(name="GroundOffset", default=0.0,
                                                                  description="")  # SU/objects/system/WarpPoint.xml
    bpy.types.Object.float_IsAdvance = bpy.props.FloatProperty(name="IsAdvance", default=0.0,
                                                               description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.float_MoveDirection = bpy.props.FloatProperty(name="MoveDirection", default=0.0,
                                                                   description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.float_MoveType = bpy.props.FloatProperty(name="MoveType", default=0.0,
                                                              description="0: Stationary   1: Move up and down   2: Move left and right   3: Shake then fall once the player touches it")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_OnFloorTime = bpy.props.FloatProperty(name="OnFloorTime", default=3.0,
                                                                 description="How long before the platform starts shaking after the player lands.")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_Phase = bpy.props.FloatProperty(name="Phase", default=0.0,
                                                           description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_ResetTime = bpy.props.FloatProperty(name="ResetTime", default=5.0,
                                                               description="How long before the platform should respawn after falling.")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_RotationPhase = bpy.props.FloatProperty(name="RotationPhase", default=0.0,
                                                                   description="")  # SU/objects/nyc_night/EvilFloor_NY5M.xml
    bpy.types.Object.float_RotationSpeed = bpy.props.FloatProperty(name="RotationSpeed", default=0.0,
                                                                   description="")  # SU/objects/nyc_night/EvilFloor_NY5M.xml
    bpy.types.Object.float_SpeedOnPath = bpy.props.FloatProperty(name="SpeedOnPath", default=1.0,
                                                                 description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.float_StopTime = bpy.props.FloatProperty(name="StopTime", default=0.0,
                                                              description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.float_CenterType = bpy.props.FloatProperty(name="CenterType", default=0.0,
                                                                description="")  # SU/objects/eggman_obj/Egg_Fan.xml
    bpy.types.Object.float_FanNum = bpy.props.FloatProperty(name="FanNum", default=4.0,
                                                            description="")  # SU/objects/eggman_obj/Egg_Fan.xml
    bpy.types.Object.float_Num = bpy.props.FloatProperty(name="Num", default=5.0,
                                                         description="")  # SU/objects/adabat_day/Beach_ThornPillar.xml
    bpy.types.Object.float_Length = bpy.props.FloatProperty(name="Length", default=5.0,
                                                            description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_AddRange = bpy.props.FloatProperty(name="AddRange", default=0.0,
                                                              description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_AppearStopTime = bpy.props.FloatProperty(name="AppearStopTime", default=0.5,
                                                                    description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_AppearTime = bpy.props.FloatProperty(name="AppearTime", default=0.5,
                                                                description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_DisappearStopTime = bpy.props.FloatProperty(name="DisappearStopTime", default=0.5,
                                                                       description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_DisappearTime = bpy.props.FloatProperty(name="DisappearTime", default=1.0,
                                                                   description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_OnShakeTime = bpy.props.FloatProperty(name="OnShakeTime", default=0.0,
                                                                 description="How long the platform should shake before falling.")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_PathReverseTime = bpy.props.FloatProperty(name="PathReverseTime", default=2.0,
                                                                     description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_PathSpeed = bpy.props.FloatProperty(name="PathSpeed", default=1.0,
                                                               description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_PressDirection = bpy.props.FloatProperty(name="PressDirection", default=0.0,
                                                                    description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.float_PathVel = bpy.props.FloatProperty(name="PathVel", default=3.0,
                                                             description="")  # SU/objects/eggman_obj/EvilCoffeeCup.xml
    bpy.types.Object.float_WaitTime = bpy.props.FloatProperty(name="WaitTime", default=5.0,
                                                              description="")  # SU/objects/eggman_obj/EvilCoffeeCup.xml
    bpy.types.Object.float_ActionType = bpy.props.FloatProperty(name="ActionType", default=2.0,
                                                                description="")  # SU/objects/eggman_obj/Egg_TimeFloor.xml
    bpy.types.Object.float_AliveTime = bpy.props.FloatProperty(name="AliveTime", default=3.0,
                                                               description="")  # SU/objects/eggman_obj/Egg_TimeFloor.xml
    bpy.types.Object.float_HeraldTime = bpy.props.FloatProperty(name="HeraldTime", default=1.0,
                                                                description="")  # SU/objects/adabat_day/Beach_FlashFlood.xml
    bpy.types.Object.float_OffTime = bpy.props.FloatProperty(name="OffTime", default=1.0,
                                                             description="")  # SU/objects/holoska_day/Snow_ColdAir.xml
    bpy.types.Object.float_OnTime = bpy.props.FloatProperty(name="OnTime", default=2.0,
                                                            description="")  # SU/objects/holoska_day/Snow_ColdAir.xml
    bpy.types.Object.float_LeftTime = bpy.props.FloatProperty(name="LeftTime", default=5.0,
                                                              description="")  # SU/objects/eggman_obj/Egg_BeltCollisionSV.xml
    bpy.types.Object.float_MaterialIndex = bpy.props.FloatProperty(name="MaterialIndex", default=0.0,
                                                                   description="")  # SU/objects/eggman_obj/Egg_BeltCollision.xml
    bpy.types.Object.float_RightTime = bpy.props.FloatProperty(name="RightTime", default=0.0,
                                                               description="")  # SU/objects/eggman_obj/Egg_BeltCollisionSV.xml
    bpy.types.Object.float_Speed = bpy.props.FloatProperty(name="Speed", default=1.0,
                                                           description="")  # SU/objects/adabat_day/Beach_ThornBar.xml
    bpy.types.Object.float_Width = bpy.props.FloatProperty(name="Width", default=13.3,
                                                           description="")  # SU/objects/playersystem/SonicStopCollision.xml
    bpy.types.Object.float_Acceleration = bpy.props.FloatProperty(name="Acceleration", default=80.0,
                                                                  description="")  # SU/objects/eggman_obj/Egg_Coaster.xml
    bpy.types.Object.float_MaxSpeed = bpy.props.FloatProperty(name="MaxSpeed", default=130.0,
                                                              description="")  # SU/objects/china_day/ChinaRocket.xml
    bpy.types.Object.float_MinSpeed = bpy.props.FloatProperty(name="MinSpeed", default=60.0,
                                                              description="")  # SU/objects/eggman_obj/Egg_Coaster.xml
    bpy.types.Object.float_BreakTime = bpy.props.FloatProperty(name="BreakTime", default=2.5,
                                                               description="")  # SU/objects/china_night/EvilBreakableHandle_ChinaAa.xml
    bpy.types.Object.float_DefaultMode = bpy.props.FloatProperty(name="DefaultMode", default=0.0,
                                                                 description="")  # SU/objects/china_night/EvilBreakableHandle_ChinaAa.xml
    bpy.types.Object.float_ResurgeTime = bpy.props.FloatProperty(name="ResurgeTime", default=0.0,
                                                                 description="")  # SU/objects/china_night/EvilBreakableHandle_ChinaAa.xml
    bpy.types.Object.float_Vitality = bpy.props.FloatProperty(name="Vitality", default=1.0,
                                                              description="")  # SU/objects/china_night/EvilBreakableHandle_ChinaAa.xml
    bpy.types.Object.float_FallTime = bpy.props.FloatProperty(name="FallTime", default=3.3,
                                                              description="")  # SU/objects/nyc_night/EvilFallBalance_NewyorkB.xml
    bpy.types.Object.float_AttackInterval = bpy.props.FloatProperty(name="AttackInterval", default=5.0,
                                                                    description="")  # SU/objects/night_enemies/eThunderBall.xml
    bpy.types.Object.float_AttackTime = bpy.props.FloatProperty(name="AttackTime", default=5.0,
                                                                description="")  # SU/objects/night_enemies/eThunderBall.xml
    bpy.types.Object.float_Intencity = bpy.props.FloatProperty(name="Intencity", default=1000.0,
                                                               description="")  # SU/objects/night_objects/EvilFlameNozzle.xml
    bpy.types.Object.float_IntencityEvil = bpy.props.FloatProperty(name="IntencityEvil", default=5.0,
                                                                   description="")  # SU/objects/night_objects/EvilFlameNozzle.xml
    bpy.types.Object.float_ShockTimeEvil = bpy.props.FloatProperty(name="ShockTimeEvil", default=20.0,
                                                                   description="")  # SU/objects/night_objects/EvilFlameNozzle.xml
    bpy.types.Object.float_StartTime = bpy.props.FloatProperty(name="StartTime", default=10.0,
                                                               description="")  # SU/objects/night_enemies/eThunderBall.xml
    bpy.types.Object.float_PatternIndex = bpy.props.FloatProperty(name="PatternIndex", default=1.0,
                                                                  description="")  # SU/objects/eggman_obj/Egg_BeltCollision.xml
    bpy.types.Object.float_RingInterval = bpy.props.FloatProperty(name="RingInterval", default=1.5,
                                                                  description="")  # SU/objects/eggman_obj/Egg_BeltCollision.xml
    bpy.types.Object.float_TimeInterval = bpy.props.FloatProperty(name="TimeInterval", default=0.5,
                                                                  description="")  # SU/objects/eggman_obj/Egg_BeltCollision.xml
    bpy.types.Object.float_EnemyMaxCount = bpy.props.FloatProperty(name="EnemyMaxCount", default=4.0,
                                                                   description="")  # SU/objects/eggman_obj/EvilBigElevator.xml
    bpy.types.Object.float_FirstState = bpy.props.FloatProperty(name="FirstState", default=0.0,
                                                                description="")  # SU/objects/night_enemies/EvilEnemySpookyR.xml
    bpy.types.Object.float_HangerNum = bpy.props.FloatProperty(name="HangerNum", default=2.0,
                                                               description="")  # SU/objects/eggman_obj/EvilBigElevator.xml
    bpy.types.Object.float_Personality = bpy.props.FloatProperty(name="Personality", default=2.0,
                                                                 description="")  # SU/objects/night_enemies/EvilEnemyMoleelHole.xml
    bpy.types.Object.float_Damage = bpy.props.FloatProperty(name="Damage", default=100.0,
                                                            description="")  # SU/objects/eggman_obj/EvilDamageFanSmall_Eggmanland.xml
    bpy.types.Object.float_Type = bpy.props.FloatProperty(name="Type", default=0.0,
                                                          description="")  # SU/objects/system/SequenceChangeCollision.xml
    bpy.types.Object.float_Friction = bpy.props.FloatProperty(name="Friction", default=0.1,
                                                              description="")  # SU/objects/china_night/EvilPachinkoChina.xml
    bpy.types.Object.float_Kasoku = bpy.props.FloatProperty(name="Kasoku", default=0.3,
                                                            description="")  # SU/objects/china_night/EvilPachinkoChina.xml
    bpy.types.Object.float_Layer = bpy.props.FloatProperty(name="Layer", default=2.0,
                                                           description="")  # SU/objects/day_objects/PressThorn.xml
    bpy.types.Object.float_ModelRotation = bpy.props.FloatProperty(name="ModelRotation", default=0.0,
                                                                   description="")  # SU/objects/unused_night/Handle.xml
    bpy.types.Object.float_TimeLimit = bpy.props.FloatProperty(name="TimeLimit", default=0.0,
                                                               description="")  # SU/objects/night_objects/WoodBoxBomb.xml
    bpy.types.Object.float_Direction = bpy.props.FloatProperty(name="Direction", default=1.0,
                                                               description="")  # SU/objects/day_objects/MovingThorn.xml
    bpy.types.Object.float_RotationAngle = bpy.props.FloatProperty(name="RotationAngle", default=0.0,
                                                                   description="")  # SU/objects/unused_night/MovingFloorEvil.xml
    bpy.types.Object.float_ScaleX = bpy.props.FloatProperty(name="ScaleX", default=10.0,
                                                            description="")  # SU/objects/unused/MovingFloor.xml
    bpy.types.Object.float_ScaleY = bpy.props.FloatProperty(name="ScaleY", default=2.0,
                                                            description="")  # SU/objects/unused/MovingFloor.xml
    bpy.types.Object.float_ScaleZ = bpy.props.FloatProperty(name="ScaleZ", default=2.0,
                                                            description="")  # SU/objects/unused/MovingFloor.xml
    bpy.types.Object.float_Energy = bpy.props.FloatProperty(name="Energy", default=5.0,
                                                            description="")  # SU/objects/unused_night/Rock.xml
    bpy.types.Object.float_Path0Length = bpy.props.FloatProperty(name="Path0_Length", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path0Offset = bpy.props.FloatProperty(name="Path0_Offset", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path1Length = bpy.props.FloatProperty(name="Path1_Length", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path1Offset = bpy.props.FloatProperty(name="Path1_Offset", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path2Length = bpy.props.FloatProperty(name="Path2_Length", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path2Offset = bpy.props.FloatProperty(name="Path2_Offset", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path3Length = bpy.props.FloatProperty(name="Path3_Length", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_Path3Offset = bpy.props.FloatProperty(name="Path3_Offset", default=0.0,
                                                                 description="")  # SU/objects/unused_night/GroundBox.xml
    bpy.types.Object.float_EaseTimeEnter = bpy.props.FloatProperty(name="Ease_Time_Enter", default=0.5,
                                                                   description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.float_EaseTimeLeave = bpy.props.FloatProperty(name="Ease_Time_Leave", default=0.5,
                                                                   description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.float_Fovy = bpy.props.FloatProperty(name="Fovy", default=80.0,
                                                          description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.float_OffsetFarFront = bpy.props.FloatProperty(name="Offset_Far__Front_", default=8.0,
                                                                    description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetFarHeight = bpy.props.FloatProperty(name="Offset_Far__Height", default=3.5,
                                                                     description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetFarLength = bpy.props.FloatProperty(name="Offset_Far__Length", default=30.0,
                                                                     description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetFarPointHeight = bpy.props.FloatProperty(name="Offset_Far__Point_Height", default=-6.0,
                                                                          description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetNearFront = bpy.props.FloatProperty(name="Offset_Near_Front_", default=10.0,
                                                                     description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetNearHeight = bpy.props.FloatProperty(name="Offset_Near_Height", default=4.0,
                                                                      description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetNearLength = bpy.props.FloatProperty(name="Offset_Near_Length", default=5.0,
                                                                      description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_OffsetNearPointHeight = bpy.props.FloatProperty(name="Offset_Near_Point_Height",
                                                                           default=-4.0,
                                                                           description="")  # SU/objects/cameras/ObjCameraPointTarget.xml
    bpy.types.Object.float_TargetType = bpy.props.FloatProperty(name="Target_Type", default=0.0,
                                                                description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.float_ZRot = bpy.props.FloatProperty(name="ZRot", default=0.0,
                                                          description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.float_CollisionHeight = bpy.props.FloatProperty(name="Collision_Height", default=20.0,
                                                                     description="")  # SU/objects/system/StartDynamicPreloadingCollision.xml
    bpy.types.Object.float_CollisionLength = bpy.props.FloatProperty(name="Collision_Length", default=13.0,
                                                                     description="")  # SU/objects/system/EventPathHolding.xml
    bpy.types.Object.float_CollisionWidth = bpy.props.FloatProperty(name="Collision_Width", default=20.0,
                                                                    description="")  # SU/objects/system/StartDynamicPreloadingCollision.xml
    bpy.types.Object.float_Range = bpy.props.FloatProperty(name="Range", default=100.0,
                                                           description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.float_BaseSpacePathPosition = bpy.props.FloatProperty(name="BaseSpacePathPosition",
                                                                           default=109.711,
                                                                           description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_Distance = bpy.props.FloatProperty(name="Distance", default=200.0,
                                                              description="")  # SU/objects/holoska_day/Snow_ThornBallAppear.xml
    bpy.types.Object.float_EaseTime = bpy.props.FloatProperty(name="EaseTime", default=1.0,
                                                              description="")  # SU/objects/system/ChangeToneMapBegin.xml
    bpy.types.Object.float_ID = bpy.props.FloatProperty(name="ID", default=0.0,
                                                        description="")  # SU/objects/system/ChangeToneMapVolume.xml
    bpy.types.Object.float_RotationY = bpy.props.FloatProperty(name="Rotation_Y", default=-0.4,
                                                               description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_RotationZ = bpy.props.FloatProperty(name="Rotation_Z", default=-0.3,
                                                               description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_TargetFrontOffsetBias = bpy.props.FloatProperty(name="Target_Front_Offset_Bias", default=1.8,
                                                                           description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_TargetFrontOffsetMax = bpy.props.FloatProperty(name="Target_Front_Offset_Max", default=4.0,
                                                                          description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_TargetFrontOffsetSpeedScale = bpy.props.FloatProperty(name="Target_Front_Offset_Speed_Scale",
                                                                                 default=0.1,
                                                                                 description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_TargetUpOffset = bpy.props.FloatProperty(name="Target_Up_Offset", default=2.0,
                                                                    description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.float_OffsetPitch = bpy.props.FloatProperty(name="OffsetPitch", default=0.0,
                                                                 description="")  # SU/objects/cameras/ObjCameraPanVertical.xml
    bpy.types.Object.float_OffsetYaw = bpy.props.FloatProperty(name="OffsetYaw", default=0.0,
                                                               description="")  # SU/objects/cameras/ObjCameraPanVertical.xml
    bpy.types.Object.float_Pitch = bpy.props.FloatProperty(name="Pitch", default=0.0,
                                                           description="")  # SU/objects/china_day/ChinaRocket.xml
    bpy.types.Object.float_TargetOffsetFront = bpy.props.FloatProperty(name="TargetOffset_Front", default=1.0,
                                                                       description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.float_TargetOffsetRight = bpy.props.FloatProperty(name="TargetOffset_Right", default=0.0,
                                                                       description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.float_TargetOffsetUp = bpy.props.FloatProperty(name="TargetOffset_Up", default=-1.0,
                                                                    description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.float_Yaw = bpy.props.FloatProperty(name="Yaw", default=0.0,
                                                         description="")  # SU/objects/china_day/ChinaRocket.xml
    bpy.types.Object.float_BlendBase = bpy.props.FloatProperty(name="BlendBase", default=0.0,
                                                               description="")  # SU/objects/cameras/ObjCameraBlend.xml
    bpy.types.Object.float_BlendSpeed = bpy.props.FloatProperty(name="BlendSpeed", default=3.5,
                                                                description="")  # SU/objects/cameras/ObjCameraBlend.xml
    bpy.types.Object.float_BlendType = bpy.props.FloatProperty(name="BlendType", default=0.0,
                                                               description="")  # SU/objects/cameras/ObjCameraBlend.xml
    bpy.types.Object.float_AxisType = bpy.props.FloatProperty(name="AxisType", default=0.0,
                                                              description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_BackStopperPos = bpy.props.FloatProperty(name="BackStopperPos", default=3.0,
                                                                    description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_FrontStopperPos = bpy.props.FloatProperty(name="FrontStopperPos", default=100.0,
                                                                     description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_LeftSideAngleAxis = bpy.props.FloatProperty(name="LeftSideAngleAxis", default=0.0,
                                                                       description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_LeftSideType = bpy.props.FloatProperty(name="LeftSideType", default=0.0,
                                                                  description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_LimitLeftAngleAxis = bpy.props.FloatProperty(name="LimitLeftAngleAxis", default=-45.0,
                                                                        description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_LimitRightAngleAxis = bpy.props.FloatProperty(name="LimitRightAngleAxis", default=45.0,
                                                                         description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_RightSideAngleAxis = bpy.props.FloatProperty(name="RightSideAngleAxis", default=0.0,
                                                                        description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_RightSideType = bpy.props.FloatProperty(name="RightSideType", default=0.0,
                                                                   description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_Sensitivity = bpy.props.FloatProperty(name="Sensitivity", default=0.1,
                                                                 description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_VerticalType = bpy.props.FloatProperty(name="VerticalType", default=1.0,
                                                                  description="")  # SU/objects/cameras/ObjCameraCrossRail.xml
    bpy.types.Object.float_CameraPositionMode = bpy.props.FloatProperty(name="CameraPositionMode", default=1.0,
                                                                        description="")  # SU/objects/cameras/ObjCameraPanVertical.xml
    bpy.types.Object.float_FaceType = bpy.props.FloatProperty(name="FaceType", default=0.0,
                                                              description="")  # SU/objects/cameras/ObjCameraPanVertical.xml
    bpy.types.Object.float_Radius = bpy.props.FloatProperty(name="Radius", default=10.0,
                                                            description="")  # SU/objects/sounds/ObjWindNoiseCollision.xml
    bpy.types.Object.float_EyeSpeed = bpy.props.FloatProperty(name="EyeSpeed", default=4.0,
                                                              description="")  # SU/objects/cameras/ObjCameraPathTarget.xml
    bpy.types.Object.float_LookSpeed = bpy.props.FloatProperty(name="LookSpeed", default=5.0,
                                                               description="")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.float_OffsetOnEyePath = bpy.props.FloatProperty(name="OffsetOnEyePath", default=3.1,
                                                                     description="")  # SU/objects/cameras/ObjCameraPathTarget.xml
    bpy.types.Object.float_OffsetOnLookPath = bpy.props.FloatProperty(name="OffsetOnLookPath", default=0.0,
                                                                      description="")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.float_ShapeType = bpy.props.FloatProperty(name="Shape_Type", default=0.0,
                                                               description="")  # SU/objects/system/EventPathHolding.xml
    bpy.types.Object.float_TargetOffsetVel = bpy.props.FloatProperty(name="TargetOffset_Vel", default=0.0,
                                                                     description="")  # SU/objects/cameras/ObjCameraObjectLook.xml
    bpy.types.Object.float_TargetOffsetWorldX = bpy.props.FloatProperty(name="TargetOffset_WorldX", default=0.0,
                                                                        description="")  # SU/objects/cameras/ObjCameraObjectLook.xml
    bpy.types.Object.float_TargetOffsetWorldY = bpy.props.FloatProperty(name="TargetOffset_WorldY", default=6.1,
                                                                        description="")  # SU/objects/cameras/ObjCameraObjectLook.xml
    bpy.types.Object.float_TargetOffsetWorldZ = bpy.props.FloatProperty(name="TargetOffset_WorldZ", default=0.0,
                                                                        description="")  # SU/objects/cameras/ObjCameraObjectLook.xml
    bpy.types.Object.float_VelOffsetXYZ = bpy.props.FloatProperty(name="VelOffsetXYZ", default=0.0,
                                                                  description="")  # SU/objects/cameras/ObjCameraObjectLook.xml
    bpy.types.Object.float_EyePathType = bpy.props.FloatProperty(name="EyePathType", default=1.0,
                                                                 description="")  # SU/objects/cameras/ObjCameraPathTarget.xml
    bpy.types.Object.float_PanAndTangentBlend = bpy.props.FloatProperty(name="PanAndTangentBlend", default=0.3,
                                                                        description="")  # SU/objects/cameras/ObjCameraPathTarget.xml
    bpy.types.Object.float_PathID = bpy.props.FloatProperty(name="PathID", default=1.0,
                                                            description="ID of the guide path to follow.")  # SU/objects/day_objects/Pulley.xml
    bpy.types.Object.float_ACameraPriority = bpy.props.FloatProperty(name="ACameraPriority", default=0.0,
                                                                     description="")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_ALinkSide = bpy.props.FloatProperty(name="ALinkSide", default=1.0,
                                                               description="")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_AObjType = bpy.props.FloatProperty(name="AObjType", default=0.0,
                                                              description="")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_BCameraPriority = bpy.props.FloatProperty(name="BCameraPriority", default=0.0,
                                                                     description="")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_BLinkSide = bpy.props.FloatProperty(name="BLinkSide", default=0.0,
                                                               description="")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_BObjType = bpy.props.FloatProperty(name="BObjType", default=0.0,
                                                              description="")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_EaseTimeAtoB = bpy.props.FloatProperty(name="EaseTime_AtoB", default=1.0,
                                                                  description="Time taken to swap between cameras.")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_EaseTimeBtoA = bpy.props.FloatProperty(name="EaseTime_BtoA", default=1.0,
                                                                  description="Time taken to swap between cameras.")  # SU/objects/cameras/CameraCollisionBoard.xml
    bpy.types.Object.float_mParamDistance = bpy.props.FloatProperty(name="m_Param.Distance", default=8.0,
                                                                    description="")  # SU/objects/cameras/ObjCameraNormal.xml
    bpy.types.Object.float_mParamFovy = bpy.props.FloatProperty(name="m_Param.Fovy", default=45.0,
                                                                description="")  # SU/objects/cameras/ObjCameraNormal.xml
    bpy.types.Object.float_mParamTargetPitch = bpy.props.FloatProperty(name="m_Param.TargetPitch", default=0.0,
                                                                       description="")  # SU/objects/cameras/ObjCameraNormal.xml
    bpy.types.Object.float_mParamTargetYaw = bpy.props.FloatProperty(name="m_Param.TargetYaw", default=0.0,
                                                                     description="")  # SU/objects/cameras/ObjCameraNormal.xml
    bpy.types.Object.float_mParamVerticalOffset = bpy.props.FloatProperty(name="m_Param.VerticalOffset", default=2.7,
                                                                          description="")  # SU/objects/cameras/ChangeNormalCameraParam.xml
    bpy.types.Object.float_VerticalOffsetForSonic = bpy.props.FloatProperty(name="VerticalOffsetForSonic", default=1.7,
                                                                            description="")  # SU/objects/cameras/ObjCameraNormal.xml
    bpy.types.Object.float_TimerOFF = bpy.props.FloatProperty(name="TimerOFF", default=0.0,
                                                              description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.float_TimerON = bpy.props.FloatProperty(name="TimerON", default=0.0,
                                                             description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.float_Height = bpy.props.FloatProperty(name="Height", default=6.0,
                                                            description="")  # SU/objects/adabat_day/Beach_WaterColumn.xml
    bpy.types.Object.float_Space = bpy.props.FloatProperty(name="Space", default=1.0,
                                                           description="")  # SU/objects/night_objects/EvilFlameWall.xml
    bpy.types.Object.float_OffTimer = bpy.props.FloatProperty(name="OffTimer", default=5.0,
                                                              description="")  # SU/objects/common/Switch.xml
    bpy.types.Object.float_ModelIndex = bpy.props.FloatProperty(name="ModelIndex", default=0.0,
                                                                description="")  # SU/objects/night_objects/EvilWaterBarrel.xml
    bpy.types.Object.float_Eventrightoff = bpy.props.FloatProperty(name="Eventright_off", default=0.0,
                                                                   description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.float_Eventrighton = bpy.props.FloatProperty(name="Eventright_on", default=1.0,
                                                                  description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.float_ReturnTime = bpy.props.FloatProperty(name="ReturnTime", default=5.0,
                                                                description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.float_Timerrightoff = bpy.props.FloatProperty(name="Timerright_off", default=0.0,
                                                                   description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.float_Timerrighton = bpy.props.FloatProperty(name="Timerright_on", default=0.0,
                                                                  description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.float_ModelType = bpy.props.FloatProperty(name="ModelType", default=3.0,
                                                               description="")  # SU/objects/adabat_day/Beach_FlashFlood.xml
    bpy.types.Object.float_DefaultValue = bpy.props.FloatProperty(name="DefaultValue", default=0.0,
                                                                  description="")  # SU/objects/night_objects/EvilCrank.xml
    bpy.types.Object.float_LimitAngle = bpy.props.FloatProperty(name="LimitAngle", default=360.0,
                                                                description="")  # SU/objects/night_objects/EvilCrank.xml
    bpy.types.Object.float_Time = bpy.props.FloatProperty(name="Time", default=0.5,
                                                          description="")  # SU/objects/holoska_day/Snow_ThornBallAppear.xml
    bpy.types.Object.float_ItemType = bpy.props.FloatProperty(name="ItemType", default=0.0,
                                                              description="")  # SU/objects/common/ObjectPhysics.xml
    bpy.types.Object.float_MaxHp = bpy.props.FloatProperty(name="MaxHp", default=3.0,
                                                           description="")  # SU/objects/nyc_night/EvilNewyorkAdvertizeE.xml
    bpy.types.Object.float_Weight = bpy.props.FloatProperty(name="Weight", default=0.4,
                                                            description="")  # SU/objects/nyc_night/EvilPushBox_NewYork.xml
    bpy.types.Object.float_YRotation = bpy.props.FloatProperty(name="YRotation", default=0.0,
                                                               description="")  # SU/objects/nyc_night/EvilColumn_NewyorkAa.xml
    bpy.types.Object.float_WallLength = bpy.props.FloatProperty(name="WallLength", default=6.0,
                                                                description="")  # SU/objects/night_objects/EvilElectricWall.xml
    bpy.types.Object.float_Course = bpy.props.FloatProperty(name="Course", default=1.0,
                                                            description="")  # SU/objects/darkgaia_obj/Boss_DarkGaia.xml
    bpy.types.Object.float_ActiveRange = bpy.props.FloatProperty(name="ActiveRange", default=100.0,
                                                                 description="")  # SU/objects/darkgaia_obj/Boss_Hydra.xml
    bpy.types.Object.float_CollisionRange = bpy.props.FloatProperty(name="CollisionRange", default=100.0,
                                                                    description="")  # SU/objects/darkgaia_obj/Boss_Hydra_Generator.xml
    bpy.types.Object.float_LifeTime = bpy.props.FloatProperty(name="LifeTime", default=20.0,
                                                              description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_TargetPosSync = bpy.props.FloatProperty(name="TargetPos_Sync", default=0.0,
                                                                   description="")  # SU/objects/darkgaia_obj/Boss_Hydra.xml
    bpy.types.Object.float_TargetPositionX = bpy.props.FloatProperty(name="TargetPosition_X", default=0.0,
                                                                     description="")  # SU/objects/darkgaia_obj/Boss_Hydra.xml
    bpy.types.Object.float_TargetPositionY = bpy.props.FloatProperty(name="TargetPosition_Y", default=0.0,
                                                                     description="")  # SU/objects/darkgaia_obj/Boss_Hydra.xml
    bpy.types.Object.float_TargetPositionZ = bpy.props.FloatProperty(name="TargetPosition_Z", default=0.0,
                                                                     description="")  # SU/objects/darkgaia_obj/Boss_Hydra.xml
    bpy.types.Object.float_RoboStartDegree = bpy.props.FloatProperty(name="Robo_Start_Degree", default=-112.5,
                                                                     description="")  # SU/objects/darkgaia_obj/Boss_FinalDarkGaia.xml
    bpy.types.Object.float_RebornTime = bpy.props.FloatProperty(name="RebornTime", default=10.0,
                                                                description="")  # SU/objects/darkgaia_obj/Boss_FinalDarkGaia_FloatRock.xml
    bpy.types.Object.float_RockSize = bpy.props.FloatProperty(name="RockSize", default=0.0,
                                                              description="")  # SU/objects/darkgaia_obj/Boss_FinalDarkGaia_FloatRock.xml
    bpy.types.Object.float_Scale = bpy.props.FloatProperty(name="Scale", default=3.5,
                                                           description="")  # SU/objects/darkgaia_obj/Boss_FinalDarkGaia_FloatRock.xml
    bpy.types.Object.float_TentacleNum = bpy.props.FloatProperty(name="TentacleNum", default=7.0,
                                                                 description="")  # SU/objects/darkgaia_obj/Boss_FinalDarkGaia_FloatRock.xml
    bpy.types.Object.float_mBoostSpeed = bpy.props.FloatProperty(name="m_BoostSpeed", default=56.0,
                                                                 description="")  # SU/objects/darkgaia_obj/SpaceHurrier.xml
    bpy.types.Object.float_mDebugCylinderHeight = bpy.props.FloatProperty(name="m_DebugCylinderHeight", default=40.0,
                                                                          description="")  # SU/objects/playersystem/ChangeDiveEnd.xml
    bpy.types.Object.float_mNormalSpeed = bpy.props.FloatProperty(name="m_NormalSpeed", default=28.0,
                                                                  description="")  # SU/objects/darkgaia_obj/SpaceHurrier.xml
    bpy.types.Object.float_mRange = bpy.props.FloatProperty(name="m_Range", default=13.9,
                                                            description="")  # SU/objects/playersystem/ChangeDiveEnd.xml
    bpy.types.Object.float_GenerateNum = bpy.props.FloatProperty(name="GenerateNum", default=1.0,
                                                                 description="")  # SU/objects/darkgaia_obj/Boss_Hydra_Generator.xml
    bpy.types.Object.float_RestartTime = bpy.props.FloatProperty(name="RestartTime", default=5.0,
                                                                 description="")  # SU/objects/darkgaia_obj/Boss_Hydra_Generator.xml
    bpy.types.Object.float_SizeType = bpy.props.FloatProperty(name="SizeType", default=0.0,
                                                              description="Size of the board.   0: Small   1: Big")  # SU/objects/day_objects/JumpBoard.xml
    bpy.types.Object.float_ThornAmplitude = bpy.props.FloatProperty(name="ThornAmplitude", default=2.8,
                                                                    description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornBaseOffset = bpy.props.FloatProperty(name="ThornBaseOffset", default=2.08,
                                                                     description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornCycle = bpy.props.FloatProperty(name="ThornCycle", default=8.0,
                                                                description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornModelType = bpy.props.FloatProperty(name="ThornModelType", default=0.0,
                                                                    description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornMoveType = bpy.props.FloatProperty(name="ThornMoveType", default=2.0,
                                                                   description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornNumBtm = bpy.props.FloatProperty(name="ThornNumBtm", default=0.0,
                                                                 description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornNumTop = bpy.props.FloatProperty(name="ThornNumTop", default=0.0,
                                                                 description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornPhase = bpy.props.FloatProperty(name="ThornPhase", default=0.0,
                                                                description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornSpace = bpy.props.FloatProperty(name="ThornSpace", default=3.0,
                                                                description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_ThornStopTime = bpy.props.FloatProperty(name="ThornStopTime", default=2.0,
                                                                   description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.float_AppearOffset = bpy.props.FloatProperty(name="AppearOffset", default=5.0,
                                                                  description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.float_AppearVelocityL = bpy.props.FloatProperty(name="AppearVelocityL", default=8.0,
                                                                     description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.float_HeightFromPath = bpy.props.FloatProperty(name="HeightFromPath", default=2.0,
                                                                    description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.float_LaserChargeTime = bpy.props.FloatProperty(name="LaserChargeTime", default=0.1,
                                                                     description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.float_MaxVelocity = bpy.props.FloatProperty(name="MaxVelocity", default=35.0,
                                                                 description="Maximum speed of the barrel")  # SU/objects/euc_day/RollingBarrel.xml
    bpy.types.Object.float_MinVelocity = bpy.props.FloatProperty(name="MinVelocity", default=30.0,
                                                                 description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.float_WavingVelocity = bpy.props.FloatProperty(name="WavingVelocity", default=180.0,
                                                                    description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.float_AppearSpeed = bpy.props.FloatProperty(name="AppearSpeed", default=20.0,
                                                                 description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_AttackRatioLaser = bpy.props.FloatProperty(name="AttackRatioLaser", default=0.7,
                                                                      description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_AttackRatioShockwave = bpy.props.FloatProperty(name="AttackRatioShockwave", default=0.3,
                                                                          description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_AttackTimeAdd = bpy.props.FloatProperty(name="AttackTimeAdd", default=0.0,
                                                                   description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_AttackTimeMultiply = bpy.props.FloatProperty(name="AttackTimeMultiply", default=0.6,
                                                                        description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_CameraAppearLengthToSonic = bpy.props.FloatProperty(name="CameraAppearLengthToSonic",
                                                                               default=15.0,
                                                                               description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ChangeCameraEnterTime = bpy.props.FloatProperty(name="ChangeCameraEnterTime", default=0.5,
                                                                           description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ChangeCameraLeaveTime = bpy.props.FloatProperty(name="ChangeCameraLeaveTime", default=0.5,
                                                                           description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ChaseDistance = bpy.props.FloatProperty(name="ChaseDistance", default=20.0,
                                                                   description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ChaseSpeedScaleFasterThanSonic = bpy.props.FloatProperty(
        name="ChaseSpeedScaleFasterThanSonic", default=5.0, description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ChaseSpeedScaleSlowerThanSonic = bpy.props.FloatProperty(
        name="ChaseSpeedScaleSlowerThanSonic", default=10.0, description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_EnterBoostScale = bpy.props.FloatProperty(name="EnterBoostScale", default=80.0,
                                                                     description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_FinishCameraKeepTime = bpy.props.FloatProperty(name="FinishCameraKeepTime", default=0.5,
                                                                          description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserCount = bpy.props.FloatProperty(name="LaserCount", default=1.0,
                                                                description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserImpulseTangent = bpy.props.FloatProperty(name="LaserImpulseTangent", default=20.0,
                                                                         description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserImpulseY = bpy.props.FloatProperty(name="LaserImpulseY", default=15.0,
                                                                   description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserPreShotTime = bpy.props.FloatProperty(name="LaserPreShotTime", default=0.75,
                                                                      description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserShiftScale = bpy.props.FloatProperty(name="LaserShiftScale", default=0.2,
                                                                     description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserSpeed = bpy.props.FloatProperty(name="LaserSpeed", default=1.0,
                                                                description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LaserTime = bpy.props.FloatProperty(name="LaserTime", default=2.0,
                                                               description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LeaveBoostScale = bpy.props.FloatProperty(name="LeaveBoostScale", default=40.0,
                                                                     description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_LifePoint = bpy.props.FloatProperty(name="LifePoint", default=6.0,
                                                               description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_MaximumSpeed = bpy.props.FloatProperty(name="MaximumSpeed", default=80.0,
                                                                  description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_MinimumSpeed = bpy.props.FloatProperty(name="MinimumSpeed", default=40.0,
                                                                  description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_PunchImpulseTangent = bpy.props.FloatProperty(name="PunchImpulseTangent", default=35.0,
                                                                         description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_PunchImpulseY = bpy.props.FloatProperty(name="PunchImpulseY", default=15.0,
                                                                   description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ShockwaveImpulseTangent = bpy.props.FloatProperty(name="ShockwaveImpulseTangent",
                                                                             default=20.0,
                                                                             description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ShockwaveImpulseY = bpy.props.FloatProperty(name="ShockwaveImpulseY", default=15.0,
                                                                       description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_ShockwaveSpeed = bpy.props.FloatProperty(name="ShockwaveSpeed", default=70.0,
                                                                    description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_SonicAutoRunSpeed = bpy.props.FloatProperty(name="SonicAutoRunSpeed", default=40.0,
                                                                       description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_WaitTimeAfterPunch = bpy.props.FloatProperty(name="WaitTimeAfterPunch", default=1.0,
                                                                        description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.float_Interval = bpy.props.FloatProperty(name="Interval", default=1.5,
                                                              description="Space between each ring")  # SU/objects/unused/RingGenerator.xml
    bpy.types.Object.float_RadiusAction = bpy.props.FloatProperty(name="RadiusAction", default=30.0,
                                                                  description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_RadiusSearch = bpy.props.FloatProperty(name="RadiusSearch", default=50.0,
                                                                  description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_ViewAngleTate = bpy.props.FloatProperty(name="ViewAngleTate", default=30.0,
                                                                   description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_ViewAngleYoko = bpy.props.FloatProperty(name="ViewAngleYoko", default=30.0,
                                                                   description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_RadiusActive = bpy.props.FloatProperty(name="RadiusActive", default=10.0,
                                                                  description="")  # SU/objects/day_enemies/eShackleFView.xml
    bpy.types.Object.float_RadiusAttack = bpy.props.FloatProperty(name="RadiusAttack", default=5.0,
                                                                  description="")  # SU/objects/day_enemies/eShackleFView.xml
    bpy.types.Object.float_IntervalAttack = bpy.props.FloatProperty(name="IntervalAttack", default=1.0,
                                                                    description="")  # SU/objects/day_enemies/eMoleCannon.xml
    bpy.types.Object.float_IntervalShot = bpy.props.FloatProperty(name="IntervalShot", default=0.5,
                                                                  description="")  # SU/objects/day_enemies/eMoleCannon.xml
    bpy.types.Object.float_RadiusAppear = bpy.props.FloatProperty(name="RadiusAppear", default=40.0,
                                                                  description="")  # SU/objects/day_enemies/eMoleCannon.xml
    bpy.types.Object.float_RadiusEscape = bpy.props.FloatProperty(name="RadiusEscape", default=10.0,
                                                                  description="")  # SU/objects/day_enemies/eMoleCannon.xml
    bpy.types.Object.float_RadiusAttackFar = bpy.props.FloatProperty(name="RadiusAttackFar", default=70.0,
                                                                     description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.float_RadiusAttackNear = bpy.props.FloatProperty(name="RadiusAttackNear", default=3.0,
                                                                      description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.float_ShotIntervel = bpy.props.FloatProperty(name="ShotIntervel", default=2.0,
                                                                  description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.float_UserRange = bpy.props.FloatProperty(name="UserRange", default=0.0,
                                                               description="")  # SU/objects/china_day/ChinaRotationFloor.xml
    bpy.types.Object.float_FirstSpeed = bpy.props.FloatProperty(name="FirstSpeed", default=80.4,
                                                                description="Initial speed of the launch")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.float_TimeBomb = bpy.props.FloatProperty(name="TimeBomb", default=1.0,
                                                              description="")  # SU/objects/day_enemies/eBurstFView.xml
    bpy.types.Object.float_CollisionX = bpy.props.FloatProperty(name="Collision_X", default=65.0,
                                                                description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_CollisionY = bpy.props.FloatProperty(name="Collision_Y", default=24.0,
                                                                description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_CollisionZ = bpy.props.FloatProperty(name="Collision_Z", default=21.0,
                                                                description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.float_StageType = bpy.props.FloatProperty(name="StageType", default=0.0,
                                                               description="")  # SU/objects/common/PointMarker.xml
    bpy.types.Object.float_BossKeyType = bpy.props.FloatProperty(name="BossKeyType", default=3.0,
                                                                 description="")  # SU/objects/common/GoalRing.xml
    bpy.types.Object.float_MediaIndex = bpy.props.FloatProperty(name="MediaIndex", default=10.0,
                                                                description="")  # SU/objects/common/ItemIllustBook.xml
    bpy.types.Object.float_ColorScaleA = bpy.props.FloatProperty(name="ColorScale_A", default=1.0,
                                                                 description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.float_ColorScaleB = bpy.props.FloatProperty(name="ColorScale_B", default=1.0,
                                                                 description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.float_ColorScaleG = bpy.props.FloatProperty(name="ColorScale_G", default=1.0,
                                                                 description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.float_ColorScaleR = bpy.props.FloatProperty(name="ColorScale_R", default=1.0,
                                                                 description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.float_SphereRadius = bpy.props.FloatProperty(name="SphereRadius", default=25.0,
                                                                  description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.float_VolumeScale = bpy.props.FloatProperty(name="VolumeScale", default=2.0,
                                                                 description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.float_ChangeTime = bpy.props.FloatProperty(name="ChangeTime", default=-0.1,
                                                                description="")  # SU/objects/common/Hint.xml
    bpy.types.Object.float_DrawCharWait = bpy.props.FloatProperty(name="DrawCharWait", default=-0.01,
                                                                  description="")  # SU/objects/common/Hint.xml
    bpy.types.Object.float_EndWait = bpy.props.FloatProperty(name="EndWait", default=-0.1,
                                                             description="")  # SU/objects/common/Hint.xml
    bpy.types.Object.float_Index = bpy.props.FloatProperty(name="Index", default=0.0,
                                                           description="")  # SU/objects/common/MedalSun.xml
    bpy.types.Object.float_ItemNum = bpy.props.FloatProperty(name="ItemNum", default=0.0,
                                                             description="")  # SU/objects/common/ObjectPhysics.xml
    bpy.types.Object.float_RangeIn = bpy.props.FloatProperty(name="RangeIn", default=1000.0,
                                                             description="Distance from object before it spawns")  # SU/objects/common/FallDeadCollision.xml
    bpy.types.Object.float_RangeOut = bpy.props.FloatProperty(name="RangeOut", default=1200.0,
                                                              description="Distance from object before it despawns")  # SU/objects/common/FallDeadCollision.xml
    bpy.types.Object.float_Unknown3 = bpy.props.FloatProperty(name="Unknown3", default=0.0,
                                                              description="")  # SU/objects/common/FallDeadCollision.xml
    bpy.types.Object.float_TimerOff = bpy.props.FloatProperty(name="TimerOff", default=0.0,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.float_TimerOff2 = bpy.props.FloatProperty(name="TimerOff2", default=0.0,
                                                               description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.float_TimerOn = bpy.props.FloatProperty(name="TimerOn", default=0.0,
                                                             description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.float_TimerOn2 = bpy.props.FloatProperty(name="TimerOn2", default=0.0,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.float_HP = bpy.props.FloatProperty(name="HP", default=1000.0,
                                                        description="")  # SU/objects/holoska_night/EvilBreakableIcePillar.xml
    bpy.types.Object.float_MoveLimit = bpy.props.FloatProperty(name="MoveLimit", default=1.0,
                                                               description="")  # SU/objects/africa_night/EvilDialFloor_Africa.xml
    bpy.types.Object.float_BreakTime1 = bpy.props.FloatProperty(name="BreakTime1", default=-5.0,
                                                                description="")  # SU/objects/holoska_night/EvilIcicle.xml
    bpy.types.Object.float_BreakTime2 = bpy.props.FloatProperty(name="BreakTime2", default=-6.2,
                                                                description="")  # SU/objects/holoska_night/EvilIcicle.xml
    bpy.types.Object.float_ClearTime = bpy.props.FloatProperty(name="ClearTime", default=0.5,
                                                               description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_ColliRangeBoxScalex = bpy.props.FloatProperty(name="ColliRangeBoxScale.x", default=100.0,
                                                                         description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_ColliRangeBoxScaley = bpy.props.FloatProperty(name="ColliRangeBoxScale.y", default=100.0,
                                                                         description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_ColliRangeBoxScalez = bpy.props.FloatProperty(name="ColliRangeBoxScale.z", default=100.0,
                                                                         description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_ColliRangeSphereRadius = bpy.props.FloatProperty(name="ColliRangeSphereRadius",
                                                                            default=100.0,
                                                                            description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_Density = bpy.props.FloatProperty(name="Density", default=50.0,
                                                             description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_DensityTime = bpy.props.FloatProperty(name="DensityTime", default=1.0,
                                                                 description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_LeaveTimeMax = bpy.props.FloatProperty(name="LeaveTimeMax", default=0.5,
                                                                  description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_MoveDirx = bpy.props.FloatProperty(name="MoveDir.x", default=0.0,
                                                              description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_MoveDiry = bpy.props.FloatProperty(name="MoveDir.y", default=0.0,
                                                              description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_MoveDirz = bpy.props.FloatProperty(name="MoveDir.z", default=1.0,
                                                              description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_MoveSpeedMax = bpy.props.FloatProperty(name="MoveSpeedMax", default=1.7,
                                                                  description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_MoveSpeedMin = bpy.props.FloatProperty(name="MoveSpeedMin", default=1.5,
                                                                  description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_OffsetYMax = bpy.props.FloatProperty(name="OffsetYMax", default=0.5,
                                                                description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_OffsetYMin = bpy.props.FloatProperty(name="OffsetYMin", default=-0.5,
                                                                description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_RangeBoxScalex = bpy.props.FloatProperty(name="RangeBoxScale.x", default=100.0,
                                                                    description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_RangeBoxScaley = bpy.props.FloatProperty(name="RangeBoxScale.y", default=100.0,
                                                                    description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_RangeBoxScalez = bpy.props.FloatProperty(name="RangeBoxScale.z", default=100.0,
                                                                    description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_RangeSphereRadius = bpy.props.FloatProperty(name="RangeSphereRadius", default=100.0,
                                                                       description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_ScaleMax = bpy.props.FloatProperty(name="ScaleMax", default=4.0,
                                                              description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_ScaleMin = bpy.props.FloatProperty(name="ScaleMin", default=2.0,
                                                              description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.float_RotationDirection = bpy.props.FloatProperty(name="RotationDirection", default=0.0,
                                                                       description="")  # SU/objects/euc_night/EvilRotationGearA.xml
    bpy.types.Object.float_TimerDown1F = bpy.props.FloatProperty(name="TimerDown_1F", default=0.0,
                                                                 description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.float_TimerUp2F = bpy.props.FloatProperty(name="TimerUp_2F", default=0.0,
                                                               description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.float_DownAcc = bpy.props.FloatProperty(name="DownAcc", default=10.0,
                                                             description="")  # SU/objects/shamar_day/Petra_FallingRock.xml
    bpy.types.Object.float_DownSpeed = bpy.props.FloatProperty(name="DownSpeed", default=0.25,
                                                               description="")  # SU/objects/shamar_day/Petra_FallingRock.xml
    bpy.types.Object.float_ShakeTime = bpy.props.FloatProperty(name="ShakeTime", default=0.1,
                                                               description="")  # SU/objects/adabat_day/Beach_BreakBridge.xml
    bpy.types.Object.float_StabilityTime = bpy.props.FloatProperty(name="StabilityTime", default=20.0,
                                                                   description="")  # SU/objects/adabat_night/EvilAppearFloatIsland.xml
    bpy.types.Object.float_FlyStartRange = bpy.props.FloatProperty(name="FlyStartRange", default=8.0,
                                                                   description="")  # SU/objects/euc_day/Pigeon.xml
    bpy.types.Object.float_WalkingRadius = bpy.props.FloatProperty(name="WalkingRadius", default=3.0,
                                                                   description="")  # SU/objects/holoska_day/Penguin.xml
    bpy.types.Object.float_OutOfControl = bpy.props.FloatProperty(name="OutOfControl", default=1.0,
                                                                  description="Time taken before restoring control to the player.")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.float_Velocity = bpy.props.FloatProperty(name="Velocity", default=40.0,
                                                              description="")  # SU/objects/holoska_day/BobsleighEndCollision.xml
    bpy.types.Object.float_FirstVelocity = bpy.props.FloatProperty(name="FirstVelocity", default=26.0,
                                                                   description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.float_GenerationTime = bpy.props.FloatProperty(name="GenerationTime", default=1.5,
                                                                    description="Time taken before spawning a barrel")  # SU/objects/euc_day/RollingBarrel.xml
    bpy.types.Object.float_RandomRange = bpy.props.FloatProperty(name="RandomRange", default=5.0,
                                                                 description="")  # SU/objects/euc_day/RollingBarrel.xml
    bpy.types.Object.float_ThornRatio = bpy.props.FloatProperty(name="ThornRatio", default=0.5,
                                                                description="How often a spiked barrel should spawn")  # SU/objects/euc_day/RollingBarrel.xml
    bpy.types.Object.float_ReviveTime = bpy.props.FloatProperty(name="ReviveTime", default=3.0,
                                                                description="Time taken before respawning.")  # SU/objects/euc_day/Balloon.xml
    bpy.types.Object.float_SpeedMax = bpy.props.FloatProperty(name="SpeedMax", default=70.0,
                                                              description="")  # SU/objects/mykonos_day/Seagull.xml
    bpy.types.Object.float_SpeedMin = bpy.props.FloatProperty(name="SpeedMin", default=40.0,
                                                              description="")  # SU/objects/mykonos_day/Seagull.xml
    bpy.types.Object.float_UpSpeed = bpy.props.FloatProperty(name="UpSpeed", default=7.0,
                                                             description="")  # SU/objects/adabat_day/Beach_UpFloor.xml
    bpy.types.Object.float_DstOffsetY = bpy.props.FloatProperty(name="DstOffsetY", default=2.0,
                                                                description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.float_DstOffsetZ = bpy.props.FloatProperty(name="DstOffsetZ", default=0.0,
                                                                description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.float_SrcOffsetY = bpy.props.FloatProperty(name="SrcOffsetY", default=2.0,
                                                                description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.float_SrcOffsetZ = bpy.props.FloatProperty(name="SrcOffsetZ", default=-5.0,
                                                                description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.float_DefaultStatus = bpy.props.FloatProperty(name="DefaultStatus", default=0.0,
                                                                   description="")  # SU/objects/system/EventPathHolding.xml
    bpy.types.Object.float_StateCaution = bpy.props.FloatProperty(name="State_Caution", default=20.0,
                                                                  description="")  # SU/objects/day_bosses/Boss_EggLancer_ChangeStateCollision.xml
    bpy.types.Object.float_StateDanger = bpy.props.FloatProperty(name="State_Danger", default=20.0,
                                                                 description="")  # SU/objects/day_bosses/Boss_EggLancer_ChangeStateCollision.xml
    bpy.types.Object.float_StateNormal = bpy.props.FloatProperty(name="State_Normal", default=8.0,
                                                                 description="")  # SU/objects/day_bosses/Boss_EggLancer_ChangeStateCollision.xml
    bpy.types.Object.float_MotionSpeed = bpy.props.FloatProperty(name="MotionSpeed", default=1.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_Offset = bpy.props.FloatProperty(name="Offset", default=0.0,
                                                            description="How far away from the origin the bar should appear")  # SU/objects/china_day/China_ThornBar.xml
    bpy.types.Object.float_Acc = bpy.props.FloatProperty(name="Acc", default=80.0,
                                                         description="")  # SU/objects/china_day/ChinaRocket.xml
    bpy.types.Object.float_JumpTime = bpy.props.FloatProperty(name="JumpTime", default=0.8,
                                                              description="")  # SU/objects/china_day/ChinaRocket.xml
    bpy.types.Object.float_ExtendTime = bpy.props.FloatProperty(name="ExtendTime", default=10.0,
                                                                description="")  # SU/objects/unused/TimeExtend.xml
    bpy.types.Object.float_CarSpeed = bpy.props.FloatProperty(name="CarSpeed", default=40.0,
                                                              description="")  # SU/objects/unused/CarGenerator.xml
    bpy.types.Object.float_mFPS = bpy.props.FloatProperty(name="m_FPS", default=30.0,
                                                          description="")  # SU/objects/unused/ConstantFrame.xml
    bpy.types.Object.float_mPathEaseTime = bpy.props.FloatProperty(name="m_PathEaseTime", default=0.5,
                                                                   description="")  # SU/objects/playersystem/ChangeMode_3Dto2D.xml
    bpy.types.Object.float_ImpulseSpeedOnBoost = bpy.props.FloatProperty(name="ImpulseSpeedOnBoost", default=50.0,
                                                                         description="Launch speed when boosting.")  # SU/objects/day_objects/JumpBoard.xml
    bpy.types.Object.float_ImpulseSpeedOnNormal = bpy.props.FloatProperty(name="ImpulseSpeedOnNormal", default=35.0,
                                                                          description="Launch speed when running.")  # SU/objects/day_objects/JumpBoard.xml
    bpy.types.Object.float_TerrainIgnoreTime = bpy.props.FloatProperty(name="TerrainIgnoreTime", default=0.25,
                                                                       description="")  # SU/objects/playersystem/JumpCollision.xml
    bpy.types.Object.float_Template = bpy.props.FloatProperty(name="Template", default=0.0,
                                                              description="A debug shortcut used to quickly set CurveCorrectionForce and PathCorrectionForce:   0: Narrow Road   1: Wide Road   2: Custom")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.float_mCurveCorrectionForce = bpy.props.FloatProperty(name="m_CurveCorrectionForce", default=0.0,
                                                                           description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.float_mDashPathSideMoveRate = bpy.props.FloatProperty(name="m_DashPathSideMoveRate", default=0.6,
                                                                           description="How aggressively the camera corrects.")  # SU/objects/playersystem/ChangeMode_3DtoForward.xml
    bpy.types.Object.float_mPathCorrectionForce = bpy.props.FloatProperty(name="m_PathCorrectionForce", default=0.5,
                                                                          description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.float_EnteringLimitTime = bpy.props.FloatProperty(name="EnteringLimitTime", default=3.0,
                                                                       description="Duration before gravity resets to normal.")  # SU/objects/playersystem/GravityChangeCollision.xml
    bpy.types.Object.float_LaunchVelocity = bpy.props.FloatProperty(name="LaunchVelocity", default=13.0,
                                                                    description="Speed after stumbling.")  # SU/objects/playersystem/StumbleCollision.xml
    bpy.types.Object.float_NoControlTime = bpy.props.FloatProperty(name="NoControlTime", default=0.45,
                                                                   description="Duration of the stumble.")  # SU/objects/playersystem/StumbleCollision.xml
    bpy.types.Object.float_mSpeed = bpy.props.FloatProperty(name="m_Speed", default=60.0,
                                                            description="How fast the player should move")  # SU/objects/playersystem/ChangeVelocity.xml
    bpy.types.Object.float_mSpeedRate = bpy.props.FloatProperty(name="m_SpeedRate", default=1.0,
                                                                description="")  # SU/objects/playersystem/SpeedDownCollision.xml
    bpy.types.Object.float_KeepTime = bpy.props.FloatProperty(name="KeepTime", default=5.0,
                                                              description="Time taken before restoring control to the player.")  # SU/objects/playersystem/AutorunStartCollision.xml
    bpy.types.Object.float_ToPathEaseTime = bpy.props.FloatProperty(name="ToPathEaseTime", default=0.5,
                                                                    description="Time to be corrected on the path.")  # SU/objects/playersystem/AutorunStartCollision.xml
    bpy.types.Object.float_ActivateCategory = bpy.props.FloatProperty(name="ActivateCategory", default=1.0,
                                                                      description="")  # SU/objects/playersystem/LayerChange.xml
    bpy.types.Object.float_ActivateIndex = bpy.props.FloatProperty(name="ActivateIndex", default=2.0,
                                                                   description="")  # SU/objects/playersystem/LayerChange.xml
    bpy.types.Object.float_DeactivateCategory = bpy.props.FloatProperty(name="DeactivateCategory", default=0.0,
                                                                        description="")  # SU/objects/playersystem/LayerChange.xml
    bpy.types.Object.float_DeactivateIndex = bpy.props.FloatProperty(name="DeactivateIndex", default=0.0,
                                                                     description="")  # SU/objects/playersystem/LayerChange.xml
    bpy.types.Object.float_mMaxLength = bpy.props.FloatProperty(name="m_MaxLength", default=100.0,
                                                                description="")  # SU/objects/day_objects/Paraloop.xml
    bpy.types.Object.float_ThresholdStumble = bpy.props.FloatProperty(name="ThresholdStumble", default=30.0,
                                                                      description="")  # SU/objects/day_objects/eBigChaserBomb.xml
    bpy.types.Object.float_FirstOutOfControl = bpy.props.FloatProperty(name="FirstOutOfControl", default=1.5,
                                                                       description="")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_FirstPitch = bpy.props.FloatProperty(name="FirstPitch", default=50.0999,
                                                                description="How high the player should travel upon touching the panel.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_SecondOutOfControl = bpy.props.FloatProperty(name="SecondOutOfControl", default=1.0,
                                                                        description="")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_SecondPitch = bpy.props.FloatProperty(name="SecondPitch", default=52.0999,
                                                                 description="Launch angle on the Y axis upon winning the Quick Time Event.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_SecondSpeed = bpy.props.FloatProperty(name="SecondSpeed", default=55.0998,
                                                                 description="Speed of the launch for winning the Quick Time Event.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_TrickCount1 = bpy.props.FloatProperty(name="TrickCount1", default=5.0,
                                                                 description="Number of button prompts on the first set of tricks.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_TrickCount2 = bpy.props.FloatProperty(name="TrickCount2", default=0.0,
                                                                 description="Number of button prompts on the second set of tricks.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_TrickCount3 = bpy.props.FloatProperty(name="TrickCount3", default=0.0,
                                                                 description="Number of button prompts on the third set of tricks.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_TrickTime1 = bpy.props.FloatProperty(name="TrickTime1", default=5.0,
                                                                description="Time allotted for the first set of tricks.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_TrickTime2 = bpy.props.FloatProperty(name="TrickTime2", default=0.0,
                                                                description="Time allotted for the second set of tricks.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_TrickTime3 = bpy.props.FloatProperty(name="TrickTime3", default=0.0,
                                                                description="Time allotted for the third set of tricks.")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_mDifficulty = bpy.props.FloatProperty(name="m_Difficulty", default=1.0,
                                                                 description="")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.float_mScore = bpy.props.FloatProperty(name="m_Score", default=1000.0,
                                                            description="")  # SU/objects/day_objects/ReactionPlate.xml
    bpy.types.Object.float_AddMaxVelocity = bpy.props.FloatProperty(name="AddMaxVelocity", default=0.0,
                                                                    description="Additional height granted when bouncing near the end of the pole")  # SU/objects/day_objects/JumpPole.xml
    bpy.types.Object.float_AddMinVelocity = bpy.props.FloatProperty(name="AddMinVelocity", default=0.0,
                                                                    description="Additional height granted when bouncing near the base of the pole")  # SU/objects/day_objects/JumpPole.xml
    bpy.types.Object.float_BallNum = bpy.props.FloatProperty(name="BallNum", default=5.0,
                                                             description="")  # SU/objects/day_objects/RollingBall.xml
    bpy.types.Object.float_ModelOffsetY = bpy.props.FloatProperty(name="ModelOffsetY", default=6.0,
                                                                  description="")  # SU/objects/day_objects/Hammer.xml
    bpy.types.Object.float_ModelOffsetZ = bpy.props.FloatProperty(name="ModelOffsetZ", default=6.0,
                                                                  description="")  # SU/objects/day_objects/Hammer.xml
    bpy.types.Object.float_OffsetTime = bpy.props.FloatProperty(name="OffsetTime", default=0.0,
                                                                description="")  # SU/objects/day_objects/Hammer.xml
    bpy.types.Object.float_RotateAngleWidth = bpy.props.FloatProperty(name="RotateAngleWidth", default=90.0,
                                                                      description="")  # SU/objects/day_objects/Hammer.xml
    bpy.types.Object.float_DebugShotTimeLength = bpy.props.FloatProperty(name="DebugShotTimeLength", default=2.0,
                                                                         description="A debug visualization tool.")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.float_KeepVelocityDistance = bpy.props.FloatProperty(name="KeepVelocityDistance", default=5.0,
                                                                          description="Distance before restoring gravity to Sonic. If set too high, gravity will be disabled until hitting another spring or object")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.float_AngleType = bpy.props.FloatProperty(name="AngleType", default=0.0,
                                                               description="Angle at which the player will launch.")  # SU/objects/day_objects/JumpBoard.xml
    bpy.types.Object.float_DownThornTime = bpy.props.FloatProperty(name="DownThornTime", default=1.0,
                                                                   description="Time the thorn remains down.")  # SU/objects/day_objects/ThornSpring.xml
    bpy.types.Object.float_UpThornTime = bpy.props.FloatProperty(name="UpThornTime", default=2.0,
                                                                 description="Time the thorn remains up.")  # SU/objects/day_objects/ThornSpring.xml
    bpy.types.Object.float_BottomStopTime = bpy.props.FloatProperty(name="BottomStopTime", default=0.3,
                                                                    description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.float_DownTime = bpy.props.FloatProperty(name="DownTime", default=0.15,
                                                              description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.float_TopStoptime = bpy.props.FloatProperty(name="TopStoptime", default=1.7,
                                                                 description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.float_UpDownWidth = bpy.props.FloatProperty(name="UpDownWidth", default=2.8,
                                                                 description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.float_UpTime = bpy.props.FloatProperty(name="UpTime", default=1.0,
                                                            description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.float_MainAcceptingTime = bpy.props.FloatProperty(name="MainAcceptingTime", default=1.1,
                                                                       description="")  # SU/objects/day_objects/ReactionPlate.xml
    bpy.types.Object.float_PreAcceptingTime = bpy.props.FloatProperty(name="PreAcceptingTime", default=0.5,
                                                                      description="")  # SU/objects/day_objects/ReactionPlate.xml
    bpy.types.Object.float_mFailOutOfControlTime = bpy.props.FloatProperty(name="m_FailOutOfControlTime", default=2.5,
                                                                           description="")  # SU/objects/day_objects/TrickAttackPanel.xml
    bpy.types.Object.float_mJumpMaxVelocity = bpy.props.FloatProperty(name="m_JumpMaxVelocity", default=0.0,
                                                                      description="")  # SU/objects/day_objects/ReactionPlate.xml
    bpy.types.Object.float_mJumpMinVelocity = bpy.props.FloatProperty(name="m_JumpMinVelocity", default=0.0,
                                                                      description="")  # SU/objects/day_objects/ReactionPlate.xml
    bpy.types.Object.float_mFailSpeed = bpy.props.FloatProperty(name="m_FailSpeed", default=40.5999,
                                                                description="")  # SU/objects/day_objects/TrickAttackPanel.xml
    bpy.types.Object.float_mSuccessSpeed = bpy.props.FloatProperty(name="m_SuccessSpeed", default=50.5998,
                                                                   description="")  # SU/objects/day_objects/TrickAttackPanel.xml
    bpy.types.Object.float_mTrickCount = bpy.props.FloatProperty(name="m_TrickCount", default=3.0,
                                                                 description="")  # SU/objects/day_objects/TrickAttackPanel.xml
    bpy.types.Object.float_mTrickTime = bpy.props.FloatProperty(name="m_TrickTime", default=5.6,
                                                                description="")  # SU/objects/day_objects/TrickAttackPanel.xml
    bpy.types.Object.float_AddUserRange = bpy.props.FloatProperty(name="AddUserRange", default=0.0,
                                                                  description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_EndPosition = bpy.props.FloatProperty(name="EndPosition", default=3.0,
                                                                 description="How close to the end of the spline the pulley should be before forcing the player off. The larger the number, the earlier the drop.")  # SU/objects/day_objects/Pulley.xml
    bpy.types.Object.float_StartPosition = bpy.props.FloatProperty(name="StartPosition", default=0.0,
                                                                   description="Adjusts how far along the spline the pulley spawns.")  # SU/objects/day_objects/Pulley.xml
    bpy.types.Object.float_ImpulseVelocity = bpy.props.FloatProperty(name="ImpulseVelocity", default=18.0,
                                                                     description="Speed at which the player is launched when the reel reaches its peak.")  # SU/objects/day_objects/UpReel.xml
    bpy.types.Object.float_UpSpeedMax = bpy.props.FloatProperty(name="UpSpeedMax", default=50.0,
                                                                description="Speed at which the handle rises.")  # SU/objects/day_objects/UpReel.xml
    bpy.types.Object.float_ForetasteTime = bpy.props.FloatProperty(name="ForetasteTime", default=0.5,
                                                                   description="")  # SU/objects/day_objects/DirectionalThorn.xml
    bpy.types.Object.float_MoveTime = bpy.props.FloatProperty(name="MoveTime", default=0.5,
                                                              description="")  # SU/objects/day_objects/DirectionalThorn.xml
    bpy.types.Object.float_DownShotForce = bpy.props.FloatProperty(name="DownShotForce", default=10.0,
                                                                   description="Speed granted when launching with the B button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_DownShotOutOfControl = bpy.props.FloatProperty(name="DownShotOutOfControl", default=0.3,
                                                                          description="Time taken before restoring control to the player after launching with the B button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_FrontJumpForce = bpy.props.FloatProperty(name="FrontJumpForce", default=25.0,
                                                                    description="Speed granted when launching with the X button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_FrontJumpOutOfControl = bpy.props.FloatProperty(name="FrontJumpOutOfControl", default=0.3,
                                                                           description="Time taken before restoring control to the player after launching with the X button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_InputTime = bpy.props.FloatProperty(name="InputTime", default=1.0,
                                                               description="How long the player has to input a direction")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_SuccessButton = bpy.props.FloatProperty(name="SuccessButton", default=2.0,
                                                                   description="The button displayed on the jump selector:   0: A   1: B   2: X")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_UpJumpForce = bpy.props.FloatProperty(name="UpJumpForce", default=21.0,
                                                                 description="Speed granted when launching with the A button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_UpJumpOutOfControl = bpy.props.FloatProperty(name="UpJumpOutOfControl", default=0.0,
                                                                        description="Time taken before restoring control to the player after launching with the A button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_UpJumpPitch = bpy.props.FloatProperty(name="UpJumpPitch", default=0.0,
                                                                 description="Angle of the launch on the Y axis after launching with the A button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.float_Event0 = bpy.props.FloatProperty(name="Event0", default=1.0,
                                                            description="The event to fire")  # SU/objects/day_objects/StompingSwitch.xml
    bpy.types.Object.float_Timer0 = bpy.props.FloatProperty(name="Timer0", default=0.0,
                                                            description="Delay before activating Event0")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_AddShotNum = bpy.props.FloatProperty(name="AddShotNum", default=0.0,
                                                                description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_AppearWaitTime = bpy.props.FloatProperty(name="AppearWaitTime", default=0.0,
                                                                    description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_ButtonType = bpy.props.FloatProperty(name="ButtonType", default=4.0,
                                                                description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_ChildNum = bpy.props.FloatProperty(name="ChildNum", default=0.0,
                                                              description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_EnemyType = bpy.props.FloatProperty(name="EnemyType", default=0.0,
                                                               description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_GroupQteNum = bpy.props.FloatProperty(name="GroupQteNum", default=1.0,
                                                                 description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_LeaveType = bpy.props.FloatProperty(name="LeaveType", default=10.0,
                                                               description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_PathType = bpy.props.FloatProperty(name="PathType", default=0.0,
                                                              description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_ShotTiming = bpy.props.FloatProperty(name="ShotTiming", default=0.0,
                                                                description="")  # SU/objects/tornado_obj/ExStageEnemy.xml
    bpy.types.Object.float_BossDist = bpy.props.FloatProperty(name="BossDist", default=150.0,
                                                              description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.float_BossSpeed = bpy.props.FloatProperty(name="BossSpeed", default=12.0,
                                                               description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.float_HatchState = bpy.props.FloatProperty(name="HatchState", default=0.0,
                                                                description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.float_PlayExSound = bpy.props.FloatProperty(name="PlayExSound", default=-1.0,
                                                                 description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.float_PlayerMotion = bpy.props.FloatProperty(name="PlayerMotion", default=3.0,
                                                                  description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.float_PlayerSpeed = bpy.props.FloatProperty(name="PlayerSpeed", default=83.0,
                                                                 description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.float_DecPosition = bpy.props.FloatProperty(name="DecPosition", default=310.0,
                                                                 description="")  # SU/objects/mykonos_day/Seagull.xml
    bpy.types.Object.float_RollingSpeed = bpy.props.FloatProperty(name="RollingSpeed", default=1.0,
                                                                  description="")  # SU/objects/mykonos_day/Seagull.xml
    bpy.types.Object.float_DefaultOpenNum = bpy.props.FloatProperty(name="DefaultOpenNum", default=0.0,
                                                                    description="")  # SU/objects/china_night/EvilTripleDoor.xml
    bpy.types.Object.float_OutControl = bpy.props.FloatProperty(name="OutControl", default=0.5,
                                                                description="")  # SU/objects/adabat_day/Beach_Buoy.xml
    bpy.types.Object.float_DownSpeed0 = bpy.props.FloatProperty(name="DownSpeed0", default=10.0,
                                                                description="")  # SU/objects/adabat_day/Beach_FallPillar.xml
    bpy.types.Object.float_DownSpeed1 = bpy.props.FloatProperty(name="DownSpeed1", default=12.0,
                                                                description="")  # SU/objects/adabat_day/Beach_FallPillar.xml
    bpy.types.Object.float_DownSpeed2 = bpy.props.FloatProperty(name="DownSpeed2", default=9.0,
                                                                description="")  # SU/objects/adabat_day/Beach_FallPillar.xml
    bpy.types.Object.float_DownSpeed3 = bpy.props.FloatProperty(name="DownSpeed3", default=13.0,
                                                                description="")  # SU/objects/adabat_day/Beach_FallPillar.xml
    bpy.types.Object.float_MoveLength = bpy.props.FloatProperty(name="MoveLength", default=3.0,
                                                                description="")  # SU/objects/adabat_day/Beach_ThornPillar.xml
    bpy.types.Object.float_DamageTime = bpy.props.FloatProperty(name="DamageTime", default=2.0,
                                                                description="")  # SU/objects/adabat_day/Beach_WaterColumn.xml
    bpy.types.Object.float_EffectType = bpy.props.FloatProperty(name="EffectType", default=0.0,
                                                                description="")  # SU/objects/adabat_day/Beach_WaterColumn.xml
    bpy.types.Object.float_IdleTime = bpy.props.FloatProperty(name="IdleTime", default=2.0,
                                                              description="")  # SU/objects/adabat_day/Beach_FlashFlood.xml
    bpy.types.Object.float_ShotTime = bpy.props.FloatProperty(name="ShotTime", default=2.0,
                                                              description="")  # SU/objects/adabat_day/Beach_FlashFlood.xml
    bpy.types.Object.float_AppearType = bpy.props.FloatProperty(name="AppearType", default=1.0,
                                                                description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_HeadUpAfterSonicJump = bpy.props.FloatProperty(name="HeadUpAfterSonicJump", default=2.0,
                                                                          description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_JumpKeepVelocity = bpy.props.FloatProperty(name="JumpKeepVelocity", default=1.0,
                                                                      description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_JumpOutOfControl = bpy.props.FloatProperty(name="JumpOutOfControl", default=1.0,
                                                                      description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_JumpPitch = bpy.props.FloatProperty(name="JumpPitch", default=0.0,
                                                               description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_JumpSpeed = bpy.props.FloatProperty(name="JumpSpeed", default=100.0,
                                                               description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_JumpYaw = bpy.props.FloatProperty(name="JumpYaw", default=0.0,
                                                             description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_LeapDelay = bpy.props.FloatProperty(name="LeapDelay", default=0.25,
                                                               description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_LeapHeight = bpy.props.FloatProperty(name="LeapHeight", default=130.0,
                                                                description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_LeapSpeed = bpy.props.FloatProperty(name="LeapSpeed", default=80.0,
                                                               description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_SwimUpDistance = bpy.props.FloatProperty(name="SwimUpDistance", default=50.0,
                                                                    description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_ScaleType = bpy.props.FloatProperty(name="ScaleType", default=1.0,
                                                               description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.float_Timer = bpy.props.FloatProperty(name="Timer", default=0.3,
                                                           description="")  # SU/objects/holoska_day/Snow_BreakFloor.xml
    bpy.types.Object.float_DownLength0 = bpy.props.FloatProperty(name="DownLength0", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DownLength1 = bpy.props.FloatProperty(name="DownLength1", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DownLength2 = bpy.props.FloatProperty(name="DownLength2", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DownLength3 = bpy.props.FloatProperty(name="DownLength3", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DownLength4 = bpy.props.FloatProperty(name="DownLength4", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DownLength5 = bpy.props.FloatProperty(name="DownLength5", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DownLength6 = bpy.props.FloatProperty(name="DownLength6", default=0.0,
                                                                 description="")  # SU/objects/holoska_day/Snow_IcePillar.xml
    bpy.types.Object.float_DivingDist = bpy.props.FloatProperty(name="DivingDist", default=3.0,
                                                                description="")  # SU/objects/holoska_day/Penguin.xml
    bpy.types.Object.float_DivingSpeed = bpy.props.FloatProperty(name="DivingSpeed", default=5.0,
                                                                 description="")  # SU/objects/holoska_day/Penguin.xml
    bpy.types.Object.float_WalkDist = bpy.props.FloatProperty(name="WalkDist", default=10.0,
                                                              description="")  # SU/objects/holoska_day/Penguin.xml
    bpy.types.Object.float_WalkSpeed = bpy.props.FloatProperty(name="WalkSpeed", default=0.5,
                                                               description="")  # SU/objects/holoska_day/Penguin.xml
    bpy.types.Object.float_JumpAngle = bpy.props.FloatProperty(name="JumpAngle", default=45.0,
                                                               description="")  # SU/objects/holoska_day/BobsleighEndCollision.xml
    bpy.types.Object.float_UncontrollableTime = bpy.props.FloatProperty(name="UncontrollableTime", default=3.0,
                                                                        description="")  # SU/objects/holoska_day/BobsleighEndCollision.xml
    bpy.types.Object.float_ShotVelFail = bpy.props.FloatProperty(name="ShotVelFail", default=15.0,
                                                                 description="")  # SU/objects/africa_day/HangPole.xml
    bpy.types.Object.float_ShotVelSuccess = bpy.props.FloatProperty(name="ShotVelSuccess", default=22.0,
                                                                    description="")  # SU/objects/africa_day/HangPole.xml
    bpy.types.Object.float_CancelAngle = bpy.props.FloatProperty(name="CancelAngle", default=90.0,
                                                                 description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.float_InputAngle = bpy.props.FloatProperty(name="InputAngle", default=70.0,
                                                                description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.float_OffSpeed = bpy.props.FloatProperty(name="OffSpeed", default=5.0,
                                                              description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.float_OnSpeed = bpy.props.FloatProperty(name="OnSpeed", default=10.0,
                                                             description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.float_OutputTime = bpy.props.FloatProperty(name="OutputTime", default=3.0,
                                                                description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.float_BaseVolume = bpy.props.FloatProperty(name="BaseVolume", default=1.0,
                                                                description="")  # SU/objects/sounds/ObjBaseSound.xml
    bpy.types.Object.float_IntervalTime = bpy.props.FloatProperty(name="IntervalTime", default=5.0,
                                                                  description="")  # SU/objects/sounds/ObjBaseSound.xml
    bpy.types.Object.float_InsideRadius = bpy.props.FloatProperty(name="InsideRadius", default=3.0,
                                                                  description="")  # SU/objects/sounds/ObjWindNoiseCollision.xml
    bpy.types.Object.float_BgmVolume = bpy.props.FloatProperty(name="BgmVolume", default=0.3,
                                                               description="")  # SU/objects/sounds/ObjBgmCollision.xml
    bpy.types.Object.float_EnterChangeTime = bpy.props.FloatProperty(name="EnterChangeTime", default=0.4,
                                                                     description="")  # SU/objects/sounds/ObjBgmCollision.xml
    bpy.types.Object.float_LeaveChangeTime = bpy.props.FloatProperty(name="LeaveChangeTime", default=3.1,
                                                                     description="")  # SU/objects/sounds/ObjBgmCollision.xml
    bpy.types.Object.float_GenerateSeparateTime = bpy.props.FloatProperty(name="GenerateSeparateTime", default=1.0,
                                                                          description="")  # SU/objects/night_enemies/EnemyObjEnemyHole.xml
    bpy.types.Object.float_MoleelCount = bpy.props.FloatProperty(name="MoleelCount", default=1.0,
                                                                 description="")  # SU/objects/night_enemies/EvilEnemyMoleelHole.xml
    bpy.types.Object.float_Aggression = bpy.props.FloatProperty(name="Aggression", default=0.0,
                                                                description="")  # SU/objects/night_enemies/EvilEnemySpookyR.xml
    bpy.types.Object.float_DownWaitTime = bpy.props.FloatProperty(name="DownWaitTime", default=1.2,
                                                                  description="")  # SU/objects/night_bosses/Fence.xml
    bpy.types.Object.float_UpWaitTime = bpy.props.FloatProperty(name="UpWaitTime", default=1.6,
                                                                description="")  # SU/objects/night_bosses/Fence.xml
    bpy.types.Object.float_AddRangeDistance = bpy.props.FloatProperty(name="AddRangeDistance", default=0.0,
                                                                      description="")  # SU/objects/night_bosses/BossEggDragoonBattlePlatform.xml
    bpy.types.Object.float_AngularVelocity = bpy.props.FloatProperty(name="AngularVelocity", default=3.0,
                                                                     description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.float_DebrisVelocity = bpy.props.FloatProperty(name="DebrisVelocity", default=34.0,
                                                                    description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.float_GenerateTime = bpy.props.FloatProperty(name="GenerateTime", default=3.7,
                                                                  description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.float_KillTime = bpy.props.FloatProperty(name="KillTime", default=10.0,
                                                              description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.float_ShotAngle = bpy.props.FloatProperty(name="ShotAngle", default=20.4,
                                                               description="Pitch of the barrel")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.float_SetRotation = bpy.props.FloatProperty(name="SetRotation", default=20.4,
                                                                 description="Yaw of the barrel")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.float_LuminanceHigh = bpy.props.FloatProperty(name="LuminanceHigh", default=1.74,
                                                                   description="")  # SU/objects/system/ChangeToneMapVolume.xml
    bpy.types.Object.float_LuminanceLow = bpy.props.FloatProperty(name="LuminanceLow", default=0.25,
                                                                  description="")  # SU/objects/system/ChangeToneMapVolume.xml
    bpy.types.Object.float_ToneMapMiddleGray = bpy.props.FloatProperty(name="ToneMapMiddleGray", default=0.350002,
                                                                       description="")  # SU/objects/system/ChangeToneMapBegin.xml
    bpy.types.Object.float_ToneMapSimpleScale = bpy.props.FloatProperty(name="ToneMapSimpleScale", default=1.0,
                                                                        description="")  # SU/objects/system/ChangeToneMapBegin.xml
    bpy.types.Object.float_Timer1 = bpy.props.FloatProperty(name="Timer1", default=0.0,
                                                            description="Delay before activating Event1")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_Timer2 = bpy.props.FloatProperty(name="Timer2", default=0.0,
                                                            description="Delay before activating Event2")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_Timer3 = bpy.props.FloatProperty(name="Timer3", default=0.0,
                                                            description="Delay before activating Event3")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_EventTime = bpy.props.FloatProperty(name="EventTime", default=0.0,
                                                               description="")  # SU/objects/system/WayPoint.xml
    bpy.types.Object.float_EventCollisionDepth = bpy.props.FloatProperty(name="EventCollision_Depth", default=0.1,
                                                                         description="")  # SU/objects/system/EnemyStopCollision.xml
    bpy.types.Object.float_Condition = bpy.props.FloatProperty(name="Condition", default=0.0,
                                                               description="")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_TimesType = bpy.props.FloatProperty(name="TimesType", default=1.0,
                                                               description="")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_Trigger = bpy.props.FloatProperty(name="Trigger", default=4.0,
                                                             description="")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.float_ParameterType = bpy.props.FloatProperty(name="ParameterType", default=1.0,
                                                                   description="")  # SU/objects/system/TerrainFloatParameterChangerCollision.xml
    bpy.types.Object.float_mScale = bpy.props.FloatProperty(name="m_Scale", default=0.0,
                                                            description="")  # SU/objects/system/TerrainFloatParameterChangerCollision.xml
    bpy.types.Object.float_mValue = bpy.props.FloatProperty(name="m_Value", default=100.0,
                                                            description="")  # SU/objects/system/TerrainFloatParameterChangerCollision.xml
    bpy.types.Object.float_TimerEnter = bpy.props.FloatProperty(name="TimerEnter", default=0.0,
                                                                description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.float_TimerLeave = bpy.props.FloatProperty(name="TimerLeave", default=0.0,
                                                                description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.float_mCullingFarDistance = bpy.props.FloatProperty(name="m_CullingFarDistance", default=3000.0,
                                                                         description="")  # SU/objects/system/TerrainParameterChangerCollision.xml
    bpy.types.Object.float_mMinGIMipLevel = bpy.props.FloatProperty(name="m_MinGIMipLevel", default=2.0,
                                                                    description="")  # SU/objects/system/StartDynamicPreloadingCollision.xml
    bpy.types.Object.float_mTargetRadius = bpy.props.FloatProperty(name="m_TargetRadius", default=101.0,
                                                                   description="")  # SU/objects/system/StartDynamicPreloadingCollision.xml
    bpy.types.Object.integer_FirstState = bpy.props.IntProperty(name="FirstState", default=0,
                                                                description="")  # SU/objects/night_enemies/EvilEnemyEggFighterC.xml
    bpy.types.Object.integer_ModelType = bpy.props.IntProperty(name="ModelType", default=0,
                                                               description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.integer_Type = bpy.props.IntProperty(name="Type", default=0,
                                                          description="")  # SU/objects/night_bosses/BossEggDragoonBattlePlatform.xml
    bpy.types.Object.integer_DefaultStatus = bpy.props.IntProperty(name="DefaultStatus", default=0,
                                                                   description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.integer_LineType = bpy.props.IntProperty(name="LineType", default=0,
                                                              description="")  # SU/objects/cameras/ChangeVolumeCamera.xml
    bpy.types.Object.integer_ShapeType = bpy.props.IntProperty(name="Shape_Type", default=0,
                                                               description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.integer_EyePathID = bpy.props.IntProperty(name="EyePathID", default=1,
                                                               description="")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.integer_EyePathType = bpy.props.IntProperty(name="EyePathType", default=1,
                                                                 description="0 = Closest Point, 1 = Line Segment, 2 = Time Passage")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.integer_LookPathID = bpy.props.IntProperty(name="LookPathID", default=0,
                                                                description="")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.integer_LookPathType = bpy.props.IntProperty(name="LookPathType", default=1,
                                                                  description="0 = Closest Point, 1 = Line Segment, 2 = Time Passage")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.integer_Priority = bpy.props.IntProperty(name="Priority", default=0,
                                                              description="")  # SU/objects/cameras/ChangeVolumeCamera.xml
    bpy.types.Object.integer_EventOFF = bpy.props.IntProperty(name="EventOFF", default=0,
                                                              description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.integer_EventON = bpy.props.IntProperty(name="EventON", default=0,
                                                             description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.integer_ModelIndex = bpy.props.IntProperty(name="ModelIndex", default=1,
                                                                description="")  # SU/objects/night_objects/WoodBoxBomb.xml
    bpy.types.Object.integer_SizeType = bpy.props.IntProperty(name="SizeType", default=0,
                                                              description="Size of the board.   0: Small   1: Big")  # SU/objects/day_objects/JumpBoard3D.xml
    bpy.types.Object.integer_TaregetType = bpy.props.IntProperty(name="TaregetType", default=0,
                                                                 description="")  # SU/objects/darkgaia_obj/Boss_Hydra.xml
    bpy.types.Object.integer_AirChaser01 = bpy.props.IntProperty(name="AirChaser_01", default=0,
                                                                 description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.integer_AirChaser02 = bpy.props.IntProperty(name="AirChaser_02", default=0,
                                                                 description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.integer_AirChaser03 = bpy.props.IntProperty(name="AirChaser_03", default=0,
                                                                 description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.integer_NumEnemy = bpy.props.IntProperty(name="NumEnemy", default=1,
                                                              description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.integer_AppearType = bpy.props.IntProperty(name="AppearType", default=0,
                                                                description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.integer_LeaveType = bpy.props.IntProperty(name="LeaveType", default=0,
                                                               description="0 = Mini Jump, 1 = Maintain Speed")  # SU/objects/holoska_day/BobsleighEndCollision.xml
    bpy.types.Object.integer_NumBullet = bpy.props.IntProperty(name="NumBullet", default=10,
                                                               description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.integer_NumShotOneTime = bpy.props.IntProperty(name="NumShotOneTime", default=3,
                                                                    description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.integer_ShotType = bpy.props.IntProperty(name="ShotType", default=0,
                                                              description="")  # SU/objects/day_enemies/eAirCannonGoldCreator.xml
    bpy.types.Object.integer_MoveType = bpy.props.IntProperty(name="MoveType", default=0,
                                                              description="")  # SU/objects/night_enemies/eThunderBall.xml
    bpy.types.Object.integer_NumCurrent = bpy.props.IntProperty(name="NumCurrent", default=2,
                                                                description="")  # SU/objects/day_enemies/eAirChaserReloadChaserCollision.xml
    bpy.types.Object.integer_NumTarget = bpy.props.IntProperty(name="NumTarget", default=3,
                                                               description="")  # SU/objects/day_enemies/eAirChaserReloadChaserCollision.xml
    bpy.types.Object.integer_AttackType = bpy.props.IntProperty(name="AttackType", default=0,
                                                                description="")  # SU/objects/day_enemies/eAirChaserCollisinForceAttack.xml
    bpy.types.Object.integer_NumAttackOneTime = bpy.props.IntProperty(name="NumAttackOneTime", default=2,
                                                                      description="")  # SU/objects/day_enemies/eMoleCannon.xml
    bpy.types.Object.integer_ActionType = bpy.props.IntProperty(name="ActionType", default=0,
                                                                description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.integer_ShotTypeBackPack = bpy.props.IntProperty(name="ShotTypeBackPack", default=0,
                                                                      description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.integer_ShotTypeHorizon = bpy.props.IntProperty(name="ShotTypeHorizon", default=0,
                                                                     description="")  # SU/objects/day_enemies/eFighterMissile.xml
    bpy.types.Object.integer_IntervalDecRing = bpy.props.IntProperty(name="IntervalDecRing", default=2,
                                                                     description="")  # SU/objects/day_enemies/eShackleFView.xml
    bpy.types.Object.integer_ShieldType = bpy.props.IntProperty(name="ShieldType", default=2,
                                                                description="0 - Normal, 1 - Spring, 2 - Electric")  # SU/objects/day_enemies/eFighterSword.xml
    bpy.types.Object.integer_Category = bpy.props.IntProperty(name="Category", default=0,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.integer_CharaType = bpy.props.IntProperty(name="CharaType", default=1,
                                                               description="0 = Sonic, 1 = Chip, 2 = Tails")  # SU/objects/common/HintRing.xml
    bpy.types.Object.integer_EventOff = bpy.props.IntProperty(name="EventOff", default=0,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.integer_EventOff2 = bpy.props.IntProperty(name="EventOff2", default=0,
                                                               description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.integer_EventOn = bpy.props.IntProperty(name="EventOn", default=0,
                                                             description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.integer_EventOn2 = bpy.props.IntProperty(name="EventOn2", default=0,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.integer_State = bpy.props.IntProperty(name="State", default=0,
                                                           description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.integer_EventDown1F = bpy.props.IntProperty(name="EventDown_1F", default=0,
                                                                 description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.integer_EventUp2F = bpy.props.IntProperty(name="EventUp_2F", default=0,
                                                               description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.integer_MaxHp = bpy.props.IntProperty(name="MaxHp", default=1,
                                                           description="")  # SU/objects/adabat_night/EvilTimber.xml
    bpy.types.Object.integer_BalloonColor = bpy.props.IntProperty(name="BalloonColor", default=1,
                                                                  description="Color of the balloon.   1: Blue   2: Green   3: Red   4: Yellow")  # SU/objects/euc_day/Balloon.xml
    bpy.types.Object.integer_FloorType = bpy.props.IntProperty(name="FloorType", default=0,
                                                               description="Amount of floor:   0 - full   1 - 3/4   2 - 1/2   3 - 1/4")  # SU/objects/china_day/ChinaRotationFloor.xml
    bpy.types.Object.integer_Phase = bpy.props.IntProperty(name="Phase", default=0,
                                                           description="")  # SU/objects/day_objects/AppearThorn.xml
    bpy.types.Object.integer_PoleType = bpy.props.IntProperty(name="PoleType", default=0,
                                                              description="Which structure should appear in the middle of the wheel   0 - slight raise   1 - pillar   2 - cage   3 - cage with extra circle below   4 - flat")  # SU/objects/china_day/ChinaRotationFloor.xml
    bpy.types.Object.integer_ChaoType = bpy.props.IntProperty(name="ChaoType", default=0,
                                                              description="")  # SU/objects/mission/Chao.xml
    bpy.types.Object.integer_AreaType = bpy.props.IntProperty(name="AreaType", default=3,
                                                              description="")  # SU/objects/town/EntranceDoor.xml
    bpy.types.Object.integer_DoorType = bpy.props.IntProperty(name="DoorType", default=0,
                                                              description="")  # SU/objects/town/EntranceDoor.xml
    bpy.types.Object.integer_KeyType = bpy.props.IntProperty(name="KeyType", default=0,
                                                             description="")  # SU/objects/navi/EvilNavigation.xml
    bpy.types.Object.integer_NeedMedalNum = bpy.props.IntProperty(name="NeedMedalNum", default=1,
                                                                  description="")  # SU/objects/town/EntranceDoor.xml
    bpy.types.Object.integer_Count = bpy.props.IntProperty(name="Count", default=6,
                                                           description="Number of rings to spawn")  # SU/objects/unused/RingGenerator.xml
    bpy.types.Object.integer_ScheduleXMLFileIndex = bpy.props.IntProperty(name="ScheduleXMLFileIndex", default=0,
                                                                          description="")  # SU/objects/unused/CarGenerator.xml
    bpy.types.Object.integer_SupportLineScale = bpy.props.IntProperty(name="SupportLineScale", default=1,
                                                                      description="")  # SU/objects/unused/Occluder.xml
    bpy.types.Object.integer_Direction = bpy.props.IntProperty(name="Direction", default=0,
                                                               description="")  # SU/objects/day_objects/AppearThorn.xml
    bpy.types.Object.integer_mDifficulty = bpy.props.IntProperty(name="m_Difficulty", default=1,
                                                                 description="")  # SU/objects/day_objects/ReactionPlate.xml
    bpy.types.Object.integer_IsAdvance = bpy.props.IntProperty(name="IsAdvance", default=0,
                                                               description="")  # SU/objects/nyc_night/EvilFloor_NY5M.xml
    bpy.types.Object.integer_CollisionType = bpy.props.IntProperty(name="CollisionType", default=1,
                                                                   description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.integer_DirectionType = bpy.props.IntProperty(name="DirectionType", default=0,
                                                                   description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.integer_NavigationType = bpy.props.IntProperty(name="NavigationType", default=0,
                                                                    description="")  # SU/objects/navi/EvilNavigation.xml
    bpy.types.Object.integer_QSType = bpy.props.IntProperty(name="QSType", default=0,
                                                            description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.integer_PatrolType = bpy.props.IntProperty(name="PatrolType", default=1,
                                                                description="")  # SU/objects/night_enemies/EvilEnemyEggFighterC.xml
    bpy.types.Object.integer_Personality = bpy.props.IntProperty(name="Personality", default=1,
                                                                 description="")  # SU/objects/night_enemies/EvilEnemyEggFighterC.xml
    bpy.types.Object.integer_StartWayPointID = bpy.props.IntProperty(name="StartWayPointID", default=1,
                                                                     description="")  # SU/objects/night_enemies/EvilEnemyEggFighterC.xml
    bpy.types.Object.integer_EnemyType = bpy.props.IntProperty(name="EnemyType", default=29,
                                                               description="0: Nightmare, 1: Deep Nightmare, 2: Green Reckless, 3: Purple Spooky, 4: Red Spooky, 5: Green Killer Bee, 6: Red Killer Bee, 7: Gun Egg Fighter, 8: Sword Egg Fighter, 9: Shield Egg Fighter, 10: Shield and Sword Egg Fighter, 11: Electric Shield and Sword Egg Fighter12: Electric Shield Egg Fighter (only punches), 13: Electric Shield Egg Fighter (jabs with shield), 14: Chibi Fighter, 15: Power Master, 16: Cure Master, 17: Fright Master, 18: Fire Master, 19: Lightning Master, 20: Flower, 21: Float, 22: Shooting Float, 23: Thunder Float, 24: Flame Element, 25: Ice Element, 26: Wind Element, 27: Thunder Ball, 28: Red Reckless, 29: Standard Egg Fighter, 30: Gun Egg Fighter (doesn't shoot)")  # SU/objects/night_enemies/EnemyObjEnemyHole.xml
    bpy.types.Object.integer_GenerateMaxCount = bpy.props.IntProperty(name="GenerateMaxCount", default=1,
                                                                      description="The amount of times the enemy is spawned.")  # SU/objects/night_enemies/EnemyObjEnemyHole.xml
    bpy.types.Object.integer_Aggression = bpy.props.IntProperty(name="Aggression", default=0,
                                                                description="")  # SU/objects/night_enemies/EvilEnemySpooky.xml
    bpy.types.Object.integer_Durability = bpy.props.IntProperty(name="Durability", default=0,
                                                                description="   0: Disappears after triggering?   1: Triggers then deactivates?")  # SU/objects/system/EventCollision.xml
    bpy.types.Object.integer_Event0 = bpy.props.IntProperty(name="Event0", default=7,
                                                            description="The event to fire:   0:No event   1:Open   2:Close  3:Kill  4:Generate  5:Get_off   6:On   7:Off  8:Attack  9:Attack_Ready  10:Can't_Attack")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.integer_Event1 = bpy.props.IntProperty(name="Event1", default=0,
                                                            description="Event to fire on TargetList1. Events continued:    11:Return   12:Destroy  13:Start_Moving   14:Reset  15:Rise  16:Descent  17:Start   18:Invert  19:Clear")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.integer_Event2 = bpy.props.IntProperty(name="Event2", default=0,
                                                            description="Event to fire on TargetList2")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.integer_Event3 = bpy.props.IntProperty(name="Event3", default=0,
                                                            description="Event to fire on TargetList3")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.integer_TriggerType = bpy.props.IntProperty(name="TriggerType", default=0,
                                                                 description="   0: Trigger on Player entry   1: Target an Object")  # SU/objects/system/EventCollision.xml
    bpy.types.Object.integer_EventID = bpy.props.IntProperty(name="EventID", default=0,
                                                             description="")  # SU/objects/system/WayPoint.xml
    bpy.types.Object.integer_ID = bpy.props.IntProperty(name="ID", default=1,
                                                        description="")  # SU/objects/system/ChangeToneMapEnd.xml
    bpy.types.Object.integer_NextID = bpy.props.IntProperty(name="NextID", default=0,
                                                            description="")  # SU/objects/system/WayPoint.xml
    bpy.types.Object.integer_WayPointType = bpy.props.IntProperty(name="WayPointType", default=0,
                                                                  description="")  # SU/objects/system/WayPoint.xml
    bpy.types.Object.integer_SubsetID = bpy.props.IntProperty(name="SubsetID", default=7,
                                                              description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_VisibilityType = bpy.props.IntProperty(name="VisibilityType", default=0,
                                                                    description="")  # SU/objects/system/TerrainInstanceSubsetRenderCollision2.xml
    bpy.types.Object.integer_LoadType = bpy.props.IntProperty(name="LoadType", default=0,
                                                              description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_LoadTypeBack = bpy.props.IntProperty(name="LoadTypeBack", default=1,
                                                                  description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_LoadTypeFront = bpy.props.IntProperty(name="LoadTypeFront", default=0,
                                                                   description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_SubsetID1 = bpy.props.IntProperty(name="SubsetID_1", default=0,
                                                               description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_SubsetID2 = bpy.props.IntProperty(name="SubsetID_2", default=0,
                                                               description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_SubsetID3 = bpy.props.IntProperty(name="SubsetID_3", default=0,
                                                               description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_SubsetID4 = bpy.props.IntProperty(name="SubsetID_4", default=0,
                                                               description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.integer_EventEnter = bpy.props.IntProperty(name="EventEnter", default=0,
                                                                description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.integer_EventLeave = bpy.props.IntProperty(name="EventLeave", default=0,
                                                                description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.uint16_Unknown1 = bpy.props.IntProperty(name="Unknown1", default=0, description="", min=0,
                                                             max=65535)  # SU/objects/common/FallDeadCollision.xml
    bpy.types.Object.uint32_Unknown2 = bpy.props.IntProperty(name="Unknown2", default=0, description="", min=0,
                                                             )  # SU/objects/common/FallDeadCollision.xml
    bpy.types.Object.bool_IsFitPath = bpy.props.BoolProperty(name="IsFitPath", default=True,
                                                             description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.bool_IsUseMessage = bpy.props.BoolProperty(name="IsUseMessage", default=False,
                                                                description="")  # SU/objects/nyc_night/EvilBar_NewyorkAa.xml
    bpy.types.Object.bool_IsDamage = bpy.props.BoolProperty(name="IsDamage", default=True,
                                                            description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.bool_IsEffect = bpy.props.BoolProperty(name="IsEffect", default=False,
                                                            description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.bool_IsMessageON = bpy.props.BoolProperty(name="IsMessageON", default=False,
                                                               description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.bool_IsReverse = bpy.props.BoolProperty(name="IsReverse", default=False,
                                                             description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.bool_IsWallJump = bpy.props.BoolProperty(name="IsWallJump", default=False,
                                                              description="")  # SU/objects/africa_day/AfricaFloorC.xml
    bpy.types.Object.bool_PathSearch = bpy.props.BoolProperty(name="PathSearch", default=True,
                                                              description="")  # SU/objects/eggman_obj/EvilCoffeeCup.xml
    bpy.types.Object.bool_EnableReverse = bpy.props.BoolProperty(name="EnableReverse", default=False,
                                                                 description="")  # SU/objects/eggman_obj/Egg_BeltCollisionSV.xml
    bpy.types.Object.bool_IsRightDirection = bpy.props.BoolProperty(name="IsRightDirection", default=False,
                                                                    description="")  # SU/objects/eggman_obj/Egg_BeltCollisionSV.xml
    bpy.types.Object.bool_IsPause = bpy.props.BoolProperty(name="IsPause", default=True,
                                                           description="")  # SU/objects/nyc_night/EvilRevolveHandle_Newyork.xml
    bpy.types.Object.bool_IsLoop = bpy.props.BoolProperty(name="IsLoop", default=False,
                                                          description="")  # SU/objects/eggman_obj/Egg_Cutter.xml
    bpy.types.Object.bool_IsRotation = bpy.props.BoolProperty(name="IsRotation", default=True,
                                                              description="")  # SU/objects/eggman_obj/Egg_Cutter.xml
    bpy.types.Object.bool_CanBreak = bpy.props.BoolProperty(name="CanBreak", default=True,
                                                            description="")  # SU/objects/china_night/EvilBreakableHandle_ChinaAa.xml
    bpy.types.Object.bool_IsShakeOnRelease = bpy.props.BoolProperty(name="IsShakeOnRelease", default=True,
                                                                    description="")  # SU/objects/china_night/EvilBreakableHandle_ChinaAa.xml
    bpy.types.Object.bool_NoBreak = bpy.props.BoolProperty(name="NoBreak", default=False,
                                                           description="")  # SU/objects/nyc_night/EvilBreakDoor_Newyork.xml
    bpy.types.Object.bool_IsPush = bpy.props.BoolProperty(name="IsPush", default=True,
                                                          description="")  # SU/objects/eggman_obj/Egg_Block.xml
    bpy.types.Object.bool_IsRestore = bpy.props.BoolProperty(name="IsRestore", default=False,
                                                             description="")  # SU/objects/night_objects/WoodBoxBomb.xml
    bpy.types.Object.bool_IsCameraView = bpy.props.BoolProperty(name="IsCameraView", default=False,
                                                                description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.bool_IsCollision = bpy.props.BoolProperty(name="IsCollision", default=True,
                                                               description="")  # SU/objects/day_bosses/Boss_EggLancer_CameraQTE.xml
    bpy.types.Object.bool_IsControllable = bpy.props.BoolProperty(name="IsControllable", default=False,
                                                                  description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.bool_IsCastShadow = bpy.props.BoolProperty(name="IsCastShadow", default=True,
                                                                description="")  # SU/objects/system/TerrainGroupSubsetLoadCollision.xml
    bpy.types.Object.bool_IsBaseSpacePlayer = bpy.props.BoolProperty(name="IsBaseSpacePlayer", default=True,
                                                                     description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.bool_IsPositionBasePlayer = bpy.props.BoolProperty(name="IsPositionBasePlayer", default=True,
                                                                        description="")  # SU/objects/cameras/ObjCamera2D.xml
    bpy.types.Object.bool_IsEnableCollision = bpy.props.BoolProperty(name="IsEnableCollision", default=False,
                                                                     description="")  # SU/objects/cameras/ChangeVolumeCamera.xml
    bpy.types.Object.bool_IsDefaultOn = bpy.props.BoolProperty(name="IsDefaultOn", default=True,
                                                               description="")  # SU/objects/night_objects/EvilSeal.xml
    bpy.types.Object.bool_IsReturn = bpy.props.BoolProperty(name="IsReturn", default=False,
                                                            description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.bool_Bar1Enable = bpy.props.BoolProperty(name="Bar1_Enable", default=True,
                                                              description="")  # SU/objects/nyc_night/EvilPushBox_NewYork.xml
    bpy.types.Object.bool_Bar2Enable = bpy.props.BoolProperty(name="Bar2_Enable", default=True,
                                                              description="")  # SU/objects/nyc_night/EvilPushBox_NewYork.xml
    bpy.types.Object.bool_Bar3Enable = bpy.props.BoolProperty(name="Bar3_Enable", default=True,
                                                              description="")  # SU/objects/nyc_night/EvilPushBox_NewYork.xml
    bpy.types.Object.bool_Bar4Enable = bpy.props.BoolProperty(name="Bar4_Enable", default=True,
                                                              description="")  # SU/objects/nyc_night/EvilPushBox_NewYork.xml
    bpy.types.Object.bool_IsUseMessageElectric = bpy.props.BoolProperty(name="IsUseMessageElectric", default=False,
                                                                        description="")  # SU/objects/night_objects/EvilElectricColumn.xml
    bpy.types.Object.bool_Rotation90Snap = bpy.props.BoolProperty(name="Rotation90Snap", default=True,
                                                                  description="")  # SU/objects/nyc_night/EvilColumn_NewyorkAa.xml
    bpy.types.Object.bool_mIsFirstHurrier = bpy.props.BoolProperty(name="m_IsFirstHurrier", default=False,
                                                                   description="")  # SU/objects/darkgaia_obj/SpaceHurrier.xml
    bpy.types.Object.bool_IsGearColumn = bpy.props.BoolProperty(name="IsGearColumn", default=True,
                                                                description="")  # SU/objects/nyc_night/EvilThornColumn_NewyorkAa.xml
    bpy.types.Object.bool_IsEndAnnihilation = bpy.props.BoolProperty(name="IsEndAnnihilation", default=True,
                                                                     description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.bool_IsUseCameraAppear = bpy.props.BoolProperty(name="IsUseCameraAppear", default=True,
                                                                     description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.bool_IsUseCameraChaser = bpy.props.BoolProperty(name="IsUseCameraChaser", default=True,
                                                                     description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.bool_SnapOnPath = bpy.props.BoolProperty(name="SnapOnPath", default=False,
                                                              description="")  # SU/objects/day_enemies/eAirChaser.xml
    bpy.types.Object.bool_IsVisibleDefault = bpy.props.BoolProperty(name="IsVisibleDefault", default=True,
                                                                    description="")  # SU/objects/day_enemies/eBigChaser.xml
    bpy.types.Object.bool_OnlyPlayerAttack = bpy.props.BoolProperty(name="OnlyPlayerAttack", default=True,
                                                                    description="")  # SU/objects/day_enemies/eBlizzard.xml
    bpy.types.Object.bool_PlayAppearEffect = bpy.props.BoolProperty(name="PlayAppearEffect", default=False,
                                                                    description="")  # SU/objects/day_enemies/eBlizzard.xml
    bpy.types.Object.bool_IsUseFootIK = bpy.props.BoolProperty(name="IsUseFootIK", default=True,
                                                               description="")  # SU/objects/day_enemies/eFighterSword.xml
    bpy.types.Object.bool_MoveTypeSideView = bpy.props.BoolProperty(name="MoveTypeSideView", default=False,
                                                                    description="")  # SU/objects/day_enemies/eFighterSword.xml
    bpy.types.Object.bool_UseChibi = bpy.props.BoolProperty(name="UseChibi", default=False,
                                                            description="")  # SU/objects/day_enemies/eFighterGun.xml
    bpy.types.Object.bool_ForSideView = bpy.props.BoolProperty(name="ForSideView", default=False,
                                                               description="")  # SU/objects/day_enemies/eSpinner.xml
    bpy.types.Object.bool_EditColorFlag = bpy.props.BoolProperty(name="EditColorFlag", default=False,
                                                                 description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.bool_Loop = bpy.props.BoolProperty(name="Loop", default=True,
                                                        description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.bool_DefaultON = bpy.props.BoolProperty(name="DefaultON", default=False,
                                                             description="")  # SU/objects/common/SetRigidBody.xml
    bpy.types.Object.bool_IsPlayerTerrain = bpy.props.BoolProperty(name="IsPlayerTerrain", default=False,
                                                                   description="")  # SU/objects/common/SetRigidBody.xml
    bpy.types.Object.bool_mIsSearchInsulateOnly = bpy.props.BoolProperty(name="m_IsSearchInsulateOnly", default=False,
                                                                         description="")  # SU/objects/common/SetRigidBody.xml
    bpy.types.Object.bool_IsPushBoxWall = bpy.props.BoolProperty(name="IsPushBoxWall", default=False,
                                                                 description="")  # SU/objects/common/SetRigidBody.xml
    bpy.types.Object.bool_DrawOnce = bpy.props.BoolProperty(name="DrawOnce", default=True,
                                                            description="")  # SU/objects/common/Hint.xml
    bpy.types.Object.bool_ExistPlatform = bpy.props.BoolProperty(name="ExistPlatform", default=False,
                                                                 description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.bool_NeedInput = bpy.props.BoolProperty(name="NeedInput", default=True,
                                                             description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.bool_PlayerStop = bpy.props.BoolProperty(name="PlayerStop", default=True,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.bool_UsePicture = bpy.props.BoolProperty(name="UsePicture", default=False,
                                                              description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.bool_IsDynamic = bpy.props.BoolProperty(name="IsDynamic", default=False,
                                                             description="")  # SU/objects/common/ObjectPhysics.xml
    bpy.types.Object.bool_IsReset = bpy.props.BoolProperty(name="IsReset", default=False,
                                                           description="")  # SU/objects/common/Ring.xml
    bpy.types.Object.bool_WaitEvent = bpy.props.BoolProperty(name="WaitEvent", default=False,
                                                             description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.bool_IsLightSpeedDashTarget = bpy.props.BoolProperty(name="IsLightSpeedDashTarget", default=False,
                                                                          description="Enables the player to perform the Light Speed Dash move.")  # SU/objects/common/Ring.xml
    bpy.types.Object.bool_CanPushBox = bpy.props.BoolProperty(name="CanPushBox", default=True,
                                                              description="")  # SU/objects/africa_night/EvilDialFloor_Africa.xml
    bpy.types.Object.bool_IsDebugDraw = bpy.props.BoolProperty(name="IsDebugDraw", default=False,
                                                               description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.bool_IsUseBoxRange = bpy.props.BoolProperty(name="IsUseBoxRange", default=True,
                                                                 description="")  # SU/objects/twn_shamar/PetraDust.xml
    bpy.types.Object.bool_Start2F = bpy.props.BoolProperty(name="Start2F", default=True,
                                                           description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.bool_Back = bpy.props.BoolProperty(name="Back", default=False,
                                                        description="")  # SU/objects/china_night/EvilPachinkoChina.xml
    bpy.types.Object.bool_Front = bpy.props.BoolProperty(name="Front", default=True,
                                                         description="")  # SU/objects/china_night/EvilPachinkoChina.xml
    bpy.types.Object.bool_Left = bpy.props.BoolProperty(name="Left", default=False,
                                                        description="")  # SU/objects/china_night/EvilPachinkoChina.xml
    bpy.types.Object.bool_Right = bpy.props.BoolProperty(name="Right", default=False,
                                                         description="")  # SU/objects/china_night/EvilPachinkoChina.xml
    bpy.types.Object.bool_IsFusa = bpy.props.BoolProperty(name="IsFusa", default=True,
                                                          description="Adds a decoration on the outside of the wheel")  # SU/objects/china_day/ChinaRotationFloor.xml
    bpy.types.Object.bool_IsWall = bpy.props.BoolProperty(name="IsWall", default=True,
                                                          description="Surrounds the wheel with a cylinder")  # SU/objects/china_day/ChinaRotationFloor.xml
    bpy.types.Object.bool_IsFlying = bpy.props.BoolProperty(name="IsFlying", default=True,
                                                            description="")  # SU/objects/mission/Chao.xml
    bpy.types.Object.bool_IsIce = bpy.props.BoolProperty(name="IsIce", default=False,
                                                         description="")  # SU/objects/unused/MovingFloor.xml
    bpy.types.Object.bool_PathReverse = bpy.props.BoolProperty(name="PathReverse", default=False,
                                                               description="")  # SU/objects/unused/CarGenerator.xml
    bpy.types.Object.bool_IsDrawingSupportLine = bpy.props.BoolProperty(name="IsDrawingSupportLine", default=True,
                                                                        description="")  # SU/objects/unused/Occluder.xml
    bpy.types.Object.bool_IsDrawingBoudingSphere = bpy.props.BoolProperty(name="IsDrawingBoudingSphere", default=True,
                                                                          description="")  # SU/objects/unused/Occluder.xml
    bpy.types.Object.bool_EnableMoving = bpy.props.BoolProperty(name="EnableMoving", default=True,
                                                                description="")  # SU/objects/unused/MovingFloor.xml
    bpy.types.Object.bool_mIsChangeCamera = bpy.props.BoolProperty(name="m_IsChangeCamera", default=True,
                                                                   description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.bool_mIsEnableFromBack = bpy.props.BoolProperty(name="m_IsEnableFromBack", default=True,
                                                                     description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.bool_mIsEnableFromFront = bpy.props.BoolProperty(name="m_IsEnableFromFront", default=True,
                                                                      description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.bool_mIsPadCorrect = bpy.props.BoolProperty(name="m_IsPadCorrect", default=True,
                                                                 description="")  # SU/objects/playersystem/ChangeMode_3Dto2D.xml
    bpy.types.Object.bool_IsStartVelocityConstant = bpy.props.BoolProperty(name="IsStartVelocityConstant", default=True,
                                                                           description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsGroundOnly = bpy.props.BoolProperty(name="m_IsGroundOnly", default=False,
                                                                 description="")  # SU/objects/playersystem/JumpCollision.xml
    bpy.types.Object.bool_IsInitAll = bpy.props.BoolProperty(name="IsInitAll", default=True,
                                                             description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseON = bpy.props.BoolProperty(name="UseON", default=True,
                                                         description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseON1 = bpy.props.BoolProperty(name="UseON1", default=True,
                                                          description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseON2 = bpy.props.BoolProperty(name="UseON2", default=False,
                                                          description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseON3 = bpy.props.BoolProperty(name="UseON3", default=False,
                                                          description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseOff = bpy.props.BoolProperty(name="UseOff", default=True,
                                                          description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseOff1 = bpy.props.BoolProperty(name="UseOff1", default=False,
                                                           description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseOff2 = bpy.props.BoolProperty(name="UseOff2", default=False,
                                                           description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_UseOff3 = bpy.props.BoolProperty(name="UseOff3", default=False,
                                                           description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.bool_mIsLimitEdge = bpy.props.BoolProperty(name="m_IsLimitEdge", default=True,
                                                                description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.bool_mIsReverseCameraEnable = bpy.props.BoolProperty(name="m_IsReverseCameraEnable", default=False,
                                                                          description="")  # SU/objects/playersystem/ChangeMode_3DtoDash.xml
    bpy.types.Object.bool_mIsEnableWallWalk = bpy.props.BoolProperty(name="m_IsEnableWallWalk", default=True,
                                                                     description="")  # SU/objects/playersystem/WallWalkEnableCollision.xml
    bpy.types.Object.bool_IsStopEnemy = bpy.props.BoolProperty(name="IsStopEnemy", default=True,
                                                               description="")  # SU/objects/playersystem/StopPeopleObject.xml
    bpy.types.Object.bool_IsStopPlayer = bpy.props.BoolProperty(name="IsStopPlayer", default=True,
                                                                description="")  # SU/objects/playersystem/StopPeopleObject.xml
    bpy.types.Object.bool_mIsRate = bpy.props.BoolProperty(name="m_IsRate", default=False,
                                                           description="")  # SU/objects/playersystem/SpeedDownCollision.xml
    bpy.types.Object.bool_IsForceToGround = bpy.props.BoolProperty(name="IsForceToGround", default=False,
                                                                   description="Snaps the player to the ground")  # SU/objects/playersystem/AutorunStartCollision.xml
    bpy.types.Object.bool_mIsSign = bpy.props.BoolProperty(name="m_IsSign", default=True,
                                                           description="Display the shoe prompt")  # SU/objects/playersystem/SpeedDownCollision.xml
    bpy.types.Object.bool_IsBigChaserMode = bpy.props.BoolProperty(name="IsBigChaserMode", default=False,
                                                                   description="Determines if the bomb is used in a Big Chaser segment, allowing for the notification to appear.")  # SU/objects/day_objects/eBigChaserBomb.xml
    bpy.types.Object.bool_IsSideView = bpy.props.BoolProperty(name="IsSideView", default=False,
                                                              description="Size of the panel:   True = small   False = large")  # SU/objects/day_objects/TrickJumper.xml
    bpy.types.Object.bool_IsChangeCameraWhenPathChange = bpy.props.BoolProperty(name="IsChangeCameraWhenPathChange",
                                                                                default=True,
                                                                                description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_IsPathChange = bpy.props.BoolProperty(name="IsPathChange", default=False,
                                                                description="")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.bool_IsWallWalk = bpy.props.BoolProperty(name="IsWallWalk", default=False,
                                                              description="Enables wall running if the player launches into a wall")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.bool_IsYawUpdate = bpy.props.BoolProperty(name="IsYawUpdate", default=False,
                                                               description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsConstantFrame = bpy.props.BoolProperty(name="m_IsConstantFrame", default=False,
                                                                    description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsConstantPosition = bpy.props.BoolProperty(name="m_IsConstantPosition", default=True,
                                                                       description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsMonkeyHunting = bpy.props.BoolProperty(name="m_IsMonkeyHunting", default=False,
                                                                    description="If true, automatically steers Sonic towards the MonkeyTarget.")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsStopBoost = bpy.props.BoolProperty(name="m_IsStopBoost", default=False,
                                                                description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsTo3D = bpy.props.BoolProperty(name="m_IsTo3D", default=False,
                                                           description="Changes the perspective to 3D when interacting with the object.")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_HasBase = bpy.props.BoolProperty(name="HasBase", default=False,
                                                           description="Toggles whether the spring has an extra model at the base.")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_mIsMonkeyHuntingLowAngle = bpy.props.BoolProperty(name="m_IsMonkeyHuntingLowAngle",
                                                                            default=True,
                                                                            description="")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.bool_IsMessageOn = bpy.props.BoolProperty(name="IsMessageOn", default=True,
                                                               description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.bool_IsMoveable = bpy.props.BoolProperty(name="IsMoveable", default=True,
                                                              description="")  # SU/objects/adabat_day/Beach_PressThorn.xml
    bpy.types.Object.bool_IsTopThorn = bpy.props.BoolProperty(name="IsTopThorn", default=True,
                                                              description="")  # SU/objects/day_objects/PressThorn.xml
    bpy.types.Object.bool_IsChangeCameraWhenChangePath = bpy.props.BoolProperty(name="IsChangeCameraWhenChangePath",
                                                                                default=False,
                                                                                description="Resets the camera upon changing paths.")  # SU/objects/day_objects/DashRing.xml
    bpy.types.Object.bool_IsChangePath = bpy.props.BoolProperty(name="IsChangePath", default=False,
                                                                description="Used when leaving the current spline.")  # SU/objects/day_objects/DashRing.xml
    bpy.types.Object.bool_IsHeadToVelocity = bpy.props.BoolProperty(name="IsHeadToVelocity", default=False,
                                                                    description="")  # SU/objects/day_objects/DashRing.xml
    bpy.types.Object.bool_IsTo3D = bpy.props.BoolProperty(name="IsTo3D", default=False,
                                                          description="Changes the mode to 3D when interacting with the object.")  # SU/objects/day_objects/DashRing.xml
    bpy.types.Object.bool_IsTriangleJump = bpy.props.BoolProperty(name="IsTriangleJump", default=True,
                                                                  description="")  # SU/objects/day_objects/TriangleJumpCollision.xml
    bpy.types.Object.bool_mFailLowAngle = bpy.props.BoolProperty(name="m_FailLowAngle", default=True,
                                                                 description="")  # SU/objects/day_objects/TrickAttackPanel.xml
    bpy.types.Object.bool_IsStartPositionConstant = bpy.props.BoolProperty(name="IsStartPositionConstant", default=True,
                                                                           description="")  # SU/objects/day_objects/WideSpring.xml
    bpy.types.Object.bool_IsJumpCancel = bpy.props.BoolProperty(name="IsJumpCancel", default=True,
                                                                description="When true, allows the player to jump off the pulley.")  # SU/objects/day_objects/Pulley.xml
    bpy.types.Object.bool_IsNoBug = bpy.props.BoolProperty(name="IsNoBug", default=False,
                                                           description="")  # SU/objects/day_objects/Pulley.xml
    bpy.types.Object.bool_IsWaitUp = bpy.props.BoolProperty(name="IsWaitUp", default=False,
                                                            description="   True: Waits until an event activates it, causing it to lower.   False: Lowered by default, allowing Sonic to use it.")  # SU/objects/day_objects/UpReel.xml
    bpy.types.Object.bool_IsFront = bpy.props.BoolProperty(name="IsFront", default=True,
                                                           description="")  # SU/objects/day_objects/GrindDashPanel.xml
    bpy.types.Object.bool_IsUsePanel = bpy.props.BoolProperty(name="IsUsePanel", default=True,
                                                              description="")  # SU/objects/day_objects/DirectionalThorn.xml
    bpy.types.Object.bool_UseRigidBody = bpy.props.BoolProperty(name="UseRigidBody", default=True,
                                                                description="")  # SU/objects/day_objects/DirectionalThorn.xml
    bpy.types.Object.bool_UsePanel = bpy.props.BoolProperty(name="UsePanel", default=True,
                                                            description="")  # SU/objects/day_objects/DirectionalThorn.xml
    bpy.types.Object.bool_IsDownShot = bpy.props.BoolProperty(name="IsDownShot", default=False,
                                                              description="Plays the success sfx/animation when launching with B")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.bool_IsQuestion = bpy.props.BoolProperty(name="IsQuestion", default=False,
                                                              description="Displays a question mark as the success button")  # SU/objects/day_objects/JumpSelector.xml
    bpy.types.Object.bool_IsChangeBossParamDist = bpy.props.BoolProperty(name="IsChangeBossParamDist", default=False,
                                                                         description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.bool_IsChangeBossParamSpeed = bpy.props.BoolProperty(name="IsChangeBossParamSpeed", default=False,
                                                                          description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.bool_IsChangePlayerParamSpeed = bpy.props.BoolProperty(name="IsChangePlayerParamSpeed",
                                                                            default=True,
                                                                            description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.bool_PlaySmokeEffect = bpy.props.BoolProperty(name="PlaySmokeEffect", default=False,
                                                                   description="")  # SU/objects/tornado_obj/ExStageParamChangeCol.xml
    bpy.types.Object.bool_IsRight = bpy.props.BoolProperty(name="IsRight", default=False,
                                                           description="")  # SU/objects/mykonos_day/Pelican.xml
    bpy.types.Object.bool_IsEnterFromTail = bpy.props.BoolProperty(name="IsEnterFromTail", default=False,
                                                                   description="")  # SU/objects/holoska_day/Whale.xml
    bpy.types.Object.bool_IsWaterEffect = bpy.props.BoolProperty(name="IsWaterEffect", default=False,
                                                                 description="")  # SU/objects/holoska_day/Icicle.xml
    bpy.types.Object.bool_IsRegularly = bpy.props.BoolProperty(name="IsRegularly", default=False,
                                                               description="")  # SU/objects/sounds/ObjBaseSound.xml
    bpy.types.Object.bool_IsRevival = bpy.props.BoolProperty(name="IsRevival", default=False,
                                                             description="")  # SU/objects/night_enemies/EvilEnemyFloatCannon.xml
    bpy.types.Object.bool_EnableEffect = bpy.props.BoolProperty(name="EnableEffect", default=True,
                                                                description="Determines if the enemy spawns with particle and sound effects.")  # SU/objects/night_enemies/EnemyObjEnemyHole.xml
    bpy.types.Object.bool_IsHomeHole = bpy.props.BoolProperty(name="IsHomeHole", default=True,
                                                              description="")  # SU/objects/night_enemies/EvilEnemyMoleelHole.xml
    bpy.types.Object.bool_IsDefaultHide = bpy.props.BoolProperty(name="IsDefaultHide", default=False,
                                                                 description="")  # SU/objects/night_bosses/BossEggDragoonBattlePlatform.xml
    bpy.types.Object.bool_IsLast = bpy.props.BoolProperty(name="IsLast", default=False,
                                                          description="")  # SU/objects/night_bosses/BossEggDragoonBattlePlatform.xml
    bpy.types.Object.bool_evilegbbossobjhhcraneS = bpy.props.BoolProperty(name="evil_egbboss_obj_hh_crane_S",
                                                                          default=True,
                                                                          description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_evilegbbossobjhhfloatfloorBS = bpy.props.BoolProperty(
        name="evil_egbboss_obj_hh_floatfloorB_S", default=True,
        description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_evilegbbossobjhhrockAS = bpy.props.BoolProperty(name="evil_egbboss_obj_hh_rockA_S",
                                                                          default=False,
                                                                          description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_evilegbbossobjhhrockBS = bpy.props.BoolProperty(name="evil_egbboss_obj_hh_rockB_S",
                                                                          default=False,
                                                                          description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_evilegbbossobjhhrockCS = bpy.props.BoolProperty(name="evil_egbboss_obj_hh_rockC_S",
                                                                          default=False,
                                                                          description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_evilegbbossobjhhrockDS = bpy.props.BoolProperty(name="evil_egbboss_obj_hh_rockD_S",
                                                                          default=False,
                                                                          description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_evilegbbossobjhhrockES = bpy.props.BoolProperty(name="evil_egbboss_obj_hh_rockE_S",
                                                                          default=False,
                                                                          description="")  # SU/objects/night_bosses/EggBoss_HavokGenerator.xml
    bpy.types.Object.bool_IsControllableShotAngle = bpy.props.BoolProperty(name="IsControllableShotAngle",
                                                                           default=False,
                                                                           description="Allows the player to manually rotate the cannon.")  # SU/objects/unused_day/Cannon.xml
    bpy.types.Object.bool_mGIEnable = bpy.props.BoolProperty(name="m_GIEnable", default=True,
                                                             description="")  # SU/objects/system/StartDynamicPreloadingCollision.xml
    bpy.types.Object.bool_mTerrainEnable = bpy.props.BoolProperty(name="m_TerrainEnable", default=True,
                                                                  description="")  # SU/objects/system/StartDynamicPreloadingCollision.xml
    bpy.types.Object.vector_TargetPosition = bpy.props.FloatVectorProperty(name="TargetPosition",
                                                                           default=(0.0, 0.0, 0.0),
                                                                           description="Coordinates for the camera to lock on to.")  # SU/objects/cameras/ObjCameraFix.xml
    bpy.types.Object.vector_TargetPositionFix = bpy.props.FloatVectorProperty(name="TargetPositionFix",
                                                                              default=(0.0, 0.0, 0.0),
                                                                              description="")  # SU/objects/cameras/ObjCameraPoint.xml
    bpy.types.Object.vector_LookPathPosition = bpy.props.FloatVectorProperty(name="LookPathPosition",
                                                                             default=(0.0, 0.0, 0.0),
                                                                             description="")  # SU/objects/cameras/ObjCameraPathPath.xml
    bpy.types.Object.vector_AlivePoint = bpy.props.FloatVectorProperty(name="AlivePoint", default=(0.0, 0.0, 0.0),
                                                                       description="")  # SU/objects/night_enemies/EvilEnemyFloatNormal.xml
    bpy.types.Object.vector_ResultPosition = bpy.props.FloatVectorProperty(name="ResultPosition",
                                                                           default=(0.0, 0.0, 0.0),
                                                                           description="")  # SU/objects/common/GoalRing.xml
    bpy.types.Object.vector_ShotVelocity = bpy.props.FloatVectorProperty(name="ShotVelocity", default=(0.0, 0.0, 0.0),
                                                                         description="")  # SU/objects/euc_day/EU_Fountain.xml
    bpy.types.Object.vector_TargetDirection = bpy.props.FloatVectorProperty(name="TargetDirection",
                                                                            default=(0.0, 0.0, 0.0),
                                                                            description="")  # SU/objects/system/ChangePathCollision.xml
    bpy.types.Object.vector_mMonkeyTarget = bpy.props.FloatVectorProperty(name="m_MonkeyTarget",
                                                                          default=(0.0, 0.0, 0.0),
                                                                          description="Location to launch Sonic when IsMonkeyHunting is enabled.")  # SU/objects/africa_day/DrumSpring.xml
    bpy.types.Object.vector_SlidingPosition = bpy.props.FloatVectorProperty(name="SlidingPosition",
                                                                            default=(0.0, 0.0, 0.0),
                                                                            description="")  # SU/objects/navi/NavigationCollision.xml
    bpy.types.Object.vector_GroupMove = bpy.props.FloatVectorProperty(name="GroupMove", default=(0.0, 0.0, 0.0),
                                                                      description="")  # SU/objects/system/Grouper.xml
    bpy.types.Object.string_CharaType = bpy.props.StringProperty(name="CharaType", default="YoungWoman01C",
                                                                 description="")  # SU/objects/twn_nyc/IrremovableMobNY.xml
    bpy.types.Object.string_Motion = bpy.props.StringProperty(name="Motion", default="Sit1",
                                                              description="")  # SU/objects/twn_nyc/IrremovableMobNY.xml
    bpy.types.Object.string_EffectType = bpy.props.StringProperty(name="EffectType", default="eu_stg_fountain_water",
                                                                  description="")  # SU/objects/common/StageEffect.xml
    bpy.types.Object.string_GroupID = bpy.props.StringProperty(name="GroupID", default="hint_S_002",
                                                               description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.string_Type = bpy.props.StringProperty(name="Type", default="IronBox2",
                                                            description="")  # SU/objects/common/ObjectPhysics.xml
    bpy.types.Object.string_PositionID = bpy.props.StringProperty(name="PositionID", default="WithMauro",
                                                                  description="")  # SU/objects/npcs/Rouks.xml
    bpy.types.Object.string_Target = bpy.props.StringProperty(name="Target", default="YayaPos",
                                                              description="")  # SU/objects/town/TownTarget.xml
    bpy.types.Object.string_StageType = bpy.props.StringProperty(name="StageType", default="day1",
                                                                 description="")  # SU/objects/town/EntranceDoor.xml
    bpy.types.Object.string_SequenceID = bpy.props.StringProperty(name="SequenceID", default="ChangeTimeAfricaETF",
                                                                  description="The script loaded upon switching")  # SU/objects/town/TimeSwitch.xml
    bpy.types.Object.string_Pitch = bpy.props.StringProperty(name="Pitch", default="5",
                                                             description="Angle the player will be launched on the Y axis")  # SU/objects/playersystem/JumpCollision.xml
    bpy.types.Object.string_ONLayerIndex = bpy.props.StringProperty(name="ONLayerIndex", default="Layer1",
                                                                    description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_ONLayerIndex1 = bpy.props.StringProperty(name="ONLayerIndex1", default="Base",
                                                                     description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_ONLayerIndex2 = bpy.props.StringProperty(name="ONLayerIndex2", default="Layer0",
                                                                     description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_ONLayerIndex3 = bpy.props.StringProperty(name="ONLayerIndex3", default="Layer0",
                                                                     description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_OffLayerIndex = bpy.props.StringProperty(name="OffLayerIndex", default="Layer0",
                                                                     description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_OffLayerIndex1 = bpy.props.StringProperty(name="OffLayerIndex1", default="Layer0",
                                                                      description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_OffLayerIndex2 = bpy.props.StringProperty(name="OffLayerIndex2", default="Layer0",
                                                                      description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_OffLayerIndex3 = bpy.props.StringProperty(name="OffLayerIndex3", default="Layer0",
                                                                      description="")  # SU/objects/playersystem/LayerChangeCollision.xml
    bpy.types.Object.string_CueName = bpy.props.StringProperty(name="CueName", default="objsn_whoosh3",
                                                               description="")  # SU/objects/sounds/ObjWindNoiseCollision.xml
    bpy.types.Object.string_FileName = bpy.props.StringProperty(name="FileName", default="se_object_common_sonic",
                                                                description="")  # SU/objects/sounds/ObjWindNoiseCollision.xml
    bpy.types.Object.string_Event = bpy.props.StringProperty(name="Event", default="GetAwayFromAfricaTown",
                                                             description="")  # SU/objects/system/SequenceChangeCollision.xml
    bpy.types.Object.id_list_CameraList = bpy.props.PointerProperty(type=bpy.types.Collection, name="CameraList",
                                                                    description="")  # SU/objects/cameras/ObjCameraBlend.xml
    bpy.types.Object.id_list_TargetListOFF = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetListOFF",
                                                                       description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.id_list_TargetListON = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetListON",
                                                                      description="")  # SU/objects/holoska_night/EvilTorch.xml
    bpy.types.Object.id_list_TargetListrightoff = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                            name="TargetListright_off",
                                                                            description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.id_list_TargetListrighton = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                           name="TargetListright_on",
                                                                           description="")  # SU/objects/night_objects/EvilLeverSwitch.xml
    bpy.types.Object.id_list_TargetListOff = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetListOff",
                                                                       description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.id_list_TargetListOff2 = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                        name="TargetListOff2",
                                                                        description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.id_list_TargetListOn = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetListOn",
                                                                      description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.id_list_TargetListOn2 = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetListOn2",
                                                                       description="")  # SU/objects/common/HintRing.xml
    bpy.types.Object.id_list_TargetListDown1F = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                          name="TargetListDown_1F",
                                                                          description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.id_list_TargetListUp2F = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                        name="TargetListUp_2F",
                                                                        description="")  # SU/objects/euc_night/EvilElevator.xml
    bpy.types.Object.id_list_TargetList0 = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetList0",
                                                                     description="The first list of objects to group")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.id_list_TargetList = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetList",
                                                                    description="")  # SU/objects/system/Grouper.xml
    bpy.types.Object.id_list_TargetList1 = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetList1",
                                                                     description="The second list of objects to group")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.id_list_TargetList2 = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetList2",
                                                                     description="The third list of objects to group")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.id_list_TargetList3 = bpy.props.PointerProperty(type=bpy.types.Collection, name="TargetList3",
                                                                     description="The fourth list of objects to group")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.id_list_TriggerList = bpy.props.PointerProperty(type=bpy.types.Collection, name="TriggerList",
                                                                     description="Triggers the event(s) upon interacting with the object(s)")  # SU/objects/system/EventSetter.xml
    bpy.types.Object.id_list_TargetListEnter = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                         name="TargetListEnter",
                                                                         description="")  # SU/objects/system/EventCollision2.xml
    bpy.types.Object.id_list_TargetListLeave = bpy.props.PointerProperty(type=bpy.types.Collection,
                                                                         name="TargetListLeave",
                                                                         description="")  # SU/objects/system/EventCollision2.xml
