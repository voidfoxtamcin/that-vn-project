layeredimage Tamcin:
    fit "scale-down"

    group base:
        attribute normal default:
            "tamcin_base"
        attribute arm_up:
            "tamcin_raise_arm"

    group eyes:
        attribute idle default:
            "tamcin_expression_idle"
        attribute blink:
            "tamcin_expression_blink"
        attribute happy:
            "tamcin_expression_happy"

    group mouth:
        attribute shut default:
            "tamcin_mouth_close"
        attribute talk:
            "tamcin_mouth_open"

layeredimage Dan:
    fit "scale-down"

    group base:
        attribute normal default:
            "dan_base"
        attribute naked:
            "dan_naked"

    group eyes:
        attribute eyes_open default:
            "dan_eyes_open"
        attribute eyes_mid_open:
            "dan_eyes_mid_open"
        attribute eyes_closed:
            "dan_eyes_close"
        attribute eyes_happy:
            "dan_eyes_happy"

    group mouth:
        attribute mouth_smile default:
            "dan_mouth_close"
        attribute mouth_flat:
            "dan_mouth_poker"
        attribute mouth_open:
            "dan_mouth_open"


layeredimage Twill:
    fit "scale-down"

    group base:
        attribute normal default:
            "twill_base"

    group eyes:
        attribute idle default:
            "twill_eyes_open"
        attribute blink:
            "twill_eyes_close"
        attribute happy:
            "twill_eyes_happy"

    group mouth:
        attribute shut default:
            "twill_mouth_close"
        attribute talk:
            "twill_mouth_open"
