# Smart Security Cam

A camera-monitoring and face-detection prototype combining a Python/OpenCV camera service, video streaming, and a companion Android app.

> **Historical project / legacy code.** The implementation reflects its 2017 development environment. It is published for documentation and educational purposes, not as a production-ready security system. Some planned features were left unfinished.

## What the project does

The prototype combines a camera-side service with an Android client:

- **Face detection:** OpenCV's Haar cascade detects faces in frames captured from a connected camera.
- **Snapshot capture:** The detection script can save a camera frame as `img2.jpg` when a face is detected.
- **Live streaming:** A Flask web server serves an MJPEG camera feed to a browser or the Android app.
- **Android client:** A Java app can connect to the camera by entering an IP address or scanning a QR code, display the HTTP stream, and send an email-address setting.
- **Experimental configuration and notifications:** The repository includes a TCP settings receiver and SMTP email helper, but the notification-sending calls are commented out in the detection script. Wi-Fi auto-configuration is also incomplete.

**Important distinction:** The code implements *face detection*, not identity recognition. It does not provide a trained face-recognition system, and automated email alerts are not enabled in the committed detection code.

## Architecture

```text
Camera / webcam
      |
      v
Python + OpenCV                    Android app (Java)
  |                                  |
  +-- Gesicht.py                     +-- IP address or QR scan
  |     Face detection               +-- Camera stream in WebView
  |     Snapshot capture             +-- Settings screen
  |
  +-- camera.py
  |     Camera frames
  |
  +-- webserver.py <--- HTTP :5000 -------- Android stream view
  |     Flask / MJPEG
  |
  +-- SettingSaver.py <- TCP :64932 ------- Android settings
  |     Local text-file state
  |
  +-- Mail.py
        SMTP helper (not active in the default detection path)
```

The services were designed for a camera-connected computer, such as a Raspberry Pi. The code uses a local camera device (`cv2.VideoCapture(0)`).

## Repository structure

| Path | Purpose |
| --- | --- |
| `Gesicht.py` | Face-detection loop and snapshot capture |
| `haarcascade_frontalface_default.xml` | OpenCV Haar cascade classifier |
| `camera.py` | Camera access and JPEG frame encoding |
| `webserver.py` | Flask web interface and MJPEG stream |
| `templates/index.html` | Minimal streaming webpage |
| `SettingSaver.py` | TCP listener that receives settings and stream commands |
| `Mail.py` | SMTP email helper (not invoked by default) |
| `auto_connect.py` | Unfinished Wi-Fi configuration experiment |
| `Settings.txt`, `WName.txt`, `Wlan.txt`, `Stream.txt` | Legacy local settings / stream state files; currently contain placeholders or state |
| `app/` | Android Studio project (Java) |

## Communication and behavior

| Component | Address / port | Notes |
| --- | --- | --- |
| Flask web interface | `http://<camera-ip>:5000/` | Displays the video page |
| MJPEG feed | `http://<camera-ip>:5000/video_feed` | Used by the webpage |
| Settings receiver | TCP `64932` | No authentication or encryption |

The camera-side scripts use `Stream.txt` as a simple mode flag: `0` for the detection path and `1` for streaming. `SettingSaver.py` can change this flag when it receives the corresponding commands. The Android client's current code does **not** automatically switch the flag, so the components are not a complete, plug-and-play workflow.

## Technology (2017)

- **Camera-side:** Python 2-style code, OpenCV, NumPy, Flask, and SMTP
- **Android:** Java, Android SDK 25 (minimum API 19), ZXing / JourneyApps for QR scanning
- **Build tooling:** Android Gradle Plugin 2.3.3 and Gradle 3.3

No pinned Python dependency list is included. Modern Python, OpenCV, Android Studio, and Gradle versions are not expected to run or build this project unchanged. Reproducing the historical environment may require substantial compatibility work.

## Security Considerations

This project was developed in 2017 as a prototype
for Jugend forscht and is provided for educational
and archival purposes.

It uses legacy dependencies and does not implement
modern security measures such as encrypted
communication or authentication.

It is not intended for production use without
additional security improvements.

## Background

Smart Security Cam was developed for *Jugend forscht* in 2017 and received first place at the regional competition (*Regionalwettbewerb*). The repository preserves the original student project as a historical and educational reference.
