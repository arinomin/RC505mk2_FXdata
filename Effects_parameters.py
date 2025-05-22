# Dictionary mapping effects to their parameters
EFFECTS = {
    "LPF":
    ["LPF_RATE", "LPF_DEPTH", "LPF_RESONANCE", "LPF_CUTOFF", "LPF_STEP_RATE"],
    "BPF":
    ["BPF_RATE", "BPF_DEPTH", "BPF_RESONANCE", "BPF_CUTOFF", "BPF_STEP_RATE"],
    "HPF":
    ["HPF_RATE", "HPF_DEPTH", "HPF_RESONANCE", "HPF_CUTOFF", "HPF_STEP_RATE"],
    "PHASER": [
        "PHASER_RATE", "PHASER_DEPTH", "PHASER_RESONANCE", "PHASER_MANUAL",
        "PHASER_STEP_RATE", "PHASER_D_LEVEL", "PHASER_E_LEVEL", "PHASER_STAGE"
    ],
    "FLANGER": [
        "FLANGER_RATE", "FLANGER_DEPTH", "FLANGER_RESONANCE", "FLANGER_MANUAL",
        "FLANGER_STEP_RATE", "FLANGER_D_LEVEL", "FLANGER_E_LEVEL",
        "FLANGER_SEPARATION"
    ],
    "SYNTH":
    ["SYNTH_FREQUENCY", "SYNTH_RESONANCE", "SYNTH_DECAY", "SYNTH_BALANCE"],
    "LO-FI": ["LOFI_BITDEPTH", "LOFI_SAMPLERATE", "LOFI_BALANCE"],
    "RADIO": ["RADIO_LOFI", "RADIO_LEVEL"],
    "RINGMOD": ["RINGMOD_FREQUENCY", "RINGMOD_BALANCE", "RINGMOD_MODE"],
    "G2B": ["G2B_BALANCE", "G2B_MODE"],
    "SUSTAINER": [
        "SUSTAINER_ATTACK", "SUSTAINER_RELEASE", "SUSTAINER_LEVEL",
        "SUSTAINER_LOW_GAIN", "SUSTAINER_HI_GAIN", "SUSTAINER_SUSTAIN"
    ],
    "AUTO RIFF": [
        "AUTORIFF_PHARASE", "AUTORIFF_TEMPO", "AUTORIFF_HOLD",
        "AUTORIFF_ATTACK", "AUTORIFF_LOOP", "AUTORIFF_KEY", "AUTORIFF_BALANCE"
    ],
    "SLOW GEAR":
    ["SLOWGEAR_SENS", "SLOWGEAR_RISE_TIME", "SLOWGEAR_LEVEL", "SLOWGEAR_MODE"],
    "TRANSPOSE": ["TRANSPOSE_TRANS", "TRANSPOSE_MODE"],
    "PITCH BEND": ["PITCHBEND_PITCH", "PITCHBEND_BEND", "PITCHBEND_MODE"],
    "ROBOT": ["ROBOT_ROBOT_NOTE", "ROBOT_FORMANT", "ROBOT_MODE"],
    "ELECTRIC": [
        "ELECTRIC_SHIFT", "ELECTRIC_FORMANT", "ELECTRIC_SPEED",
        "ELECTRIC_STABILITY", "ELECTRIC_SCALE"
    ],
    "HRM MANUAL": [
        "HRMMANUAL_VOICE", "HRMMANUAL_FORMANT", "HRMMANUAL_PAN",
        "HRMMANUAL_KEY", "HRMMANUAL_D_LEVEL", "HRMMANUAL_HRM_LEVEL"
    ],
    "HRM AUTO(M)": [
        "HRMAUTO_VOICE", "HRMAUTO_FORMANT", "HRMAUTO_PAN", "HRMAUTO_HRM_MODE",
        "HRMAUTO_KEY", "HRMAUTO_D_LEVEL", "HRMAUTO_E_LEVEL"
    ],
    "VOCODER": [
        "VOCODER_CARRIER", "VOCODER_TONE", "VOCODER_ATTACK",
        "VOCODER_MOD_SENS", "VOCODER_CARRIER_THRU", "VOCODER_BALANCE"
    ],
    "OSC VOC(M)": [
        "OSCVOC_CARRIER", "OSCVOC_TONE", "OSCVOC_ATTACK", "OSCVOC_OCTAVE",
        "OSCVOC_MOD_SENS", "OSCVOC_RELEASE", "OSCVOC_BALANCE"
    ],
    "OSC BOT": [
        "OSCBOT_OSC", "OSCBOT_TONE", "OSCBOT_ATTACK", "OSCBOT_NOTE",
        "OSCBOT_MOD_SENS", "OSCBOT_BALANCE"
    ],
    "PREAMP": [
        "PREAMP_AMP_TYPE", "PREAMP_SPK_TYPE", "PREAMP_GAIN", "PREAMP_T_COMP",
        "PREAMP_BASS", "PREAMP_MIDDLE", "PREAMP_TREBLE", "PREAMP_PRESENCE",
        "PREAMP_MIC_TYPE", "PREAMP_MIC_DIS", "PREAMP_MIC_POS", "PREAMP_E_LEVEL"
    ],
    "DIST":
    ["DIST_TYPE", "DIST_TONE", "DIST_DIST", "DIST_D_LEVEL", "DIST_E_LEVEL"],
    "DYNAMICS": ["DYNAMICS_TYPE", "DYNAMICS_DYNAMICS"],
    "EQ": [
        "EQ_LOW_GAIN", "EQ_HI_GAIN", "EQ_LO_MID_FREQ", "EQ_LO_MID_Q",
        "EQ_LO_MID_GAIN", "EQ_HIGH_MID_FREQ", "EQ_HIGH_MID_Q",
        "EQ_HIGH_MID_GAIN", "EQ_LEVEL"
    ],
    "ISOLATOR": [
        "ISOLATOR_BAND", "ISOLATOR_RATE", "ISOLATOR_BAND_LEVEL",
        "ISOLATOR_DEPTH", "ISOLATOR_STEP_RATE", "ISOLATOR_WAVE_FORM"
    ],
    "OCTAVE": ["OCTAVE_OCTAVE", "OCTAVE_MODE", "OCTAVE_OCTAVE_LEVEL"],
    "AUTO PAN": [
        "AUTOPAN_RATE", "AUTOPAN_WAVEFORM", "AUTOPAN_DEPTH",
        "AUTOPAN_INIT_PHASE", "AUTOPAN_STEP_RATE"
    ],
    "MANUAL PAN": ["MANUALPAN_POSITION"],
    "STEREO ENHANCE":
    ["STEREOENHANCE_LO_CUT", "STEREOENHANCE_HI_CUT", "STEREOENHANCE_ENHANCE"],
    "TREMOLO": ["TREMOLO_RATE", "TREMOLO_DEPTH", "TREMOLO_WAVEFORM"],
    "VIBRATO": [
        "VIBRATO_RATE", "VIBRATO_DEPTH", "VIBRATO_COLOR", "VIBRATO_D_LEVEL",
        "VIBRATO_E_LEVEL"
    ],
    "PATTERN SLICER": [
        "PATTERNSLICER_RATE", "PATTERNSLICER_DUTY", "PATTERNSLICER_ATTACK",
        "PATTERNSLICER_PATTERN", "PATTERNSLICER_DEPTH",
        "PATTERNSLICER_THRESHOLD", "PATTERNSLICER_GAIN"
    ],
    "STEP SLICER": [
        "STEPSLICER_RATE", "STEPSLICER_DEPTH", "STEPSLICER_THRESHOLD",
        "STEPSLICER_GAIN"
    ],
    "DELAY": [
        "DELAY_TIME", "DELAY_FEEDBACK", "DELAY_D_LEVEL", "DELAY_LOW_CUT",
        "DELAY_HIGH_CUT", "DELAY_E_LEVEL"
    ],
    "PANNING DELAY": [
        "PANNINGDELAY_TIME", "PANNINGDELAY_FEEDBACK", "PANNINGDELAY_D_LEVEL",
        "PANNINGDELAY_LOW_CUT", "PANNINGDELAY_HIGH_CUT", "PANNINGDELAY_E_LEVEL"
    ],
    "REVERSE DELAY": [
        "REVERSEDELAY_TIME", "REVERSEDELAY_FEEDBACK", "REVERSEDELAY_D_LEVEL",
        "REVERSEDELAY_LOW_CUT", "REVERSEDELAY_HIGH_CUT", "REVERSEDELAY_E_LEVEL"
    ],
    "MOD DELAY": [
        "MODDELAY_TIME", "MODDELAY_FEEDBACK", "MODDELAY_MOD_DEPTH",
        "MODDELAY_D_LEVEL", "MODDELAY_LOW_CUT", "MODDELAY_HIGH_CUT",
        "MODDELAY_E_LEVEL"
    ],
    "TYPE ECHO 1": [
        "TYPEECHO1_REPEAT_TIME", "TYPEECHO1_INTENSITY", "TYPEECHO1_D_LEVEL",
        "TYPEECHO1_BASS", "TYPEECHO1_TREBLE", "TYPEECHO1_E_LEVEL"
    ],
    "TYPE ECHO 2": [
        "TYPEECHO2_TIME", "TYPEECHO2_FEEDBACK", "TYPEECHO2_D_LEVEL",
        "TYPEECHO2_LOW_CUT", "TYPEECHO2_HIGH_CUT", "TYPEECHO2_E_LEVEL"
    ],
    "GNR DELAY": ["GNRDELAY_TIME", "GNRDELAY_FEEDBACK", "GNRDELAY_E_LEVEL"],
    "WARP": ["WARP_LEVEL"],
    "TWIST": ["TWIST_RELEASE", "TWIST_RISE", "TWIST_FALL", "TWIST_LEVEL"],
    "ROLL 1": ["ROLL1_TIME", "ROLL1_FEEDBACK", "ROLL1_ROLL", "ROLL1_BALANCE"],
    "ROLL 2": ["ROLL2_TIME", "ROLL2_REPEAT", "ROLL2_ROLL", "ROLL2_BALANCE"],
    "FREEZE": [
        "FREEZE_ATTACK", "FREEZE_RELEASE", "FREEZE_DECAY", "FREEZE_SUSTAIN",
        "FREEZE_BALANCE"
    ],
    "CHORUS": [
        "CHORUS_RATE", "CHORUS_DEPTH", "CHORUS_LOW_CUT", "CHORUS_HIGH_CUT",
        "CHORUS_D_LEVEL", "CHORUS_E_LEVEL"
    ],
    "REVERB": [
        "REVERB_TIME", "REVERB_PRE_DELAY", "REVERB_DENSITY", "REVERB_LOW_CUT",
        "REVERB_HIGH_CUT", "REVERB_D_LEVEL", "REVERB_E_LEVEL"
    ],
    "GATE REVERB": [
        "GATEREVERB_TIME", "GATEREVERB_PRE_DELAY", "GATEREVERB_THRESHOLD",
        "GATEREVERB_LOW_CUT", "GATEREVERB_HIGH_CUT", "GATEREVERB_D_LEVEL",
        "GATEREVERB_E_LEVEL"
    ],
    "REVERSE REVERB": [
        "REVERSEREVERB_TIME", "REVERSEREVERB_PRE_DELAY",
        "REVERSEREVERB_GATE_DELAY", "REVERSEREVERB_LOW_CUT",
        "REVERSEREVERB_HIGH_CUT", "REVERSEREVERB_D_LEVEL",
        "REVERSEREVERB_E_LEVEL"
    ],
    "BEAT SCATTER": ["BEATSCATTER_TYPE", "BEATSCATTER_LENGTH"],
    "BEAT REPEAT": ["BEATREPEAT_TYPE", "BEATREPEAT_LENGTH"],
    "BEAT SHIFT": ["BEATSHIFT_TYPE", "BEATSHIFT_SHIFT"],
    "VINYL FLICK": ["VINYLFLICK_FLICK"]
}

