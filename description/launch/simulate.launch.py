from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArguments
from launch.substitutions import ThisLaunchFileDir
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    # ========================
    # === Public Arguments ===
    # ========================

    # Gazebo
    
    use_gui_arg = DeclareLaunchArguments(
        'use_gui',
        default_value='false',
        description='whether to run gazebo GUI (Default: false)',
    )

    world_arg = DeclareLaunchArguments(
        'world',
        default_value='drag_race',
        description='which world to launch (Options: drag_race , circuit, urban | Default: drag_race)',
    )

    paused_arg = DeclareLaunchArguments(
        'paused',
        default_value='false',
        description='whether to run paused mode or not (Default: false)',
    )

    # rviz

    rviz_arg = DeclareLaunchArguments(
        'rviz',
        default_value='true',
        description='whether to launch rviz (Default: false)',
    )

    # rqt_steer

    rqt_steer_arg = DeclareLaunchArguments(
        'rqt_steer',
        default_value='false',
        description='whether to launch rqt_steer node (Default: false)',
    )

    # =============
    # === Nodes ===
    # =============

    # ===============================
    # === Call Other Launch Files ===
    # ===============================

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/empty_world.launch']),
        launch_arguments={
            'use_gui': use_gui_arg,
            'world': world_arg,
            'paused': paused_arg
        }.items(),
    )

    # 

    return LaunchDescription([
        gazebo_launch
    ])
'''
<launch>
    
    <arg name="use_gui" default="false"/>
    <arg name="rqt_steer" default="false"/>
    <arg name="rviz" default="false"/>

    <arg name="world" default="drag_race"/>

    <!-- Simulate 'world' using Gazebo -->
    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(find worlds)/$(arg world).world"/>
    
        <arg name="debug" value="false"/>
        <arg name="gui" value="$(arg use_gui)"/>
        <arg name="paused" value="false"/>
    </include>

    <!-- Spawn the robot -->
    <include file="$(find description)/launch/spawn.launch"/>

    <!-- MISCALLANEOUS -->

    <!-- rqt robot steering GUI -->
    <group if="$(arg rqt_steer)">
        <node pkg="rqt_robot_steering" type="rqt_robot_steering" name="rqt_robot_steering">
            <param name="default_topic" value="/man_vel"/>
        </node>
    </group>

    <!-- RViz -->
    <group if="$(arg rviz)">
        <include file="$(find description)/launch/view.launch"/>
    </group>

</launch>
'''