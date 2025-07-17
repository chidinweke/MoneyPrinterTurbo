from moviepy import Clip, vfx


# FadeIn
def fadein_transition(clip: Clip, t: float) -> Clip:
    return clip.with_effects([vfx.FadeIn(t)])


# FadeOut
def fadeout_transition(clip: Clip, t: float) -> Clip:
    return clip.with_effects([vfx.FadeOut(t)])


# SlideIn
def slidein_transition(clip: Clip, t: float, side: str) -> Clip:
    return clip.with_effects([vfx.SlideIn(t, side)])


# SlideOut
def slideout_transition(clip: Clip, t: float, side: str) -> Clip:
    return clip.with_effects([vfx.SlideOut(t, side)])


def crossfade_transition(clip1, clip2, duration):
    return CompositeVideoClip([clip1, clip2.with_crossfadein(duration)])


def wipe_transition(clip1, clip2, duration):
    return CompositeVideoClip([clip1, clip2.with_wipe(duration)])


def circle_open_transition(clip, duration):
    return clip.fx(vfx.circle_open, duration)


def circle_close_transition(clip, duration):
    return clip.fx(vfx.circle_close, duration)