# Track A specific effects (maintaining order)
TRACK_A_EFFECTS = ["BEAT SCATTER", "BEAT REPEAT", "BEAT SHIFT", "VINYL FLICK"]

# All available effects (maintaining order from EFFECTS dictionary)
ALL_EFFECTS = [
    effect for effect in EFFECTS.keys() if effect not in set(TRACK_A_EFFECTS)
]

# Musical note options for RATE and SEQ RATE parameters
MUSICAL_NOTE_OPTIONS = [
    "4MEAS", "2MEAS", "1MEAS","𝅗𝅥", "♩.", "𝅗𝅥  3", "♩", "♪.", "♩3", "♪",
    "𝅘𝅥𝅯 .", "♪ 3", "𝅘𝅥𝅯'", "𝅘E"
]

# Delay specific options
DELAY_LO_CUT_OPTIONS = [
    "FLAT", "20Hz", "25Hz", "31.5Hz", "40Hz", "50Hz", "63Hz", "80Hz", "100Hz",
    "125Hz", "160Hz", "200Hz", "250Hz", "315Hz", "400Hz", "500Hz", "630Hz",
    "800Hz"
]

DELAY_HI_CUT_OPTIONS = [
    "630Hz", "800Hz", "1kHz", "1.25kHz", "1.6kHz", "2kHz", "2.5kHz", "3.15kHz",
    "4kHz", "5kHz", "6.3kHz", "8kHz", "10kHz", "12.5kHz", "FLAT"
]

