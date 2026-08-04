# CVB Sensor Analytics Archive Registry

Status: draft registry, started 2026-08-04

This file tracks the CVB-era sensor analytics material before anything is
ported, published, split, or scrubbed. The goal is to preserve useful evidence
of the work while avoiding accidental publication of partner data, clinical
tables, large model/data artifacts, internal meeting notes, or raw project
history that was only preserved as a private rescue archive.

## How To Use This Registry

Treat this as the working map for the archive:

- Add every discovered repo, folder, notebook bundle, paper draft, article, or
  "should-be project" as a row.
- Keep the original source path, even if the artifact eventually moves.
- Preserve git history when practical, but do not let history preservation
  override privacy, partner, data-use, or file-size concerns.
- Prefer public-facing summaries, READMEs, sanitized notebooks, and historical
  context over raw uploads of sensitive clinical/project material.

## Labels

Sensitivity:

- `low`: mostly public references, code, generic notes, or non-sensitive examples
- `medium`: old work context, internal process notes, or unclear authorship/scope
- `high`: partner docs, clinical/subject-level material, internal meetings,
  proprietary project detail, or data-use uncertainty

Bulk:

- `low`: small text/code/notebooks
- `medium`: notable notebooks or binary artifacts, but manageable after cleanup
- `high`: large data/model/log files or bulky history requiring filtering

History:

- `full`: meaningful commit history appears to be present
- `snapshot`: repo was initialized from pre-existing content
- `partial`: current checkout and history show moved/deleted/extracted pieces
- `hub`: archive repo mostly acts as connective tissue for other projects

## Repo Inventory

| Repo | Date Range | Commits | Size | History | Sensitivity | Bulk | Initial Read |
|---|---:|---:|---:|---|---|---|---|
| `/Users/kevin/github/CVB/sensor-driven-human-activity-recognition` | 2020-03-05 to 2022-01-21 | 786 | 692M | hub, partial | high | high | Central team archive with references, papers, internal notes, and duplicated project fragments. Keep private; extract selectively. |
| `/Users/kevin/github/CVB/mjf003_ppmi-verily-data-exploration` | 2020-03-30 to 2022-01-21 | 254 | 891M | partial | high | high | Major MJFF/Verily project repo. Valuable history, but raw publication is unsafe. |
| `/Users/kevin/github/CVB/int003` | 2019-04-26 to 2020-12-29 | 80 | 393M | full | medium | high | Gesture/HAR project with notebooks, package code, reports, and trained `.h5` models. Strong preserve candidate after model/data cleanup. |
| `/Users/kevin/github/CVB/apnea-ecg` | 2020-01-28 to 2020-12-29 | 114 | 253M | full, partial | medium | high | Applied ECG/apnea ML project. Contains many logs/checkpoints and notebooks. Needs cleanup before any public use. |
| `/Users/kevin/github/CVB/CVN002` | 2019-03-19 to 2020-01-23 | 19 | 35M | full | medium | low-medium | Clinical dropout-risk exploratory project using public TEDS-A/TEDS-D data as a proxy for CVN EHR work. Compact and historically useful. |
| `/Users/kevin/github/CVB/mbh001` | 2018-05-17 to 2020-01-31 | 232 | 62M | full, merged history | high | medium | Maternal health / early-term birth risk project. Keep focus on `mbh001_v3`; earlier versions mainly explain inherited project history. |
| `/Users/kevin/github/CVB/rett` | 2022-10-07 to 2023-08-05 | 101 | 44M | full, branch-dependent | high | medium | Later Rett package code for Noldus/Shimmer/spectra utilities. Main branch lacks many notebooks; notebook/dev branches retain additional work. |
| `/Users/kevin/github/CVB/sensornet` | 2020-03-30 to 2021-05-04 | 76 | 576K | full, partial | low-medium | low | Reusable sensor analytics package concept. Strong standalone/public candidate after review. |
| `/Users/kevin/github/CVB/Scalelet-Transform` | 2020-05-19 to 2020-12-29 | 58 | 3.3M | full, partial | low-medium | low | Time-series transform research project. Strong preserve candidate. |
| `/Users/kevin/github/CVB/the-right-switch` | 2020-03-30 to 2020-08-07 | 84 | 2.4M | full, partial | low | low | Activation-function research notes/experiments. Strong preserve candidate. |
| `/Users/kevin/github/CVB/Data-Augmentation-For-Time-Series` | 2021-04-05 | 1 | 3.9M | snapshot | low-medium | low | Rescued notebook bundle for time-series augmentation. Preserve as historical topic/project snapshot. |
| `/Users/kevin/github/CVB/verily-derived-data-issues` | 2021-12-06 to 2022-01-21 | 2 | 369M | snapshot | high | high | Extracted derived-data audit bundle. Contains a 274M CSV and Verily/PPMI-specific review material. Do not publish raw. |
| `/Users/kevin/github/CVB/verily-walk-detection` | 2021-12-06 | 1 | 61M | snapshot | high | medium | Extracted walk-detection notebooks from MJFF Projects 08/10. Valuable but likely needs heavy sanitization. |
| `/Users/kevin/github/CVB/data-leakage` | 2023-05-09 | 13 | 14M | full, snapshot-like | low-medium | low | Compact methodological repo with data-leakage article drafts, references, a SMOTE leakage notebook, and two presentation PDFs. Strong preserve candidate. |
| `/Users/kevin/github/CVB/time-mgmt` | 2023-01-30 to 2023-04-13 | 35 | 15M | full | high | low-medium | 2023 planning/time ledger with TPV, Rett, SleepBx, CVN Sleep, Sleep PoC, and EaSi planning notes. Use as private provenance; do not publish raw. |

