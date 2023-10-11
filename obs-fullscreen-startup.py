import obspython as obs

# ------------------------------------------------------------

def start_preview_projector_cb():
        obs.obs_frontend_open_projector("Preview", 0, "AdnQywACAAAAAAAAAAAAAAAAB38AAAQ3AAAACAAAAB8AAAeHAAAEQwAAAAAABAAAB4A=", "")
        obs.remove_current_callback()

# ------------------------------------------------------------

def script_description():
        return "Start the preview in full screen mode on display 1"

def script_update(settings):
        startup_seconds = obs.obs_data_get_int(settings, "startup_seconds")

        obs.timer_remove(start_preview_projector_cb)
        obs.timer_add(start_preview_projector_cb, startup_seconds * 1000)

def script_defaults(settings):
        obs.obs_data_set_default_int(settings, "startup_seconds", 10)

def script_properties():
        props = obs.obs_properties_create()
        obs.obs_properties_add_int(props, "startup_seconds", "Time needed for OBS startup (seconds)", 5, 3600, 1)

        return props