DELAY_TIME_MUSICAL_OPTIONS = [
    "𝅘E",
    "𝅘𝅥𝅯'",
    "♪ 3",
    "𝅘𝅥𝅯 .",
    "♪",
    "♩3",
    "♪.",
    "♩",
    "𝅗𝅥  3",
    "♩.",
    "𝅗𝅥",
]

DELAY_TIME_NUMERIC_OPTIONS = [str(i) + "ms" for i in range(1, 2001)]
DELAY_TIME_ALL_OPTIONS = DELAY_TIME_MUSICAL_OPTIONS + DELAY_TIME_NUMERIC_OPTIONS


# Generate musical notes C1 through G9
def generate_musical_notes():
    notes = []
    base_notes = [
        "C", "D♭", "D", "E♭", "E", "F", "F♯", "G", "A♭", "A", "B♭", "B"
    ]
    for octave in range(1, 10):
        for note in base_notes:
            note_with_octave = f"{note}{octave}"
            notes.append(note_with_octave)
            if note_with_octave == "G9":
                break
    return notes


MUSICAL_NOTES = generate_musical_notes()


# Generate MANUAL PAN position labels
def generate_pan_positions():
    positions = []
    for i in range(-50, 51):
        if i < 0:
            positions.append(f"L{abs(i)}")
        elif i > 0:
            positions.append(f"R{i}")
        else:
            positions.append("CENTER")
    return positions


PAN_POSITIONS = generate_pan_positions()

# Define frequency options for various parameters
FREQUENCY_OPTIONS = [
    "FLAT", "20.0Hz", "25.0Hz", "31.5Hz", "40.0Hz", "50.0Hz", "63.0Hz",
    "80.0Hz", "100Hz", "125Hz", "160Hz", "200Hz", "250Hz", "315Hz", "400Hz",
    "500Hz", "630Hz", "800Hz", "1.00kHz", "1.25kHz", "1.60kHz", "2.00kHz",
    "2.50kHz", "3.15kHz", "4.00kHz", "5.00kHz", "6.30kHz", "8.00kHz", "10.0kHz"
]

