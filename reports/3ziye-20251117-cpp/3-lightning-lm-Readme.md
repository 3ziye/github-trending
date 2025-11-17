# Lightning-LM

Lightning-Speed Lidar Localization and Mapping

Lightning-LM is a complete laser mapping and localization module.

Features of Lightning-LM:

1. [done] Complete 3D Lidar SLAM, fast LIO front-end (AA-FasterLIO), standard
2. [done] 3D to 2D map conversion (g2p5), optional, if selected outputs real-time 2D grid map, can be saved
3. [done] Real-time loop closure detection, standard, performs back-end loop closure detection and correction if
   selected
4. [done] Smooth high-precision 3D Lidar localization, standard
5. [done] Dynamic loading scheme for map partitions, suitable for large-scale scenes
6. [done] Localization with separate dynamic and static layers, adaptable to dynamic scenes, selectable strategies for
   dynamic layer, optional, if selected saves dynamic layer map content, three strategies available (short-term,
   medium-term, permanent), default is permanent
7. [done] High-frequency IMU smooth output, standard, 100Hz
8. GPS geoinformation association, optional (TODO)
9. Vehicle odometry input, optional (TODO)
10. [done] Lightweight optimization library miao and incremental optimization (derived from g2o, but lighter and faster,
    supports incremental optimization, no need to rebuild optimization model), standard, used in both loop closure and
    localization
11. [done] Two verification schemes: offline and online. Offline allows breakpoint debugging with strong consistency.
    Online allows multi-threaded concurrency, fast processing speed, dynamic frame skipping, and low resource usage.
12. [done] High-frequency output based on extrapolator and smoother, adjustable smoothing factor
13. [done] High-performance computing: All the above features can run using less than one CPU core on the pure CPU
    side (online localization 0.8 cores, mapping 1.2 cores, 32-line LiDAR, without UI).

## Updates

1. 2025.11.13

- Fix two logic typos in FasterLIO.
- Add global height constraint that can be configured in loop_closing.with_height. If set true, lightning-lm will keep
  the output map into the same height to avoid the Z-axis drifting in large scenes. It should not be set if you are
  using lightning-lm in scenes that have multi-floor or stairs structures.

## Examples

- Mapping on the VBR campus dataset:

<video controls width="100%">
  <source src="doc/slam_vbr.mp4" type="video/mp4">
</video>

- Localization on VBR

<video controls width="100%">
  <source src="doc/lm_loc_vbr_campus.mp4" type="video/mp4">
</video>

- Map on VBR
    - Point Cloud

  ![](./doc/campus_vbr.png)
    - Grid Map

  ![](./doc/campus.png)

- Localization on the NCLT dataset

<video controls width="100%">
  <source src="doc/lm_loc1_nclt.mp4" type="video/mp4">
</video>

## Build

### Environment

Ubuntu 22.04 or higher.

Ubuntu 20.04 should also work, but not tested.

### Dependencies

- ros2 humble or above
- Pangolin (for visualization, see thirdparty)
- OpenCV
- PCL
- yaml-cpp
- glog
- gflags
- pcl_conversions

On Ubuntu 22.04, run: ```bash ./scripts/install_dep.sh```.

### Build

Build this package with ```colcon build```.

Then ```source install/setup.bash``` to use it.

### Build Results

After building, you will get the corresponding online/offline mapping and localization programs for this package. The
offline programs are suitable for scenarios with offline data packets to quickly obtain mapping/localization results,
while the online programs are suitable for scenarios with actual sensors to obtain real-time results.

For example, calling the offline mapping program on the NCLT dataset:
```ros2 run lightning run_slam_offline --input_bag ~/data/NCLT/20130110/20130110.db3 --config ./config/default_nclt.yaml```

If you want to call the online version, just change the offline part to online.

## Testing on Datasets

You can directly use our converted datasets. If you need the original datasets, you need to convert them to the ros2 db3
format.

Converted dataset addresses:

- OneDrive: https://1drv.ms/f/c/1a7361d22c554503/EpDSys0bWbxDhNGDYL_O0hUBa2OnhNRvNo2Gey2id7QMQA?e=7Ui0f5
- BaiduYun:

Original dataset addresses:

- NCLT dataset: http://robots.engin.umich.edu/nclt/
- UrbanLoco dataset: https://github.com/weisongwen/UrbanLoco
- VBR dataset: https://www.rvp-group.net/slam-dataset.html

### Mapping Test

1. Real-time mapping (real-time bag playback)
    - Start the mapping program:
      ```ros2 run lightning run_slam_online --config ./config/default_nclt.yaml```
    - Play the data bag
    - Save the map ```ros2 service call /lightning/save_map lightning/srv/SaveMap "{map_id: new_map}"```
2. Offline mapping (traverse data, faster)
    - ```ros2 run lightning run_slam_offline --config ./config/default_nclt.yaml --input_bag [bag_file]```
    - It will automatically save to the data/new_map directory after finishing.
3. Viewing the map
    - View the full map: ```pcl_viewer ./data/new_map/global.pcd```
    - The actual map is stored in blocks, global.pcd is only for displaying the result.
    - map.pgm sto