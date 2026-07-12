# Loop Rubrics

Use 0-5 scoring. Any hard category at 0-2 is a reject unless the director explicitly waives it.

## Image / Keyframe Hard Categories

- **Subject prominence**: main subject reads first at thumbnail size.
- **Style coherence**: one stable visual language; no uncontrolled photo/anime/fantasy collage.
- **Face/anatomy integrity**: primary faces, hands, and limbs are intentional and readable.
- **Composition cleanliness**: large shapes read before detail; no dirty full-frame micro clutter.
- **Detail density control**: ornament belongs to hero subject and one support device.
- **Prompt compliance**: requested deity/character, setting, action, and constraints remain intact.

Common failure labels:

- `style_mixing_fail`
- `face_collapse`
- `dirty_frame`
- `subject_lost`
- `overprompted_object_parade`
- `noisy_microdetail`
- `text_artifact`
- `anatomy_fail`
- `continuity_drift`
- `prompt_drift`

## Video Prompt Hard Categories

- **Source-style inheritance**: explicitly treats the approved image/keyframe as the immutable style authority and locks medium, edges/linework, texture, palette, lighting, proportions, identity, costume/prop design, and environment treatment. Only requested motion may change. A universal `no anime` phrase is insufficient and wrong for anime sources.
- **Dynamic style fingerprint**: derives the lock from the current project and actual image; does not reuse a fixed preferred style or unrelated project language.
- **Full-duration coverage**: declares duration and covers 0.0s through the exact endpoint with ordered, gap-free beats; each beat describes visible changes and the final beat settles into a usable end frame.
- **Duration fitness**: duration is justified from the actual image, performance, camera, reveal, and stability needs; it is not a fixed 5-second default, padded hold, or overloaded one-take.
- **Professional film specification**: each beat specifies performance/blocking/eye line, camera height/axis/lens/distance/movement, shot size/composition/focus, lighting/shadows, environment/material response, continuity locks, and held values—not merely a longer prose action description.
- **Single action clarity**: one main 5-10 second action, not multiple competing actions.
- **Motion feasibility**: no impossible choreography, uncontrolled crowds, or unsupported continuity.
- **Anchor consistency**: start/end frames and visible locks are named and preserved.
- **Camera readability**: camera move is simple enough to generate or backed by previs.
- **Audio rule**: ambience/SFX only; no music/BGM unless explicitly overridden.

## Video Output Hard Categories

- **Source-style fidelity**: first, middle, and last frames remain in the source image's exact visual language; no model-default anime, realism, 3D, painterly, or other medium conversion unless explicitly requested.
- **Timeline compliance**: visible action, camera, environment, lighting/material response, and final state match the time-coded prompt rather than collapsing into one repeated motion.
- **Subject stability**: identity and silhouette remain stable.
- **Temporal coherence**: no severe flicker, melting, or random object mutation.
- **Camera coherence**: motion follows prompt/previs without accidental cuts.
- **Action readability**: viewer can understand what changed during the 10 seconds.
- **Edit usefulness**: clip has usable start/end and can cut into the sequence.

## Delivery Hard Categories

- **Completeness**: files, prompts, manifests, and QA notes exist.
- **Source mapping**: every production asset maps to source refs and attempts.
- **Director acceptance**: final package has pass or explicit known caveats.
- **Reproducibility**: prompts and attempt records are sufficient to resume or repair.
