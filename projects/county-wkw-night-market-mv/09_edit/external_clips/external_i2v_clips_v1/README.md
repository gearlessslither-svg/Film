# External I2V Clips V1 Intake

Put returned external image-to-video clips in this folder using these exact names:

- `VP001_KF001_external_i2v.mp4`
- `VP002_KF002_external_i2v.mp4`
- `VP003_KF003_external_i2v.mp4`
- `VP004_KF004_external_i2v.mp4`
- `VP005_KF005_external_i2v.mp4`
- `VP006_KF006_external_i2v.mp4`
- `VP007_KF007_external_i2v.mp4`
- `VP008_KF008_external_i2v.mp4`
- `VP009_KF009_external_i2v.mp4`
- `VP010_KF010_external_i2v.mp4`
- `VP011_KF011_external_i2v.mp4`
- `VP012_KF012_external_i2v.mp4`
- `VP013_KF013_external_i2v.mp4`
- `VP014_KF014_external_i2v.mp4`

Each external generation prompt requests ambience/SFX only and no music/BGM/soundtrack. Final music is added only in editing.

After all 14 files are present, run:

```bash
python3 09_edit/tools/assemble_external_mv_v1.py
```

To check what is still missing:

```bash
python3 09_edit/tools/assemble_external_mv_v1.py --check-only
```
