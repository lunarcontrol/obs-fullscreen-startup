import obspython as obs

# A function to reload all sources in the current scene
def reload_all_sources():
  # Get the current scene
  current_scene = obs.obs_frontend_get_current_scene()
  # Check if the current scene is not None
  if current_scene is not None:
    # Get the list of sources in the scene
    scene_items = obs.obs_scene_enum_items(current_scene)
    # Check if the scene items are not None
    if scene_items is not None:
      # Loop through each source and reload it
      for scene_item in scene_items:
        # Get the source object
        source = obs.obs_sceneitem_get_source(scene_item)
        # Get the source id
        source_id = obs.obs_source_get_id(source)
        # Check if the source is a browser source
        if source_id == "browser_source":
          # Reload the browser source
          settings = obs.obs_source_get_settings(source)
          obs.obs_source_update(source, settings)
          obs.obs_data_release(settings)
      # Release the scene and scene items
      obs.sceneitem_list_release(scene_items)
    else:
      # Print a message if the scene items are None
      print("No sources found in the current scene")
  else:
    # Print a message if the current scene is None
    print("No current scene found")
  # Release the current scene
  obs.obs_source_release(current_scene)

# A function to register a timer for reloading all sources every X minutes
def script_load(settings):
  # Get the value of X from settings
  x = obs.obs_data_get_int(settings, "x")
  # Register a timer with a callback function and an interval of X minutes
  timer_id = obs.timer_add(reload_all_sources, x * 60 * 1000)
  # Save the timer id to settings
  obs.obs_data_set_int(settings, "timer_id", timer_id)

# A function to save the settings to a file
def script_save(settings):
  # Get the file path from settings
  file_path = obs.obs_data_get_string(settings, "file_path")
  # Save the settings to the file
  obs.obs_data_save_to_json_file(settings, file_path)

# A function to show some script properties in the UI
def script_properties():
  # Create a new property list
  props = obs.obs_properties_create()
  # Add a text input for the file path
  obs.obs_properties_add_text(props, "file_path", "File Path", obs.OBS_TEXT_DEFAULT)
  # Add an integer input for the value of X
  obs.obs_properties_add_int(props, "x", "X (minutes)", 1, 60, 1)
  # Add a button to manually reload all sources
  obs.obs_properties_add_button(props, "button", "Reload All Sources", reload_all_sources)
  # Return the property list
  return props
