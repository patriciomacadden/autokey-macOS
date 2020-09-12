if window.get_active_class() == "konsole.konsole":
  keyboard.send_keys("<ctrl>+<shift>+w")
else:
  keyboard.send_keys("<ctrl>+w")