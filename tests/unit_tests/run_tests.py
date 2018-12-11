import unittest
import tests.unit_tests.navigator_tests.NavigationTest as nav
import tests.unit_tests.collision_tests.tools_test as tools
import tests.unit_tests.direction_map_tests.DirectionMapTests as dm

#Run this file to run all unit tests
#Other python running methods aren't much more better in my opinion

if __name__ == '__main__':

    nav_1 = nav.TestAngle
    nav_2 = nav.TestDirection
    nav_3 = nav.TestDistance

    tool_1=tools.ObstacleAdding
    tool_2=tools.TestMarking

    directmap_1=dm.GetingAngleTest
    directmap_2=dm.GettingDirectionTests
    directmap_3=dm.GettingPosTests
    directmap_4=dm.GettingStepSizeTests

    unittest.main()