## Loose / Disposable Source Bundles

| Source Bundle | Size | Sensitivity | Bulk | Initial Read |
|---|---:|---|---|---|
| `/Users/kevin/github/CVB/000_extra-files` | 342M | medium-high | medium | Loose rescue folder, not a git repo. MJFF subset is exact duplicate of `mjf003_ppmi-verily-data-exploration`; most DRCN/Pandoc material has better canonical copies in `sensor-driven-human-activity-recognition`; `quarantine__sensornet` contains a few non-duplicate package-planning notes. Safe to delete after useful source references are recorded or ported. |
| `/Users/kevin/Local Drive/Work/CVB` | 106G | high | high | Local project-folder archive with presentations, reports, write-ups, notebooks, and raw/support data for multiple CVB projects. This is not a single publishable source. Treat as a private evidence map and extract project-by-project. |

## Local Drive Source Folder Map

| Folder | Size | Links To Registry Thread(s) | Initial Read / Recommended Action |
|---|---:|---|---|
| `/Users/kevin/Local Drive/Work/CVB/misc` | 1.7M | clinical ML validity / data leakage; wearable articles; The Right Switch; CVB patent/papers | Small mixed folder. Contains SMOTE leakage presentation, wearable-hype writing, activation-function paper, and patent PDF. Mine selectively for articles/papers, but do not treat as a project. |
| `/Users/kevin/Local Drive/Work/CVB/EaSiEco` | 149M | EaSi ecosystem / data architecture / knowledge graph | New source thread. Contains database, Neo4j, app-dev, TimeScaleDB, knowledge graph, and EaSi Platform architecture decks/docs. Preserve selectively under data-engineering/platform architecture rather than sensor-modeling. |
| `/Users/kevin/Local Drive/Work/CVB/Rett-Folders-and-Files` | 104G | Rett sensor/video analytics; Rett package / Noldus-Shimmer analysis tools; Rett time alignment | Major private Rett source bundle. Most bulk is data (`code/rett` and `data/`). Preserve docs, presentations, trial-analysis notes, literature notes, and MachineSaidGo reports; do not publish raw data or clinical tables. |
| `/Users/kevin/Local Drive/Work/CVB/apnea` | 6.8M | Apnea-ECG | Supporting folder for apnea paper drafts, literature review, and checkpoint notebooks. Preserve with the `apnea-ecg` repo when that project is curated. |
| `/Users/kevin/Local Drive/Work/CVB/sleep` | 122M | SleepViz / EaSi Platform visualization pipeline; TPV; EaSi platform | Supporting source for SleepViz and the Sleep PoC Jupyter dashboard. Likely important for the sleep visualization/tooling story, but needs code/data audit before publication. |
| `/Users/kevin/Local Drive/Work/CVB/transcriptomics` | 1.3M | Transcriptomics / BEST RNASeq validity review; clinical ML validity / data leakage | New review/audit source thread. The underlying transcriptomics project belonged to a coworker; Kevin's artifact is the 2023 review of the RNASeq workflow, reproducibility, and possible leakage/model-validity issues. |
| `/Users/kevin/Local Drive/Work/CVB/suicide` | 295M | CVN suicide risk / wearable and EHR predictive analytics; CVN002 dropout-risk proxy; clinical ML validity / data leakage | New parent source thread, with CVN002/dropout as a subthread. Rich 2018-2019 material, but sensitive. Preserve only sanitized summaries/articles and public-data proxy work. |
| `/Users/kevin/Local Drive/Work/CVB/gesture-recognition` | 101M | Int003 / Gestures; Rett sensor/video analytics; EaSi Platform | Supporting folder for gesture recognition, INT003, early Rett posters, and EaSi platform notes. Preserve project docs/posters selectively; avoid duplicated repo data/models. |
| `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files` | 838M | TPV onboarding / takeover context; TPV Revisited / sleep-device methodology paper | Major TPV source bundle. `tpv_revisited` looks like Kevin's later restart/methodology-paper scaffold. `niks_tpv__ignore` is context from prior work and should not be foregrounded as Kevin's artifact except for transition notes. Raw data is private. |
| `/Users/kevin/Local Drive/Work/CVB/data-sci-mgmt` | 64M | Data Science Workflow / repo tooling; research writing workflow; sensor analytics management | New supporting evidence thread for project leadership, team process, repo templates, research-writing workflow, OKRs, and review material. Much is internal/private; extract public-safe workflow notes and article candidates. |
| `/Users/kevin/Local Drive/Work/CVB/MJFF` | 433M | MJFF / Verily / PPMI exploration; Verily timestamps; Verily derived-data issues; Verily PD detection; DRCN; Unconstrained HAR for PD detection | Major supporting source bundle for MJFF/Verily reports, decks, SoWs, timestamp notes, and paper drafts. Treat as high sensitivity and extract only sanitized project summaries, public-safe articles, and paper-history evidence. |
| `/Users/kevin/Local Drive/Work/CVB/DRCN` | 1.0M | DRCN / augmented unsupervised domain adaptation; autoencoder notes | Compact DRCN writing bundle. Contains paper history, local autoencoder lit review, and early HAR paper drafts. Preserve with the DRCN project. |
| `/Users/kevin/Local Drive/Work/CVB/maternal` | 20K | MBH001 v3 / maternal health early-term birth risk | Tiny supporting folder with maternal model report blurbs. Preserve as supporting MBH001 context if it adds narrative/report wording. |
| `/Users/kevin/Local Drive/Work/CVB/mouse-model` | 4K | unknown / low-priority mini-notebook | Only `mouse.ipynb` seen on first pass. Needs later quick inspection; likely skip unless it ties to a named CVB project. |
| `/Users/kevin/Local Drive/Work/CVB/eeg` | 1.5M | EEG working group biomarker notes; project environment tooling | Low-bulk supporting folder, currently mostly `conda-build-autoreject`. Preserve only if it clarifies EEG WG project setup/process. |

