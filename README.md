# design3
Projet Design III - Équipe 12

#packets nécéssaires

- opencv 2.4.9
- ros-hydro-desktop-full
- ros-hydro-cmake-modules
- ros-hydro-openni-launch
- ros-hydro-openni-camera
- curl
- realpath

#projets externes fournis dans "extern"

- ar_track_alvar (noeud ros)
- libjansson 2.7

# compiler le projet

- mettre le répertoire "design3" dans le répertoire "src" d'un workspace catkin ros-hydro:
- cd vers le répertoire "design3"
- rouler <code>$ ./build.sh</code>

# rouler le système de localisation du robot

- <code>$ roslaunch d3_table_transform d3_table_transform.launch</code>
- visualizer avec rviz (tf importantes /robot_center et /d3_table_origin)

# rouler la détection des cubes (actuellement ros-indépendant)

- cd dans le répertoire "build"
- rouler <code>bin/detect_cube color</code> (remplacer color par un des string suivants: {blue, green, yellow, red, black, white}) **Avoir une caméra de branchée

# rouler les tests des classes de vision

- cd dans le répertoire "build"
- rouler <code>for i in bin/*Test; do $i; done</code>
