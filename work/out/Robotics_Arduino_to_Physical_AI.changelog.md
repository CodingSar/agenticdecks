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
