#!/usr/bin/env bash
# Record a demo screencast using ffmpeg
# Requirements: ffmpeg, x11grab (for Linux) or avfoundation (for macOS)
# Example (Linux):
# ffmpeg -video_size 1280x720 -framerate 30 -f x11grab -i :0.0 -y screencast_demo.mp4

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  ffmpeg -video_size 1280x720 -framerate 30 -f x11grab -i :0.0 -y screencast_demo.mp4
elif [[ "$OSTYPE" == "darwin"* ]]; then
  ffmpeg -f avfoundation -framerate 30 -i "1" -video_size 1280x720 -y screencast_demo.mp4
else
  echo "Unsupported OS for automated screencast."
fi
