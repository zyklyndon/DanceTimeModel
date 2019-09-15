#!/usr/bin/env bash

mkdir ./data/target

mv $1 ./data/target/mv.mp4

mkdir checkpoints

mkdir checkpoints/target

nvidia-docker run -it -v /home/kelvin_yu98:/workspace/dance -w /workspace/dance/dancetime dance:latest python make_target.py

nvidia-docker run -it -v /home/kelvin_yu98:/workspace/dance -w /workspace/dance/dancetime dance:latest python train_pose2vid.py

nvidia-docker run -it -v /home/kelvin_yu98:/workspace/dance -w /workspace/dance/dancetime dance:latest python normalization.py

nvidia-docker run -it -v /home/kelvin_yu98:/workspace/dance -w /workspace/dance/dancetime dance:latest python transfer.py

nvidia-docker run -it -v /home/kelvin_yu98:/workspace/dance -w /workspace/dance/dancetime dance:latest python make_mp4.py

nvidia-docker run -it -v /home/kelvin_yu98:/workspace/dance -w /workspace/dance/dancetime dance:latest python simscore.py

mv test.mp4 dancetime/$2-after.mp4
mv test2.mp4 dancetime/$2-skeleton.mp4

rm -rf ./data/target

rm -rf ./checkpoints

rm -rf ./results
