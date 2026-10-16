# Robotics: Arduino to Physical AI: changelog

- **Notes in → out:** 200 → 293
- **Subdecks:** 13 → 12. "02 Microcontrollers & Arduino" and "06 Raspberry Pi & Embedded Linux" are now one subdeck, "02 Microcontrollers & Embedded Linux". The rest are renumbered 01–12.
- **Splits:** 92 source notes split, giving 94 extra notes. Most source answers ran 60–150 words and asked 2–4 things at once ("define X, give examples, name pitfalls"). Each now becomes 2–3 atomic cards: definition, why/when, and pitfall.
- **Enumerations → clozes (12):** Ohm/power, UNO R3 specs, Pi 5 essentials, depth-camera principles, PID terms, step-response metrics, C-space/task/workspace, DH parameters, vision task types, path/trajectory/control, ROS 2 primitives, Nav2 servers.
- **Merges (1):** "Why is a Raspberry Pi not a drop-in replacement for an Arduino?" (CyFdIhvSdo) was merged into "MCU vs. MPU" (ORq|{El)g7). The two made the same point: Linux timing jitter vs. deterministic MCU I/O.
- **Deletions (whole notes):** none. Trimmed instead (volatile or trivia detail moved to `extra` or dropped):
  - UNO R4 / UNO Q / Pi 5 / Jetson spec sheets: cut to the facts that change a design decision (5 V vs 3.3 V, per-pin current, RP1 GPIO break, CUDA or not).
  - ROS 2 distro list: kept the release pattern and the selection rule; the current distros moved to `extra`.
  - Humanoid "players (2026)" vendor list: dropped (marketing trivia).
  - GR00T N1.7 backbone/licence specifics, Gemini ASIMOV/tool-calling details, the Cosmos 3 announcement, and Helix/RMA paper-year citations: dropped or moved to `extra`.
  - Book/URL citations removed from `source` (URLs stripped; short author/title kept as context label).
- **Analogies added:** 69 (24% of cards). Examples: pull-up = door spring, flyback diode = water-hammer relief valve, gyro/accel fusion = fast-drifting stopwatch vs jittery wall clock, CAN arbitration = polite simultaneous speakers, FOC = merry-go-round frame, odometry drift = blindfolded step counting, DAgger = instructor grabbing the wheel, multi-modality = averaging left/right swerves into the tree.
- **Contrast/why cards added by splitting:** linear vs buck (and why not linear for a Pi), P-only steady-state error, impedance vs admittance hardware, cubic vs quintic, RL vs IL per domain, PPO vs SAC as separate cards, odom vs map frames.

## Product-content review

**Deleted**
- "Arduino UNO Q (2025): what robot architecture does it put on one board?" — dated product release; the Linux-computer + real-time-MCU pattern is already taught by the MCU-vs-MPU and two-tier compute cards
- "Raspberry Pi 5: GPIO, USB and camera ports hang off the in-house {{c1::RP1}} I/O chip; a {{c2::PCIe 2.0 ×1}} connector adds NVMe or AI accelerators; it needs a {{c3::5 V / 5 A}} USB-C supply and active cooling." — SBC spec sheet (I/O chip, PCIe, PSU rating); the power-budget and GPIO lessons live on other cards
- "Raspberry Pi Pico vs. Raspberry Pi?" — vendor lineup comparison; the MCU-vs-Linux-computer distinction is the MCU vs. MPU card

**Rewritten** (guid kept; product moved to a short example in `extra`)
- "Arduino UNO R3: {{c1::ATmega328P}}, 8-bit AVR @ 16 MHz, {{c2::5 V}} logic, {{c3::10-bit}} ADC, 6 PWM pins, external interrupts only on pins {{c4::2 and 3}}." → "Before wiring to an MCU board, check four datasheet facts: {{c1::logic level}} (5 V or 3.3 V), {{c2::ADC resolution}} and reference, which pins offer {{c3::hardware PWM}}, and which pins support {{c4::external interrupts}}."
- "Arduino UNO R4 vs R3: main upgrade, and the electrical caveat?" → "Moving a design to a newer, faster MCU board: which electrical assumption most often breaks?"
- "ESP32: why is it popular in hobby robotics?" → "What does a Wi-Fi/Bluetooth-capable MCU (e.g. ESP32) add to a hobby robot?"
- "ESP32 pitfalls?" → "Pitfalls of wireless SoC-class MCUs (e.g. ESP32)?"
- "GPIO code from a Pi 4 fails on a Pi 5. Why, and what should you use?" → "Register-poking GPIO code breaks on a new SBC revision. Why, and what should you use instead?"
- "Current Raspberry Pi camera software stack?" → "Two camera stacks on an embedded Linux board: how does each reach OpenCV?"
- "Raspberry Pi AI HAT+: what can and can't it do?" → "Edge NPU accelerator vs GPU: what can and can't a few-watt NPU (e.g. Hailo on a Pi HAT) do?"
- "When do you step up from a Raspberry Pi to an NVIDIA Jetson?" → "When does a robot need an on-board GPU computer (e.g. NVIDIA Jetson) instead of a plain SBC?"
- "Isaac Sim/Lab and Newton: what are they for?" → "GPU-parallel robot-learning simulators vs a classic ROS simulator: what distinguishes them?"
- "Helix 02 (Figure, 2026): what is 'System 0'?" → "Three-tier VLA hierarchy: what is a 'System 0' layer?"
- "NVIDIA Isaac GR00T N-series: what is it?" → "What training recipe do open humanoid foundation policies (e.g. NVIDIA GR00T N) follow?"
- "Gemini Robotics 1.5: what are the two models?" → "Orchestrator–executor split in robot foundation models: what does each model do?"
- "Gemini Robotics 1.5: what are 'Motion Transfer' and 'thinking before acting'?" → "What are motion transfer and 'thinking before acting' in VLAs?"

**Scrubbed** (dated version lists / vendor lineups removed from `extra`, card otherwise unchanged)
- "ROS 2 release pattern, and which distro should a new project pick?"
- "Gazebo vs. MuJoCo: what is each best at?"