# Parameter types and their ranges/options
PARAMETER_DEFINITIONS = {
    "SW": {
        "display_name": "SW",
        "type": "options",
        "options": ["OFF", "ON"],
        "default": "OFF"
    },
    "SW_MODE": {
        "display_name": "SW MODE",
        "type": "options",
        "options": ["TOGGLE", "MOMENT"],
        "default": "TOGGLE"
    },
    "INSERT_INPUT": {
        "display_name": "INSERT",
        "type": "options",
        "options": ["ALL", "MIC 1", "MIC 2", "INST 1", "INST 2"],
        "default": "ALL"
    },
    "INSERT_TRACK": {
        "display_name": "INSERT",
        "type": "options",
        "options": ["ALL", "TRACK 1", "TRACK 2", "TRACK 3", "TRACK 4", "TRACK 5"],
        "default": "ALL"
    },

    # LPF用のパラメータ
    "LPF_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "𝅗𝅥"
    },
    "LPF_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "LPF_RESONANCE": {
        "display_name": "RESONANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "LPF_CUTOFF": {
        "display_name": "CUTOFF",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "LPF_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "BPF_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "𝅗𝅥"
    },
    "BPF_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "BPF_RESONANCE": {
        "display_name": "RESONANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "BPF_CUTOFF": {
        "display_name": "CUTOFF",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "BPF_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "HPF_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "𝅗𝅥"
    },
    "HPF_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "HPF_RESONANCE": {
        "display_name": "RESONANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "HPF_CUTOFF": {
        "display_name": "CUTOFF",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "HPF_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "PHASER_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "𝅗𝅥"
    },
    "PHASER_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PHASER_RESONANCE": {
        "display_name": "RESONANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PHASER_MANUAL": {
        "display_name": "MANUAL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PHASER_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "PHASER_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "PHASER_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "PHASER_STAGE": {
        "display_name": "STAGE",
        "type": "options",
        "options": ["4", "8", "12", "BI-PHASE"],
        "default": "8"
    },
    "FLANGER_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "1MEAS"
    },
    "FLANGER_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "FLANGER_RESONANCE": {
        "display_name": "RESONANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "FLANGER_MANUAL": {
        "display_name": "MANUAL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "FLANGER_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "FLANGER_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "FLANGER_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "FLANGER_SEPARATION": {
        "display_name": "SEPARATION",
        "type": "range",
        "range": (0, 100),
        "default": 0
    },
    "SYNTH_FREQUENCY": {
        "display_name": "FREQUENCY",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SYNTH_RESONANCE": {
        "display_name": "RESONANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SYNTH_DECAY": {
        "display_name": "DECAY",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SYNTH_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "LOFI_BITDEPTH": {
        "display_name": "BITDEPTH",
        "type": "options",
        "options": ["OFF"] + [str(i) for i in range(31, 0, -1)],
        "default": "8"
    },
    "LOFI_SAMPLERATE": {
        "display_name": "SAMPLERATE",
        "type": "options",
        "options": ["OFF"] + [f"1/{i}" for i in range(2, 33)],
        "default": "1/4"
    },
    "LOFI_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "RADIO_LOFI": {
        "display_name": "LO-FI",
        "type": "range",
        "range": (1, 10),
        "default": 5
    },
    "RADIO_LEVEL": {
        "display_name": "LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "RINGMOD_FREQUENCY": {
        "display_name": "FREQUENCY",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "RINGMOD_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "RINGMOD_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "G2B_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "G2B_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "SUSTAINER_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SUSTAINER_RELEASE": {
        "display_name": "RELEASE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SUSTAINER_LEVEL": {
        "display_name": "LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SUSTAINER_LOW_GAIN": {
        "display_name": "LOW GAIN",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "SUSTAINER_HI_GAIN": {
        "display_name": "HI GAIN",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "SUSTAINER_SUSTAIN": {
        "display_name": "SUSTAIN",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "AUTORIFF_PHARASE": {
        "display_name": "PHARASE",
        "type": "options",
        "options": [f"P{i:02d}" for i in range(1, 31)],
        "default": "P01"
    },
    "AUTORIFF_TEMPO": {
        "display_name": "TEMPO",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "QUARTER"
    },
    "AUTORIFF_HOLD": {
        "display_name": "HOLD",
        "type": "on_off",
        "default": "OFF"
    },
    "AUTORIFF_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "AUTORIFF_LOOP": {
        "display_name": "LOOP",
        "type": "on_off",
        "default": "ON"
    },
    "AUTORIFF_KEY": {
        "display_name":
        "KEY",
        "type":
        "options",
        "options": [
            "C(Am)", "D♭(B♭m)", "D(Bm)", "E♭(Cm)", "E(C♯m)", "F(Dm)",
            "F♯(D♯m)", "G(Em)", "A♭(Fm)", "A(F♯m)", "B♭(Gm)", "B(G♯m)"
        ],
        "default":
        "C(Am)"
    },
    "AUTORIFF_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SLOWGEAR_SENS": {
        "display_name": "SENS",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SLOWGEAR_RISE_TIME": {
        "display_name": "RISE TIME",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SLOWGEAR_LEVEL": {
        "display_name": "LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SLOWGEAR_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "TRANSPOSE_TRANS": {
        "display_name": "TRANS",
        "type": "signed_range",
        "range": (-12, 12),
        "default": 0,
        "show_plus": True
    },
    "TRANSPOSE_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "PITCHBEND_PITCH": {
        "display_name": "PITCH",
        "type": "signed_range",
        "range": (-30, 40),
        "default": 40,
        "show_plus": True,
        "suffix": "CT"
    },
    "PITCHBEND_BEND": {
        "display_name": "BEND",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PITCHBEND_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "ROBOT_ROBOT_NOTE": {
        "display_name":
        "ROBOT_NOTE",
        "type":
        "options",
        "options":
        ["C", "D♭", "D", "E♭", "E", "F", "F♯", "G", "A♭", "A", "B♭", "B"],
        "default":
        "C"
    },
    "ROBOT_FORMANT": {
        "display_name": "FORMANT",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "ROBOT_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "ELECTRIC_SHIFT": {
        "type": "signed_range",
        "range": (-12, 12),
        "default": 0,
        "show_plus": True
    },
    "ELECTRIC_FORMANT": {
        "display_name": "FORMANT",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "ELECTRIC_SPEED": {
        "display_name": "SPEED",
        "type": "range",
        "range": (0, 10),
        "default": 5
    },
    "ELECTRIC_STABILITY": {
        "display_name": "STABILITY",
        "type": "signed_range",
        "range": (-10, 10),
        "default": 0,
        "show_plus": True
    },
    "ELECTRIC_SCALE": {
        "display_name":
        "SCALE",
        "type":
        "options",
        "options": [
            "CHROMATIC", "C(Am)", "D♭(B♭m)", "D(Bm)", "E♭(Cm)", "E(C♯m)",
            "F(Dm)", "F♯(D♯m)", "G(Em)", "A♭(Fm)", "A(F♯m)", "B♭(Gm)", "B(G♯m)"
        ],
        "default":
        "CHROMATIC"
    },
    "HRMMANUAL_VOICE": {
        "display_name":
        "VOICE",
        "type":
        "options",
        "options": [
            "OCT-", "-6TH", "-5TH", "-4TH", "-3RD", "UNISON", "+3RD", "+4TH",
            "+5TH", "+6TH", "OCT+"
        ],
        "default":
        "+3RD"
    },
    "HRMMANUAL_FORMANT": {
        "display_name": "FORMANT",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "HRMMANUAL_PAN": {
        "display_name": "PAN",
        "type": "options",
        "options": PAN_POSITIONS,
        "default": "CENTER"
    },
    "HRMMANUAL_KEY": {
        "display_name":
        "KEY",
        "type":
        "options",
        "options": [
            "C(Am)", "D♭(B♭m)", "D(Bm)", "E♭(Cm)", "E(C♯m)", "F(Dm)",
            "F♯(D♯m)", "G(Em)", "A♭(Fm)", "A(F♯m)", "B♭(Gm)", "B(G♯m)"
        ],
        "default":
        "C(Am)"
    },
    "HRMMANUAL_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "HRMMANUAL_HRM_LEVEL": {
        "display_name": "HRM LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 80
    },
    "HRMAUTO_VOICE": {
        "display_name": "VOICE",
        "type": "options",
        "options":
        ["OCT-", "LOWER", "LOW", "UNISON", "HIGH", "HIGHER", "OCT+"],
        "default": "HIGH"
    },
    "HRMAUTO_FORMANT": {
        "display_name": "FORMANT",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "HRMAUTO_PAN": {
        "display_name": "PAN",
        "type": "options",
        "options": PAN_POSITIONS,
        "default": "CENTER"
    },
    "HRMAUTO_HRM_MODE": {
        "display_name": "HRM MODE",
        "type": "options",
        "options": ["AUTO", "HYBRID"],
        "default": "AUTO"
    },
    "HRMAUTO_KEY": {
        "display_name":
        "KEY",
        "type":
        "options",
        "options": [
            "C(Am)", "D♭(B♭m)", "D(Bm)", "E♭(Cm)", "E(C♯m)", "F(Dm)",
            "F♯(D♯m)", "G(Em)", "A♭(Fm)", "A(F♯m)", "B♭(Gm)", "B(G♯m)"
        ],
        "default":
        "C(Am)"
    },
    "HRMAUTO_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "HRMAUTO_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 80
    },
    "VOCODER_CARRIER": {
        "display_name":
        "CARRIER",
        "type":
        "options",
        "options": [
            "MIC1", "MIC2", "INST1", "INST2", "TRACK 1", "TRACK 2", "TRACK 3",
            "TRACK 4", "TRACK 5"
        ],
        "default":
        "TRACK 1"
    },
    "VOCODER_TONE": {
        "display_name": "TONE",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "VOCODER_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "VOCODER_MOD_SENS": {
        "display_name": "MOD SENS",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "VOCODER_CARRIER_THRU": {
        "display_name": "CARRIER THRU",
        "type": "on_off",
        "default": "ON"
    },
    "VOCODER_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "OSCVOC_CARRIER": {
        "display_name":
        "CARRIER",
        "type":
        "options",
        "options": [
            "MIC1", "MIC2", "INST1", "INST2", "TRACK 1", "TRACK 2", "TRACK 3",
            "TRACK 4", "TRACK 5"
        ],
        "default":
        "TRACK 1"
    },
    "OSCVOC_TONE": {
        "display_name": "TONE",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "OSCVOC_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "OSCVOC_OCTAVE": {
        "display_name": "OCTAVE",
        "type": "options",
        "options": ["-20CT", "-10CT", "0", "+10CT"],
        "default": "0"
    },
    "OSCVOC_MOD_SENS": {
        "display_name": "MOD SENS",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "OSCVOC_RELEASE": {
        "display_name": "RELEASE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "OSCVOC_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "OSCBOT_OSC": {
        "display_name": "OSC",
        "type": "options",
        "options": ["SAW", "VINTAGE SAW", "DETUNE SAW", "SQUARE", "RECT"],
        "default": "SAW"
    },
    "OSCBOT_TONE": {
        "display_name": "TONE",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "OSCBOT_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "OSCBOT_NOTE": {
        "display_name": "NOTE",
        "type": "options",
        "options": MUSICAL_NOTES,
        "default": "C2"
    },
    "OSCBOT_MOD_SENS": {
        "display_name": "MOD SENS",
        "type": "signed_range",
        "range": (-50, 50),
        "default": 0,
        "show_plus": True
    },
    "OSCBOT_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PREAMP_AMP_TYPE": {
        "display_name":
        "AMP TYPE",
        "type":
        "options",
        "options": [
            "JC-120", "NATURAL CLEAN", "FULL RANGE", "COMBO CRUNCH",
            "STACK CRUNCH", "HIGAIN STACK", "POWER DRIVE", "EXTREM LEAD",
            "CORE METAL"
        ],
        "default":
        "COMBO CRUNCH"
    },
    "PREAMP_SPK_TYPE": {
        "display_name":
        "SPK TYPE",
        "type":
        "options",
        "options": [
            "OFF", "ORIGINAL", "1x8\"", "1x10\"", "1x12\"", "2x12\"", "4x10\"",
            "4x12\"", "8x12\""
        ],
        "default":
        "ORIGINAL"
    },
    "PREAMP_GAIN": {
        "display_name": "GAIN",
        "type": "db_range",
        "range": (0, 20),
        "default": 6,
        "show_plus": True
    },
    "PREAMP_T_COMP": {
        "display_name": "T-COMP",
        "type": "signed_range",
        "range": (0, 20),
        "default": 10,
        "show_plus": True
    },
    "PREAMP_BASS": {
        "display_name": "BASS",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PREAMP_MIDDLE": {
        "display_name": "MIDDLE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PREAMP_TREBLE": {
        "display_name": "TREBLE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PREAMP_PRESENCE": {
        "display_name": "PRESENCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PREAMP_MIC_TYPE": {
        "display_name": "MIC TYPE",
        "type": "options",
        "options": ["DYN57", "DYN421", "CND451", "CND87", "FLAT"],
        "default": "DYN57"
    },
    "PREAMP_MIC_DIS": {
        "display_name": "MIC DIS",
        "type": "options",
        "options": ["OFF MIC", "ON MIC"],
        "default": "OFF MIC"
    },
    "PREAMP_MIC_POS": {
        "display_name":
        "MIC POS",
        "type":
        "options",
        "options": [
            "CENTER", "1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm", "8cm",
            "9cm", "10cm"
        ],
        "default":
        "CENTER"
    },
    "PREAMP_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "DIST_TYPE": {
        "display_name": "TYPE",
        "type": "options",
        "options": ["VOCAL", "BOOST", "OD", "DS", "METAL", "FUZZ"],
        "default": "BOOST"
    },
    "DIST_TONE": {
        "display_name": "TONE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "DIST_DIST": {
        "display_name": "DIST",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "DIST_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 0
    },
    "DIST_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "DYNAMICS_TYPE": {
        "display_name":
        "TYPE",
        "type":
        "options",
        "options": [
            "NATURALCOMP", "MIXER COMP", "LIVE COMP", "NATURAL LIM",
            "HARD LIM", "JINGL COMP", "HARD COMP", "SOFT COMP", "CLEAN COMP",
            "DANCE COMP", "ORCH COMP", "VOCAL COMP", "ACOUSTIC", "ROCK BAND",
            "ORCHESTRA", "LOW BOOST", "BRIGHT", "DJs VOICE", "PHONE VOX"
        ],
        "default":
        "NATURALCOMP"
    },
    "DYNAMICS_DYNAMICS": {
        "display_name": "DYNAMICS",
        "type": "signed_range",
        "range": (-20, 20),
        "default": 0,
        "show_plus": True
    },
    "EQ_LOW_GAIN": {
        "display_name": "LO GAIN",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "EQ_HI_GAIN": {
        "display_name": "HI GAIN",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "EQ_LO_MID_FREQ": {
        "display_name":
        "LO MID FREQ",
        "type":
        "options",
        "options": [
            "20.0Hz", "25.0Hz", "31.5Hz", "40.0Hz", "50.0Hz", "63.0Hz",
            "80.0Hz", "100Hz", "125Hz", "160Hz", "200Hz", "250Hz", "315Hz",
            "400Hz", "500Hz", "630Hz", "800Hz", "1.00kHz", "1.25kHz",
            "1.60kHz", "2.00kHz", "2.50kHz", "3.15kHz", "4.00kHz", "5.00kHz",
            "6.30kHz", "8.00kHz", "10.0kHz"
        ],
        "default":
        "800Hz"
    },
    "EQ_LO_MID_Q": {
        "display_name": "LO MID Q",
        "type": "options",
        "options": ["0.5", "1", "2", "4", "8", "16"],
        "default": "1"
    },
    "EQ_LO_MID_GAIN": {
        "display_name": "LO MID GAIN",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "EQ_HIGH_MID_FREQ": {
        "display_name":
        "HIGH MID FREQ",
        "type":
        "options",
        "options": [
            "20.0Hz", "25.0Hz", "31.5Hz", "40.0Hz", "50.0Hz", "63.0Hz",
            "80.0Hz", "100Hz", "125Hz", "160Hz", "200Hz", "250Hz", "315Hz",
            "400Hz", "500Hz", "630Hz", "800Hz", "1.00kHz", "1.25kHz",
            "1.60kHz", "2.00kHz", "2.50kHz", "3.15kHz", "4.00kHz", "5.00kHz",
            "6.30kHz", "8.00kHz", "10.0kHz"
        ],
        "default":
        "3.15kHz"
    },
    "EQ_HIGH_MID_Q": {
        "display_name": "HIGH MID Q",
        "type": "options",
        "options": ["0.5", "1", "2", "4", "8", "16"],
        "default": "1"
    },
    "EQ_HIGH_MID_GAIN": {
        "display_name": "HIGH MID GAIN",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "EQ_LEVEL": {
        "display_name": "LEVEL",
        "type": "db_range",
        "range": (-20, 20),
        "default": 0
    },
    "ISOLATOR_BAND": {
        "display_name": "BAND",
        "type": "options",
        "options": ["LOW", "MIDDLE", "HIGH"],
        "default": "LOW"
    },
    "ISOLATOR_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "QUARTER"
    },
    "ISOLATOR_BAND_LEVEL": {
        "display_name": "BAND LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "ISOLATOR_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "ISOLATOR_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "ISOLATOR_WAVE_FORM": {
        "display_name": "WAVE_FORM",
        "type": "options",
        "options": ["TRI", "SQR"],
        "default": "TRI"
    },
    "OCTAVE_OCTAVE": {
        "display_name": "OCTAVE",
        "type": "options",
        "options": ["-20CT", "-10CT", "-10CT&-20CT"],
        "default": "-10CT"
    },
    "OCTAVE_MODE": {
        "display_name": "MODE",
        "type": "options",
        "options": [1, 2],
        "default": 2
    },
    "OCTAVE_OCTAVE_LEVEL": {
        "display_name": "OCTAVE.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "AUTOPAN_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": 50,
        "use_numeric_default": True
    },
    "AUTOPAN_WAVEFORM": {
        "display_name": "WAVEFORM",
        "type": "range",
        "range": (0, 100),
        "default": 0
    },
    "AUTOPAN_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "AUTOPAN_INIT_PHASE": {
        "display_name": "INIT PHASE",
        "type": "options",
        "options": [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180],
        "default": 0
    },
    "AUTOPAN_STEP_RATE": {
        "display_name": "STEP RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": ["OFF"] + MUSICAL_NOTE_OPTIONS,
        "default": "OFF"
    },
    "MANUALPAN_POSITION": {
        "display_name": "POSITION",
        "type": "options",
        "options": PAN_POSITIONS,
        "default": "CENTER"
    },
    "STEREOENHANCE_LO_CUT": {
        "display_name": "LO CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "STEREOENHANCE_HI_CUT": {
        "display_name": "HI CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "STEREOENHANCE_ENHANCE": {
        "display_name": "ENHANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TREMOLO_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": 85,
        "use_numeric_default": True
    },
    "TREMOLO_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TREMOLO_WAVEFORM": {
        "display_name": "WAVEFORM",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "VIBRATO_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "QUARTER"
    },
    "VIBRATO_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "VIBRATO_COLOR": {
        "display_name": "COLOR",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "VIBRATO_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 0
    },
    "VIBRATO_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "PATTERNSLICER_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "QUARTER"
    },
    "PATTERNSLICER_DUTY": {
        "display_name": "DUTY",
        "type": "range",
        "range": (1, 99),
        "default": 50
    },
    "PATTERNSLICER_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 35
    },
    "PATTERNSLICER_PATTERN": {
        "display_name": "PATTERN",
        "type": "options",
        "options": [f"P{i:02d}" for i in range(1, 21)],
        "default": "P01"
    },
    "PATTERNSLICER_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "PATTERNSLICER_THRESHOLD": {
        "display_name": "THRESHOLD",
        "type": "range",
        "range": (-30, 0),
        "default": -30
    },
    "PATTERNSLICER_GAIN": {
        "display_name": "GAIN",
        "type": "db_range",
        "range": (0, 20),
        "default": 6,
        "show_plus": True
    },
    "STEPSLICER_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "QUARTER"
    },
    "STEPSLICER_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_THRESHOLD": {
        "display_name": "THRESHOLD",
        "type": "range",
        "range": (-30, 0),
        "default": -30
    },
    "STEPSLICER_GAIN": {
        "display_name": "GAIN",
        "type": "db_range",
        "range": (0, 20),
        "default": 6,
        "show_plus": True
    },
    "STEPSLICER_STEP_MAX": {
        "display_name": "STEP MAX",
        "type": "options",
        "options": list(range(1, 17)),
        "default": 16
    },
    "STEPSLICER_STEP_LEN1": {
        "display_name": "STEP LEN1",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN2": {
        "display_name": "STEP LEN2",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN3": {
        "display_name": "STEP LEN3",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN4": {
        "display_name": "STEP LEN4",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN5": {
        "display_name": "STEP LEN5",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN6": {
        "display_name": "STEP LEN6",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN7": {
        "display_name": "STEP LEN7",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN8": {
        "display_name": "STEP LEN8",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN9": {
        "display_name": "STEP LEN9",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN10": {
        "display_name": "STEP LEN10",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN11": {
        "display_name": "STEP LEN11",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN12": {
        "display_name": "STEP LEN12",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN13": {
        "display_name": "STEP LEN13",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN14": {
        "display_name": "STEP LEN14",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN15": {
        "display_name": "STEP LEN15",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LEN16": {
        "display_name": "STEP LEN16",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "STEPSLICER_STEP_LVL1": {
        "display_name": "STEP LVL1",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL2": {
        "display_name": "STEP LVL2",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL3": {
        "display_name": "STEP LVL3",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL4": {
        "display_name": "STEP LVL4",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL5": {
        "display_name": "STEP LVL5",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL6": {
        "display_name": "STEP LVL6",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL7": {
        "display_name": "STEP LVL7",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL8": {
        "display_name": "STEP LVL8",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL9": {
        "display_name": "STEP LVL9",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL10": {
        "display_name": "STEP LVL10",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL11": {
        "display_name": "STEP LVL11",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL12": {
        "display_name": "STEP LVL12",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL13": {
        "display_name": "STEP LVL13",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL14": {
        "display_name": "STEP LVL14",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL15": {
        "display_name": "STEP LVL15",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "STEPSLICER_STEP_LVL16": {
        "display_name": "STEP LVL16",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "DELAY_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 200,
        "use_numeric_default": True,
        "show_buttons": True,
        "suffix": "ms"
    },
    "DELAY_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 20
    },
    "DELAY_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "DELAY_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": DELAY_LO_CUT_OPTIONS,
        "default": "FLAT"
    },
    "DELAY_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": DELAY_HI_CUT_OPTIONS,
        "default": "FLAT"
    },
    "DELAY_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 120),
        "default": 50
    },
    "PANNINGDELAY_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 200,
        "use_numeric_default": True,
        "show_buttons": True,
        "suffix": "ms"
    },
    "PANNINGDELAY_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 20
    },
    "PANNINGDELAY_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "PANNINGDELAY_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": DELAY_LO_CUT_OPTIONS,
        "default": "FLAT"
    },
    "PANNINGDELAY_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": DELAY_HI_CUT_OPTIONS,
        "default": "FLAT"
    },
    "PANNINGDELAY_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 120),
        "default": 50
    },
    "REVERSEDELAY_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 200,
        "use_numeric_default": True,
        "show_buttons": True,
        "suffix": "ms"
    },
    "REVERSEDELAY_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 20
    },
    "REVERSEDELAY_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "REVERSEDELAY_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": DELAY_LO_CUT_OPTIONS,
        "default": "FLAT"
    },
    "REVERSEDELAY_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": DELAY_HI_CUT_OPTIONS,
        "default": "FLAT"
    },
    "REVERSEDELAY_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 120),
        "default": 50
    },
    "MODDELAY_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 200,
        "use_numeric_default": True,
        "show_buttons": True,
        "suffix": "ms"
    },
    "MODDELAY_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 20
    },
    "MODDELAY_MOD_DEPTH": {
        "display_name": "MOD DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "MODDELAY_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "MODDELAY_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": DELAY_LO_CUT_OPTIONS,
        "default": "FLAT"
    },
    "MODDELAY_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": DELAY_HI_CUT_OPTIONS,
        "default": "FLAT"
    },
    "MODDELAY_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 120),
        "default": 50
    },
    "TYPEECHO1_REPEAT_TIME": {
        "display_name": "REPEAT TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 200,
        "use_numeric_default": True,
        "show_buttons": True,
        "suffix": "ms"
    },
    "TYPEECHO1_INTENSITY": {
        "display_name": "INTENSITY",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TYPEECHO1_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "TYPEECHO1_BASS": {
        "display_name": "BASS",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TYPEECHO1_TREBLE": {
        "display_name": "TREBLE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TYPEECHO1_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 120),
        "default": 50
    },
    "TYPEECHO2_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 200,
        "use_numeric_default": True,
        "show_buttons": True,
        "suffix": "ms"
    },
    "TYPEECHO2_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 20
    },
    "TYPEECHO2_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "TYPEECHO2_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": DELAY_LO_CUT_OPTIONS,
        "default": "FLAT"
    },
    "TYPEECHO2_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": DELAY_HI_CUT_OPTIONS,
        "default": "FLAT"
    },
    "TYPEECHO2_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 120),
        "default": 50
    },
    "GNRDELAY_TIME": {
        "display_name": "TIME",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "GNRDELAY_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 70
    },
    "GNRDELAY_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "WARP_LEVEL": {
        "display_name": "LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TWIST_RELEASE": {
        "display_name": "RELEASE",
        "type": "options",
        "options": ["FADE", "FALL"],
        "default": "FALL"
    },
    "TWIST_RISE": {
        "display_name": "RISE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TWIST_FALL": {
        "display_name": "FALL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "TWIST_LEVEL": {
        "display_name": "LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "ROLL1_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": "QUARTER",
        "show_buttons": True,
        "suffix": "ms"
    },
    "ROLL1_FEEDBACK": {
        "display_name": "FEEDBACK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "ROLL1_ROLL": {
        "display_name": "ROLL",
        "type": "options",
        "options": ["OFF", "1/2", "1/4", "1/8", "1/16"],
        "default": "OFF"
    },
    "ROLL1_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "ROLL2_TIME": {
        "display_name": "TIME",
        "type": "combined",
        "numeric_range": (1, 2000),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": "QUARTER",
        "show_buttons": True,
        "suffix": "ms"
    },
    "ROLL2_REPEAT": {
        "display_name": "REPEAT",
        "type": "options",
        "options": [str(i) for i in range(1, 101)] + ["∞"],
        "default": "50"
    },
    "ROLL2_ROLL": {
        "display_name": "ROLL",
        "type": "options",
        "options": ["OFF", "1/2", "1/4", "1/8", "1/16"],
        "default": "OFF"
    },
    "ROLL2_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "FREEZE_ATTACK": {
        "display_name": "ATTACK",
        "type": "range",
        "range": (0, 100),
        "default": 30
    },
    "FREEZE_RELEASE": {
        "display_name": "RELEASE",
        "type": "range",
        "range": (0, 100),
        "default": 30
    },
    "FREEZE_DECAY": {
        "display_name": "DECAY",
        "type": "range",
        "range": (0, 100),
        "default": 30
    },
    "FREEZE_SUSTAIN": {
        "display_name": "SUSTAIN",
        "type": "range",
        "range": (0, 100),
        "default": 30
    },
    "FREEZE_BALANCE": {
        "display_name": "BALANCE",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "CHORUS_RATE": {
        "display_name": "RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": DELAY_TIME_MUSICAL_OPTIONS,
        "default": 50,
        "use_numeric_default": True
    },
    "CHORUS_DEPTH": {
        "display_name": "DEPTH",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "CHORUS_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "CHORUS_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "CHORUS_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "CHORUS_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "REVERB_TIME": {
        "display_name": "TIME",
        "type": "options",
        "options": [f"{str(round(i/10, 1))}s" for i in range(1, 101)],
        "default": "3.0s"
    },
    "REVERB_PRE_DELAY": {
        "display_name": "PRE DELAY",
        "type": "range",
        "range": (0, 500),
        "default": 0
    },
    "REVERB_DENSITY": {
        "display_name": "DENSITY",
        "type": "range",
        "range": (0, 9),
        "default": 4
    },
    "REVERB_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "REVERB_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "REVERB_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "REVERB_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "GATEREVERB_TIME": {
        "display_name": "TIME",
        "type": "options",
        "options": [f"{str(round(i/10, 1))}s" for i in range(1, 101)],
        "default": "3.0s"
    },
    "GATEREVERB_PRE_DELAY": {
        "display_name": "PRE DELAY",
        "type": "range",
        "range": (0, 500),
        "default": 0
    },
    "GATEREVERB_THRESHOLD": {
        "display_name": "THRESHOLD",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "GATEREVERB_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "GATEREVERB_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "GATEREVERB_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "GATEREVERB_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "REVERSEREVERB_TIME": {
        "display_name": "TIME",
        "type": "options",
        "options": [f"{str(round(i/10, 1))}s" for i in range(1, 10)],
        "default": "0.5s"
    },
    "REVERSEREVERB_PRE_DELAY": {
        "display_name": "PRE DELAY",
        "type": "range",
        "range": (0, 500),
        "default": 0
    },
    "REVERSEREVERB_GATE_DELAY": {
        "display_name": "GATE DELAY",
        "type": "options",
        "options": [f"{str(round(i/10, 1))}s" for i in range(1, 10)],
        "default": "0.5s"
    },
    "REVERSEREVERB_D_LEVEL": {
        "display_name": "D.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 100
    },
    "REVERSEREVERB_LOW_CUT": {
        "display_name": "LOW CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "REVERSEREVERB_HIGH_CUT": {
        "display_name": "HIGH CUT",
        "type": "options",
        "options": FREQUENCY_OPTIONS,
        "default": "FLAT"
    },
    "REVERSEREVERB_E_LEVEL": {
        "display_name": "E.LEVEL",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "BEATSCATTER_TYPE": {
        "display_name": "TYPE",
        "type": "options",
        "options": [f"P{i:02d}" for i in range(1, 4)],
        "default": "P1"
    },
    "BEATSCATTER_LENGTH": {
        "display_name": "LENGTH",
        "type": "options",
        "options": ["THRU", "𝅗𝅥", "♩", "♪", "𝅘𝅥𝅯'"],
        "default": "QUARTER"
    },
    "BEATREPEAT_TYPE": {
        "display_name": "TYPE",
        "type": "options",
        "options": ["FORWARD", "REWIND", "MIX"],
        "default": "FORWARD"
    },
    "BEATREPEAT_LENGTH": {
        "display_name": "LENGTH",
        "type": "options",
        "options": ["THRU", "𝅗", "𝅗𝅥", "♩", "♪", "𝅘𝅥𝅯'", "𝅘E"],
        "default": "QUARTER"
    },
    "BEATSHIFT_TYPE": {
        "display_name": "TYPE",
        "type": "options",
        "options": ["FUTURE", "PAST"],
        "default": "FUTURE"
    },
    "BEATSHIFT_SHIFT": {
        "display_name": "SHIFT",
        "type": "options",
        "options": ["THRU", "𝅘𝅥𝅯'", "♪", "♩", "𝅗𝅥", "𝅗"],
        "default": "QUARTER"
    },
    "VINYLFLICK_FLICK": {
        "display_name": "FLICK",
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "DEFAULT_RANGE": {
        "type": "range",
        "range": (0, 100),
        "default": 50
    },
    "SW": {
        "display_name": "SW",
        "type": "on_off",
        "default": "OFF"
    },
    "SYNC": {
        "display_name": "SYNC",
        "type": "on_off",
        "default": "OFF"
    },
    "RETRIG": {
        "display_name": "RETRIG",
        "type": "on_off",
        "default": "OFF"
    },
    "SEQ RATE": {
        "display_name": "SEQ RATE",
        "type": "combined",
        "numeric_range": (0, 100),
        "options": MUSICAL_NOTE_OPTIONS,
        "default": "♩",
        "use_numeric_default": False
    },
    "SEQ MAX": {
        "display_name": "SEQ MAX",
        "type": "range",
        "range": (1, 16),
        "default": 16
    },
    "TARGET": {
        "display_name": "TARGET",
        "type": "options",
        "options": [],
        "default": None
    }
}

# Define which effects can use the sequencer
SEQUENCER_EFFECTS = [
    "LPF", "BPF", "HPF", "PHASER", "FLANGER", "SYNTH", "RINGMOD", "PITCH BEND",
    "ISOLATOR", "OCTAVE", "TREMOLO", "VIBRATO", "MANUAL PAN", "OSC BOT"
]

# Sequencer parameters list
SEQUENCER_PARAMETERS = [
    "SW", "SYNC", "RETRIG", "TARGET", "SEQ RATE", "SEQ MAX"
] + [f"SEQ VAL{i}" for i in range(1, 17)]


def get_parameter_info(param_id, selected_effect=None):
    """
    Get parameter information based on parameter ID and effect type
    param_id: Parameter's internal ID (e.g., GNRDELAY_TIME)
    selected_effect: Currently selected effect (e.g., "GNR DELAY")
    """
    # Special case for GNR DELAY
    if selected_effect == "GNR DELAY":
        if param_id == "GNRDELAY_TIME":
            return {
                "display_name": "TIME",
                "type": "range",
                "range": (0, 100),
                "default": 50
            }
        elif param_id == "GNRDELAY_FEEDBACK":
            return {
                "display_name": "FEEDBACK",
                "type": "range",
                "range": (0, 100),
                "default": 70
            }

    # Check for defined parameters
    if param_id in PARAMETER_DEFINITIONS:
        return PARAMETER_DEFINITIONS[param_id]

    # Default range parameters if not found
    return {
        "display_name": param_id,
        "type": "range",
        "range": (0, 100),
        "default": 50
    }


def get_parameter_display_name(param_id):
    """Get display name for parameter"""
    param_info = get_parameter_info(param_id)
    return param_info.get("display_name", param_id)


STANDARD_PARAMS = [
    "DEPTH", "RESONANCE", "CUTOFF", "D.LEVEL", "E.LEVEL", "BALANCE", "LEVEL",
    "MANUAL", "FREQUENCY", "DECAY", "ATTACK", "RELEASE", "SUSTAIN", "SENS",
    "RISE TIME", "BEND", "BASS", "MIDDLE", "TREBLE", "PRESENCE", "BAND LEVEL",
    "OCTAVE.LEVEL", "WAVEFORM", "ENHANCE", "COLOR", "TIME", "FEEDBACK", "FLICK"
]

TARGET_OPTIONS = {
    "LPF": ["CUTOFF"],
    "BPF": ["CUTOFF"],
    "HPF": ["CUTOFF"],
    "PHASER": ["MANUAL"],
    "FLANGER": ["MANUAL"],
    "SYNTH": ["FREQUENCY"],
    "RINGMOD": ["FREQUENCY"],
    "TRANSPOSE": ["TRANS"],
    "PITCH BEND": ["BEND"],
    "OSC BOT": ["NOTE"],
    "ISOLATOR": ["BAND LEVEL"],
    "OCTAVE": ["OCTAVE"],
    "MANUAL PAN": ["POSITION"],
    "TREMOLO": ["DEPTH", "LEVEL"],
    "VIBRATO": ["DEPTH", "D.LEVEL", "E.LEVEL"]
}

TARGET_DEFAULTS = {
    "LPF": "CUTOFF",
    "BPF": "CUTOFF",
    "HPF": "CUTOFF",
    "PHASER": "MANUAL",
    "FLANGER": "MANUAL",
    "SYNTH": "FREQUENCY",
    "RINGMOD": "FREQUENCY",
    "TRANSPOSE": "TRANS",
    "PITCH BEND": "PITCH",
    "OSC BOT": "NOTE",
    "ISOLATOR": "BAND LEVEL",
    "OCTAVE": "OCTAVE",
    "MANUAL PAN": "POSITION",
    "TREMOLO": "DEPTH",
    "VIBRATO": "DEPTH"
}

SEQ_VAL_CONFIGS = {
    "DEFAULT": {
        "type": "options",
        "options": [str(i) for i in range(0, 101)],
        "default": "50"
    },
    "OSC BOT": {
        "type": "options",
        "options": MUSICAL_NOTES,
        "default": "C1"
    },
    "MANUAL PAN": {
        "type": "options",
        "options": PAN_POSITIONS,
        "default": "CENTER"
    }
}

SEQUENCER_EFFECTS = [
    "LPF", "BPF", "HPF", "PHASER", "FLANGER", "SYNTH", "RINGMOD", "PITCH BEND",
    "ISOLATOR", "OCTAVE", "TREMOLO", "VIBRATO", "MANUAL PAN", "OSC BOT"
]

SEQUENCER_PARAMETERS = [
    "SW", "SYNC", "RETRIG", "TARGET", "SEQ RATE", "SEQ MAX"
] + [f"SEQ VAL{i}" for i in range(1, 17)]
