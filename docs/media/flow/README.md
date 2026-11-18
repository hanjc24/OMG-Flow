# Execution gallery

Eight curated clips from the sixteen standing-start runs recorded on November 9,
2026: 50 Hz control, 0.2 s replanning, TensorRT FP16 Euler-10, P25, 8 Hz suffix
filter, checkpoint 190,500. These are selected illustrations, not an evaluation sample.

The no-LFS branch omits the eight source MP4 files. GIFs are 8-second excerpts
at 320 × 240 and 8 fps, generated from the same complete saved `executed`
trajectories. No poses are modified and no physics or inference is rerun.
Original NPZ bytes are preserved.

| Clip | Visible motion | GIF start (s) |
|---|---|---:|
| [dance](dance.gif) | Small steps and gestures | 0 |
| [turn](turn.gif) | Repeated turns | 0 |
| [wave_arms](wave_arms.gif) | Raise and wave arms | 4 |
| [kick](kick.gif) | Low kicks and steps | 8 |
| [walking_forward](walking_forward.gif) | Walk forward | 8 |
| [spin](spin.gif) | Spin around | 4 |
| [side_step](side_step.gif) | Side steps | 12 |
| [crouch_rebound](crouch_rebound.gif) | Crouch and rebound | 0 |

The selection favors visible, varied movement: gestures, turning, arm raises,
low kicks, forward and lateral steps, rotation, and a crouch/rebound. Captions
describe visible motion; the original prompts remain in [cases.json](cases.json).
In particular, crouch/rebound does not establish a high jump, and the side-step
execution has substantial reference-position drift. Full metrics remain in each
clip's JSON; camera tracking does not remove that error from the recorded data.

[manifest.json](manifest.json) preserves source/asset hashes, selected-case metrics
and presentation settings. Per-clip JSONs use portable model paths; their hashes
reflect this sanitization. The full sixteen-case evidence is in
[commit 6cc9331](https://github.com/KunYing-Lee/OMG-Flow/tree/6cc9331/docs/media/flow).

Re-render the saved trajectories locally (render/tracking dependencies required):

```bash
PYTHONPATH=src python scripts/validation/render_gallery.py
```

To run fresh inference and physics on one idle GPU:
`make showcase SHOWCASE_ARGS="--gpu 0"`. That command retains its diagnostic
paired rendering; use the saved-trajectory renderer above for this gallery layout.

Training data includes Motion Data by [Bones Studio](https://bones.studio/).
Use of the underlying dataset is subject to the BONES Motion Capture Dataset License Agreement.