## Project And Thread Registry

| Project / Thread | Source(s) | Date Range | Sensitivity | Bulk | Artifact Type | Public Destination Idea | Recommended Action | Missing / Related Sources |
|---|---|---:|---|---|---|---|---|---|
| Sensor-driven HAR and digital biomarkers literature review | `sensor-driven-human-activity-recognition/README.md`; `references/human-activity-recognition/` | 2020-2022 | low-medium | low | literature review, link list, notes | `kitchensink/health/` or `kitchensink/time-series/` plus articles index | Preserve as curated public-safe reference artifact; clean dead/private links. | Cross-reference with MJFF, Rett, Int003, Sensornet. |
| Sensor analytics team hub | `sensor-driven-human-activity-recognition` | 2020-2022 | high | high | team archive, project map, references | private source only | Do not publish raw. Use as evidence source and index. | Some folders were intentionally cut out before upload. |
| Sensornet reusable package | `sensornet`; references in team planning notes | 2020-2021 | low-medium | low | Python package, reusable model/tools repo | separate public repo or `kitchensink/robotics/sensor-analytics/` | Audit code, add historical README, preserve history if public. | May need pieces from Int003, Scalelet, Data Aug, The Right Switch. |
| Int003 / Gestures | `int003`; `sensor-driven-human-activity-recognition/our-projects/gestures`; scratchpad notes | 2019-2020 | medium | high | notebooks, package code, reports, trained models | separate scrubbed repo, linked from kitchensink | Preserve project history but remove `.h5` models and any private data references. | May connect to Rett and Sensornet. |
| Apnea-ECG | `apnea-ecg`; `sensor-driven-human-activity-recognition/our-projects/apnea-ecg`; `/Users/kevin/Local Drive/Work/CVB/apnea` | 2020 | medium | high | notebooks, ML experiments, logs, code, paper drafts, lit review | separate scrubbed repo or kitchensink project | Filter logs/checkpoints; keep notebooks/code/README and paper-history docs if manageable. | Related to Scalelet Transform and older apnea paper plans. |
| Scalelet Transform | `Scalelet-Transform`; team planning references | 2020 | low-medium | low | research notes, notebooks, code | `kitchensink/time-series/` or separate repo | Preserve. Add README explaining historical aim and current status. | May require apnea data notes and related presentations/write-ups. |
| The Right Switch | `the-right-switch`; scratchpad references | 2020 | low | low | activation-function notes, notebooks, code | `kitchensink/deep-learning/` or separate repo | Preserve. Good historical theory/experimentation artifact. | Related: Box-Cox Batch Norm, vanishing/exploding gradient notes. |
| Data augmentation for time series | `Data-Augmentation-For-Time-Series`; `references/data-augmentation`; DRCN paper; Sensornet augmentation code | 2020-2021 | low-medium | low | notebook bundle, references, methods | `kitchensink/time-series/` and maybe `deep-learning/` | Preserve snapshot; consider merging references and notebooks into a small project folder. | Additional repo/folders may exist; user may link later. |
| DRCN / augmented unsupervised domain adaptation | `sensor-driven-human-activity-recognition/our-papers/drcn-paper`; `mjf003/Project05_DomainAdaptation`; `mjf003/Project07_DRCN_Verily`; `/Users/kevin/Local Drive/Work/CVB/DRCN`; `/Users/kevin/Local Drive/Work/CVB/MJFF/HAR_paper_v2.md` | 2020 | medium-high | high | paper draft, notebooks, tables, figures, results, project history | separate sanitized project or `kitchensink/time-series/domain-adaptation-2020` | Preserve curated version; exclude data/results artifacts if sensitive or bulky. | Check authorship/collaboration and whether paper was submitted/published. |
| MJFF / Verily / PPMI exploration | `mjf003_ppmi-verily-data-exploration`; `sensor-driven-human-activity-recognition/our-projects/mjff-verily`; `/Users/kevin/Local Drive/Work/CVB/MJFF` | 2020-2022 | high | high | clinical sensor analytics project repo, presentations, progress reports, proposals | private source; public summary only | Do not publish raw. Extract high-level methods and public-safe historical summaries only. | Partner docs, PPMI materials, clinical tables, and derived data need careful handling. |
| Verily walk detection / step counting | `verily-walk-detection`; historical `mjf003/Project08_Verily_WalkDetection`; historical `mjf003/Project10_WalkDetection_Frequency` | 2020-2021 | high | medium | notebooks, validation code, walk-like event detection | sanitized project summary or private-only repo | Audit for data leakage/sensitive records; preserve methods if public-safe. | Related to Sensornet, MJFF derived data, Project01-04 datasets. |
| Verily derived-data issues | `verily-derived-data-issues`; historical `mjf003/Project14_Verily-Derived-Data-Profiling` | 2021-2022 | high | high | derived-data audit, notebooks, presentation, CSVs | likely private; maybe sanitized write-up | Do not publish raw. If preserving publicly, write a generic data QA case study without data. | Contains 274M `derived-data_triplets.csv` and PPMI/Verily-specific material. |
| Verily timestamps / time reconstruction | `mjf003/Project13_Timestamps`; `/Users/kevin/Local Drive/Work/CVB/MJFF/2021-06_MJFF-Project13-Timestamps_README.md`; `/Users/kevin/Local Drive/Work/CVB/MJFF/2021-05-27_MJFF-Project13-Timestamps_waxing-poetic-about-age-and-time_KU.md` | 2021 | high | low | notes, timestamp reverse engineering | sanitized article/case study if allowed | Good writing and reasoning artifact; scrub partner specifics before public use. | Related to derived-data issues and walk detection. |
| Verily on/off medication analysis | `mjf003/Project12_On-Off-Medication` | 2021 | high | medium | clinical analysis notes/code/data | private or heavily summarized | Do not publish raw due medication/clinical context. | Contains medication tables and PPMI-derived context. |
| Verily PD detection | `mjf003/Project11_PD_Detection`; journal article drafts in sensor archive | 2020-2021 | high | medium | notebooks, paper drafts, clinical ML | private source; sanitized methods only | Treat as sensitive. Preserve only high-level public-safe narrative unless publication status allows more. | Related to DRCN, derived data, on/off medication. |
| Dataset similarity metrics | `mjf003/Project06_DatasetSimilarityMetrics`; scratchpad TODO | 2020 | medium | medium | notebooks, metrics experiments | `kitchensink/time-series/` if data is public/synthetic | Audit. Potentially useful methodological mini-project. | Need inspect for sensitive data and public dataset dependency. |
| Early MJFF public-dataset explorations | historical `mjf003/Project01_Exploratory_Unconstrained-Smartphones`; `Project02_UCI-HAR-and-Chest-Mounted`; `Project03_USC-HAD`; `Project04_ExtraSensory`; `Project09_CleanDatasets` | 2020-2021 | low-medium | unknown | exploratory notebooks, public HAR datasets | recover from history or link to missing repos | Locate extracted repos or decide whether to recover from MJFF history. | Current local CVB folder does not include these as separate repos. |
| SleepViz / EaSi Platform visualization pipeline | `sensor-driven-human-activity-recognition/our-projects/easi-platform/analytics/sleep-poc-viz/sleepviz`; `/Users/kevin/Local Drive/Work/CVB/sleep`; `/Users/kevin/Local Drive/Work/CVB/sleep/sleep-poc-jupyter-dashboard` | 2021 | medium-high | high | Python package, notebooks, visualization pipeline, dashboard docs | separate scrubbed repo candidate | Strong candidate, but audit data/source assumptions and internal references. | `sleep-poc-jupyter-dashboard` exists in Local Drive source bundle. |
| Rett sensor/video analytics | `sensor-driven-human-activity-recognition/our-projects/rett`; scratchpad notes | 2020-2021 | high | medium | references, internal docs, trial planning, notebooks | mostly private; public reference notes only | Do not publish raw. Extract public literature notes if useful. | Related to Int003/Gestures and sensor analytics package. |
| EEG working group biomarker notes | `sensor-driven-human-activity-recognition/our-projects/eeg-wg` | 2021 | high | low | meeting notes, reference notes | private or sanitized literature notes | Mostly keep private; possibly extract public reference notes. | May overlap with health/statistics/biomarkers. |
| Sensor-Phenomenon-Biomarker Dictionary | planning notes in `internal-affairs/team-planning` and references | 2021 | medium-high | low | should-be project, dictionary concept | possible public conceptual README | Create a small project if enough artifacts exist. | Need locate actual dictionary files if they exist. |
| Research writing workflow | `our-papers/README.md`; `our-papers/templates`; DRCN paper process notes; scratchpad Pandoc journal; Markdown-slides notes; `/Users/kevin/Local Drive/Work/CVB/data-sci-mgmt` | 2020-2021 | low-medium | medium | process docs, templates, scripts, article candidates | `kitchensink/misc/research-writing/` and `kitchensink/articles/YYYY/` | Preserve selected public-safe process notes; avoid bulky template/vendor clutter. | May overlap with articles/papers imported from website. See article candidate source list below. |
| Outreach articles | `our-papers/outreach-articles` | 2019-2020 | low-medium | low | articles/drafts | `kitchensink/articles/YYYY/` | Preserve good public-safe articles with history if useful. | Check duplicates already imported from website. |
| Clinical ML validity / data leakage | `data-leakage`; outreach article; scratchpad `model-metrics.md`; `/Users/kevin/Local Drive/Work/CVB/suicide/03_ehr-dropout-risk`; `/Users/kevin/Local Drive/Work/CVB/transcriptomics`; notes across repos | 2019-2023 | low-medium | low | article/notes, notebook, presentations, code-review notes | `kitchensink/articles`, `statistics/`, or a compact clinical-ML-validity project | Preserve and cross-reference. `data-leakage` is the clearest source repo for this theme, with CVN002 and transcriptomics review notes as concrete case studies. | Some text may duplicate website imports. |
| CVB 2023 planning and time ledger | `time-mgmt/90-day-plan_Feb-Mar-Apr-2023.md`; `time-mgmt/time-sheet-notes.md`; `time-mgmt/README.md` | 2023 | high | low | planning notes, time ledger, provenance | private source only | Use to date work and map project relationships, not as a public artifact. | Contains internal project codes, meeting context, and casual notes. |
| TPV onboarding / takeover context | `time-mgmt/PROJECTS/TPV`; `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/TPV`; `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/niks_tpv__ignore` | 2023-2024 | high | medium | onboarding notes, prior-work context, journal, links, figures | private source plus possible sanitized TPV retrospective | Track as important context for Kevin taking over/restarting TPV work. Do not publish raw TPV links, prior-worker notebooks, or journal. | Use `niks_tpv__ignore` as background only; foreground `tpv_revisited` separately. |
| TPV Revisited / sleep-device methodology paper | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/tpv_revisited`; `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/temp-tpv`; `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/presentations` | 2024-2026 | high | medium | methodology-paper scaffold, bounded-DTW notes, notebooks, presentations | standalone repo, indexed from `kitchensink` | Strong candidate for project-by-project preservation after rights/data review. This appears to be Kevin's restart of the TPV analysis/methodology story. | Requires careful authorship/data-rights framing before public release. `kitchensink` should have a lightweight project folder/README that links to the standalone repo. |
| Rett time alignment / MNE / multitaper notes | `time-mgmt/PROJECTS/Rett`; `rett`; external Rett reports/write-ups | 2023 | high | low-medium | journal notes, presentation, links | private source plus possible sanitized Rett methods note | Preserve as supporting Rett context, especially the time-alignment presentation. Do not publish raw project links. | Related Rett notebooks/reports likely exist outside current repos. |
| SleepBx / voice biomarker company diligence | `time-mgmt/PROJECTS/SleepBx` | 2023 | medium-high | low | due-diligence notes, literature review links | low-priority private source or health/digital-biomarker notes | Preserve only if useful later. It is more vendor/research diligence than a standalone technical project. | May overlap with CVN Sleep and Sleep PoC notes. |
| CVN Sleep Study / Sleep PoC / DigitalBxCOU / EaSiBizPlan planning notes | `time-mgmt/PROJECTS/CVN-Sleep-Study`; `PROJECTS/Sleep-PoC`; `PROJECTS/DigitalBxCOU`; `PROJECTS/EasiBizPlan` | 2023 | medium-high | low | meeting notes, planning notes | likely skip raw; maybe private cross-reference only | Low priority. Use for chronology/context if needed, but do not promote as standalone public artifacts. | More complete project folders may exist elsewhere. |
| CVN suicide risk / wearable and EHR predictive analytics | `/Users/kevin/Local Drive/Work/CVB/suicide/01_wearable-suicide-risk`; `/Users/kevin/Local Drive/Work/CVB/suicide/02_ehr-mental-health-risk`; `/Users/kevin/Local Drive/Work/CVB/suicide/write-ups` | 2018-2020 | high | medium | literature review, roadmaps, presentations, grant/write-up material | sanitized health/articles only, or private source | New parent thread. Rich historical evidence of mental-health/suicide-risk analytics work, but sensitive and likely not public raw. | CVN002 dropout-risk is a more concrete subproject. |
| CVN002 / clinical dropout risk proxy work | `CVN002/teds`; `/Users/kevin/Local Drive/Work/CVB/suicide/03_ehr-dropout-risk`; TEDS-A/TEDS-D public data notes and notebooks | 2019-2020 | medium-high | low-medium | notebooks, journal notes, public dataset exploration, presentations | `kitchensink/health/clinical-dropout-risk-2019` or separate compact repo | Strong preserve candidate after removing `.DS_Store` and confirming no private CVN data is present. | The journal notes are valuable because they critique leakage, length-of-stay misuse, and practical deployability. Local Drive has key presentation/report context. |
| MBH001 v3 / maternal health early-term birth risk | `mbh001/mbh001_v3`; top-level `mbh001` README explains merged project history; `/Users/kevin/Local Drive/Work/CVB/maternal` | 2019-2020 | high | medium | notebooks, modeling audit, inherited-project forensic analysis, report blurbs | private source plus possible sanitized case-study summary | Preserve evidence of rigorous negative-result work, but do not publish raw data. Public version should likely be a narrative/case study with code only if scrubbed. | Earlier `mbh001_cu` and `mbh001_cu_v2` are context, not primary target. |
| Rett package / Noldus-Shimmer analysis tools | `rett`; branches `origin/notebooks` and `origin/msg/dev`; `sensor-driven-human-activity-recognition/our-projects/rett`; `/Users/kevin/Local Drive/Work/CVB/Rett-Folders-and-Files` | 2020-2023 | high | high | Python package, processed tables, dev notebooks on branches, reports, presentations, literature notes | private source; maybe sanitized methods/package summary | Useful but not public raw. Main branch has cleaned code, while branch history and Local Drive folders contain notebooks, figures, presentations, reports, and meeting notes. | Local Drive bundle has the missing reports/write-ups but is 104G and data-heavy. |
| EaSi ecosystem / data architecture / knowledge graph | `/Users/kevin/Local Drive/Work/CVB/EaSiEco`; `sensor-driven-human-activity-recognition/our-projects/easi-platform`; `/Users/kevin/Local Drive/Work/CVB/gesture-recognition/easi-platform` | 2018-2021 | medium-high | medium | platform architecture decks, data-modeling docs, Neo4j/TimeScaleDB notes, knowledge graph docs | `misc/data-engineering/` or private source plus selected articles | New source thread. Professionally useful, but likely internal architecture material. Extract only public-safe architecture/process notes. | Cross-reference SleepViz, TPV, Rett, and data-science workflow. |
| Transcriptomics / BEST RNASeq validity review | `/Users/kevin/Local Drive/Work/CVB/transcriptomics` | 2023 | medium-high | low | coworker project review, R/Rmd workflow audit, code-review notes, leakage critique | `kitchensink/health/omics-validity-review-2023` or private source summary | New review/audit thread. Strong compact evidence of being asked to assess a coworker's clinical/omics ML workflow for reproducibility, clarity, and model-validity risks. Needs sensitivity/authorship review before public release. | Related to data leakage and clinical ML validity. |
| Box-Cox Batch Norm | team planning and scratchpad TODO references | 2020 | low | unknown | should-be project / idea | maybe under The Right Switch | Add as related concept unless separate repo/folder appears. | User may have separate files elsewhere. |
| Temporal Convolution Experiments | GitLab reference `krbn/temporal-convolution-experiments` | 2020 | low-medium | unknown | external repo reference | separate audit if available | Await source repo/folder. | Not currently local under `/Users/kevin/github/CVB`. |
| NSL Examples | scratchpad TODO and notebooks | 2020 | low-medium | low | notebooks/code examples | `kitchensink/notebooks/` or `deep-learning/` | Preserve only if notebooks have enough content. | Existing files in `internal-affairs/scratchpads/kevin/notebooks/nsl_examples`. |
| Data Science Workflow / repo tooling | `src/miniconda`, `src/docker`, references to `data-science-workflow` and `wiki-handbook`; `/Users/kevin/Local Drive/Work/CVB/data-sci-mgmt/data-science-workflow`; `/Users/kevin/Local Drive/Work/CVB/data-sci-mgmt/data-science-mgmt-tools` | 2020-2021 | medium | low | tooling/process notes, cookiecutter repo template, workflow docs | `kitchensink/misc/dev-workflows/` | Preserve selected generic notes only. | Local Drive has likely source copies of `data-science-workflow` and wiki/blog tooling notes. |
| Sensor analytics management / project leadership evidence | `/Users/kevin/Local Drive/Work/CVB/data-sci-mgmt`; `sensor-driven-human-activity-recognition/internal-affairs/team-planning` | 2020-2021 | high | medium | OKRs, project management notes, reviews, team workflow presentations | private source only; selected public-safe process notes | New supporting thread. Useful portfolio-context evidence, but much is personnel/internal material and should not be public raw. | Extract only generic project/process artifacts if professionally useful. |
| External affairs / publication strategy | `external-affairs`, conference/journal notes; `/Users/kevin/Local Drive/Work/CVB/data-sci-mgmt/README_External-Affairs.md` | 2020-2021 | low-medium | low | journals, conferences, outreach notes | probably low-priority misc/reference | Preserve only if useful; otherwise summarize or skip. | Mostly process/reference material. |

## Article Candidate Source List

These are source references worth revisiting as `kitchensink/articles` entries
or as cleaned supporting notes in project folders. Prefer the canonical source
paths because they live in git history. Use `000_extra-files` mostly as a
reminder of what was discovered.

| Candidate | Canonical Source(s) | Extra-Files Clue | Date | Suggested Destination | Notes |
|---|---|---|---:|---|---|
| Markdown, Pandoc, LaTeX, and scientific-paper workflow | `sensor-driven-human-activity-recognition/internal-affairs/scratchpads/kevin/JOURNAL/pandoc/2020-07-28-T__JOURNAL.md`; `sensor-driven-human-activity-recognition/internal-affairs/scratchpads/kevin/JOURNAL/pandoc/ENTRIES/2020-07-30__JOURNAL.md`; `sensor-driven-human-activity-recognition/internal-affairs/scratchpads/kevin/JOURNAL/pandoc/ENTRIES/2020-07-31__JOURNAL.md`; `sensor-driven-human-activity-recognition/our-papers/drcn-paper/notes/pandoc-markdown-conversion.md` | `000_extra-files/pandoc-markdown/pandoc/`; `000_extra-files/pandoc-markdown/md-research-papers/README.md` | 2020-07-28 to 2020-07-31 | `articles/2020/`; cross-reference from `misc/research-writing/` | Strong article candidate. Preserve the reasoning about GitLab Markdown, Pandoc Markdown, math handling, journal templates, and conversion pain. Skip generated/vendor clutter. |
| Markdown-slides / presentation-from-Markdown experiment | `sensor-driven-human-activity-recognition/internal-affairs/scratchpads/kevin/misc/2021-03-12_convert-your-markdown-to-beautiful-presentations-with-markdown-slides.md` | `000_extra-files/pandoc-markdown/md-presentations/this-thing/prez.md` | 2021-03-12 | `articles/2021/`; cross-reference from `misc/research-writing/` or `misc/automation/` | Article-shaped and personality-rich. Do not preserve the vendored `prez/` Reveal.js/KaTeX tree unless there is a specific reason. |
| Autoencoder notes for DRCN / domain adaptation | `sensor-driven-human-activity-recognition/our-papers/drcn-paper/notes/autoencoders.md` | `000_extra-files/pandoc-markdown/drcn-paper/notes/autoencoders.md` | 2020 | `articles/2020/`; cross-reference from `deep-learning/`, `time-series/`, and DRCN project folder | Long technical notes. Better as a lightly cleaned article or supporting note than as loose scratchpad text. |
| DRCN paper drafts and versioned Markdown | `sensor-driven-human-activity-recognition/our-papers/drcn-paper/paper.md`; `sensor-driven-human-activity-recognition/our-papers/drcn-paper/keep/v*_augmented-unsupervised-domain-adaptation-for-deep-time-series-models.md`; `sensor-driven-human-activity-recognition/our-papers/drcn-paper/README.md` | `000_extra-files/pandoc-markdown/drcn-paper/`; `000_extra-files/pandoc-markdown/DRCN-README_pandoc-markdown.md` | 2020 | DRCN project folder, not generic articles first | Preserve as part of the DRCN/domain-adaptation project story. Article extraction may be useful later, but the primary artifact is a project/paper trail. |
| Sensornet package structure and naming notes | no matching canonical source found in `sensornet`; possible canonical context in `sensor-driven-human-activity-recognition/internal-affairs/team-planning/` | `000_extra-files/quarantine__sensornet/package-layout.md`; `000_extra-files/quarantine__sensornet/package-conventions.md`; optional private context in `README.md` | 2021 | Sensornet project folder or private source notes | Not really an article, but worth salvaging before deleting `000_extra-files`. `version-control.md` has no meaningful content. |

## Missing Or Possibly Separate Sources To Ask About Later

These are named in the current material but are not present as obvious local
repos under `/Users/kevin/github/CVB`:

- `Project01_Exploratory_Unconstrained-Smartphones`
- `Project02_Exploratory_UCI-HAR-and-Chest-Mounted-Datasets`
- `Project03_USC-HAD`
- `Project04_ExtraSensory`
- `Project09_CleanDatasets`
- `sleep-poc-jupyter-dashboard`
- `data-science-workflow`
- `wiki-handbook`
- `temporal-convolution-experiments`
- `tpv_revisited`
- `Box-Cox Batch Norm`
- `NSL Examples` beyond the scratchpad copy
- `Sensor-Phenomenon-Biomarker Dictionary`
- CVN002, MBH001, and Rett presentation/report folders outside the git repos
- Any presentations/write-ups stored outside git repos

## Immediate Risk Notes

- `.gitignore` prevents newly-created matching files from being added, but it
  does not remove files that are already tracked or already present in history.
- `int003` includes trained `.h5` models that should not be carried into a
  lightweight public history unless there is a specific reason.
- `apnea-ecg` includes many logs, checkpoints, traces, and profiling artifacts.
- `CVN002` appears to use public TEDS data, but public release should still
  verify that no private CVN data or local exports were committed.
- `mbh001` includes tracked clinical/project data artifacts, including v3
  notebook CSV data and earlier-version spreadsheets/documents.
- `rett` includes tracked processed tables and hard-coded de-identified subject
  IDs/timestamps in package utilities; treat as private until scrubbed.
- `mjf003_ppmi-verily-data-exploration` contains large public dataset files,
  vendored protobuf material, clinical/partner project material, and many
  notebooks.
- `sensor-driven-human-activity-recognition` includes internal affairs,
  meeting notes, hiring/team planning, partner docs, PPMI/Verily docs, clinical
  tables, and duplicated project material.
- `verily-derived-data-issues` includes a large derived-data CSV and
  PPMI/Verily-specific analysis outputs.
- `verily-walk-detection` includes validation files and a pickled label file
  that should be treated as sensitive until proven otherwise.
- `data-leakage` is comparatively low-risk, but still has presentation PDFs and
  notebook HTML that should be reviewed before publishing.
- `time-mgmt` contains internal time sheets, SharePoint/study links, project
  codes, and at least one password-reference note. Treat it as private
  provenance rather than a public repo.

## Recommended Review Batches

1. Core reusable sensor analytics:
   `sensornet`, `int003`, `Data-Augmentation-For-Time-Series`,
   `Scalelet-Transform`, `the-right-switch`.

2. Bulky applied ML projects:
   `apnea-ecg`, `CVN002`, `mbh001_v3`, SleepViz / EaSi Platform.

3. MJFF / Verily material:
   `mjf003_ppmi-verily-data-exploration`, `verily-walk-detection`,
   `verily-derived-data-issues`, timestamp notes, derived-data notes.

4. Rett material:
   `rett`, `sensor-driven-human-activity-recognition/our-projects/rett`, and
   external Rett project folders with notebooks/reports/write-ups.

5. Articles, references, and process artifacts:
   outreach articles, HAR references, data leakage/model validity notes,
   research-writing workflow, external affairs.

6. 2023 planning and TPV material:
   `time-mgmt`, Rett time-alignment notes, SleepBx diligence notes, and
   `tpv_revisited` once found.

## Current Working Recommendation

Do not publish the CVB archive as a single repo. Keep the raw CVB repositories
private/local, then produce a curated public archive made of:

- clean standalone repos for substantial code projects with strong history,
- `kitchensink` topic/project folders for smaller historical artifacts,
- `kitchensink/articles` entries for public-safe writing,
- private-only summaries for sensitive clinical/partner work,
- explicit README notes explaining historical dates, incomplete status, and why
  certain datasets/models are intentionally omitted.

## TPV Revisited Focus Pass

### Source Layers

| Layer | Source | Role | Initial Handling |
|---|---|---|---|
| Kevin rebuild history | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/niks_tpv__ignore/tpv_std` branch `kurban`, paths `krbn_tpv/` and `tpv_revisited/` | Real Git history for Kevin's TPV restart/rebuild, January-May 2024. Includes commits from initial `krbn_tpv` work through the final `tpv_revisited` package/notebooks. | Preserve with history filtering. Include both `krbn_tpv/` and `tpv_revisited/` so the rename/reorganization history is not lost. |
| Current organized project | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/tpv_revisited` | Later organized project/manuscript scaffold. Contains 2024 source files plus 2026 roadmap, DTW report, communication/authorship strategy, and methodology-paper draft. | Layer on top of the history-preserved extraction as later cleanup/planning commits, not backdated. |
| Duplicate/older loose copy | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/temp-tpv` | Older loose shape matching the final-day package more closely. Appears mostly duplicative of current `tpv_revisited`, but useful for comparison. | Collate into the project home under an ignored `source-archives/` or confirm duplicate before deleting. |
| Onboarding/provenance notes | `/Users/kevin/github/CVB/time-mgmt/PROJECTS/TPV` | Journal, onboarding notes, links, and images documenting Kevin taking over TPV and untangling prior work. | Keep private/ignored by default. Extract only sanitized excerpts if useful for a README or article. |
| Prior TPV implementation | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/niks_tpv__ignore` | Nik's inherited repo and context. Important historically but not the foreground artifact. | Preserve as private/ignored context only. Credit Nik where prior outputs are referenced; do not present this as Kevin-authored code. |
| Raw/standardized data | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/data` and `methodology-paper/notebooks/tpv.db` | Private TPV study data and derived database. | Collate locally under the project home, but gitignore by default. Public repo should document that data is intentionally omitted unless publication rights are resolved. |
| Reports, figures, presentations | `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/TPV`; `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/TPV Papers`; `/Users/kevin/Local Drive/Work/CVB/TPV-Folders-and-Files/presentations` | Results plots, board/paper presentations, and report artifacts. | Collate locally. Treat as private until reviewed; selected figures/slides may be useful in README or article if public-safe. |

### History Strategy

- Use the old `tpv_std` repo's `kurban` branch as the canonical Git-history
  source for Kevin's rebuild.
- Include both historical path names:
  - `krbn_tpv/` for January-April 2024 rebuild commits.
  - `tpv_revisited/` for April-May 2024 package/notebook commits.
- Rewrite the extracted history into a standalone repo, currently preferred as
  `/Users/kevin/github/sleep-device-validation-methods`.
- Do not preserve the full inherited TPV repo as public history for this
  artifact. It is context, and it includes Nik-authored implementation history,
  bulk notebooks, internal files, and study data.
- Treat the 2026 planning files in the loose `tpv_revisited` folder as honest
  later cleanup/planning work. They should be committed with their real current
  dates, not folded into the 2024 history.

### One-Home Project Layout Candidate

The preferred home is now a standalone repo:

```text
/Users/kevin/github/sleep-device-validation-methods/
  README.md
  methodology-paper/
  source-archives/      # ignored local-only copies of source bundles
  private-data/         # ignored local-only data/database/source JSONs
  private-notes/        # ignored journal/onboarding/meeting context
  private-presentations/# ignored unless selected decks are scrubbed
```

The important rule: all relevant TPV files should be collated under this one
project home, even when they are intentionally ignored. The `.gitignore` should
separate publishable project files from private/local artifacts; it should not
be used as an excuse to leave project materials scattered across the computer.

### Public / Ignored Split

Likely public-safe after review:

- `README.md` and historical/provenance note.
- Core `tpv_revisited` package code, after checking for paths, credentials, and
  private identifiers.
- Methodology-paper scaffolding and bounded-DTW notes, with data-rights caveats.
- `DTW_REPORT.md`, because it explains the technical contribution clearly.
- Selected sanitized figures or descriptions if they do not expose private
  subject-level information.

Likely ignored/private:

- Raw and standardized TPV study data.
- `tpv.db` unless rights are explicitly resolved.
- Journal/onboarding notes from `time-mgmt`.
- Prior-worker source tree except for local context.
- Meeting notes, links, SharePoint references, and credentials-adjacent notes.
- Board decks and presentations until individually reviewed.

### Initial Recommendation

Build TPV Revisited as a standalone, history-preserved repo at
`/Users/kevin/github/sleep-device-validation-methods`. Then add a lightweight project/index
folder in `kitchensink` with a README that explains the project, links to the
standalone repo, and cross-references it from `health`, `time-series`,
`statistics`, and publications/articles.
